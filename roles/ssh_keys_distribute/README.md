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

# ssh_keys_distribute

Generate and distribute ssh keys for host to host communication


Generate and distribute ssh keys for host to host communication
Role has two modes of operation - present and absent, see variable ssh_keys_distribute_state
If state=present role will ensure that ssh key (see below about key name)
is present, key will be generated if absent, key will never be regenerated.
After that role will distribute this key to other hosts, see how list of hosts defined below.

If state=absent, role will make sure that key authorization on all hosts is removed.
ssh key, even if it was generated will not be removed by the role.




## Role Variables

### Required parameters:

 

#### ssh_keys_distribute_state


_Type:_ `str`

_Default:_ `present`

_Required:_ `False`
_Choices:_
- present
- absent
_Description:_
State=present - role will ensure that ssh keys are present (generated)
State=absent - role will ensure that ssh key with name defined in variable ssh_keys_distribute_key
cannot be used to login to hosts (using user defined in ssh_keys_distribute_user)


 

#### ssh_keys_distribute_user


_Type:_ `str`

_Default:_ `root`

_Required:_ `False`
_Description:_
User for which key if be generated (if required) and distributed to all the hosts
ansible_user should be able to sudo to this user


 

#### ssh_keys_distribute_key


_Type:_ `str`

_Default:_ `id_rsa`

_Required:_ `False`
_Description:_
Name of the key to distribute, should not contain '*.pub'

 

#### ssh_keys_distribute_hosts


_Type:_ `list`


_Required:_ `False`
_Description:_
Lists of hosts, where key will be distributed, default value is ansible magic variable ansible_play_hosts

 
 

## Limitations



## Dependencies

Role depend on collection community.crypto

## Example Playbooks

 - name: Run role ssh_keys_distribute
   ansible.builtin.include_role:
     name: sap.sap_operations.ssh_keys_distribute

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
