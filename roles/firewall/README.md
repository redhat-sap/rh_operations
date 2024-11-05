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

# firewall

Configure firewall for SAP instances


Role will fail if no firewalld service exist and running
Role requires root access
Role will list all SAP instances on the host and enable/disable
firewalld configuration for ports exposed in AccessPointList for the instance

Only SAP instances are taken into account, not installed databases
Role is idempotent



## Role Variables

### Required parameters:

 

#### firewall_zone


_Type:_ `str`

_Default:_ `public`

_Required:_ `False`
_Choices:_
- drop
- block
- public
- external
- dmz
- work
- home
- internal
- trusted
_Description:_
Firewall zone to configure

 

#### firewall_protocol


_Type:_ `str`

_Default:_ `tcp`

_Required:_ `False`
_Choices:_
- tcp
- udp
- sctp
- dccp
_Description:_
Firewall protocol to configure

 

#### firewall_permanent


_Type:_ `bool`

_Default:_ `True`

_Required:_ `False`
_Description:_
If set to true firewall configuration will be permanent

 

#### firewall_immediate


_Type:_ `bool`

_Default:_ `True`

_Required:_ `False`
_Description:_
If set to true firewall configuration will be immediate

 

#### firewall_state


_Type:_ `str`

_Default:_ `enabled`

_Required:_ `False`
_Choices:_
- enabled
- disabled
_Description:_
Enable or disable specified firewalld configuration

 
 

## Limitations

Only takes into account SAP instances, not databases

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks


- name: Configure firewall for SAP instances
  ansible.builtin.include_role:
    name: sap.sap_operations.firewall


## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
