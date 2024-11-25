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


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.sap.sap_operations.plugins.module_utils.common import (  # noqa: E501
    convert_string2bool,
)


class AnsibleModuleEnqAdmin(AnsibleModule):
    def __init__(
        self,
        argument_spec=None,
        required_together=None,
        mutually_exclusive=None,
        required_one_of=None,
        supports_check_mode=False,
        required_if=None,
        required_by=None,
    ):
        """Custom AnsibleModule for enq_admin tool."""
        enq_admin_argument_spec = dict(
            profile_filepath=dict(
                type="path", required=False, aliases=["pf", "profile"]
            ),
            sid=dict(type="str", required=False),
            hostname=dict(type="str", required=False, aliases=["host"]),
            port=dict(type="int", required=False),
        )
        enq_admin_required_together = [["sid", "hostname", "port"]]
        enq_admin_mutually_exclusive = [
            ["profile_filepath", "sid"],
            ["profile_filepath", "hostname"],
            ["profile_filepath", "port"],
        ]
        enq_admin_required_one_of = [["profile_filepath", "sid", "hostname", "port"]]

        if argument_spec is not None:
            argument_spec = {
                k: v
                for d in (argument_spec, enq_admin_argument_spec)
                for k, v in d.items()
            }
        else:
            argument_spec = enq_admin_argument_spec
        required_together = [] if required_together is None else required_together
        mutually_exclusive = [] if mutually_exclusive is None else mutually_exclusive
        required_one_of = [] if required_one_of is None else required_one_of
        required_if = [] if required_if is None else required_if
        required_by = {} if required_by is None else required_by

        super(AnsibleModuleEnqAdmin, self).__init__(
            argument_spec=argument_spec,
            mutually_exclusive=mutually_exclusive + enq_admin_mutually_exclusive,
            required_together=required_together + enq_admin_required_together,
            required_one_of=required_one_of + enq_admin_required_one_of,
            supports_check_mode=supports_check_mode,
            required_if=required_if,
            required_by=required_by,
        )


def run_enq_admin(args, module=None):
    if module is None:
        return (0, "", "module is required")

    profile_filepath = module.params.get("profile_filepath")
    sid = module.params.get("sid")
    hostname = module.params.get("hostname")
    port = module.params.get("port")

    enq_admin_path = module.get_bin_path("enq_admin")

    if profile_filepath:
        default_args = [enq_admin_path, "pf={0}".format(profile_filepath)]
    else:
        default_args = [
            enq_admin_path,
            "--sid={0}".format(sid),
            "--host={0}".format(hostname),
            "--port={0}".format(port),
        ]

    return module.run_command(default_args + args)


def get_table_from_csv_data(data):
    data_lines = data.split("\n")
    if len(data_lines) < 2:
        return dict(
            table=[],
            table_name="",
        )
    table_name = data_lines[0].strip().strip(":")
    column_names = data_lines[1].split(";")
    column_names = [name.strip() for name in column_names if name != ""]
    table = []
    for row in data_lines[2:]:
        values = row.split(";")
        values = [convert_string2bool(value) for value in values]
        table.append(dict(zip(column_names, values)))

    return dict(
        table=table,
        table_name=table_name,
    )


def enq_admin_process_stdout(stdout):
    [header, data, footer] = stdout.split("\n\n")
    table = get_table_from_csv_data(data)
    return dict(
        header=header,
        data=data,
        footer=footer,
        table=table["table"],
        table_name=table["table_name"],
    )


long_lock_type = {
    "X": "Exclusive",
    "E": "Write",
    "S": "Read",
    "O": "Optimistic",
}


def lock_has_same_attributes(lock, lock_type, owner1, owner2, name, argument):
    return (
        lock["Type"] == long_lock_type[lock_type]
        and lock["Owner 1"] == owner1
        and lock["Owner 2"] == owner2
        and lock["Name"] == name
        and lock["Argument"] == argument
    )


def exclusive_lock_with_same_attributes_exists(
    lock, lock_type, owner1, owner2, name, argument
):
    return (
        lock["Type"] == long_lock_type["X"]
        and lock["Owner 1"] == owner1
        and lock["Owner 2"] == owner2
        and lock["Name"] == name
        and lock["Argument"] == argument
    )


def find_locks_in_locks_list(locks, lock_type, owner1, owner2, name, argument):
    return [
        lock
        for lock in locks
        if lock_has_same_attributes(lock, lock_type, owner1, owner2, name, argument)
        or exclusive_lock_with_same_attributes_exists(
            lock, lock_type, owner1, owner2, name, argument
        )
    ]


def lock_exists_in_locks_list(locks, lock_type, owner1, owner2, name, argument):
    return (
        len(find_locks_in_locks_list(locks, lock_type, owner1, owner2, name, argument))
        > 0
    )


def get_enq_admin_locks_info(
    module, run_enq_admin, n="*", client="*", user="*", name="*", argument="*"
):
    args = [
        "--csv",
        "--no_color",
        "--locks={0}:{1}:{2}:{3}:{4}".format(n, client, user, name, argument),
    ]

    rc, stdout, stderr = run_enq_admin(module=module, args=args)

    if rc == 0:
        data = enq_admin_process_stdout(stdout)
        return dict(changed=False, stdout=stdout, enq_admin_locks_info=data["table"])
    return dict(
        failed=True,
        msg="Failed to get information from enq_admin tool",
        stderr=stderr,
        stdout=stdout,
        rc=rc,
    )


def ensure_locks(
    state, lock_type, owner1, owner2, name, argument, run_enq_admin, module
):
    lock_command = "--set_locks" if state == "present" else "--release_locks"
    args = [
        "--csv",
        "--no_color",
        "{0}=1:{1}:{2}:{3}:{4}:{5}".format(
            lock_command, lock_type, owner1, owner2, name, argument
        ),
    ]

    rc, stdout, stderr = run_enq_admin(module=module, args=args)
    return rc, stdout, stderr
