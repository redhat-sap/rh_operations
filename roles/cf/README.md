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

# cf

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`cf_state`](#parameter-cf_state)
  * [`cf_package_name`](#parameter-cf_package_name)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role to manage Cloud Foundry cli
> Role requires root access, ansible user should be able to sudo
> Role will add Cloud Foundry repo and install cf cli
> If cf_state is absent, cf cli package will be removed.

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-cf_state"></a>`cf_state` | `str` | No | `"present"` | Cloud Foundry cli state<br>*Choices:* present, absent |
| <a id="parameter-cf_package_name"></a>`cf_package_name` | `str` | No | `"cf8-cli"` | Cloud Foundry cli version, that will be installed, or removed<br>*Choices:* cf8-cli, cf7-cli |

## Example Playbooks<a id="examples"></a>

```ansible
- hosts: all
  tasks:
   - name: Ensure cf cli present
     ansible.builtin.include_role:
       name: sap.sap_operations.cf
     vars:
       cf_state: present

   - name: Ensure cf cli present
     ansible.builtin.include_role:
       name: sap.sap_operations.cf
     vars:
       cf_state: absent
```

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

None

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
