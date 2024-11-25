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
# If not, see <https://www.gnu.org/licenses/>

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: hana_system_replication_info
extends_documentation_fragment:
  - sap.sap_operations.community
  - sap.sap_operations.hana
author:
  - Kirill Satarin (@kksat)
short_description: Get info about SAP HANA system replication configuration
description:
  - Get information about SAP HANA system replication configuration
version_added: 2.11.0
seealso:
  # - module: sap.sap_operations.hana_system_replication
  - module: sap.sap_operations.hana_backup
  - module: sap.sap_operations.hana_restore
options: {}
"""

EXAMPLES = """
---
- name: Get hana system replication configuration information
  sap.sap_operations.hana_system_replication_info:
  become: true
  become_user: hsradm
  become_flags: -i
  vars:
    ansible_python_interpreter: "/usr/libexec/platform-python -E"
"""

RETURN = """
---
hana_system_replication_info:
    description: Dictionary with HSR configuration info
    type: dict
    returned: success
    sample:
      has_secondaries_consumers_attached: false
      is_primary_suspended: false
      is_secondary_consumer_system: false
      is_source_system: true
      is_takeover_active: false
      mode: primary
      online: true
      operation_mode: "primary"
      site_id: "1"
      site_name: "test"
stdout:
    description: Stdout of the 'hdbnsutil -sr_state' command
    type: str
    returned: always
    sample: |
      System Replication State
      ~~~~~~~~~~~~~~~~~~~~~~~~

      online: true

      mode: primary
      operation mode: primary
      site id: 1
      site name: test

      is source system: true
      is secondary/consumer system: false
      has secondaries/consumers attached: false
      is a takeover active: false
      is primary suspended: false

      Host Mappings:
      ~~~~~~~~~~~~~~


      Site Mappings:
      ~~~~~~~~~~~~~~
      test (primary/)

      Tier of test: 1

      Replication mode of test: primary

      Operation mode of test:


      Hint based routing site:
      done.
stderr:
    description: Stderr of the 'hdbnsutil -sr_state' command
    type: str
    returned: always
    sample: |
      Performing Final Memory Release with 8 threads.
      Finished Final Memory Release successfully.
rc:
    description: Return code of the 'hdbnsutil -sr_state' command
    type: int
    returned: always
    sample: 0
"""

from ansible_collections.sap.sap_operations.plugins.module_utils.monad import (
    Failure,
    Success,
)
from ansible_collections.sap.sap_operations.plugins.module_utils.hana import (
    get_hana_system_replication_info_from_stdout,
    get_hdbnsutil_run_command,
)
from ansible.module_utils.basic import AnsibleModule
from collections.abc import Callable


def get_hana_system_replication_info(hdbnsutil_run_command: Callable, params: dict):
    rc, stdout, stderr = hdbnsutil_run_command(["-sr_state"])
    if rc != 0:
        return Failure(
            {
                "msg": "Failed to get information about SAP HANA system replication configuration",
                "rc": rc,
                "stdout": stdout,
                "stderr": stderr,
            }
        )
    return Success(
        {
            "hana_system_replication_info": get_hana_system_replication_info_from_stdout(
                stdout
            ),
            "rc": rc,
            "stdout": stdout,
            "stderr": stderr,
        }
    )


def run_module(hdbnsutil_run_command: Callable, params: dict):
    return get_hana_system_replication_info(hdbnsutil_run_command, params)


def main():
    module_args = dict()

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    hdbnsutil_run_command = get_hdbnsutil_run_command(module)
    result = run_module(
        params=module.params, hdbnsutil_run_command=hdbnsutil_run_command
    )

    if result.is_failure():
        module.fail_json(**result.result)
    module.exit_json(
        **result.result,
    )


if __name__ == "__main__":
    main()
