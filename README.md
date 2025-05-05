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

RHEL 7 is no longer supported as managed host.

Added documentation website [docs.galaxy.saponrhel.org](https://docs.galaxy.saponrhel.org/?utm_source=galaxy)

Added role to download SAP SWDC downloadbasket content.

Added role to download SAP software from SWDC.

# sap.sap_operations

Ansible collection to automate SAP operations

## Description

Ansible roles, modules and plugins to automate SAP operations.

Following use cases are covered in this collection:

- SAP HANA Automation

- SAP Netweaver Automation

- SAP ABAP automation

- SAP Software Download Automation

- SAP host automation (sap host agent related functionality)

- Automation for pacemaker cluster in context of SAP (HANA and NW clusters)

- SAP BTP automation

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

- manage SAP BTP global account and subaccounts

- download SAP software from SWDC

- install SAP cloud connector

- manage SAP license information

- start / stop / restart SAP system

- get status and configuration information about SAP clusters

- manage SAP ASCS and ERS locks

- manage SAP transport requests in ABAP systems

- get configuration information from SAP ABAP system

- run non invasive SAP quality checks and get results

- run non invasive cluster configuration checks

- unpack SAP software from archives

- validate SAP system id (SID)

## Testing

Collection tested automatically using ansible molecule and Azure molecule driver <https://github.com/redhat-sap/molecule.driver>

Ansible plugins and modules are covered with python unit and integration tests.

Test cover RHEL 8, RHEL 9 and RHEL 10 - supported versions.

Supported (and thus tested) ansible-core and python versions on controller and managed hosts see below.

## Requirements

### Ansible

Ansible collection is designed to work with following Ansible versions (on controller host)

ansible-core 2.15

ansible-core 2.16

ansible-core 2.17

ansible-core 2.18

## Contributing

Contributions are accepted at <https://github.com/redhat-sap/rh_operations> - galaxy branch.

See details in that repository.

## Support

This collection is community supported.

If support is needed, please use collection from AAP.

<https://console.redhat.com/ansible/automation-hub/repo/published/sap/sap_operations/>

## Release Notes and Roadmap

This collection follows Red Hat Ansible Automation Platform Lifecycle policy

<https://access.redhat.com/support/policy/updates/ansible-automation-platform>

This collection aims to provide support for more RHEL version that it is mentioned in AAP support policy.

This collection aims to provide support for RHEL for SAP versions that are currently supported, where it is possible and technically feasible.

See <https://access.redhat.com/support/policy/updates/errata> for RHEL for SAP support policy.

Extract from RHEL for SAP support policy:

For Red Hat Enterprise Linux for SAP Solutions on RHEL 8, Update Services for SAP Solutions is currently available for the following releases:

8.4 (ends May 31, 2025)

8.6 (ends May 31, 2026)

8.8 (ends May 31, 2027)

For Red Hat Enterprise Linux for SAP Solutions on RHEL 9, Update Services for SAP Solutions is currently available for the following releases:

9.0 (ends May 31, 2026)

9.2 (ends May 31, 2027)

9.4 (ends April 30, 2028)

## Related Information

Collection documentation located at

<docs.galaxy.saponrhel.org>

## License Information

GPL-3.0-only

GNU General Public License v3.0

See <https://www.gnu.org/licenses/gpl-3.0.txt> for details

2022 - 2025 (c) Project Atmosphere

## Python supported versions

Ansible collection is designed to work with following python versions on controller host

python 3.8

python 3.9

python 3.10

python 3.11

python 3.12

python 3.13

Ansible collection is designed to work with following python versions on managed host

python 3.8

python 3.9

python 3.10

python 3.11

python 3.12

python 3.13

With one exception NW RFC modules to not work on python 2.7. This is because SAP PyRFC does not support python 2.7 see <https://github.com/SAP/PyRFC>

If there is a requirement to use NW RFC modules on python 2.7, please use HTTP connection only - this does not required PyRFC and works with python 2.7.

Not all python and ansible version combination are expected to work. Please use python version supported by respective ansible version.

### Supported Ansible and Python version combinations

Collection is supported as part of Red Hat Ansible Automation Platform subscription with limitations described in Ansible Automation support policy.

<https://access.redhat.com/support/policy/updates/ansible-automation-platform>
