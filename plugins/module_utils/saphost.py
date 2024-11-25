#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2023 Kirill Satarin (@kksat)
#
# Copyright 2023 Kirill Satarin (@kksat)
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import socket
import ssl
import traceback

try:
    from urllib.request import HTTPHandler
except ImportError:
    from ansible.module_utils.urls import (
        UnixHTTPHandler as HTTPHandler,
    )  # recommended replacement for urllib2
# https://docs.ansible.com/archive/ansible/2.3/dev_guide/developing_modules_checklist.html

from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.sap.sap_operations.plugins.module_utils.compat import (
    dict_union,
)

try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection

try:
    from suds.client import Client
    from suds.transport.http import HttpAuthenticated, HttpTransport
except (ImportError, NameError):
    try:
        from virtwho.virt.esx.suds.client import Client
        from virtwho.virt.esx.suds.transport.http import (
            HttpAuthenticated,
            HttpTransport,
        )
    except (ImportError, NameError):
        HttpAuthenticated = object
        HttpTransport = object
        HAS_SUDS_LIBRARY = False
        SUDS_LIBRARY_IMPORT_ERROR = traceback.format_exc()
    else:
        SUDS_LIBRARY_IMPORT_ERROR = None
        HAS_SUDS_LIBRARY = True
        SUDS_LIBRARY_IMPORT_ERROR = None
else:
    HAS_SUDS_LIBRARY = True
    SUDS_LIBRARY_IMPORT_ERROR = None


class C(object):
    SAPHOSTCTRL = "saphostcrtl"
    SAPCONTROL = "sapcontrol"


class SAPControl(object):
    YELLOW = ("SAPControl-YELLOW",)  # In transition
    GREEN = ("SAPControl-GREEN",)  # Running
    RED = ("SAPControl-RED",)  # Failure
    GRAY = ("SAPControl-GRAY",)  # Stopped


class SAPHostSecurity(object):
    NONE = "none"
    SYSTEM = "system"
    CUSTOM = "custom"


# TODO add unit tests for convert2ansible
def convert2ansible(obj):
    if hasattr(obj, "item"):
        if hasattr(obj.item[0], "mKey") and hasattr(obj.item[0], "mValue"):
            ret = {}
            for element in obj.item:
                ret[element["mKey"]] = convert2ansible(element["mValue"])
            return ret
        return [convert2ansible(element) for element in obj.item]
    if hasattr(obj, "__dict__"):
        return {
            k: convert2ansible(v)
            for k, v in obj.__dict__.items()
            if not k.startswith("__")
        }
    return obj


class LocalSocketHttpConnection(HTTPConnection):
    def __init__(  # noqa: D107
        self,
        host,
        port=None,
        timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
        source_address=None,
        socketpath=None,
    ):
        super().__init__(host, port, timeout, source_address)
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(socketpath)


class LocalSocketHandler(HTTPHandler):
    def __init__(  # noqa: D107
        self,
        debuglevel=0,
        socketpath=None,
    ):
        self._debuglevel = debuglevel
        self._socketpath = socketpath

    def http_open(self, req):
        return self.do_open(LocalSocketHttpConnection, req, socketpath=self._socketpath)


class LocalSocketHttpAuthenticated(HttpAuthenticated):
    def __init__(self, socketpath, **kwargs):  # noqa: D107
        HttpAuthenticated.__init__(self, **kwargs)
        self._socketpath = socketpath

    def u2handlers(self):
        handlers = HttpTransport.u2handlers(self)
        handlers.append(LocalSocketHandler(socketpath=self._socketpath))
        return handlers


