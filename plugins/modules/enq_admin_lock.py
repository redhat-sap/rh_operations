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
module: enq_admin_lock

extends_documentation_fragment:
  - sap.sap_operations.community
  - sap.sap_operations.enq_admin

author:
  - Kirill Satarin (@kksat)

short_description: Manage enque server locks for ENSA2 SAP instances
version_added: 1.29.0
description:
  - Manage enque server locks for ENSA2 SAP instances
  - This module will set/release only one lock at a time (parameter n for enq_admin equals 1, see documentation)
  - If several locks are needed, use this module several times or in loop, see examples
  - If exclusive lock is set, other locks will not be created, information about existing exclusive lock will be created
  - Module is idempotent, new locks will not be created if this type of lock or exclusive lock already exists with the same parameters
  - |
    Value '%u' for parameters is not supported - because only one lock is set/released at a time,
    this is not handled by this module. Use ansible loops for this.

options:
  state:
    description: State of the lock (present or absent)
    required: false
    type: str
    default: "present"
    choices:
      - absent
      - present
  lock_type:
    description:
      - Lock type
      - X - Exclusive lock ("Exclusive")
      - E - Exclusive non cumulative lock ("Write")
      - S - Shared lock ("Read")
      - O - Optimistic lock ("Optimistic")
      - if exclusive lock is set, other locks are not allowed
    required: true
    type: str
    aliases:
      - type
    choices:
      - X
      - E
      - S
      - O
  owner1:
    description: Pattern for dialog lock owner
    required: false
    type: str
    default: ""
  owner2:
    description: Pattern for update lock owner
    required: false
    type: str
    default: ""
  name:
    description: Pattern for lock name
    required: false
    type: str
    default: ""
  argument:
    description:
      - Pattern for lock argument
    required: false
    type: str
    default: ""
"""

EXAMPLES = r"""
---
- name: Set lock
  sap.sap_operations.enq_admin_lock:
    pf: /usr/sap/S4H/SYS/profile/S4H_ASCS20_s4ascsa
    state: present
    lock_type: E
    owner1: DIAG
    owner2: ""
    name: ANSIBLE
    argument: ANSIBLE

- name: Release lock
  sap.sap_operations.enq_admin_lock:
    pf: /usr/sap/S4H/SYS/profile/S4H_ASCS20_s4ascsa
    state: absent
    lock_type: E
    owner1: DIAG
    owner2: ""
    name: ANSIBLE
    argument: ANSIBLE
"""

RETURN = r"""
---
enq_admin_lock:
  description: Lock information
  returned: if state is present and execution was successful
  type: dict
  sample:
    Argument: ANSIBLE
    BCK: false
    Client: '000'
    Count 1: '1'
    Count 2: '0'
    Name: ANSIBLE
    Object: E_FILL
    Owner 1: DIAG
    Owner 2: ''
    TCODE: SFILL
    Type: Write
    User: FILL_USER
"""


from ansible_collections.sap.sap_operations.plugins.module_utils.enq_admin import (
    AnsibleModuleEnqAdmin,
    find_locks_in_locks_list,
    run_enq_admin,
    get_enq_admin_locks_info,
    ensure_locks,
)


def run_module(module, run_enq_admin):
    lock_type = module.params.get("lock_type")
    owner1 = module.params.get("owner1")
    owner2 = module.params.get("owner2")
    name = module.params.get("name")
    argument = module.params.get("argument")
    state = module.params.get("state", "present")

    existing_locks = get_enq_admin_locks_info(
        module=module, run_enq_admin=run_enq_admin
    )
    if existing_locks.get("failed"):
        return dict(
            failed=True,
            msg="Failed to get existing locks from enq_admin tool",
            stdout=existing_locks.get("stdout"),
            stderr=existing_locks.get("stderr"),
            rc=existing_locks.get("rc"),
        )

    existing_locks = find_locks_in_locks_list(
        locks=existing_locks.get("enq_admin_locks_info", []),
        lock_type=lock_type,
        owner1=owner1,
        owner2=owner2,
        name=name,
        argument=argument,
    )
    if state == "present" and existing_locks:
        return dict(
            changed=False,
            enq_admin_lock=existing_locks[0],
        )
    elif state == "present" and not existing_locks:
        rc, stdout, stderr = ensure_locks(
            state, lock_type, owner1, owner2, name, argument, run_enq_admin, module
        )

        if rc == 0:
            created_locks = get_enq_admin_locks_info(
                module=module, run_enq_admin=run_enq_admin
            )
            if created_locks.get("failed"):
                return dict(
                    failed=True,
                    msg="Failed to get locks from enq_admin tool",
                    stdout=created_locks.get("stdout"),
                    stderr=created_locks.get("stderr"),
                    rc=created_locks.get("rc"),
                )

            created_locks = find_locks_in_locks_list(
                locks=created_locks.get("enq_admin_locks_info", []),
                lock_type=lock_type,
                owner1=owner1,
                owner2=owner2,
                name=name,
                argument=argument,
            )
            if not created_locks:
                return dict(
                    failed=True,
                    msg="Failed to get created lock from enq_admin tool",
                    stdout=created_locks.get("stdout"),
                    stderr=created_locks.get("stderr"),
                    rc=created_locks.get("rc"),
                )

            return dict(changed=True, enq_admin_lock=created_locks[0])
        else:
            return dict(
                failed=True,
                msg="Failed to get information from enq_admin tool",
                stderr=stderr,
            )

    if state == "absent" and not existing_locks:
        return dict(
            changed=False,
            enq_admin_lock=[],
        )

    if state == "absent" and existing_locks:
        rc, stdout, stderr = ensure_locks(
            state, lock_type, owner1, owner2, name, argument, run_enq_admin, module
        )
        if rc == 0:
            return dict(changed=True, enq_admin_lock=[])
        else:
            return dict(
                failed=True,
                msg="Failed to release enq_admin tool",
                stderr=stderr,
                stdout=stdout,
                rc=rc,
            )


def main():
    argument_spec = dict(
        state=dict(type="str", choices=["absent", "present"], default="present"),
        lock_type=dict(
            type="str", choices=["X", "E", "S", "O"], aliases=["type"], required=True
        ),
        owner1=dict(type="str", default=""),
        owner2=dict(type="str", default=""),
        name=dict(type="str", default=""),
        argument=dict(type="str", default=""),
    )

    module = AnsibleModuleEnqAdmin(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    result = run_module(module, run_enq_admin=run_enq_admin)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
