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
# If not, see <https://www.gnu.org/licenses/>

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: hana_restore

extends_documentation_fragment: sap.sap_operations.community

author:
  - Ondra Machacek (@machacekondra)
  - Kirill Satarin (@kksat)

short_description: Restore SAP HANA database backup

description:
  - Restores HANA system or tenant DB backup. Currently it is possible to perform timestamp
    restore or restore to specific full backup.

version_added: 1.12.0

seealso:
  - module: sap.sap_operations.hana_restore

options:

  hdbsqluserstore_key:
    description:
      - hdbuserstore record to be used to connect to database.
    type: str

  hana_db_system_password:
    description:
      - Password for HANA SYSTEM database user.
    type: str

  database_name:
    description:
      - SAP HANA system tenant or SYSTEMDB to restore. If not provided SYSTEMDB is default value.
    type: str
    default: "SYSTEMDB"

  full_backup_type:
    description:
      - Path to full backup to use for restore.
    type: str
    choices: [FILE, BACKINT]
    default: FILE

  full_backup:
    description:
      - Path to full backup to use for restore.
      - It ends with prefix used to create full backup (full backup consists of multiple files).
      - It can be absolute or relative path.
      - Mutually exclusive with I(timestamp_backup).
    type: path

  timestamp_backup:
    description:
      - Recovers an SAP HANA database to a specific point in time.
      - Timestamp is always in UTC timezone.
      - "Example 2022-01-02 11:22:33."
      - Empty string means now.
      - Mutually exclusive with I(full_backup).
    type: str
    default: ''

  using:
    description:
      - Specify non-default catalog/data/log path.
      - Use if files are mounted on different path then when they were created.
    type: dict
    suboptions:
      catalog_path:
        description:
          - Catalog path.
        type: path
      data_path:
        description:
          - Data path.
        type: list
        elements: path
      log_path:
        description:
          - Log path.
        type: list
        elements: path

  clear_log:
    description:
      - Prevent entries from the log area from being used for the recovery.
      - No log entries from the log area are replayed, and the log area is initialized.
      - As a consequence, the content of the log area is lost.
      - For I(timestamp_backup) prevents the recovery of entries from the log area. No log entries from the
        log area are replayed, and the log area is initialized. As a consequence, the content of the log area is lost.
      - You must set I(clear_log) in the following situation the log area is unusable or recovering the database to a different system.
    type: bool
    default: False

  instance_directory:
    description:
      - Path to instance directory.
    type: str
    default: ''

"""  # noqa E501

EXAMPLES = """
---
- name: Fetch the binary path of the hdbsql
  sap.sap_operations.parameter_info:
    instance_number: "00"
    name: DIR_INSTANCE
  register: dir_instance

- name: Restore HANA SYSTEMDB to latest state
  sap.sap_operations.hana_restore:
    hana_db_system_password: CHANGEME
    database_name: SYSTEMDB
    instance_directory: "{{ dir_instance.parameter_value | first }}"
  become: true
  become_user: rheadm

- name: Restore HANA for RHE tenant to specific timestamp
  sap.sap_operations.hana_restore:
    instance_directory: "{{ dir_instance.parameter_value | first }}"
    hana_db_system_password: CHANGEME
    instance_number: "00"
    timestamp_backup: '2022-01-17 23:59:59'
  become: true
  become_user: rheadm

- name: Restore HANA for RHE tenant to specific full backup
  sap.sap_operations.hana_restore:
    hana_db_system_password: CHANGEME
    full_backup: MONDAY
  become: true
  become_user: rheadm

- name: Restore HANA for TENANT2@RHE tenant from PR1@PR1 tenant to specific full backup
  sap.sap_operations.hana_restore:
    hana_db_system_password: CHANGEME
    database_name: TENANT2
    full_backup: '/hana/PR1/backup/MONDAY'
  become: true
  become_user: rheadm

- name: Restore HANA for TENANT2@RHE tenant from PR1@PR1 tenant to specific timestamp
  sap.sap_operations.hana_restore:
    hana_db_system_password: CHANGEME
    database_name: TENANT2
    clear_log: true
    timestamp_backup: '2022-01-17 23:59:59'
    using:
      catalog_path: /hana/PR1/backup/catalog
      data_path: [/hana/PR1/backup/data]
      log_path: [/hana/PR1/backup/log]
  become: true
  become_user: rheadm
"""

RETURN = """ # """

from ansible.module_utils.basic import AnsibleModule
import os


def get_path_sql(module, key):
    """Get SQL path.

    key=catalog_path - is always a single path
    key=data_path or log_path - each is a list of path entries
    """
    using = module.params["using"]
    if not using:
        return ""

    path_value = using.get(key)
    if not path_value:
        return ""

    if key == "catalog_path":
        return "USING CATALOG PATH ('{0}')".format(path_value)

    path_name = "DATA" if key == "data_path" else "LOG"
    path_value_quoted = ["'{0}'".format(pp) for pp in path_value if pp]
    if not path_value_quoted:
        return ""
    path_list = ",".join(path_value_quoted)
    return "USING {0} PATH ({1})".format(path_name, path_list)


