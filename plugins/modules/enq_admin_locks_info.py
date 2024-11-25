#!/usr/bin/python

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
module: enq_admin_locks_info

extends_documentation_fragment:
- sap.sap_operations.community
- sap.sap_operations.enq_admin

author:
  - Kirill Satarin (@kksat)

short_description: Get information about enque server locks for ENSA2 SAP instances

description: Get information about enque server locks for ENSA2 SAP instances

version_added: 1.29.0

options:
  n:
    description: Number of locks to retrieve
    required: false
    type: str
    default: '*'
    aliases:
      - number
  client:
    description: Pattern for client
    required: false
    type: str
    default: '*'
  user:
    description: Pattern for user name
    required: false
    type: str
    default: '*'
  name:
    description: Pattern for lock name
    required: false
    type: str
    default: '*'
  argument:
    description: Pattern for lock argument
    required: false
    type: str
    default: '*'
"""

EXAMPLES = r"""
---
- name: Get information about locks from enq_admin tool for ENSA2 systems
  sap.sap_operations.enq_admin_locks_info:
    pf: /usr/sap/S4H/SYS/profile/S4H_ASCS20_s4ascsa
"""

RETURN = r"""
---
enq_admin_locks_info:
  description: List of locks, filtered by provided parameters
  returned: success
  type: list
  elements: dict
  sample:
    - Argument: "0"
      BCK: false
      Client: "000"
      Count 1: "1"
      Count 2: "0"
      Name: ANSIBLE2
      Object: E_FILL
      Owner 1: DIAG
      Owner 2: ""
      TCODE: SFILL
      Type: Exclusive
      User: FILL_USER
    - Argument: O
      BCK: false
      Client: "000"
      Count 1: "1"
      Count 2: "0"
      Name: ANSIBLE
      Object: E_FILL
      Owner 1: DIAG
      Owner 2: ""
      TCODE: SFILL
      Type: Optimistic
      User: FILL_USER
stdout:
  description: Standard output of the enq_admin tool
  returned: always
  type: str
  sample: |
    Enqueue Server 2
    LID=(17591/1714468346); RN=(300151); Current=20; Peak=30; Maximum=250000

    Locks:
    Type;Count 1;Count 2;BCK;Object;User;Client;TCODE;Owner 1;Owner 2;Name;Argument;
    Exclusive;1;0;false;E_FILL;FILL_USER;000;SFILL;DIAG;;ANSIBLE2;0;
    Optimistic;1;0;false;E_FILL;FILL_USER;000;SFILL;DIAG;;ANSIBLE;O;

    2024-05-03 15:36:25; OK; 'Lock List'; Response=578 usec
    ===================================================================================================
"""


from ansible_collections.sap.sap_operations.plugins.module_utils.enq_admin import (
    AnsibleModuleEnqAdmin,
    run_enq_admin,
    get_enq_admin_locks_info,
)


def main():
    argument_spec = dict(
        n=dict(type="str", default="*", aliases=["number"]),
        client=dict(type="str", default="*"),
        user=dict(type="str", default="*"),
        name=dict(type="str", default="*"),
        argument=dict(type="str", default="*"),
    )

    module = AnsibleModuleEnqAdmin(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    n = module.params.get("n", "*")
    client = module.params.get("client", "*")
    user = module.params.get("user", "*")
    name = module.params.get("name", "*")
    argument = module.params.get("argument", "*")

    result = get_enq_admin_locks_info(
        module=module,
        run_enq_admin=run_enq_admin,
        n=n,
        client=client,
        user=user,
        name=name,
        argument=argument,
    )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
