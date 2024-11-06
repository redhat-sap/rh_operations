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

# ssfs_sync

Sync SAP HANA SSFS keys (for HSR)


Sync SAP HANA SSFS keys (for HSR)
Role will find all the SAP instances on source host (see role variables)
and make sure that SSFS *.KEY and *.DAT files and synced from source host
to destination hosts (see role variables).

Files will be synced to destination hosts only if they exist on destination hosts.
Role requires that ansible_user can sudo to root.
Role uses ansible.builtin.synchronize to sync files and this implies that there should be host to hosts communication established.
How to generate ssh keys for ansible host to host communication see role sap.sap_operations.ssh_keys_distribute




## Role Variables

### Required parameters:


- [ssfs_sync_source_host](#ssfs_sync_source_host)
 

#### ssfs_sync_source_host


_Type:_ `str`


_Required:_ `True`
_Description:_
Host that will be sources for SSFS files sync

 

#### ssfs_sync_destination_hosts


_Type:_ `list`


_Required:_ `False`
_Description:_
Host of list of hosts that will be destination for SSFS files sync.
By default - all hosts in the play (magic variable ansible_play_hosts)


 
 

## Limitations

Not tested with scaleout systems
Not tested in case when several SAP HANA systems are installed on single host

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks

 name: Sync SSFS
 ansible.builtin.include_role:
   name: sap.sap_operations.ssfs_sync
 vars:
   ssfs_sync_source_host: hsr1
   ssfs_sync_destination_hosts: hsr2

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
