<!--
SPDX-License-Identifier: GPL-3.0-only
SPDX-FileCopyrightText: 2023 Red Hat, Project Atmosphere

Copyright 2023 Red Hat, Project Atmosphere

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

# Ansible Collection - sap.sap_operations

This collection contains modules and plugins to assist in automating SAP day 2 operations with Ansible.

## Installation and Usage

```bash
ansible-galaxy collection install sap.sap_operations
```

Role `prepare` will make sure that all necessary package dependencies are installed on RHEL host, so content from this collection can be executed.

Please see documentation for role `prepare`.

## Requirements

### Ansible

ansible-core 2.12

ansible-core 2.13

ansible-core 2.14

### Python

Ansible Automation Platform requires at minimum Python 3.8 to function as designed.

## LICENSE

GNU General Public License v3.0

See <https://www.gnu.org/licenses/gpl-3.0.txt> for details
