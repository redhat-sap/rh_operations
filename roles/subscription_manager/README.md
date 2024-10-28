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

# subscription_manager

Register host with subscription-manager


Register host with subscription-manager
Role is suitable for containers as well
Role expects that ansible_user can sudo to root
Role expects that subscription-manager tool is already present



## Role Variables

### Required parameters:


- [subscription_manager_validate](#subscription_manager_validate)
 

#### subscription_manager_validate


_Type:_ `bool`


_Required:_ `True`
_Choices:_
- True
_Description:_
Internal role variable used to validate variables

 

#### subscription_manager_state


_Type:_ `str`

_Default:_ `registered`

_Required:_ `False`
_Choices:_
- registered
- unregistered
_Description:_
Final state after role applied

 

#### subscription_manager_org


_Type:_ `str`


_Required:_ `False`
_Description:_
Organization to use for registration
Organization and Activation key are both required together - role will fail if one is defined and another is not

 

#### subscription_manager_activationkey


_Type:_ `str`


_Required:_ `False`
_Description:_
Activation key to use for registration
Organization and Activation key are both required together - role will fail if one is defined and another is not

 

#### subscription_manager_username


_Type:_ `str`


_Required:_ `False`
_Description:_
Username to use for registration
Username and Password are both required together - role will fail if one is defined and another is not
If Username and Password are defined they will be used over org and Activation key

 

#### subscription_manager_password


_Type:_ `str`


_Required:_ `False`
_Description:_
Password to use for registration
Username and Password are both required together - role will fail if one is defined and another is not
If Username and Password are defined they will be used over org and Activation key

 
 

## Register host with subscription-manager

Register host with subscription-manager
Role is suitable for containers as well
Role expects that ansible_user can sudo to root
Role expects that subscription-manager tool is already present

## Limitations



## Dependencies

N
o
n
e

## Example Playbooks

- name: Run role subscription_manager (registered)
  ansible.builtin.include_role:
  name: sap.sap_operations.subscription_manager
- name: Run role subscription_manager (unregistered)
  ansible.builtin.include_role:
  name: sap.sap_operations.subscription_manager
  vars:
    subscription_manager_state: unregistered

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
