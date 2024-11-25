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
module: abap_transports_info

extends_documentation_fragment:
  - sap.sap_operations.abap_rfc_doc
  - sap.sap_operations.community

author:
  - Kirill Satarin (@kksat)

short_description: Fetch transport requests from SAP ABAP system based on search criteria

description:
  - Fetch transport requests from SAP ABAP system based on search criteria
  - Information if fetched from SAP ABAP system using remote enabled RFC CTS_WBO_API_READ_REQUESTS_RFC

version_added: 1.13.0

options:

  category:
    description: |
      Transport request category
      'K' = Workbench
      'W' = Customizing
      '*' = any category
    type: str
    required: false
    default: '*'
    choices: ['K', 'W', '*']

  transport_status:
    description: |
      Transport request status
      'D' = Changeable (including 'L')
      'R' = Released (including 'O')
      '*' = all statuses (default)
    type: str
    required: false
    default: 'D'
    choices: ["R", "D", "*"]

  target_system:
    description: Target system
    type: str
    required: false
    default: '*'

  owner:
    description: |
      Transport request owner
      If not provided, current user will be used.
      Use '*' to search for all owners.
    type: str
    required: false

  client:
    description: |
      SAP ABAP system client
      If not provided, current client (mandant) will be used.
    type: str
    required: false
    aliases: [ "mandant" ]

  read_attributes:
    description: If true read attributes of transport request
    type: bool
    required: false
    default: false

  attributes_keys:
    description: List of attributes keys to read
    type: list
    required: false
    elements: str
    default: []

  read_task_headers:
    description: If true read task headers of transport request
    type: bool
    required: false
    default: false
"""

EXAMPLES = r"""
- name: Find all my transport requests in current system and client that are in changeable status
  sap.sap_operations.abap_transports_info:
  rfc_connection:
      ashost: application-instance-hostname
      client: '000'
      user: DDIC
      passwd: "SecretPa$$word"
      sysnr: '00'

- name: Find all my transport requests in current system and client that are released
  sap.sap_operations.abap_transports_info:
  transport_status: R
  rfc_connection:
      ashost: application-instance-hostname
      client: '000'
      user: DDIC
      passwd: "SecretPa$$word"
      sysnr: '00'
"""

RETURN = r"""
abap_transports_info:
  description: |
    List of transport requests with information about them
  type: list
  elements: dict
  returned: success
  sample:
    REQUESTS:
      - REQ_ATTRS: []
        REQ_HEADER:
          AS4DATE: '20230405'
          AS4TEXT: Workbench Request Config. Task Manager
          AS4TIME: '182918'
          AS4USER: DDIC
          CLIENT: '001'
          TARSYSTEM: ''
          TRFUNCTION: K
          TRKORR: NPLK900022
          TRSTATUS: D
        TASK_HEADERS:
          - AS4DATE: '20230405'
            AS4TEXT: Workbench Request Config. Task Manager
            AS4TIME: '182919'
            AS4USER: DDIC
            TRFUNCTION: X
            TRKORR: NPLK900023
            TRSTATUS: D

      - REQ_ATTRS: []
        REQ_HEADER:
          AS4DATE: '20231214'
          AS4TEXT: test
          AS4TIME: '130602'
          AS4USER: DDIC
          CLIENT: '001'
          TARSYSTEM: ''
          TRFUNCTION: W
          TRKORR: NPLK900062
          TRSTATUS: D
        TASK_HEADERS:
          - AS4DATE: '20231214'
            AS4TEXT: test
            AS4TIME: '130611'
            AS4USER: DDIC
            TRFUNCTION: Q
            TRKORR: NPLK900063
            TRSTATUS: D
"""

from ansible_collections.sap.sap_operations.plugins.module_utils.abap import (
    AnsibleModuleABAP,
)


def main():
    argument_spec = dict(
        category=dict(type="str", required=False, choices=["K", "W", "*"], default="*"),
        transport_status=dict(
            type="str", required=False, default="D", choices=["R", "D", "*"]
        ),
        target_system=dict(type="str", required=False, default="*"),
        owner=dict(type="str", required=False),
        client=dict(type="str", required=False, aliases=["mandant"]),
        read_attributes=dict(type="bool", required=False, default=False),
        attributes_keys=dict(
            type="list", required=False, default=[], elements="str", no_log=False
        ),
        read_task_headers=dict(type="bool", required=False, default=False),
    )

    module = AnsibleModuleABAP(argument_spec=argument_spec, supports_check_mode=True)
    category = module.params["category"]
    transport_status = module.params["transport_status"]
    target_system = module.params["target_system"]
    owner = module.params["owner"]
    client = module.params["client"]
    read_attributes = "X" if module.params["read_attributes"] else " "
    attributes_keys = module.params["attributes_keys"]
    read_task_headers = "X" if module.params["read_task_headers"] else " "

    params = dict(
        TRFUNCTION=category,
        TRSTATUS=transport_status,
        TARSYSTEM=target_system,
        READ_ATTRS=read_attributes,
        READ_TASK_HEADERS=read_task_headers,
        REQ_ATTR_KEYS=attributes_keys,
    )

    if owner:
        params["AS4USER"] = owner

    if client:
        params["CLIENT"] = client

    with module as abap:
        abap_transports_info = abap(
            "CTS_WBO_API_READ_REQUESTS_RFC",
            **params,
        )

    module.exit_json(
        changed=False,
        failed=False,
        abap_transports_info=abap_transports_info,
    )


if __name__ == "__main__":
    main()
