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

import traceback
import json
import xml.etree.ElementTree as ET  # nosec B405
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import missing_required_lib
from ansible_collections.sap.sap_operations.plugins.module_utils.compat import (
    dict_union,
)
from ansible_collections.sap.sap_operations.plugins.module_utils.me_constants import (
    me_timeout,
)

from ansible_collections.sap.sap_operations.plugins.module_utils.me_constants import (
    ME_USER_AGENT,
)


try:
    import requests
    from requests.auth import AuthBase
except ImportError:
    requests = object
    AuthBase = object
    HAS_REQUESTS_LIBRARY = False
    REQUESTS_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_REQUESTS_LIBRARY = True
    REQUESTS_LIBRARY_IMPORT_ERROR = None

try:
    from lxml import etree  # nosec B410
except ImportError:
    etree = object
    HAS_LXML_LIBRARY = False
    LXML_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_LXML_LIBRARY = True
    LXML_IMPORT_ERROR = None

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class FileInfo(object):
    def __init__(self, username, password, file_id):
        """Class to get file information from SAP swdc.

        :param username: SAP username
        :param password: SAP password
        :param file_id: File ID
        """
        self.username = username
        self.password = password
        self.fileid = file_id

    def get(self):
        r = requests.get(
            "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('{0}')".format(  # noqa: E501
                self.fileid
            ),
            auth=SAPAuth(username=self.username, password=self.password),
            timeout=me_timeout,
            headers={"Accept": "application/json"},
        )

        return json.loads(r.text)["d"]


class DownloadBasket(object):
    def __init__(self, username, password):
        """Class to get download basket from SAP swdc."""
        self.username = username
        self.password = password

    def get(self):
        r = requests.get(
            "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadBasketItemSet?sap-language=en",  # noqa: E501
            auth=SAPAuth(username=self.username, password=self.password),
            timeout=me_timeout,
            headers={"Accept": "application/json"},
        )

        return json.loads(r.text)["d"]


class SAPNoteUrl(object):
    def __init__(self, username, password, sapnote):
        """Get SAP note URL from SAP support portal."""
        self.username = username
        self.password = password
        self.sapnote = sapnote

    def get(self):
        # data= """
        # <?xml version="1.0" encoding="UTF-8"?>
        # -<asx:abap xmlns:asx="http://www.sap.com/abapxml" version="1.0">
        #     -<asx:values>
        #         -<NOTES>
        #             <CWBNTNUMM>{self.sapnote}</CWBNTNUMM>
        #         </NOTES>
        #         <USERID>S00</USERID>
        #         <NO_URL/>
        #         <NO_DEP>X</NO_DEP>
        #     </asx:values>
        # </asx:abap>
        # """

        r = requests.get(
            "https://apps.support.sap.com/sap/support/lp/notes/hcp/down4snote/down4snote.htm?iv_num={self.sapnote}&sap-language=EN",  # noqa: E501
            auth=SAPAuth(username=self.username, password=self.password),
            timeout=me_timeout,
            headers={"Accept": "application/json"},
        )
        # r = requests.post(
        #     "https://apps.support.sap.com/sap/support/",
        #     auth=SAPAuth(username=self.username, password=self.password),
        #     headers={'content-type': 'application/xml'},
        #     data=data
        # )
        # print(r)
        return json.loads(r.text)["d"]


