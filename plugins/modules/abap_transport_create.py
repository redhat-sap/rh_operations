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
module: abap_transport_create

extends_documentation_fragment:
  - sap.sap_operations.abap_rfc_doc
  - sap.sap_operations.community

author:
  - Kirill Satarin (@kksat)

short_description: Create transport request in SAP ABAP system

description:
  - Create transport request in SAP ABAP system
  - |
    Module uses following SAP ABAP system remote enabled RFCs:
    CTS_API_CREATE_CHANGE_REQUEST
    CTS_API_READ_CHANGE_REQUEST

version_added: 1.13.0

options:
  description:
    description: Transport request description
    type: str
    required: true

  owner:
    description: Transport request owner
    type: str
    required: true

  client:
    description: SAP ABAP system client
    type: str
    required: true

  category:
    description: Transport request category
    type: str
    required: true
    choices: ["K", "W"]
"""

EXAMPLES = r"""
- name: Create transport request in SAP ABAP system
  sap.sap_operations.abap_transport_create:
    description: Transport request description
    owner: DDIC
    client: "000"
    category: K
    rfc_connection:
      ashost: application-instance-hostname
      client: "000"
      user: DDIC
      passwd: "SecretPa$$word"
      sysnr: "00"
"""

RETURN = r"""
REQUEST:
  description: ABAP transport request id of created transport request
  type: str
  returned: success
  sample: NPLK900034

RETCODE:
  description: |
    RFC return code
    '000' - success, all other codes are errors
  type: str
  returned: success
  sample: "000"

abap_transport_info:
  description: ABAP transport info for created transport request
  type: dict
  returned: success
  sample:
    CATEGORY: K
    CLIENT: "000"
    DESCRIPTION: Transport request description
    MESSAGE: Request NPLK900034 read
    OBJECTS: []
    OWNER: DDIC
    RETCODE: "000"
    STATUS: D
"""

from ansible_collections.sap.sap_operations.plugins.module_utils.abap import (
    AnsibleModuleABAP,
    AnsibleModuleABAPFailException,
)


def main():
    argument_spec = dict(
        description=dict(type="str", required=True),
        owner=dict(type="str", required=True),
        client=dict(type="str", required=True),
        category=dict(type="str", required=True, choices=["K", "W"]),
    )

    module = AnsibleModuleABAP(argument_spec=argument_spec, supports_check_mode=False)
    description = module.params["description"]
    owner = module.params["owner"]
    client = module.params["client"]
    category = module.params["category"]

    with module as abap:
        abap_transport_create = abap(
            "CTS_API_CREATE_CHANGE_REQUEST",
            DESCRIPTION=description,
            OWNER=owner,
            CLIENT=client,
            CATEGORY=category,
        )
        if abap_transport_create.get("RETCODE") != "000":
            raise AnsibleModuleABAPFailException(
                msg="Failed to create transport request", **abap_transport_create
            )
        abap_transport_info = abap(
            "CTS_API_READ_CHANGE_REQUEST", REQUEST=abap_transport_create["REQUEST"]
        )

    module.exit_json(
        changed=True,
        failed=False,
        REQUEST=abap_transport_create["REQUEST"],
        RETCODE=abap_transport_create["RETCODE"],
        abap_transport_info=abap_transport_info,
    )


if __name__ == "__main__":
    main()
