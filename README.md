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

Added link to collection documentation

<https://catalog.redhat.com/software/collection/sap/sap_operations>

# sap.sap_operations

Ansible collection to automate SAP operations

## Description

Ansible roles, modules and plugins to automate SAP operations.

Following use cases are covered in this collection:

- SAP HANA Automation

- SAP Netweaver Automation

- SAP ABAP automation

- SAP host automation (sap host agent related functionality)

See playbook examples in playbook folder.

## Installation

```bash
ansible-galaxy collection install sap.sap_operations

ansible-galaxy collection install sap.sap_operations --upgrade
```

Role `prepare` will make sure that all necessary package dependencies are installed on RHEL host, so content from this collection can be executed.

Please see documentation for role `prepare`.

## Use cases

- SAP HANA update

- SAP NW kernel update

- get information about current SAP landscape

- start / stop / restart SAP system

- get status and configuration information about SAP clusters

- get configuration information from SAP ABAP system

- unpack SAP software from archives

## Testing

Collection tested automatically using ansible molecule and Azure molecule driver <https://github.com/redhat-sap/molecule.driver>

Ansible plugins and modules are covered with python unit and integration tests.

Test cover RHEL 7, RHEL 8 and RHEL 9 - supported versions.

Supported (and thus tested) ansible-core and python versions on controller and managed hosts see below.

## Requirements

### Ansible

Ansible collection is designed to work with following Ansible versions (on controller host)

ansible-core 2.15

ansible-core 2.16

ansible-core 2.17

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

## Contributing

Contributions are accepted at <https://github.com/redhat-sap/rh_operations> - main branch.

See details in that repository.

## Support

This collection is supported by Red Hat with limitations described in Ansible Automation Platform Lifecycle.

<https://access.redhat.com/support/policy/updates/ansible-automation-platform>

## Release Notes and Roadmap

## Related Information

## License Information

GPL-3.0-only

GNU General Public License v3.0

See <https://www.gnu.org/licenses/gpl-3.0.txt> for details

2022 - 2024 (c) Project Atmosphere
