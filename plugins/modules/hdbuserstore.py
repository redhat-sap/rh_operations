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
module: hdbuserstore

author:
  - Ondra Machacek (@machacekondra)
extends_documentation_fragment:
  - sap.sap_operations.hana
  - action_common_attributes

short_description: Manage the HANA user store (HANA command hdbuserstore)

description: |
  Manage the HANA user store (HANA command hdbuserstore)
  Get and set HANA user store records.
version_added: 1.0.0

options:
  state:
    description:
      - "If I(present) the key will be created, removed otherwise."
    type: str
    choices: ['present', 'absent']
    default: 'present'
  binary_path:
    description: |
      Custom path of the I(hdbuserstore) binary.
      Variable I(binary_path) is required if hdbuserstore command cannot be found in PATH environment variable (with user running the module).
      See examples section to find several ways not to provide value for this variable.
    type: str
    required: false
    default: ''
  key:
    description:
      - "Manage the I(key)."
    type: str
    required: true
  env:
    description: |
      Database location (host:port).
      Required only if C(state=present)
    type: str
  username:
    description: |
      Username for the hdb store
      Required only if you set new key, C(state=present)
    type: str
  password:
    description: |
      Password for the hdb store username.
      Required only if you set new key, state=present
    type: str
  force:
    description: |
      If I(true) the key will be updated even if already exists. Used to update password.
      If set to I(false) (default value) module will return OK, but will not update the key, key will be created only if it does not exists
    type: bool
    default: false
requirements:
  - python >= 3.6
attributes:
  check_mode:
    support: full
  diff_mode:
    support: none
  platform:
    platforms: posix
"""

EXAMPLES = """
---
- name: Set the key mykey (recommended way, see notes)
  sap.sap_operations.hdbuserstore:
    key: mykey
    env: "localhost:30113"
    username: myuser
    password: mypassword
  become: true
  become_user: <hanasid>adm
  become_flags: -i
  vars:
    ansible_python_interpreter: "/usr/libexec/platform-python -E"
"""

RETURN = """
---
key:
  description: HDB key name
  type: str
  returned: always
  sample: mykey
env:
  description: HDB env name
  type: str
  returned: When state is C(present)
  sample: myenv
username:
  description: HDB username for key
  type: str
  returned: When state is C(present)
  sample: myusername
"""

from ansible.module_utils.basic import AnsibleModule
import os


def ensure_created(module):
    binary = os.path.join(module.params.get("binary_path"), "hdbuserstore")
    key = module.params.get("key")
    env = module.params.get("env")
    username = module.params.get("username")
    password = module.params.get("password")
    force = module.params.get("force")
    return_key = {"key": key, "env": env, "username": username}

    # Fetch the key:
    rc, stdout, _err = module.run_command(args=[binary, "List", key])
    if rc not in [0, 100]:
        module.fail_json(msg="Failed to execute list: {0}".format(stdout))

    if rc == 0 and not force:
        return False, stdout, return_key

    # Store the key:
    if not module.check_mode:
        rc, stdout, _err = module.run_command(
            args=[binary, "Set", key, env, username, password]
        )
        if rc != 0:
            module.fail_json(msg="Failed to execute Set: {0}".format(stdout))

    return True, stdout, return_key


def ensure_absent(module):
    binary = os.path.join(module.params.get("binary_path"), "hdbuserstore")
    key = module.params.get("key")

    rc, stdout, _err = module.run_command(args=[binary, "List", key])
    if not module.check_mode and rc == 0:
        rc, _out, _err = module.run_command(args=[binary, "Delete", key])

    if rc not in [0, 100]:
        module.fail_json(msg="Failed to execute delete: {0}".format(stdout))

    return rc == 0, stdout, {"key": key}


def main():
    module_args = dict(
        state=dict(
            type="str",
            choices=[
                "present",
                "absent",
            ],
            default="present",
        ),
        key=dict(type="str", required=True, no_log=False),
        env=dict(type="str"),
        username=dict(type="str"),
        password=dict(type="str", no_log=True),
        binary_path=dict(type="str", default=""),
        force=dict(type="bool", default=False),
    )

    result = dict(changed=False)
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[
            ["state", "present", ["env", "username", "password"]],
        ],
    )

    state = module.params.get("state")
    if state == "present":
        result["changed"], result["stdout"], return_key = ensure_created(module)
    else:
        result["changed"], result["stdout"], return_key = ensure_absent(module)

    result.update(return_key)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