class SAPHostSOAPClient(object):
    """Class to call soap methods that are provided by sap host agent binaries.

    For instance
        sapcontrol
        saphostctrl
    As there are slightly different approaches how to call methods provided by these binaries,
    Two child classes will handle method calls.
    This class should not be used directly, only via child classes.

    Methods are lookedup via __getattr__(), if method is not found, exception will happen,
    this exception has to be handled by higher class.
    """

    poll_interval = 3

    def __init__(  # noqa: D107
        self,
        hostname=None,
        username=None,
        password=None,
        ca_file=None,
        security=None,
        instance=None,
        binary=C.SAPHOSTCTRL,
    ):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.instance = instance
        self.ca_file = ca_file
        self.security = security
        self.secure_port = (
            "1129"
            if binary == C.SAPHOSTCTRL
            else "5{0}14".format(str(instance).zfill(2))
        )
        self.unsecure_port = (
            "1128"
            if binary == C.SAPHOSTCTRL
            else "5{0}13".format(str(instance).zfill(2))
        )
        self.unix_socket = (
            "/tmp/.sapstream1128"  # nosec B108
            if binary == C.SAPHOSTCTRL
            else "/tmp/.sapstream5{0}13".format(str(self.instance).zfill(2))  # nosec B108
        )
        self.local = False if self.hostname else True
        self.protocol = "http" if self.security == SAPHostSecurity.NONE else "https"
        self.port = (
            self.unsecure_port
            if self.security == SAPHostSecurity.NONE
            else self.secure_port
        )
        if self.local:
            if binary == C.SAPHOSTCTRL:
                self.url = "http://localhost:{0}/SAPHostControl/?wsdl".format(
                    self.port)
            else:
                self.url = "http://localhost/sapcontrol?wsdl"
        else:
            if binary == C.SAPHOSTCTRL:
                self.url = "{0}://{1}:{2}/SAPHostControl/?wsdl".format(
                    self.protocol, self.hostname, self.port
                )
            else:
                self.url = "{0}://{1}:{2}/sapcontrol?wsdl".format(
                    self.protocol, self.hostname, self.port
                )
        self.client = None

        self.connect()

    def connect(self):
        if self.local:
            return self._connect_local()

        return self._connect_http()

    def _connect_local(self):
        try:
            localsocket = LocalSocketHttpAuthenticated(self.unix_socket)
            client = Client(self.url, transport=localsocket)
        except Exception as e:
            raise e

        self.client = client

    def _connect_http(self):
        if self.security == SAPHostSecurity.SYSTEM:
            if self.ca_file is not None:
                ssl._create_default_https_context = lambda: ssl.create_default_context(
                    cafile=self.ca_file
                )
        elif self.security == SAPHostSecurity.CUSTOM:
            if self.ca_file is not None:
                ssl._create_default_https_context = (
                    lambda: ssl._create_unverified_context(
                        cafile=self.ca_file)  # nosec B323
                )
        try:
            client = Client(self.url, username=self.username,
                            password=self.password)
        except Exception as e:
            raise Exception(str(e) + self.url)

        self.client = client


class AnsibleModuleSAPHostAgent(AnsibleModule):
    def __init__(  # noqa: D107
        self,
        argument_spec,
        bypass_checks=False,
        no_log=False,
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        add_file_common_args=False,
        supports_check_mode=False,
        required_if=None,
        required_by=None,
    ):
        saphostagent_argument_spec = dict(
            hostname=dict(type="str", required=False),
            username=dict(type="str", required=False),
            password=dict(type="str", no_log=True, required=False),
            ca_file=dict(
                type="path",
                required=False,
                required_by={"security": (SAPHostSecurity.CUSTOM,)},
            ),
            security=dict(
                type="str",
                default=SAPHostSecurity.SYSTEM,
                required=False,
                choices=[
                    SAPHostSecurity.SYSTEM,
                    SAPHostSecurity.CUSTOM,
                    SAPHostSecurity.NONE,
                ],
            ),
        )

        saphostagent_required_together = [
            ("hostname", "username", "password"),
        ]
        saphostagent_required_if = [
            ("security", SAPHostSecurity.CUSTOM, ("ca_file",)),
        ]
        saphostagent_required_by = {"hostname": ("username", "password")}
        if required_together is not None:
            required_together = required_together + saphostagent_required_together
        else:
            required_together = saphostagent_required_together
        if required_if is not None:
            required_if = required_if + saphostagent_required_if
        else:
            required_if = saphostagent_required_if
        if required_by is not None:
            required_by = dict_union(required_by, saphostagent_required_by)
        else:
            required_by = saphostagent_required_by

        super(AnsibleModuleSAPHostAgent, self).__init__(
            argument_spec=dict_union(
                saphostagent_argument_spec, argument_spec),
            bypass_checks=bypass_checks,
            no_log=no_log,
            mutually_exclusive=mutually_exclusive,
            required_together=required_together,
            required_one_of=required_one_of,
            add_file_common_args=add_file_common_args,
            supports_check_mode=supports_check_mode,
            required_if=required_if,
            required_by=required_by,
        )
        if not HAS_SUDS_LIBRARY:
            self.fail_json(
                msg=missing_required_lib("suds"),
                exception=SUDS_LIBRARY_IMPORT_ERROR,
            )


def saphostctrl(
    hostname=None, username=None, password=None, ca_file=None, security=None
):
    return SAPHostSOAPClient(
        hostname=hostname,
        username=username,
        password=password,
        ca_file=ca_file,
        security=security,
        binary=C.SAPHOSTCTRL,
    )


def sapcontrol(
    instance, hostname=None, username=None, password=None, ca_file=None, security=None
):
    return SAPHostSOAPClient(
        hostname=hostname,
        username=username,
        password=password,
        ca_file=ca_file,
        security=security,
        instance=instance,
        binary=C.SAPCONTROL,
    )
