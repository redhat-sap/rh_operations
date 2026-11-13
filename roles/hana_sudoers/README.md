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

# hana_sudoers

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`hana_sudoers_sids`](#parameter-hana_sudoers_sids)
  * [`hana_sudoers_state`](#parameter-hana_sudoers_state)
  * [`hana_sudoers_data_centers`](#parameter-hana_sudoers_data_centers)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Manage SAP HANA sudoers records
> See https://access.redhat.com/articles/6093611
> Role requires root access

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-hana_sudoers_sids"></a>`hana_sudoers_sids` | `list of str` | No | `[]` | SAP HANA sid (system id) to configure sudoers file<br><br>Can be list of single value<br><br>If not defined or is empty list, list of installed SAP HANA instances will be determined by the role |
| <a id="parameter-hana_sudoers_state"></a>`hana_sudoers_state` | `str` | No | `"present"` | Ensure records are present or absent in sudoers file<br>*Choices:* present, absent |
| <a id="parameter-hana_sudoers_data_centers"></a>`hana_sudoers_data_centers` | `str` | No | `"['*']"` | List of data centers to create records for. By default records will not be limited to datacenter (see default value) |

## Example Playbooks<a id="examples"></a>



## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Role was tested only on x86_64 architecture

Role tested only for scaleup systems

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
