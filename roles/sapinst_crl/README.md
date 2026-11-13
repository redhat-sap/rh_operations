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

# sapinst_crl

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`sapinst_crl_become`](#parameter-sapinst_crl_become)
  * [`sapinst_crl_become_user`](#parameter-sapinst_crl_become_user)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Download SAP inst certificate revocation list (CRL)
> Role will download SAP inst certificate revocation list (CRL)
> Hardcoded url that is used to download CRL is https://tcs.mysap.com/crl/crlbag.p7s
> By default CRL will be placed in root use home directory ~/.sapinst/crlbag.p7s
> See documentation in SAP Note 3207613 - SAPinst Framework 7.53 Central Note

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-sapinst_crl_become"></a>`sapinst_crl_become` | `bool` | No | `true` | Become directive for user, see sapinst_crl_become_user |
| <a id="parameter-sapinst_crl_become_user"></a>`sapinst_crl_become_user` | `str` | No | `"root"` | User in which home directory CRL will be placed |

## Example Playbooks<a id="examples"></a>

- name: Download SAP inst CRL
  hosts: all
  gather_facts: false
  tasks:
    - name: Download SAP inst CRL
      ansible.builtin.include_role:
        name: sap.sap_operations.sapinst_crl

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Ansible user should be able to become user sapinst_crl_become_user (root by default)

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