def construct(all, string):
    if string:
        return " ".join([all, string])
    return all


def build_sql(module):
    sql_for_tenant = ""
    if module.params["database_name"] != "SYSTEMDB":
        sql_for_tenant = "FOR {0}".format(module.params["database_name"])

    sql_clear_log = ""
    if module.params["clear_log"] or module.params["full_backup"]:
        sql_clear_log = "CLEAR LOG"

    if module.params["timestamp_backup"]:
        query = "RECOVER DATABASE"
        query = construct(query, sql_for_tenant)
        query = construct(
            query, "UNTIL TIMESTAMP '{0}'".format(module.params["timestamp_backup"])
        )
        query = construct(query, get_path_sql(module, "catalog_path"))
        query = construct(query, get_path_sql(module, "data_path"))
        query = construct(query, get_path_sql(module, "log_path"))
        return construct(query, "CHECK ACCESS ALL")
    else:
        query = "RECOVER DATA"
        query = construct(query, sql_for_tenant)
        query = construct(
            query,
            "USING {0}('{1}')".format(
                module.params["full_backup_type"], module.params["full_backup"]
            ),
        )
        return construct(query, sql_clear_log)


def get_hdbsql_cmd(module):
    binary_path = os.path.join(module.params.get("instance_directory"), "hdbsql")
    args = [binary_path]
    if module.params.get("hana_db_system_password"):
        args.extend(
            [
                "-x",
                "-a",
                "-u",
                "SYSTEM",
                "-p",
                module.params.get("hana_db_system_password"),
            ]
        )
    elif module.params.get("hdbsqluserstore_key"):
        args.extend(["-x", "-a", "-U", module.params.get("hdbsqluserstore_key")])
    return args


def run_command(module, args):
    return module.run_command(args=args)


def list_deactivated_tenant_dbs(module):
    return _list_tenant_dbs(module, "NO")


def list_activated_tenant_dbs(module):
    return _list_tenant_dbs(module, "YES")


def _list_tenant_dbs(module, state):
    sql_list_dbs = 'SELECT DATABASE_NAME,ACTIVE_STATUS from "SYS"."M_DATABASES"'
    hdbsql_cmd = get_hdbsql_cmd(module)
    rc, stdout, _stderr = run_command(hdbsql_cmd, sql_list_dbs)
    if rc:
        raise module.fail_json(stdout)

    dbs = []
    for line in stdout.splitlines():
        db_name, db_active = line.split(",")
        if db_active.strip('"') == state:
            dbs.append(db_name.strip('"'))
    return dbs


def tenant_db_start_stop(module, db_name, state):
    hdbsql_cmd = get_hdbsql_cmd(module)
    sql_alter_system = "ALTER SYSTEM {0} DATABASE {1}".format(state, db_name)
    rc, _stdout, _stderr = run_command(hdbsql_cmd, sql_alter_system)
    if rc:
        raise module.fail_json(_stdout)


def start_tenant_dbs(module):
    dbs = list_deactivated_tenant_dbs(module)
    for db_name in dbs:
        tenant_db_start_stop(module, db_name, "START")


def ensure_backup_restored(module):
    hdbsql_cmd = get_hdbsql_cmd(module)
    sql_cmd = build_sql(module)
    if module.params["database_name"] == "SYSTEMDB":
        hdbsettings_sh = os.path.join(
            module.params["instance_directory"], "HDBSettings.sh"
        )
        cmd = [hdbsettings_sh, "recoverSys.py", "--command", sql_cmd]
        rc, stdout, stderr = run_command(module, cmd)
        if rc:
            raise module.fail_json(stdout)
        start_tenant_dbs(module)
        return True, stdout, stderr, cmd
    else:
        tenant_db_start_stop(module, module.params["database_name"], "STOP")
        rc, stdout, stderr = run_command(hdbsql_cmd, sql_cmd)
        if rc:
            raise module.fail_json(stdout)
        return True, stdout, stderr, sql_cmd


def main():
    module_args = dict(
        database_name=dict(type="str", default="SYSTEMDB"),
        instance_directory=dict(type="str", default=""),
        clear_log=dict(default=False, type="bool"),
        hana_db_system_password=dict(type="str", no_log=True),
        hdbsqluserstore_key=dict(type="str", no_log=False),
        full_backup=dict(type="path"),
        full_backup_type=dict(type="str", choices=["FILE", "BACKINT"], default="FILE"),
        timestamp_backup=dict(default="", type="str"),
        using=dict(
            type="dict",
            options=dict(
                catalog_path=dict(type="path"),
                data_path=dict(elements="path", type="list"),
                log_path=dict(elements="path", type="list"),
            ),
        ),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_one_of=[
            ["hana_db_system_password", "hdbsqluserstore_key"],
        ],
        mutually_exclusive=[
            ["full_backup", "timestamp_backup"],
            ["full_backup_type", "timestamp_backup"],
        ],
    )
    changed, out, err, args = ensure_backup_restored(module)
    module.exit_json(changed=changed, stdout=out, stderr=err, cmd=args)


if __name__ == "__main__":
    main()
