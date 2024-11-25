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
module: abap_transport_info

extends_documentation_fragment:
  - sap.sap_operations.abap_rfc_doc
  - sap.sap_operations.community

author:
  - Kirill Satarin (@kksat)

short_description: Fetch information about transport request from SAP ABAP system

description:
  - Fetch information about transport request from SAP ABAP system
  - Information if fetched from SAP ABAP system using remote enabled RFC CTS_API_READ_CHANGE_REQUEST

version_added: 1.13.0

options:
  transport_request_id:
    description: Transport request ID
    type: str
    required: true

"""

EXAMPLES = r"""
- name: Collection information about SAP ABAP system
  sap.sap_operations.abap_transport_info:
  transport_request_id: NPLK900002
  rfc_connection:
      ashost: application-instance-hostname
      client: '000'
      user: DDIC
      passwd: "SecretPa$$word"
      sysnr: '00'
"""

RETURN = r"""

abap_transport_info:
  description: ABAP transport info
  type: dict
  returned: success
  sample:
    CATEGORY: K
    CLIENT: '000'
    DESCRIPTION: SAP_NOTE_IMPL
    MESSAGE: Request NPLK900002 read
    OWNER: SNOTE
    RETCODE: '000'
    STATUS: R
    OBJECTS:
      - NAME: NPLK900003 20170221 093250 SNOTE
        OBJECT: RELE
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: SHDB_GET_INDEXES
        OBJECT: FUNC
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: SUMO_RESOLVE_E071_OBJ
        OBJECT: FUNC
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: SDB1FHDB
        OBJECT: REPS
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '002075125841        0000045863'
        OBJECT: CINS
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '002075125841        0000095848'
        OBJECT: CINS
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '002075125841        0000095849'
        OBJECT: CINS
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '002075125841        0000095850'
        OBJECT: CINS
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '002075125841        0000095901'
        OBJECT: CINS
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '002075125841        0000095902'
        OBJECT: CINS
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '0002344014'
        OBJECT: NOTE
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''
      - NAME: '0002401259'
        OBJECT: NOTE
        TABKEY: ''
        TABU_NAME: ''
        VIEW_NAME: ''

abap_transport_info2:
  description: ABAP transport info
  type: dict
  returned: transport_request_id not found
  sample:
    CATEGORY: ''
    CLIENT: ''
    DESCRIPTION: ''
    MESSAGE: Task/request does_not_exist does not exist in system NPL
    OBJECTS: []
    OWNER: ''
    RETCODE: '003'
    STATUS: ''

"""

from ansible_collections.sap.sap_operations.plugins.module_utils.abap import (
    AnsibleModuleABAP,
)


def main():
    argument_spec = dict(
        transport_request_id=dict(type="str", required=True),
    )

    module = AnsibleModuleABAP(argument_spec=argument_spec, supports_check_mode=True)
    transport_request_id = module.params["transport_request_id"]

    with module as abap:
        abap_transport_info = abap("CTS_API_READ_CHANGE_REQUEST", REQUEST=transport_request_id)

    module.exit_json(
        changed=False,
        failed=False,
        abap_transport_info=abap_transport_info,
    )


if __name__ == "__main__":
    main()
