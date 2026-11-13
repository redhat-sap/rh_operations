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

# subscription_manager

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`subscription_manager_state`](#parameter-subscription_manager_state)
  * [`subscription_manager_org`](#parameter-subscription_manager_org)
  * [`subscription_manager_activationkey`](#parameter-subscription_manager_activationkey)
  * [`subscription_manager_username`](#parameter-subscription_manager_username)
  * [`subscription_manager_password`](#parameter-subscription_manager_password)
  * [`subscription_manager_validate`](#parameter-subscription_manager_validate)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Register host with subscription-manager
> Role is suitable for containers as well
> Role expects that ansible_user can sudo to root
> Role expects that subscription-manager tool is already present

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-subscription_manager_state"></a>`subscription_manager_state` | `str` | No | `"registered"` | Final state after role applied<br>*Choices:* registered, unregistered |
| <a id="parameter-subscription_manager_org"></a>`subscription_manager_org` | `str` | No | N/A | Organization to use for registration<br><br>Organization and Activation key are both required together - role will fail if one is defined and another is not |
| <a id="parameter-subscription_manager_activationkey"></a>`subscription_manager_activationkey` | `str` | No | N/A | Activation key to use for registration<br><br>Organization and Activation key are both required together - role will fail if one is defined and another is not |
| <a id="parameter-subscription_manager_username"></a>`subscription_manager_username` | `str` | No | N/A | Username to use for registration<br><br>Username and Password are both required together - role will fail if one is defined and another is not<br><br>If Username and Password are defined they will be used over org and Activation key |
| <a id="parameter-subscription_manager_password"></a>`subscription_manager_password` | `str` | No | N/A | Password to use for registration<br><br>Username and Password are both required together - role will fail if one is defined and another is not<br><br>If Username and Password are defined they will be used over org and Activation key |
| <a id="parameter-subscription_manager_validate"></a>`subscription_manager_validate` | `bool` | Yes | N/A | Internal role variable used to validate variables<br>*Choices:* True |

## Example Playbooks<a id="examples"></a>

- name: Run role subscription_manager (registered)
  ansible.builtin.include_role:
  name: sap.sap_operations.subscription_manager
- name: Run role subscription_manager (unregistered)
  ansible.builtin.include_role:
  name: sap.sap_operations.subscription_manager
  vars:
    subscription_manager_state: unregistered

## Dependencies<a id="dependencies"></a>

None

## Limitations<a id="limitations"></a>



## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
