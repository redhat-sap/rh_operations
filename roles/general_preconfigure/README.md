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

# general_preconfigure

Role attempts to prepare host to SAP products installation


Role attempts to prepare host to SAP products installation
Role will install packages, configure selinux, configure tmpfs, configured services, configure kernel parameters



## Role Variables

### Required parameters:

 

#### general_preconfigure_reboot


_Type:_ `str`

_Default:_ `postpone`

_Required:_ `False`
_Choices:_
- none
- postpone
- now
_Description:_
How reboot has to be handled
none - no reboot will be be required after role applied,
role will not install packages that might require reboot. Not all requirements can be fulfilled that way.
List of packages to be skipped see <https://access.redhat.com/solutions/27943>
postpone - (default behavior) reboot might be required after packages installation by the role,
role will not reboot machine, role will not notify reboot action, in this case reboot has to be handled separately by the user.
now - role will force reboot of the host at the end of the execution - this is not idempotent and reboot will be forced each time role is executed.


 

#### general_preconfigure_tmpfs_size_gb


_Type:_ `str`

_Default:_ `{{ ((0.75 * (ansible_facts['memtotal_mb'] + ansible_facts['swaptotal_mb'])) / 1024) | round | int }}`

_Required:_ `False`
_Description:_
Size of tmpfs to configure (in gigabytes)

 
 

## Limitations

Role was tested only on x86_64 architecture

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks



## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
