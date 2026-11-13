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

# sap_kernel_update

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`sap_kernel_update_instance`](#parameter-sap_kernel_update_instance)
  * [`sap_force_update`](#parameter-sap_force_update)
  * [`sap_kernel_update_sid`](#parameter-sap_kernel_update_sid)
  * [`sap_kernel_update_kernel_path`](#parameter-sap_kernel_update_kernel_path)
  * [`sap_kernel_update_new_kernel_path`](#parameter-sap_kernel_update_new_kernel_path)
  * [`sap_kernel_update_backup`](#parameter-sap_kernel_update_backup)
  * [`sap_kernel_update_kernel_backup_suffix`](#parameter-sap_kernel_update_kernel_backup_suffix)
* [Requirements](#requirements)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role replaces existing SAP kernel with kernel provided in SAP CAR files.

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-sap_kernel_update_instance"></a>`sap_kernel_update_instance` | `str` | Yes | N/A | The instance number to be managed. |
| <a id="parameter-sap_force_update"></a>`sap_force_update` | `str` | No | `false` | Update the system if rolling upgrade can't be used. Stop and start the system, so there is downtime. |
| <a id="parameter-sap_kernel_update_sid"></a>`sap_kernel_update_sid` | `str` | Yes | N/A | SAP System ID. |
| <a id="parameter-sap_kernel_update_kernel_path"></a>`sap_kernel_update_kernel_path` | `str` | Yes | N/A | Path to directory with installed SAP kernel. |
| <a id="parameter-sap_kernel_update_new_kernel_path"></a>`sap_kernel_update_new_kernel_path` | `str` | Yes | N/A | Path to new kernel. |
| <a id="parameter-sap_kernel_update_backup"></a>`sap_kernel_update_backup` | `str` | No | `true` | Backup previous kernel. |
| <a id="parameter-sap_kernel_update_kernel_backup_suffix"></a>`sap_kernel_update_kernel_backup_suffix` | `str` | No | `"backup-{{ ansible_date_time.iso8601_basic_short }}"` | Suffix that will be appended to the backup of the previous kernel. |

## Requirements<a id="requirements"></a>

Most role tasks must be executed under root account. Some tasks are executed under sidadm account.

SAPCAR binary must be installed on the host

## Example Playbooks<a id="examples"></a>

```ansible
- hosts: all
  tasks:
    - name: Update SAP kernel
      ansible.builtin.include_role:
        name: sap.sap_operations.sap_kernel_update
      vars:
        sap_kernel_update_sid: S4H
        sap_kernel_update_instance: "00"
        sap_kernel_update_kernel_path: /usr/sap/S4H/SYS/exe/uc/linuxx86_64
        sap_kernel_update_new_kernel_path: /tmp/new_kernel
```


## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

None

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Red Hat, Inc.


<!-- ANSIBLE DOCSMITH MAIN END -->
