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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`ssh_keys_distribute_state`](#parameter-ssh_keys_distribute_state)
  * [`ssh_keys_distribute_user`](#parameter-ssh_keys_distribute_user)
  * [`ssh_keys_distribute_key`](#parameter-ssh_keys_distribute_key)
  * [`ssh_keys_distribute_hosts`](#parameter-ssh_keys_distribute_hosts)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Generate and distribute ssh keys for host to host communication
> Role has two modes of operation - present and absent, see variable ssh_keys_distribute_state
> If state=present role will ensure that ssh key (see below about key name)
> is present, key will be generated if absent, key will never be regenerated.
> After that role will distribute this key to other hosts, see how list of hosts defined below.
> If state=absent, role will make sure that key authorization on all hosts is removed.
> ssh key, even if it was generated will not be removed by the role.

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-ssh_keys_distribute_state"></a>`ssh_keys_distribute_state` | `str` | No | `"present"` | State=present - role will ensure that ssh keys are present (generated) State=absent - role will ensure that ssh key with name defined in variable ssh_keys_distribute_key cannot be used to login to hosts (using user defined in […]<br>*Choices:* present, absent |
| <a id="parameter-ssh_keys_distribute_user"></a>`ssh_keys_distribute_user` | `str` | No | `"root"` | User for which key if be generated (if required) and distributed to all the hosts ansible_user should be able to sudo to this user |
| <a id="parameter-ssh_keys_distribute_key"></a>`ssh_keys_distribute_key` | `str` | No | `"id_rsa"` | Name of the key to distribute, should not contain '*.pub' |
| <a id="parameter-ssh_keys_distribute_hosts"></a>`ssh_keys_distribute_hosts` | `list of str` | No | N/A | Lists of hosts, where key will be distributed, default value is ansible magic variable ansible_play_hosts |

## Example Playbooks<a id="examples"></a>

 - name: Run role ssh_keys_distribute
   ansible.builtin.include_role:
     name: sap.sap_operations.ssh_keys_distribute

## Dependencies<a id="dependencies"></a>

Role depend on collection community.crypto

## Limitations<a id="limitations"></a>



## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
