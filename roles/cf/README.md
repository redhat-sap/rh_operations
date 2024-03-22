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

# cf

Role to manage Cloud Foundry cli


Role requires root access, ansible user should be able to sudo
Role will add Cloud Foundry repo and install cf cli
If cf_state is absent, cf cli package will be removed.



## Role Variables

### Required parameters:

 

#### cf_state


_Type:_ `str`

_Default:_ `present`

_Required:_ `False`
_Choices:_
- present
- absent
_Description:_
Cloud Foundry cli state

 

#### cf_package_name


_Type:_ `str`

_Default:_ `cf8-cli`

_Required:_ `False`
_Choices:_
- cf8-cli
- cf7-cli
_Description:_
Cloud Foundry cli version, that will be installed, or removed

 
 

## Limitations

None

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks

```ansible
- hosts: all
  tasks:
   - name: Ensure cf cli present
     ansible.builtin.include_role:
       name: sap.sap_operations.cf
     vars:
       cf_state: present

   - name: Ensure cf cli present
     ansible.builtin.include_role:
       name: sap.sap_operations.cf
     vars:
       cf_state: absent
```

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
