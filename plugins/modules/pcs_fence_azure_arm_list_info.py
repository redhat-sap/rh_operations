#!/usr/bin/python

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

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""

module: pcs_fence_azure_arm_list_info

extends_documentation_fragment: sap.sap_operations.experimental

author: Kirill Satarin (@kksat)

short_description: Get list of hosts from Azure fence ARM

description:
  - Get list of hosts from Azure fence ARM
  - This module will execute command C(fence_azure_arm --action=list) and process results to present them nicely in Ansible
  - If C(fence_azure_arm) is not installed, module will fail
  - Required user with permissions to execute C(pcs --version --full) command

version_added: 1.4.0-galaxy

options:
  username:
    description:
      - Username for Azure authentication
      - Required if C(msi) is set to false
    required: false
    type: str

  password:
    description:
      - Password for Azure authentication
      - Required if C(msi) is set to false
    required: false
    type: str

  resource_group:
    description:
      - Resource group name
    required: false
    type: str

  subscription_id:
    description:
      - Subscription ID for Azure authentication
    required: false
    type: str

  msi:
    description:
      - Use MSI authentication
    required: false
    default: false
    type: bool

  tenant_id:
    description:
      - Tenant ID for Azure authentication
    required: false
    type: str

"""

EXAMPLES = r"""
"""

RETURN = r"""

rc:
  description: Return code of the command executed
  returned: success
  type: int
  sample: 0

stdout:
  description: Standard output of the command executed
  returned: success
  type: str
  sample: host1,host2,host3

stderr:
  description: Standard error of the command executed
  returned: success
  type: str
  sample: ""

hosts:
  description: List of hosts
  returned: success
  type: list
  elements: str
  sample:
    - "host1"
    - "host2"
    - "host3"
"""


from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = dict(
        username=dict(type="str", required=False),
        password=dict(type="str", required=False, no_log=True),
        resource_group=dict(type="str", required=False),
        subscription_id=dict(type="str", required=False),
        msi=dict(type="bool", required=False, default=False),
        tenant_id=dict(type="str", required=False),
    )
    required_together = [
        ("resource_group", "subscription_id"),
    ]
    required_if = [
        ("msi", False, ("resource_group", "subscription_id", "username", "password")),
        ("msi", True, ("resource_group", "subscription_id")),
    ]

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_together=required_together,
        required_if=required_if,
        supports_check_mode=True,
    )
    args = ["fence_azure_arm", "--action=list"]

    if module.params["msi"]:
        args.append("--msi")
    if module.params["username"]:
        args.append("--username={}".format(module.params["username"]))
    if module.params["password"]:
        args.append("--password={}".format(module.params["password"]))
    if module.params["resource_group"]:
        args.append("--resourceGroup={}".format(module.params["resource_group"]))
    if module.params["subscription_id"]:
        args.append("--subscriptionId={}".format(module.params["subscription_id"]))
    if module.params["tenant_id"]:
        args.append("--tenantId={}".format(module.params["tenant_id"]))

    rc, stdout, stderr = module.run_command(args, check_rc=True)
    hosts = [line.strip(",").strip() for line in stdout.splitlines()]
    module.exit_json(
        changed=False,
        rc=rc,
        stdout=stdout,
        stderr=stderr,
        hosts=hosts,
    )


if __name__ == "__main__":
    main()
