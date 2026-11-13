<!--
SPDX-License-Identifier: GPL-3.0-only
SPDX-FileCopyrightText: 2023-2025 Red Hat, Project Atmosphere

Copyright 2023-2025 Red Hat, Project Atmosphere

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

# saphostagent_sar

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`saphostagent_sar_source`](#parameter-saphostagent_sar_source)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Install SAP hostagent from SAR archive
> Role will unpack SAR archive \ and run saphostagent command to install saphostagent
> Role will check if there is file \ '/usr/sap/hostctrl/exe/saphostexec' \ if this file exists role will do nothing

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-saphostagent_sar_source"></a>`saphostagent_sar_source` | `path` | Yes | N/A | Exact path to SAR archive for saphostagent \ not just folder with that archive |

## Example Playbooks<a id="examples"></a>

- name: Install saphostagent from SAR file
  hosts: all
  gather_facts: false
  tasks:
    - name: Install saphostagent from SAR file
      ansible.builtin.include_role:
        name: sap.sap_operations.saphostagent_sar
      vars:
        saphostagent_sar_source: /software/sap/SAPHOSTAGENT<SP-version>.SAR

## Dependencies<a id="dependencies"></a>

Role depend on sap.sap_operations.unpack role, \ see requirements and documentation for that role

Role requires user to be able to become root to run

## Limitations<a id="limitations"></a>

Only supported on linux and darwin (macos) systems

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
