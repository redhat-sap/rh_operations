#!/usr/bin/python
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2023 Red Hat, Project Atmosphere
#
# Copyright 2023 Red Hat, Project Atmosphere
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

DOCUMENTATION = """
---
module: hdbuserstore_info

author:
  - Ondra Machacek (@machacekondra)
extends_documentation_fragment:
  - sap.sap_operations.hana

short_description: Get information from HANA user store (HANA command hdbsuserstore)

description: |
  Get information from HANA user store (HANA command hdbsuserstore)
  Key name is returned in case key exists (set previously)

version_added: 1.0.0

notes:
  - See NOTE in documentation for I(hdbuserstore) module in regards to running ansible modules when becoming <hanasid>adm user with '-i' \
    flag. Otherwise you might face issues with ansible module executions in SAP HANA environments."

options:
  binary_path:
    description:
      - Custom path of the I(hdbuserstore) binary.
    type: str
    required: false
    default: ''
  key:
    description:
      - Get info about the I(key)
    type: str
"""

EXAMPLES = """
---
- name: Get info about the key mykey from HDB user store (recommended way, see notes)
  sap.sap_operations.hdbuserstore_info:
    key: mykey
  become: true
  become_user: <hanasid>adm
  become_flags: -i
  vars:
    ansible_python_interpreter: "/usr/libexec/platform-python -E"
"""

RETURN = """
---
stdout:
    description: HDB key info
    type: str
    returned: always
"""

from ansible.module_utils.basic import AnsibleModule
import os


def main():
    module_args = dict(
        key=dict(type="str", no_log=False),
        binary_path=dict(type="str", default=""),
    )

    result = dict(changed=False, env={})
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    binary = os.path.join(module.params.get("binary_path"), "hdbuserstore")
    key = module.params.get("key", "")
    _rc, result["stdout"], _err = module.run_command(args=[binary, "List", key])

    module.exit_json(**result)


if __name__ == "__main__":
    main()
