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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`hana_update_sid`](#parameter-hana_update_sid)
  * [`hana_update_component_medium`](#parameter-hana_update_component_medium)
  * [`hana_update_master_password`](#parameter-hana_update_master_password)
  * [`hana_update_password`](#parameter-hana_update_password)
  * [`hana_update_sapadm_password`](#parameter-hana_update_sapadm_password)
  * [`hana_update_system_user_password`](#parameter-hana_update_system_user_password)
  * [`hana_update_root_password`](#parameter-hana_update_root_password)
  * [`hana_update_cleanup`](#parameter-hana_update_cleanup)
  * [`hana_update_hdb_installer_trace_file_default`](#parameter-hana_update_hdb_installer_trace_file_default)
  * [`hana_update_mapping`](#parameter-hana_update_mapping)
  * [`hana_update_options`](#parameter-hana_update_options)
    * [`hana_update_options['prepare_update']`](#parameter-hana_update_options/prepare_update)
    * [`hana_update_options['components']`](#parameter-hana_update_options/components)
    * [`hana_update_options['install_hostagent']`](#parameter-hana_update_options/install_hostagent)
    * [`hana_update_options['check_only']`](#parameter-hana_update_options/check_only)
    * [`hana_update_options['verify_signature']`](#parameter-hana_update_options/verify_signature)
    * [`hana_update_options['update_execution_mode']`](#parameter-hana_update_options/update_execution_mode)
    * [`hana_update_options['configure_python']`](#parameter-hana_update_options/configure_python)
    * [`hana_update_options['scope']`](#parameter-hana_update_options/scope)
    * [`hana_update_options['hana_update_hdb_installer_trace_file']`](#parameter-hana_update_options/hana_update_hdb_installer_trace_file)
    * [`hana_update_options['hdblcm_logdir_copy']`](#parameter-hana_update_options/hdblcm_logdir_copy)
    * [`hana_update_options['component_dirs']`](#parameter-hana_update_options/component_dirs)
    * [`hana_update_options['ignore']`](#parameter-hana_update_options/ignore)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role updates a SAP HANA system or instance on a given host.
> A path to new HANA version installation is required. It can be specified by variable hana_update_component_medium
> Limitations:
> - Role was tested only on single host.
> - During upgrade hdblcm is configured to use SSH (not saphostagent) to connect to the host.
> - Role only works on X86_64
> - Role is not idempotent. It will always try to update SAP HANA system.
> - Expected that hdblcm tool will take care of any issues (like updating to previous version)

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-hana_update_sid"></a>`hana_update_sid` | `str` | Yes | N/A | SAP HANA System ID. |
| <a id="parameter-hana_update_component_medium"></a>`hana_update_component_medium` | `str` | Yes | N/A | Location of Installation Medium |
| <a id="parameter-hana_update_master_password"></a>`hana_update_master_password` | `str` | No | N/A | SAP HANA update master password.<br><br>Master password is not required when all other passwords are set.<br><br>If any other password is not set it will default to master password. |
| <a id="parameter-hana_update_password"></a>`hana_update_password` | `str` | No | N/A | System Administrator Password (adm). If not set will default to hana_update_master_password variable. |
| <a id="parameter-hana_update_sapadm_password"></a>`hana_update_sapadm_password` | `str` | No | N/A | SAP Host Agent User (sapadm) password. If not set will default to hana_update_master_password variable. |
| <a id="parameter-hana_update_system_user_password"></a>`hana_update_system_user_password` | `str` | No | N/A | Database User Password. If not set will default to hana_update_master_password variable. |
| <a id="parameter-hana_update_root_password"></a>`hana_update_root_password` | `str` | No | N/A | Root User Password For Remote Hosts. If not set will default to hana_update_master_password variable. |
| <a id="parameter-hana_update_cleanup"></a>`hana_update_cleanup` | `bool` | No | `true` | If set to `true` xml file with passwords will be removed after installation (failed or successful).<br><br>Recommendation is always keep default value for this parameter `true` to avoid having passwords in plain text. |
| <a id="parameter-hana_update_hdb_installer_trace_file_default"></a>`hana_update_hdb_installer_trace_file_default` | `path` | No | `"/tmp/hdb_installer_trace_file.trc"` | Default location of the trace file for the SAP HANA hdblcm installer. |
| <a id="parameter-hana_update_mapping"></a>`hana_update_mapping` | `dict` | No | N/A | Mapping of SAP component numbers to SAP HANA component names. |
| <a id="parameter-hana_update_options"></a>`hana_update_options` | `dict` | No | N/A | Optional arguments for SAP HANA update |
| <a id="parameter-hana_update_options/prepare_update"></a>`hana_update_options['prepare_update']` | `bool` | No | N/A | Stop update before software version switch, resumable ( Default n=false ) |
| <a id="parameter-hana_update_options/components"></a>`hana_update_options['components']` | `str` | No | N/A | Components ( Valid values: all \| client \| es \| ets \| lcapps \| server \| smartda \| streaming \| rdsync \| xs \| studio \| afl \| sca \| sop \| eml \| rme \| rtl \| trp )<br>*Choices:* all, client, es, ets, lcapps, server, smartda, streaming, rdsync, xs, studio, afl, sca, sop, eml, rme, rtl, trp |
| <a id="parameter-hana_update_options/install_hostagent"></a>`hana_update_options['install_hostagent']` | `bool` | No | N/A | Enable the installation or upgrade of the SAP Host Agent ( Default y = true) |
| <a id="parameter-hana_update_options/check_only"></a>`hana_update_options['check_only']` | `bool` | No | N/A | Execute checks, do not update SAP HANA System ( Default n = false) |
| <a id="parameter-hana_update_options/verify_signature"></a>`hana_update_options['verify_signature']` | `bool` | No | N/A | Verify the authenticity of SAP HANA components ( Default: n = false) |
| <a id="parameter-hana_update_options/update_execution_mode"></a>`hana_update_options['update_execution_mode']` | `str` | No | N/A | Update Execution Mode ( Default: standard; Valid values: standard \| optimized )<br>*Choices:* standard, optimized |
| <a id="parameter-hana_update_options/configure_python"></a>`hana_update_options['configure_python']` | `str` | No | N/A | Configure Python version ( Default: python2; Valid values: python2 \| python3 )<br>*Choices:* python2, python3 |
| <a id="parameter-hana_update_options/scope"></a>`hana_update_options['scope']` | `str` | No | N/A | Execution Scope ( Default: system; Valid values: instance \| system )<br>*Choices:* instance, system |
| <a id="parameter-hana_update_options/hana_update_hdb_installer_trace_file"></a>`hana_update_options['hana_update_hdb_installer_trace_file']` | `path` | No | `""` | Sets environment variable HDB_INSTALLER_TRACE_FILE to enable SAP HANA hdblcm trace. The environment variable 'HDB_INSTALLER_TRACE_FILE=' enables the trace. |
| <a id="parameter-hana_update_options/hdblcm_logdir_copy"></a>`hana_update_options['hdblcm_logdir_copy']` | `path` | No | `""` | Sets environment variable HDBLCM_LOGDIR_COPY to enable SAP HANA logs copy. The environment variable HDBLCM_LOGDIR_COPY= creates a copy of the log directory. |
| <a id="parameter-hana_update_options/component_dirs"></a>`hana_update_options['component_dirs']` | `list` | No | N/A | List of component directories |
| <a id="parameter-hana_update_options/ignore"></a>`hana_update_options['ignore']` | `list` | No | N/A | Specifies failing prerequisite checks that the SAP HANA platform lifecycle management tools should ignore.<br>*Choices:* check_busy_files, check_component_dependencies, check_diskspace, check_min_mem, check_pending_upgrade, check_platform, check_resume_hostname, check_signature_file, check_version, verify_signature |

## Example Playbooks<a id="examples"></a>

q""q
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

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Role was tested only on single host.

During upgrade hdblcm is configured to use SSH (not saphostagent) to connect to the host.

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
