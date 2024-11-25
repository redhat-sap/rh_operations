#!/usr/bin/python
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2024 Kirill Satarin (@kksat)
#
# Copyright 2024 Kirill Satarin (@kksat)
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
---
module: ha_check_config_info
extends_documentation_fragment:
  - sap.sap_operations.saphost

author:
  - Kirill Satarin (@kksat)

short_description: Run sap host agent function HACheckConfig

description:
  - Collect information about installed SAP instances on the host

options:
  instance_number:
    description: Instance number
    type: str
    required: false
    default: "00"

version_added: 1.14.0
"""

RETURN = """
ha_check_config_info:
    description: Result of HACheckConfig method execution on host with SAP HANA installed
    type: list
    elements: dict
    returned: success
    sample:
    - category: SAPControl-SAP-CONFIGURATION
      comment: 0 ABAP instances detected
      description: Redundant ABAP instance configuration
      state: SAPControl-HA-SUCCESS
    - category: SAPControl-SAP-CONFIGURATION
      comment: 0 Java instances detected
      description: Redundant Java instance configuration
      state: SAPControl-HA-SUCCESS
    - category: SAPControl-SAP-CONFIGURATION
      comment: All Enqueue server separated from application server
      description: Enqueue separation
      state: SAPControl-HA-SUCCESS
    - category: SAPControl-SAP-CONFIGURATION
      comment: All MessageServer separated from application server
      description: MessageServer separation
      state: SAPControl-HA-SUCCESS
"""

EXAMPLES = """
- name: Run ha_check_config_info
  sap.sap_operations.ha_check_config_info:
    instance_number: "00"
"""


from ansible_collections.sap.sap_operations.plugins.module_utils.saphost import (
    AnsibleModuleSAPHostAgent,
    sapcontrol,
    convert2ansible,
)


def main():
    argument_spec = dict(
        instance_number=dict(type="str", required=False, default="00"),
    )
    module = AnsibleModuleSAPHostAgent(
        argument_spec=argument_spec, supports_check_mode=True
    )

    try:
        instance_sapcontrol = sapcontrol(
            instance=module.params.get("instance_number", "00"),
            hostname=module.params.get("hostname"),
            username=module.params.get("username"),
            password=module.params.get("password"),
            ca_file=module.params.get("ca_file"),
            security=module.params.get("security"),
        )

        ha_check_config_info = convert2ansible(
            instance_sapcontrol.client.service.HACheckConfig()
        )

        module.exit_json(
            ha_check_config_info=ha_check_config_info,
        )
    except Exception as e:
        module.fail_json(
            msg="Issue during calling SOAP host agent methods",
            exception=str(e),
        )


if __name__ == "__main__":
    main()
