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

Manage SAP HANA instance


Manage SAP HANA instance
Role will not do anything is there is an instance already installed with SID=hana_sid or hana_instance_number is already occupied



## Role Variables

### Required parameters:


- [hana_medium](#hana_medium)

- [hana_sid](#hana_sid)
 

#### hana_medium


_Type:_ `path`


_Required:_ `True`
_Description:_
Location of Installation Medium

 

#### hana_sid


_Type:_ `str`


_Required:_ `True`
_Description:_
SAP HANA SID

 

#### hana_state


_Type:_ `str`

_Default:_ `present`

_Required:_ `False`
_Choices:_
- present
- absent
_Description:_
Defines if SAP HANA has to be installed or uninstalled.

 

#### hana_master_password


_Type:_ `str`


_Required:_ `False`
_Description:_
SAP HANA master password.
Master password is not required when all other passwords are set.
If any other password is not set it will default to master password.

 

#### hana_password


_Type:_ `str`


_Required:_ `False`
_Description:_
System Administrator Password (<sid>adm). If not set will default to hana_master_password variable.

 

#### hana_sapadm_password


_Type:_ `str`


_Required:_ `False`
_Description:_
SAP Host Agent User (sapadm) password. If not set will default to hana_master_password variable.

 

#### hana_system_user_password


_Type:_ `str`


_Required:_ `False`
_Description:_
Database User Password. If not set will default to hana_master_password variable.

 

#### hana_root_password


_Type:_ `str`


_Required:_ `False`
_Description:_
Root User Password For Remote Hosts. If not set will default to hana_master_password variable.

 

#### hana_instance_number


_Type:_ `str`


_Required:_ `False`
_Description:_
SAP HANA instance number

 
 

## Limitations

Role was tested only on single host.

## Dependencies

Role has no dependencies to other roles.

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