class me_AnsibleModule(AnsibleModule):
    def __init__(
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
        """Ansible module for SAP web services (launchpad, me.sap.com)."""
        me_argument_spec = dict(
            username=dict(type="str", required=True),
            password=dict(type="str", required=True, no_log=True),
        )
        me_required_by = {}
        required_by = me_required_by if required_by is None else required_by

        super(me_AnsibleModule, self).__init__(
            argument_spec=dict_union(argument_spec, me_argument_spec),
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
        if not HAS_REQUESTS_LIBRARY:
            self.fail_json(
                msg=missing_required_lib("requests"),
                exception=REQUESTS_LIBRARY_IMPORT_ERROR,
            )
        if not HAS_LXML_LIBRARY:
            self.fail_json(
                msg=missing_required_lib("lxml"),
                exception=LXML_IMPORT_ERROR,
            )

    def __call__(self, url):
        try:
            response = requests.get(
                url,
                auth=SAPAuth(
                    username=self.params.get("username"),
                    password=self.params.get("password"),
                ),
                timeout=me_timeout,
                headers={"Accept": "application/json"},
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.fail_json(
                msg="Failed to fetch information from SAP web service",
                url=url,
                response=response.text,
                exception=str(e),
            )
        try:
            result = json.loads(response.text)
        except ValueError as e:
            self.fail_json(
                msg="Failed to parse response from SAP web service",
                url=url,
                response=response.text,
                exception=str(e),
            )
        return result


def get_all_inputs(text):
    ret = {}
    for i in ET.fromstring(text, parser=etree.HTMLParser()).xpath(  # nosec B314
        ".//body//form[@method='post']//input"
    ):
        if i.attrib.get("name") and i.attrib.get("value"):
            ret[i.attrib["name"]] = i.attrib["value"]

    return ret


def get_next_url(text):
    next_url = (
        ET.fromstring(text, parser=etree.HTMLParser())  # nosec B314
        .xpath(".//body//form[@method='post']")[0]
        .attrib["action"]
    )

    next_url = (
        next_url
        if "https://" in next_url
        else "https://accounts.sap.com{0}".format(next_url)
    )
    return next_url


def get_gigya_params(response):
    api_key = None
    saml_context = None
    for p in urlparse(response.url).query.split("&"):
        if p.startswith("samlContext="):
            saml_context = p[len("samlContext="):]
        elif p.startswith("apiKey="):
            api_key = p[len("apiKey="):]

    return saml_context, api_key


def get_swdc_headers(url, username, password):
    session = requests.Session()

    session.headers.update({"User-Agent": ME_USER_AGENT})
    session.allow_redirects = True
    session.timeout = me_timeout

    response = session.get(url)
    next_url = get_next_url(response.text)
    post_data = get_all_inputs(response.text)

    response = session.post(
        next_url,
        data=post_data,
    )

    next_url = get_next_url(response.text)
    post_data = get_all_inputs(response.text)
    post_data.update({"j_username": username})

    response = session.post(
        next_url,
        data=post_data,
    )

    next_url = get_next_url(response.text)
    post_data = get_all_inputs(response.text)
    response = session.post(
        next_url,
        data=post_data,
    )

    saml_context, api_key = get_gigya_params(response)
    response = session.post(
        "https://core-api.account.sap.com/uid-core/authenticate?reqId=https://hana.ondemand.com/supportportal",  # noqa: E501
        json={"login": username, "password": password},
    )
    data = json.loads(response.text)
    login_token = data["cookieValue"]

    response = requests.get(
        "https://cdc-api.account.sap.com/saml/v2.0/{0}/idp/sso/continue?loginToken={1}&samlContext={2}".format(  # noqa: E501
            api_key,
            login_token,
            saml_context,
        ),
        timeout=me_timeout,
    )

    next_url = get_next_url(response.text)
    post_data = get_all_inputs(response.text)
    response = session.post(
        next_url,
        data=post_data,
    )
    next_url = get_next_url(response.text)
    post_data = get_all_inputs(response.text)

    post_url = post_data["RelayState"]
    session.headers.update({"Content-Type": "application/x-www-form-urlencoded"})
    response = session.post(url=post_url, data=post_data, allow_redirects=False)

    while response.status_code == 302:
        response = session.send(response._next, allow_redirects=False, stream=True)

    ret = {}
    ret["url"] = response.request.url
    ret["headers"] = dict(response.request.headers)

    session.close()
    return ret


class SAPAuth(AuthBase):
    """SAPAuth is class which implements the SAP launchpad authentication."""

    sso_url = "https://accounts.sap.com/saml2/idp/sso"

    def get_next_url(self, text):
        return (
            ET.fromstring(text, parser=etree.HTMLParser())  # nosec B314
            .xpath(".//body//form[@method='post']")[0]
            .attrib["action"]
        )

    def get_all_inputs(self, text):
        ret = {}
        for i in ET.fromstring(text, parser=etree.HTMLParser()).xpath(  # nosec B314
            ".//body//form[@method='post']//input"
        ):
            if i.attrib.get("name") and i.attrib.get("value"):
                ret[i.attrib["name"]] = i.attrib["value"]

        return ret

    def __init__(self, username=None, password=None):
        """Class to handle SAP launchpad authentication for requests."""
        self._username = username
        self._password = password

    def _next_step(self, response, history, next_url=None, headers=None, **kwargs):
        if next_url is None:
            next_url = self.get_next_url(response.text)

        post_data = self.get_all_inputs(response.text)

        for k, v in kwargs.items():
            post_data[k] = v

        cookies = dict()
        for r in history:
            cookies.update(dict(r.cookies.items()))
        next_url = (
            next_url
            if "https://" in next_url
            else "https://accounts.sap.com{0}".format(next_url)
        )
        if headers is None:
            headers = dict()
        headers.update({"User-Agent": ME_USER_AGENT})

        next_response = requests.post(
            next_url,
            data=post_data,
            cookies=cookies,
            headers=headers,
            timeout=me_timeout,
        )

        history.append(next_response)

        return next_response

    def _get_gigya_params(self, response):
        api_key = None
        saml_context = None
        for p in urlparse(response.url).query.split("&"):
            if p.startswith("samlContext="):
                saml_context = p[len("samlContext="):]
            elif p.startswith("apiKey="):
                api_key = p[len("apiKey="):]

        return saml_context, api_key

    def _get_login_token(self, history):
        response = requests.post(
            "https://core-api.account.sap.com/uid-core/authenticate?reqId=https://hana.ondemand.com/supportportal",  # noqa: E501
            json={"login": self._username, "password": self._password},
            timeout=me_timeout,
            # For some reason requests/python user agent is not accepted:
            headers={"User-Agent": "curl/7.82.0"},
        )
        history.append(response)
        data = json.loads(response.text)
        return data["cookieValue"]

    def _get_saml_response(self, response, history):
        saml_context, api_key = self._get_gigya_params(response)
        login_token = self._get_login_token(history)

        response = requests.get(
            "https://cdc-api.account.sap.com/saml/v2.0/{0}/idp/sso/continue?loginToken={1}&samlContext={2}".format(  # noqa: E501
                api_key,
                login_token,
                saml_context,
            ),
            timeout=me_timeout,
        )
        history.append(response)
        return response

    def _gigya(self, response, history):
        response = self._next_step(response, history)
        response = self._next_step(response, history, j_username=self._username)
        response = self._next_step(response, history)
        response = self._get_saml_response(response, history)
        response = self._next_step(response, history)
        response = self._next_step(response, history)
        return self._next_step(response, history, headers=self._headers)

    def handle_response(self, response, **kwargs):
        history = [response]

        if "@" in self._username:
            return self._gigya(response, history)

        response = self._next_step(response, history)
        response = self._next_step(response, history, j_username=self._username)
        # We need to pass the next_url explicitly, because the response only contains relative URL for some reason:  # noqa: E501
        response = self._next_step(
            response, history, next_url=self.sso_url, j_password=self._password
        )
        response = self._next_step(response, history)
        return self._next_step(response, history, headers=self._headers)

    def __call__(self, request):
        request.register_hook("response", self.handle_response)
        self._headers = request.headers
        return request


class SWDCAuth(SAPAuth):
    """SWDCAuth is class which implements the SAP software download center authentication."""

    def _gigya(self, response, history):
        response = self._next_step(response, history)
        response = self._next_step(response, history, j_username=self._username)
        response = self._next_step(response, history)
        response = self._get_saml_response(response, history)
        response = self._next_step(response, history)
        # response = self._next_step(response, history)
        return response
