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

Download SAP inst certificate revocation list (CRL)


Role will download SAP inst certificate revocation list (CRL)
Hardcoded url that is used to download CRL is https://tcs.mysap.com/crl/crlbag.p7s
By default CRL will be placed in root use home directory ~/.sapinst/crlbag.p7s
See documentation in SAP Note 3207613 - SAPinst Framework 7.53 Central Note



## Role Variables

### Required parameters:

 

#### sapinst_crl_become


_Type:_ `bool`

_Default:_ `True`

_Required:_ `False`
_Description:_
Become directive for user, see sapinst_crl_become_user

 

#### sapinst_crl_become_user


_Type:_ `str`

_Default:_ `root`

_Required:_ `False`
_Description:_
User in which home directory CRL will be placed

 
 

## Limitations

Ansible user should be able to become user sapinst_crl_become_user (root by default)

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks

- name: Download SAP inst CRL
  hosts: all
  gather_facts: false
  tasks:
    - name: Download SAP inst CRL
      ansible.builtin.include_role:
        name: sap.sap_operations.sapinst_crl

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
