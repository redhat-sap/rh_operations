#!/usr/bin/python
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

DOCUMENTATION = r"""
module: abap_transport_import

extends_documentation_fragment:
  - sap.sap_operations.abap_rfc_doc
  - sap.sap_operations.community

author:
  - Kirill Satarin (@kksat)

short_description: Import transport request

description:
  - Import transport request
  - Module uses SAP ABAP system remote enabled RFC CTS_API_IMPORT_CHANGE_REQUEST
  - Tested only on single system, transport to other systems is not supported
  - Transport system (trx STMS) must be configured in SAP ABAP system for this module to function properly

version_added: 1.13.0

options:

  client:
    description: SAP ABAP system client
    type: str
    required: true

  system:
    description: SAP ABAP system name
    type: str
    required: true

  transport_request_ids:
    description: List of transport request IDs
    type: list
    required: true
    elements: str
"""

EXAMPLES = r"""
- name: Import transport request
  sap.sap_operations.abap_transport_import:
    transport_request_ids:
      - NPLK900002
    client: "000"
    system: NPL
    rfc_connection:
      ashost: application-instance-hostname
      client: "000"
      user: DDIC
      passwd: "SecretPa$$word"
      sysnr: "00"
"""

RETURN = r"""

REQUESTS:
  description: List of transport requests with import status
  type: list
  elements: dict
  returned: success
  sample:
    - REQUEST: NPLK900002
      RETCODE: '000'
    - REQUEST: NPLK900003
      RETCODE: '000'

RETCODE:
  description: |
    Max return code of all transport requests that were imported
    '000' - success, all other codes are errors
  type: str
  returned: success
  sample: '000'

MESSAGE:
  description: Error Message (if any)
  type: str
  returned: success
  sample: Request NPLK900002 imported
"""

from ansible_collections.sap.sap_operations.plugins.module_utils.abap import (
    AnsibleModuleABAP,
    AnsibleModuleABAPFailException,
)


def main():
    argument_spec = dict(
        client=dict(type="str", required=True),
        system=dict(type="str", required=True),
        transport_request_ids=dict(type="list", required=True, elements="str"),
    )

    module = AnsibleModuleABAP(argument_spec=argument_spec, supports_check_mode=False)

    client = module.params["client"]
    system = module.params["system"]
    transport_request_ids = module.params["transport_request_ids"]

    with module as abap:
        abap_transport_import = abap(
            "CTS_API_IMPORT_CHANGE_REQUEST",
            SYSTEM=system,
            CLIENT=client,
            REQUESTS=[{"REQUEST": request_id} for request_id in transport_request_ids],
        )
        if abap_transport_import.get("RETCODE") != "000":
            raise AnsibleModuleABAPFailException(
                msg="Failed to import transport request", **abap_transport_import
            )

    module.exit_json(
        changed=True,
        failed=False,
        MESSAGE=abap_transport_import["MESSAGE"],
        RETCODE=abap_transport_import["RETCODE"],
        REQUESTS=abap_transport_import["REQUESTS"],
    )


if __name__ == "__main__":
    main()
