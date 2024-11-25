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


from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: proc_info
extends_documentation_fragment: sap.sap_operations.community
short_description: Reads content from files in the /proc directory
version_added: 1.18.0
description:
  - This module is designed to read the contents of files located within the /proc directory.
  - It prevents directory traversal attacks by ensuring that the requested path is within the /proc directory.
options:
  proc:
    description:
      - The path to the file within the /proc directory to read.
      - This path might be relative to the /proc directory or absolute; absolute paths are adjusted accordingly.
      - To read /proc/cpuinfo from the root directory, one should set this parameter to "/proc/cpuinfo" or "cpuinfo"
    required: true
    type: path
author:
  - Kirill Satarin (@kksat)
"""

EXAMPLES = r"""
- name: Read cpuinfo
  sap.sap_operations.proc_info:
    proc: "cpuinfo"
- name: Try to read outside /proc
  sap.sap_operations.proc_info:
    proc: "/etc/passwd"
"""

RETURN = r"""
rc:
  description: Return code from the 'cat' command.
  type: int
  returned: always
stdout:
  description: The content of the file read from /proc.
  type: str
  returned: success
stderr:
  description: The standard error from the 'cat' command if it fails.
  type: str
  returned: failure
proc_path:
  description: The absolute path to the file that was read.
  type: str
  returned: always
"""


from ansible.module_utils.basic import AnsibleModule
import os


def sanitize_path(module, base_path, user_input):
    user_path = os.path.abspath(os.path.join(base_path, user_input))
    if os.path.commonprefix([user_path, base_path]) != base_path:
        module.fail_json(
            msg="Don't try directory traversal attacks on me!",
            base_path=base_path,
            user_input=user_input,
            user_path=user_path,
        )
    return user_path


def main():
    argument_spec = dict(
        proc=dict(type="path", required=True),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    proc = module.params["proc"]
    proc = "." + proc if proc[0] == "/" else proc
    proc = proc if proc[0:4] == "/proc" else ("." + proc if proc[0] == "/" else proc)
    proc_path = sanitize_path(module, "/proc/", proc)
    rc, stdout, stderr = module.run_command(["cat", proc_path], check_rc=True)
    module.exit_json(
        rc=rc,
        stdout=stdout,
        stderr=stderr,
        proc_path=proc_path,
    )


if __name__ == "__main__":
    main()
