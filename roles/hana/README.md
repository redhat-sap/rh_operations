<!--
SPDX-License-Identifier: GPL-3.0-only
SPDX-FileCopyrightText: 2023-2024 Red Hat, Project Atmosphere

Copyright 2023-2024 Red Hat, Project Atmosphere

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

# hana

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`hana_state`](#parameter-hana_state)
  * [`hana_medium`](#parameter-hana_medium)
  * [`hana_master_password`](#parameter-hana_master_password)
  * [`hana_password`](#parameter-hana_password)
  * [`hana_sapadm_password`](#parameter-hana_sapadm_password)
  * [`hana_system_user_password`](#parameter-hana_system_user_password)
  * [`hana_root_password`](#parameter-hana_root_password)
  * [`hana_sid`](#parameter-hana_sid)
  * [`hana_instance_number`](#parameter-hana_instance_number)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Manage SAP HANA instance
> Role will not do anything is there is an instance already installed with SID=hana_sid or hana_instance_number is already occupied

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-hana_state"></a>`hana_state` | `str` | No | `"present"` | Defines if SAP HANA has to be installed or uninstalled.<br>*Choices:* present, absent |
| <a id="parameter-hana_medium"></a>`hana_medium` | `path` | Yes | N/A | Location of Installation Medium |
| <a id="parameter-hana_master_password"></a>`hana_master_password` | `str` | No | N/A | SAP HANA master password.<br><br>Master password is not required when all other passwords are set.<br><br>If any other password is not set it will default to master password. |
| <a id="parameter-hana_password"></a>`hana_password` | `str` | No | N/A | System Administrator Password (adm). If not set will default to hana_master_password variable. |
| <a id="parameter-hana_sapadm_password"></a>`hana_sapadm_password` | `str` | No | N/A | SAP Host Agent User (sapadm) password. If not set will default to hana_master_password variable. |
| <a id="parameter-hana_system_user_password"></a>`hana_system_user_password` | `str` | No | N/A | Database User Password. If not set will default to hana_master_password variable. |
| <a id="parameter-hana_root_password"></a>`hana_root_password` | `str` | No | N/A | Root User Password For Remote Hosts. If not set will default to hana_master_password variable. |
| <a id="parameter-hana_sid"></a>`hana_sid` | `str` | Yes | N/A | SAP HANA SID |
| <a id="parameter-hana_instance_number"></a>`hana_instance_number` | `str` | No | N/A | SAP HANA instance number |

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Role was tested only on single host.

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
