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

from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils.basic import AnsibleModule
import decimal

from ansible_collections.sap.sap_operations.plugins.module_utils.suds_helper import (
    deep_asdict,
)

from ansible_collections.sap.sap_operations.plugins.module_utils.compat import (
    dict_union,
)

try:
    from pyrfc import (
        Connection,
        # RFCError,
        # RFCLibError,
        # LogonError,
        # CommunicationError,
        # ABAPApplicationError,
        # ABAPRuntimeError,
        # ExternalAuthorizationError,
        # ExternalRuntimeError,
        # ExternalApplicationError
    )

except ImportError:
    HAS_PYRFC_LIBRARY = False
    PYRFC_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_PYRFC_LIBRARY = True
    PYRFC_LIBRARY_IMPORT_ERROR = None

try:
    from suds.client import Client
except ImportError:
    try:
        from virtwho.virt.esx.suds.client import Client
    except ImportError:
        HAS_SUDS_LIBRARY = False
        SUDS_LIBRARY_IMPORT_ERROR = traceback.format_exc()
        Client = None
        HttpAuthenticated = None
        HttpTransport = None
    else:
        HAS_SUDS_LIBRARY = True
        SUDS_LIBRARY_IMPORT_ERROR = None
else:
    HAS_SUDS_LIBRARY = True
    SUDS_LIBRARY_IMPORT_ERROR = None


def ClassMembers(classname):
    return [
        attr
        for attr in dir(classname)
        if not callable(getattr(classname, attr)) and not attr.startswith("__")
    ]


ABAP_LANGU_CHOICES = [
    "SR",
    "ZH",
    "TH",
    "KO",
    "RO",
    "SL",
    "HR",
    "MS",
    "UK",
    "ET",
    "AR",
    "HE",
    "CS",
    "DE",
    "EN",
    "FR",
    "EL",
    "HU",
    "IT",
    "JA",
    "DA",
    "PL",
    "ZF",
    "NL",
    "NO",
    "PT",
    "SK",
    "RU",
    "ES",
    "TR",
    "FI",
    "SV",
    "BG",
    "LT",
    "LV",
    "Z1",
    "AF",
    "IS",
    "CA",
    "SH",
    "ID",
    "HI",
    "KK",
    "VI",
]
"""
ABAP_LANG2SPRAS - conversion dictionary from 2 char language code to one char language code
Example
 EN -> E
 DE -> D
 JA- > J

 See table T002 in SAP system
"""
ABAP_LANG2SPRAS = {
    "SR": "0",
    "ZH": "1",
    "TH": "2",
    "KO": "3",
    "RO": "4",
    "SL": "5",
    "HR": "6",
    "MS": "7",
    "UK": "8",
    "ET": "9",
    "AR": "A",
    "HE": "B",
    "CS": "C",
    "DE": "D",
    "EN": "E",
    "FR": "F",
    "EL": "G",
    "HU": "H",
    "IT": "I",
    "JA": "J",
    "DA": "K",
    "PL": "L",
    "ZF": "M",
    "NL": "N",
    "NO": "O",
    "PT": "P",
    "SK": "Q",
    "RU": "R",
    "ES": "S",
    "TR": "T",
    "FI": "U",
    "SV": "V",
    "BG": "W",
    "LT": "X",
    "LV": "Y",
    "Z1": "Z",
    "AF": "a",
    "IS": "b",
    "CA": "c",
    "SH": "d",
    "ID": "i",
    "HI": "묩",
    "KK": "뱋",
    "VI": "쁩",
}

ABAP_SPRAS2LANG = {
    "0": "SR",
    "1": "ZH",
    "2": "TH",
    "3": "KO",
    "4": "RO",
    "5": "SL",
    "6": "HR",
    "7": "MS",
    "8": "UK",
    "9": "ET",
    "A": "AR",
    "B": "HE",
    "C": "CS",
    "D": "DE",
    "E": "EN",
    "F": "FR",
    "G": "EL",
    "H": "HU",
    "I": "IT",
    "J": "JA",
    "K": "DA",
    "L": "PL",
    "M": "ZF",
    "N": "NL",
    "O": "NO",
    "P": "PT",
    "Q": "SK",
    "R": "RU",
    "S": "ES",
    "T": "TR",
    "U": "FI",
    "V": "SV",
    "W": "BG",
    "X": "LT",
    "Y": "LV",
    "Z": "Z1",
    "a": "AF",
    "b": "IS",
    "c": "CA",
    "d": "SH",
    "i": "ID",
    "묩": "HI",
    "뱋": "KK",
    "쁩": "VI",
}

