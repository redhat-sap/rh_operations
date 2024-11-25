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

module: saplikey_get_info

extends_documentation_fragment:
  - sap.sap_operations.experimental
  - sap.sap_operations.saplikey_common

author:
  - Kirill Satarin (@kksat)

short_description: Get host hardware key information and other useful information with saplikey program.

description:
  - Get host hardware key information and other useful information with saplikey program.
  - This module will execute command C(saplikey -get) and parse its output.

version_added: 1.8.0-galaxy

"""  # noqa: E501

EXAMPLES = r"""
- name: Get sap hardware key for the host
  sap.sap_operations.saplikey_get_info:
  become: true
  become_user: <sid>adm
  become_flags: '-i'
"""

RETURN = r"""

rc:
  description: Return code of the saplikey program execution.
  returned: always
  type: int
  sample: 0

stdout:
  description: The standard output of the saplikey program execution.
  returned: always
  type: list
  elements: str
  sample:
    - SAP License Key Administration  -  Copyright (C) 2003 - 2012 SAP AG
    - System ID. . . . : AAA
    - Hardware Key . . : D1111111111        (of this computer)
    - Installation No. : 0000000000
    - System No. . . . : 000000000000000000
    - Release. . . . . : 749
    - Software products: NetWeaver_SYB

stderr:
  description: The standard error of the saplikey program execution.
  returned: always
  type: str
  sample: ""

saplikey_get_info:
  description: The parsed output of the saplikey program execution.
  returned: success
  type: dict
  contains:
    hardware_key:
      description: The hardware key of the host.
      returned: success
      type: str
      sample: D1111111111
    installation_number:
      description: The installation number of the host.
      returned: success
      type: str
      sample: 0000000000
    release:
      description: The release of the host.
      returned: success
      type: str
      sample: 749
    software_products:
      description: The software products of the host.
      returned: success
      type: str
      sample: NetWeaver_SYB
    system_id:
      description: The system ID of the host.
      returned: success
      type: str
      sample: AAA
    system_number:
      description: The system number of the host.
      returned: success
      type: str
      sample: 000000000000000000
"""


from ansible_collections.sap.sap_operations.plugins.module_utils.saplikey import (  # noqa: E501
    AnsibleModule_saplikey,
    get_saplikey_get_info_from_stdout,
)


def main():
    module = AnsibleModule_saplikey(
        argument_spec={},
        supports_check_mode=True,
        required_by={},
    )

    rc, stdout, stderr = module.run_saplikey_command(["-get"])
    saplikey_get_info = get_saplikey_get_info_from_stdout(stdout)
    module.exit_json(
        changed=False,
        rc=rc,
        stdout=stdout,
        stderr=stderr,
        saplikey_get_info=saplikey_get_info,
    )


if __name__ == "__main__":
    main()
