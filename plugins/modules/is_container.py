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

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: is_container
extends_documentation_fragment: sap.sap_operations.community
author: Kirill Satarin (@kksat)
short_description: Determine if the current host is a container
description:
  - Determine if the current host is a container
  - Two methods are used to determine if the current host is a container
  - The C(systemd-detect-virt) command is used to detect if the host is a container
  - The C(/.dockerenv) and C(/run/.containerenv) files are checked to see if they exist
version_added: 2.4.0
options: {}
"""

EXAMPLES = """
---
- name: Are we running in a container?
  sap.sap_operations.is_container:
"""

RETURN = """
---
is_container:
  description: Whether the current host is a container
  returned: success
  type: bool
"""

from ansible.module_utils.basic import AnsibleModule
import os


def main():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)

    is_container = False
    try:
        rc, stdout, stderr = module.run_command(
            "systemd-detect-virt",
            check_rc=False,
            handle_exceptions=False,
        )
        is_container = is_container or (rc == 0 and "container" in stdout)
    except Exception:
        pass

    is_container = is_container or (
        os.path.exists("/.dockerenv") or os.path.exists("/run/.containerenv")
    )

    module.exit_json(is_container=is_container)


if __name__ == "__main__":
    main()