ABAP_TIME_ZONE_CHOICES = [
    "AFGHAN",
    "ALA",
    "ALAW",
    "AST",
    "AUSACT",
    "AUSLHI",
    "AUSNSW",
    "AUSNT",
    "AUSQLD",
    "AUSSA",
    "AUSTAS",
    "AUSVIC",
    "AUSWA",
    "AZOREN",
    "BRAZIL",
    "BRZLAN",
    "BRZLEA",
    "BRZLWE",
    "CAT",
    "CET",
    "CHILE",
    "CHILEE",
    "CST",
    "CSTNO",
    "CYPRUS",
    "EET",
    "EGYPT",
    "EST",
    "EST_",
    "ESTNO",
    "FLKLND",
    "GMTUK",
    "GST",
    "GSTE",
    "GSTW",
    "HAW",
    "INDIA",
    "IRAN",
    "IRAQ",
    "ISRAEL",
    "JAPAN",
    "JORDAN",
    "LBANON",
    "MST",
    "MSTNO",
    "NEPAL",
    "NFDL",
    "NORFLK",
    "NST",
    "NZCHA",
    "NZST",
    "PARAGY",
    "PIERRE",
    "PST",
    "RUS03",
    "RUS04",
    "RUS05",
    "RUS06",
    "RUS07",
    "RUS08",
    "RUS09",
    "RUS10",
    "RUS11",
    "RUS12",
    "RUS13",
    "RUS14",
    "SYRIA",
    "UK",
    "UTC",
    "UTC-1",
    "UTC-10",
    "UTC-11",
    "UTC-12",
    "UTC-2",
    "UTC-3",
    "UTC-4",
    "UTC-5",
    "UTC-6",
    "UTC-7",
    "UTC-8",
    "UTC-83",
    "UTC-9",
    "UTC+1",
    "UTC+10",
    "UTC+11",
    "UTC+12",
    "UTC+13",
    "UTC+14",
    "UTC+2",
    "UTC+3",
    "UTC+4",
    "UTC+5",
    "UTC+53",
    "UTC+6",
    "UTC+63",
    "UTC+7",
    "UTC+8",
    "UTC+9",
    "VERM02",
    "VERM10",
    "VERP02",
    "VERP10",
    "WAT",
    "WDFT",
    "WET",
]
ABAP_COUNTRY_CHOICES = [
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AU",
    "AW",
    "AX",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BM",
    "BN",
    "BO",
    "BQ",
    "BR",
    "BS",
    "BT",
    "BV",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CS",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "GA",
    "GB",
    "GD",
    "GE",
    "GF",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GP",
    "GQ",
    "GR",
    "GS",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MQ",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NF",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PS",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "SS",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TF",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TP",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "UM",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
]


class AnsibleModuleABAPException(Exception):
    pass


class AnsibleModuleABAPExitException(AnsibleModuleABAPException):
    def __init__(self, **kwargs):
        """Class handle AnsibleModule.exit_json."""
        self.kwargs = kwargs


class AnsibleModuleABAPFailException(AnsibleModuleABAPException):
    def __init__(self, msg, **kwargs):
        """Class handle AnsibleModule.fail_json."""
        self.msg = msg
        self.kwargs = kwargs


