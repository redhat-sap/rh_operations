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

Manage SAP HANA sudoers records


Manage SAP HANA sudoers records
See https://access.redhat.com/articles/6093611
Role requires root access



## Role Variables

### Required parameters:

 

#### hana_sudoers_sids


_Type:_ `list`

_Default:_ `[]`

_Required:_ `False`
_Description:_
SAP HANA sid (system id) to configure sudoers file
Can be list of single value
If not defined or is empty list, list of installed SAP HANA instances will be determined by the role

 

#### hana_sudoers_state


_Type:_ `str`

_Default:_ `present`

_Required:_ `False`
_Choices:_
- present
- absent
_Description:_
Ensure records are present or absent in sudoers file

 

#### hana_sudoers_data_centers


_Type:_ `str`

_Default:_ `['*']`

_Required:_ `False`
_Description:_
List of data centers to create records for. By default records will not be limited to datacenter (see default value)

 
 

## Limitations

Role was tested only on x86_64 architecture
Role tested only for scaleup systems

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks



## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
