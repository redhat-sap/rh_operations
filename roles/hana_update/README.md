<!--
SPDX-License-Identifier: GPL-3.0-only
SPDX-FileCopyrightText: 2023 Red Hat, Project Atmosphere

Copyright 2023 Red Hat, Project Atmosphere

This program is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

You should have received a copy of the GNU General Public License along with this program.
If not, see <https://www.gnu.org/licenses/>.
-->

# hana_update

Role updates a SAP HANA system or instance on a given host.

A path to new HANA version installation is required.

It can be specified by variable hana_update_component_medium

## Requirements

Role requires 'unzip' command to be installed. Role uses module 'ansible.builtin.unarchive', see documentation for that module.

SAPCAR should be installed in location 'unpack_sapcar_exe_path' (collection variable 'sap_operations_sapcar_exe_path'). Variable 'unpack_sapcar_exe_path' has precedence over 'sap_operations_sapcar_exe_path', if variable 'unpack_sapcar_exe_path' is set, value of variable 'sap_operations_sapcar_exe_path' is ignored.

## Limitations

Role was tested only on single host.

During upgrade hdblcm is configured to use SSH (not saphostagent) to connect to the host.

Role only works on X86_64

Role is not idempotent. It will always try to update SAP HANA system.
Expected that hdblcm tool will take care of any issues (like updating to previous version)

<!-- BEGIN: Role Input Parameters -->

## Role Variables

Required parameters:

- [hana_update_component_medium](#hana_update_component_medium)

- [hana_update_sid](#hana_update_sid)

### hana_update_component_medium

- _Type:_ `str`
- _Required:_ `True`

Location of Installation Medium

### hana_update_sid

- _Type:_ `str`
- _Required:_ `True`

SAP HANA System ID.

### hana_update_cleanup

- _Type:_ `bool`
- _Default:_ `True`
- _Required:_ `False`

If set to true xml file with passwords will be removed after installation (failed or successful).
Recommendation is always keep default value for this parameter (true) to avoid having passwords in plain text.

### hana_update_master_password

- _Type:_ `str`
- _Required:_ `False`

SAP HANA update master password.
Master password is not required when all other passwords are set.
If any other password is not set it will default to master password.

### hana_update_options

- _Type:_ `dict`
- _Required:_ `False`

Optional arguments for SAP HANA update

  - **check_only**<br>
            Execute checks, do not update SAP HANA System ( Default: n = false)

      - **component_dirs**<br>
            List of component directories

      - **components**<br>
            Components ( Valid values: all | client | es | ets | lcapps | server | smartda | streaming | rdsync | xs | studio | afl | sca | sop | eml | rme | rtl | trp )

      - **configure_python**<br>
            Configure Python version ( Default: python2; Valid values: python2 | python3 )

      - **hana_update_hdb_installer_trace_file**<br>
        _Default:_ ``<br>
            Sets environment variable HDB_INSTALLER_TRACE_FILE to enable SAP HANA hdblcm trace.
The environment variable 'HDB_INSTALLER_TRACE_FILE=<file>' enables the trace.

      - **hdblcm_logdir_copy**<br>
        _Default:_ ``<br>
            Sets environment variable HDBLCM_LOGDIR_COPY to enable SAP HANA logs copy.
The environment variable HDBLCM_LOGDIR_COPY=<target directory> creates a copy of the log directory.

      - **ignore**<br>
            Specifies failing prerequisite checks that the SAP HANA platform lifecycle management tools should ignore.

      - **install_hostagent**<br>
            Enable the installation or upgrade of the SAP Host Agent ( Default: y = true)

      - **prepare_update**<br>
            Stop update before software version switch, resumable ( Default: n=false )

      - **scope**<br>
            Execution Scope ( Default: system; Valid values: instance | system )

      - **update_execution_mode**<br>
            Update Execution Mode ( Default: standard; Valid values: standard | optimized )

      - **verify_signature**<br>
            Verify the authenticity of SAP HANA components ( Default: n = false)

    
### hana_update_password

- _Type:_ `str`
- _Required:_ `False`

System Administrator Password (<sid>adm). If not set will default to hana_update_master_password variable.

### hana_update_root_password

- _Type:_ `str`
- _Required:_ `False`

Root User Password For Remote Hosts. If not set will default to hana_update_master_password variable.

### hana_update_sapadm_password

- _Type:_ `str`
- _Required:_ `False`

SAP Host Agent User (sapadm) password. If not set will default to hana_update_master_password variable.

### hana_update_system_user_password

- _Type:_ `str`
- _Required:_ `False`

Database User Password. If not set will default to hana_update_master_password variable.

<!-- END: Role Input Parameters -->

## Dependencies

Role has no dependencies to other roles.

## Example Playbook

```ansible
- hosts: all
  tasks:
    - name: Update SAP HANA
      ansible.builtin.include_role:
        name: sap.sap_operations.hana_update
      vars:
        hana_update_sid: HAN
        hana_update_password: "SecurePa$$word"
        hana_update_sapadm_password: "SecurePa$$word"
        hana_update_system_user_password: "SecurePa$$word"
        hana_update_root_password: "SecurePa$$word"
        hana_update_component_medium: /hana/software/HANAsp06
        hana_update_options:
          prepare_update: false
          components: server
          install_hostagent: false
          check_only: false
          verify_signature: true
          update_execution_mode: standard
          configure_python: python3
          scope: system
```

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
