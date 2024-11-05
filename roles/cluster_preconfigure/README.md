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

# cluster_preconfigure

Install packages required for cluster configuration


Install packages required for cluster configuration
Role will fail is architecture and os combination is not supported by this role
Role requires root access to install packages



## Role Variables

### Required parameters:

 
 

## Limitations

Role was tested only on x86_64 architecture

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks


- name: Run role cluster_preconfigure
  ansible.builtin.include_role:
    name: sap.sap_operations.cluster_preconfigure


## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