class SAPRFCClient(object):
    def __init__(self, rstrip, return_import_params, **kwargs):
        """Class handle SAP RFC connection."""
        self.rstrip = rstrip
        self.return_import_params = return_import_params
        self.params = {
            k: v for k, v in kwargs.items() if v is not None
        }  # Required, because if parameter is not set, Ansible sets it to None
        self.__connection = None
        # self.unit = None

    @property
    def connection(self):
        if self.__connection is not None:
            return self.__connection
        try:
            self.__connection = Connection(
                **self.params,
                config=dict(
                    rstrip=self.rstrip, return_import_params=self.return_import_params
                ),
            )
        except Exception as e:
            raise e
        return self.__connection

    def close(self):
        # if self.unit is not None:
        #     try:
        #         self.confirm_unit()
        #     except Exception as e:
        #         raise e
        # if self.connection is not None:
        try:
            self.connection.close()
        except Exception as e:
            raise e

    # def __del__(self):
    #     if self.connection is not None:
    #         self.connection.close()

    # def connect(self):
    #     if self.connection is not None:
    #         return self.connection
    #     try:
    #         self.connection = Connection(
    #             **self.params,
    #             config=dict(rstrip=self.rstrip, return_import_params=self.return_import_params),
    #         )
    #     except Exception as e:
    #         raise e
    #     return self.connection

    # def get_connection(self):
    #     if self.connection is not None:
    #         return self.connection
    #     try:
    #         self.connection = self.connect()
    #     except Exception as e:
    #         raise e
    #     return self.connection
    @property
    def unit(self):
        if self.__unit is not None:
            return self.__unit
        self.__unit = self.connection.initialize_unit(background=False)
        return self.__unit

    # def get_unit(self):
    #     if self.unit is not None:
    #         return self.unit
    #     self.unit = self.get_connection().initialize_unit(background=False)

    def confirm_unit(self):
        try:
            self.connection.confirm_unit(self.unit)
        except Exception as e:
            raise e
        finally:
            self.__unit = None

    def fill_and_submit_unit(self, func_name: str, **kwargs):
        # if self.unit is None:
        #     self.get_unit()
        try:
            self.connection.fill_and_submit_unit(
                self.unit, list(func_name, {}), queue_names=None, attributes=None
            )
        except Exception as e:
            raise e

    def __call__(self, func_name: str, **kwargs) -> dict:
        try:
            # return self.get_connection().call(func_name=func_name, **kwargs)
            return self.connection.call(func_name=func_name, **kwargs)
            # self.get_unit()
            # return self.get_connection().fill_and_submit_unit(self.unit,[(func_name, kwargs)])
        except Exception as e:
            raise e


class SAPHTTPSOAPClient(object):
    def __init__(self, hostname, username, password, language, client, port, security):
        """Class handle SAP ABAP HTTP(S) SOAP connection."""
        # /sap/public/ping
        if hostname is not None:
            self.hostname = hostname
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if language is not None:
            self.language = language
        if client is not None:
            self.client = client
        if port is not None:
            self.port = port
        if security is not None:
            self.security = security
        self.protocol = "https://" if security else "http://"

    def __call__(self, func_name: str, **kwargs) -> dict:
        escaped_func_name = func_name.replace("/", "_-")
        try:
            url = "{0}{1}:{2}/sap/bc/soap/wsdl?sap-client={3}&services={4}".format(
                self.protocol, self.hostname, self.port, self.client, escaped_func_name
            )
            try:
                self.soap_client = Client(
                    url, username=self.username, password=self.password
                )
            except Exception as e:
                raise e
            return deep_asdict(
                getattr(self.soap_client.service, escaped_func_name)(**kwargs)
            )
        except Exception as e:
            raise e

    def close(self):
        pass


