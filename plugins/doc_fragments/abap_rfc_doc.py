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


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
description:
  - Uses NWRFC binary to connect to SAP and call remote enabled RFCs.
author:
  - Kirill Satarin (@kksat)
  - Gloria Ciavarrini (@gciavarrini)
requirements:
  - python >= 3.6
  - pyrfc >= 2.7.0
  - See documentation for SAP pyrfc http://sap.github.io/PyRFC/pyrfc.html
  - SAP nwrfc SDK installed, see https://support.sap.com/en/product/connectors/nwrfcsdk.html
options:
  rfc_connection:
    description:
      - "Dictionary with RFC connection parameters and configuration to connect to SAP ABAP system"
    type: dict
    required: false
    aliases:
      - abap_system
    suboptions:
      client:
        description: SAP ABAP connection client (mandant)
        required: false
        type: str
        default: '000'
      user:
        description: SAP ABAP connection user
        required: false
        type: str
      passwd:
        description:
          - SAP ABAP connection user password
          - This is a no_log parameter - values will not be logged in ansible output
        required: false
        type: str
      lang:
        description: SAP ABAP connection user language
        required: false
        type: str
        default: EN
        choices:
          - SR
          - ZH
          - TH
          - KO
          - RO
          - SL
          - HR
          - MS
          - UK
          - ET
          - AR
          - HE
          - CS
          - DE
          - EN
          - FR
          - EL
          - HU
          - IT
          - JA
          - DA
          - PL
          - ZF
          - NL
          - "NO"
          - PT
          - SK
          - RU
          - ES
          - TR
          - FI
          - SV
          - BG
          - LT
          - LV
          - Z1
          - AF
          - IS
          - CA
          - SH
          - ID
          - HI
          - KK
          - VI
      trace:
        description:
          - Trace level for NW RFC SDK (0-3)
        required: false
        type: str
        default: "0"
        choices:
          - "0"
          - "1"
          - "2"
          - "3"
      ashost:
        description: SAP ABAP application instance hostname
        required: false
        type: str
      sysnr:
        description: SAP ABAP application system number
        required: false
        type: str
      mshost:
        description: SAP ABAP application message server hostname
        required: false
        type: str
      msserv:
        description:
          - SAP ABAP message server service
          - msserv is needed only, if the service of the message server is not defined as sapms<SYSID> in /etc/services.
        required: false
        type: str
      sysid:
        description: SAP ABAP system id (SID)
        required: false
        type: str
      group:
        description: SAP ABAP application system connection group (when connected to message service)
        required: false
        type: str
      rstrip:
        description:
          - |
            ABAP allows two different ways to store strings
            A fixed length string type C and a dynamic length string type STRING.
          - Strings of type C are padded with blanks, if the content is shorter than the predefined length.
          - In order to unify the connectors behavior regarding strings, the rstrip option was introduced.
          - If set to True, all strings are right-stripped before being returned by an RFC call.
          - See <http://sap.github.io/PyRFC/client.html>
          - There is no equivalent parameter when connecting via HTTP(s), see I(http_connection).
        type: bool
        default: True
      return_import_params:
        description:
          - Importing parameters of RFC call are returned by the RFC call
          - Usually, you do not need the IMPORT parameters in the result of Connection.call().
          - If I(return_import_params) is set to C(False), parameters of type IMPORT are filtered out.
          - |
            Setting I(return_import_params) to C(True) is only recommended for debugging purposes.
            This will change return values of all NW RFC modules.
          - There is no equivalent parameter when connecting via HTTP(s), see I(http_connection).
        type: bool
        default: False

  http_connection:
    description:
      - "Dictionary with HTTP(s) connection parameters and configuration to connect to SAP ABAP system"
    type: dict
    required: false
    aliases:
      - abap_system_http
    suboptions:
      hostname:
        description:
          - SAP ABAP system hostname (to connect via http/https)
        type: str
        required: true
      username:
        description: SAP ABAP connection user
        required: false
        type: str
      password:
        description:
          - SAP ABAP connection user password
          - This is a no_log parameter - values will not be logged in ansible output
        required: false
        type: str
      client:
        description: SAP ABAP connection client (mandant)
        required: false
        type: str
        default: '000'
      port:
        description: SAP ABAP http(https) connection port
        required: false
        type: int
        default: 443
      security:
        description:
          - Flag to select connection protocol
          - C(True) - https protocol
          - C(False) - http protocol
        required: false
        type: bool
        default: True
      language:
        description: SAP ABAP connection user language
        required: false
        type: str
        default: EN
        choices:
          - SR
          - ZH
          - TH
          - KO
          - RO
          - SL
          - HR
          - MS
          - UK
          - ET
          - AR
          - HE
          - CS
          - DE
          - EN
          - FR
          - EL
          - HU
          - IT
          - JA
          - DA
          - PL
          - ZF
          - NL
          - "NO"
          - PT
          - SK
          - RU
          - ES
          - TR
          - FI
          - SV
          - BG
          - LT
          - LV
          - Z1
          - AF
          - IS
          - CA
          - SH
          - ID
          - HI
          - KK
          - VI

  """
