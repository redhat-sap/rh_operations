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

# RECENT UPDATES

Added documentation website [docs.galaxy.saponrhel.org>](https://docs.galaxy.saponrhel.org/?utm_source=galaxy)

Added modules to manage SAP BTP resources.

- sap.sap_operations.btp_global_account_info
- sap.sap_operations.btp_global_account_assignments_info
- sap.sap_operations.btp_subaccount
- sap.sap_operations.btp_subaccounts_info

Added modules to manage SAP BTP Cloud Foundry.

- sap.sap_operations.cf_marketplace_info
- sap.sap_operations.cf_service_instance
- sap.sap_operations.cf_service_instance_info
- sap.sap_operations.cf_service_instance_key
- sap.sap_operations.cf_service_instance_keys_info
- sap.sap_operations.cf_service_instances_info
- sap.sap_operations.cf_service_plans_info
- sap.sap_operations.cf_spaces_info

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

Ansible collection is designed to work with following Ansible versions (on controller host)

ansible-core 2.15

ansible-core 2.16

### Python

Ansible collection is designed to work with following python versions on controller host

python 3.8

python 3.9

python 3.10

python 3.11

python 3.12

Ansible collection is designed to work with following python versions on managed host

python 2.7

python 3.5

python 3.6

python 3.7

python 3.8

python 3.9

python 3.10

python 3.11

python 3.12

With one exception NW RFC modules to not work on python 2.7. This is because SAP PyRFC does not support python 2.7 see <https://github.com/SAP/PyRFC>

If there is a requirement to use NW RFC modules on python 2.7, please use HTTP connection only - this does not required PyRFC and works with python 2.7.

Not all python and ansible version combination are expected to work. Please use python version supported by respective ansible version.

### Supported Ansible and Python version combinations

Collection is supported as part of Red Hat Ansible Automation Platform subscription with limitations described in Ansible Automation support policy.

<https://access.redhat.com/support/policy/updates/ansible-automation-platform>

## LICENSE

GNU General Public License v3.0

See <https://www.gnu.org/licenses/gpl-3.0.txt> for details