class AnsibleModuleABAP(AnsibleModule):
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
        """Class handle AnsibleModule with ABAP connection parameters."""
        rfc_config = dict(
            rstrip=dict(type="bool", default=True),
            return_import_params=dict(type="bool", default=False),
        )

        rfc_params = dict(
            client=dict(type="str", required=False, default="000"),
            user=dict(type="str", required=False),
            passwd=dict(type="str", required=False, no_log=True),
            lang=dict(
                type="str", required=False, default="EN", choices=ABAP_LANGU_CHOICES
            ),
            trace=dict(
                type="str", required=False, default="0", choices=["0", "1", "2", "3"]
            ),
            ashost=dict(type="str", required=False),
            sysnr=dict(type="str", required=False),
            mshost=dict(type="str", required=False),
            msserv=dict(type="str", required=False),
            sysid=dict(type="str", required=False),
            group=dict(type="str", required=False),
            # TODO SNC not supported yet
            # snc_qop=dict(type='str', required= False, default='3', choices=['1','2','3','8','9']),
            # snc_myname=dict(type='str', required= False),  #default - user
            # snc_partnername=dict(type='str', required= False),
            # snc_lib=dict(type='str', required= False),
        )
        # sapconnection=dict(type='dict', options=dict(config=config, params = params))
        # abap_argument_spec=dict(rfc_connection=dict(type='dict', options=(rfc_config | rfc_params)))

        # https://docs.ansible.com/ansible/latest/dev_guide/developing_program_flow_modules.html#dependencies-between-module-options
        abap_mutually_exclusive = [
            ("rfc_connection", "http_connection"),
        ]
        rfc_mutually_exclusive = [
            ("ashost", "mshost"),
            ("ashost", "msserv"),
            ("ashost", "sysid"),
            ("ashost", "group"),
            ("sysnr", "mshost"),
            ("sysnr", "msserv"),
            ("sysnr", "sysid"),
            ("sysnr", "group"),
            # TODO SNC not supported yet
            # ('user','snc_qop'),
            # ('user','snc_myname'),
            # ('user','snc_partnername'),
            # ('user','snc_lib'),
            # ('passwd','snc_qop'),
            # ('passwd','snc_myname'),
            # ('passwd','snc_partnername'),
            # ('passwd','snc_lib'),
        ]
        rfc_required_together = [
            ("client", "user", "passwd"),
            ("sysnr", "ashost"),
            ("mshost", "sysid", "group"),
            # TODO SNC not supported yet
            # ('snc_qop','snc_myname','snc_partnername'),
        ]

        http_parameters = dict(
            hostname=dict(type="str", required=True),
            username=dict(type="str", required=False),
            password=dict(type="str", required=False, no_log=True),
            client=dict(type="str", required=False, default="000"),
            port=dict(type="int", required=False, default=443),
            security=dict(type="bool", required=False, default=True),
            language=dict(
                type="str", required=False, default="EN", choices=ABAP_LANGU_CHOICES
            ),
        )
        http_required_together = [
            ("hostname", "username", "password"),
        ]

        abap_mutually_exclusive = []
        abap_required_together = []
        abap_required_one_of = [
            ("rfc_connection", "http_connection"),
        ]
        abap_required_if = []
        abap_required_by = {}
        abap_argument_spec = dict(
            rfc_connection=dict(
                type="dict",
                aliases=["abap_system"],
                options=dict_union(rfc_config, rfc_params),
                mutually_exclusive=rfc_mutually_exclusive,
                required_together=rfc_required_together,
            ),
            http_connection=dict(
                type="dict",
                aliases=["abap_system_http"],
                options=http_parameters,
                mutually_exclusive=[],
                required_together=http_required_together,
            ),
        )

        mutually_exclusive = (
            mutually_exclusive + abap_mutually_exclusive
            if mutually_exclusive
            else abap_mutually_exclusive
        )
        required_together = (
            required_together + abap_required_together
            if required_together
            else abap_required_together
        )
        required_one_of = (
            required_one_of + abap_required_one_of
            if required_one_of
            else abap_required_one_of
        )
        required_if = (
            required_if + abap_required_if if required_if else abap_required_if
        )
        required_by = (
            required_by | abap_required_by if required_by else abap_required_by
        )

        super().__init__(
            argument_spec={**argument_spec, **abap_argument_spec},
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

    def __enter__(self):
        """Class handle AnsibleModule with ABAP connection parameters."""
        self.rfc_connection = self.params.get("rfc_connection")
        self.http_connection = self.params.get("http_connection")
        if self.rfc_connection:
            if not HAS_PYRFC_LIBRARY:
                self.fail_json(
                    msg=missing_required_lib("pyrfc"),
                    exception=PYRFC_LIBRARY_IMPORT_ERROR,
                )
            self.abap_client = SAPRFCClient(**self.rfc_connection)
        elif self.http_connection:
            if not HAS_SUDS_LIBRARY:
                self.fail_json(
                    msg=missing_required_lib("suds"),
                    exception=SUDS_LIBRARY_IMPORT_ERROR,
                )
            self.abap_client = SAPHTTPSOAPClient(**self.http_connection)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Class handle AnsibleModule with ABAP connection parameters."""
        if exc_type:
            if isinstance(exc_value, AnsibleModuleABAPException):
                if isinstance(exc_value, AnsibleModuleABAPFailException):
                    self.fail_json(msg=exc_value.msg, **exc_value.kwargs)
                if isinstance(exc_value, AnsibleModuleABAPExitException):
                    self.exit_json(**exc_value.kwargs)
            else:
                self.fail_json(
                    msg="Exception {0} occurred.".format(
                        exc_type.__class__.__name__),
                    exception=str(exc_value),
                    traceback=traceback.format_tb(exc_tb),
                )
        if self.abap_client is not None:
            self.abap_client.close()

    def convert2ansible(self, result):
        if not isinstance(result, dict):
            if isinstance(result, decimal.Decimal):
                return str(
                    result
                )  # Decimal is not supported by Ansible, converted to string
            if isinstance(result, bytes):
                # Bytes are decoded to strings
                return result.decode(encoding="utf-8")
        else:
            for k, v in result.items():
                result[k] = self.convert2ansible(v)
        return result

    def __call__(self, func_name: str, **kwargs) -> dict:
        try:
            result = self.abap_client(func_name, **kwargs)

            return self.convert2ansible(result)
        except Exception as e:
            raise e
