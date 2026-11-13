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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`firewall_zone`](#parameter-firewall_zone)
  * [`firewall_protocol`](#parameter-firewall_protocol)
  * [`firewall_permanent`](#parameter-firewall_permanent)
  * [`firewall_immediate`](#parameter-firewall_immediate)
  * [`firewall_state`](#parameter-firewall_state)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Configure firewall for SAP instances
> Role will fail if no firewalld service exist and running
> Role requires root access
> Role will list all SAP instances on the host and enable/disable
> firewalld configuration for ports exposed in AccessPointList for the instance
> Only SAP instances are taken into account, not installed databases
> Role is idempotent

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-firewall_zone"></a>`firewall_zone` | `str` | No | `"public"` | Firewall zone to configure<br>*Choices:* drop, block, public, external, dmz, work, home, internal, trusted |
| <a id="parameter-firewall_protocol"></a>`firewall_protocol` | `str` | No | `"tcp"` | Firewall protocol to configure<br>*Choices:* tcp, udp, sctp, dccp |
| <a id="parameter-firewall_permanent"></a>`firewall_permanent` | `bool` | No | `true` | If set to true firewall configuration will be permanent |
| <a id="parameter-firewall_immediate"></a>`firewall_immediate` | `bool` | No | `true` | If set to true firewall configuration will be immediate |
| <a id="parameter-firewall_state"></a>`firewall_state` | `str` | No | `"enabled"` | Enable or disable specified firewalld configuration<br>*Choices:* enabled, disabled |

## Example Playbooks<a id="examples"></a>


- name: Configure firewall for SAP instances
  ansible.builtin.include_role:
    name: sap.sap_operations.firewall


## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Only takes into account SAP instances, not databases

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
