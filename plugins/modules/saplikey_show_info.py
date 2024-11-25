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

module: saplikey_show_info

extends_documentation_fragment:
  - sap.sap_operations.experimental
  - sap.sap_operations.saplikey_common

author:
  - Kirill Satarin (@kksat)

short_description: Get information about SAP license keys with saplikey program.

description:
  - Get information about SAP license keys with saplikey program.
  - This module will execute command C(saplikey -show) and parse its output.

version_added: 1.8.0-galaxy

"""

EXAMPLES = r"""
- name: Show all sap license keys
  sap.sap_operations.saplikey_show_info:
  become: true
  become_user: <sid>adm
  become_flags: '-i'
"""  # noqa: E501

RETURN = r"""

rc:
  description: Return code of the saplikey program execution.
  returned: always
  type: int
  sample: 0

stdout:
  description: The standard output of the saplikey program execution.
  returned: always
  type: str
  sample: |
    SAP License Key Administration  -  Copyright (C) 2003 - 2012 SAP AG

    List of installed License Keys:
    ==========================================

    1. License Key:
    ------------------------------------------
    System                : AAA
    Hardware Key          : D1111111111
    Software Product      : NetWeaver_SYB
    Software Product Limit: 2000000000
    Type of License Key   : permanent
    Installation Number   : 0000000000
    System Number         : 000000000000000000
    Begin of Validity     : 20230111
    End   of Validity     : 20240712
    Last successful check : 00000000
    Validity              : valid

    ------------------------------------------
    1 license keys listed.

stderr:
  description: The standard error of the saplikey program execution.
  returned: always
  type: str
  sample: ""

license_keys:
  description:
    - The list of installed license keys.
    - Please pay attention that all dates are in format YYYYMMDD.
    - Please pay attention that all numeric values are returned as strings.
  returned: success
  type: list
  elements: dict
  sample:
    - begin_of_validity: '20230111'
      end_of_validity: '20240712'
      hardware_key: D1111111111
      installation_number: 0000000000
      last_successful_check: '20231016'
      software_product: NetWeaver_SYB
      software_product_limit: '2000000000'
      system_id: AAA
      system_number: '000000000000000000'
      type_of_license_key: permanent
      validity: valid
    - begin_of_validity: '20230111'
      end_of_validity: '20240712'
      hardware_key: D1111111111
      installation_number: 0000000000
      last_successful_check: '00000000'
      software_product: Maintenance_SYB
      software_product_limit: '2000000000'
      system_id: AAA
      system_number: '000000000000000000'
      type_of_license_key: permanent
      validity: valid

"""


from ansible_collections.sap.sap_operations.plugins.module_utils.saplikey import (  # noqa: E501
    AnsibleModule_saplikey,
    get_license_keys_from_stdout,
)


def main():
    module = AnsibleModule_saplikey(
        argument_spec={},
        supports_check_mode=True,
        required_by={},
    )

    rc, stdout, stderr = module.run_saplikey_command(["-show"])
    license_keys = get_license_keys_from_stdout(stdout)
    module.exit_json(
        changed=False,
        rc=rc,
        stdout=stdout,
        stderr=stderr,
        license_keys=license_keys,
    )


if __name__ == "__main__":
    main()
