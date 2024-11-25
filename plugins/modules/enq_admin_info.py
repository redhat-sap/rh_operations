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
module: enq_admin_info

extends_documentation_fragment:
- sap.sap_operations.community
- sap.sap_operations.enq_admin

author:
  - Kirill Satarin (@kksat)

short_description: Get information from enq_admin tool for ENSA2 systems

description: Get information from enq_admin tool for ENSA2 systems

version_added: 1.29.0

options: {}
"""

EXAMPLES = r"""
---
- name: Get information from enq_admin tool for ENSA2 systems
  sap.sap_operations.enq_admin_info:
    pf: /usr/sap/S4H/SYS/profile/S4H_ASCS20_s4ascsa
"""

RETURN = r"""
---
stdout:
  description: Standard output from enq_admin tool
  returned: success
  type: str
  sample: |
    Enqueue Server 2
    Server Status : STATUS_RUNNING
    Repl.State    : REPLICATION_ON
    Repl.Type     : REPLICATION_REPLICATOR
    Process ID    : 17591
    Start Time    : 2024-04-30 11:12:13
    Release       : 789
    Patch Level   : 100
    Compiled On   : Linux GNU SLES-15 x86_64  cc10.3.0 use-pr230217
    Compiled At   : Feb 17 2023 18:43:20
    Number Clients: 38
    Dev.Trc. Level: 1
    Req.Trc. Level: 0

    2024-05-03 15:35:11; OK; 'Process Information'; Response=281 usec
    ===================================================================================================
"""


from ansible_collections.sap.sap_operations.plugins.module_utils.enq_admin import (
    AnsibleModuleEnqAdmin,
    run_enq_admin,
)


def run_module(module, run_enq_admin):
    rc, stdout, stderr = run_enq_admin(module=module, args=["--info", "--no_color"])

    if rc == 0:
        return dict(changed=False, stdout=stdout)
    return dict(
        failed=True,
        msg="Failed to get information from enq_admin tool",
        stderr=stderr,
    )


def main():

    module = AnsibleModuleEnqAdmin(
        argument_spec={},
        supports_check_mode=True,
    )
    result = run_module(module, run_enq_admin=run_enq_admin)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
