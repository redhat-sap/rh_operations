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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`general_preconfigure_reboot`](#parameter-general_preconfigure_reboot)
  * [`general_preconfigure_tmpfs_size_gb`](#parameter-general_preconfigure_tmpfs_size_gb)
  * [`general_preconfigure_reboot_timeout`](#parameter-general_preconfigure_reboot_timeout)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role attempts to prepare host to SAP products installation
> Role will install packages, configure selinux, configure tmpfs, configured services, configure kernel parameters

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-general_preconfigure_reboot"></a>`general_preconfigure_reboot` | `str` | No | `"postpone"` | How reboot has to be handled none - no reboot will be be required after role applied, role will not install packages that might require reboot. Not all requirements can be fulfilled that way. List of packages to be skipped see postpone - (default […]<br>*Choices:* none, postpone, now |
| <a id="parameter-general_preconfigure_tmpfs_size_gb"></a>`general_preconfigure_tmpfs_size_gb` | `str` | No | `"{% raw %}{{ ((0.75 * (ansible_facts['memtotal_mb'] + ansible_facts['swaptotal_mb'])) / 1024) | round | int }}{% endraw %}"` | Size of tmpfs to configure (in gigabytes) |
| <a id="parameter-general_preconfigure_reboot_timeout"></a>`general_preconfigure_reboot_timeout` | `int` | No | `3600` | Timeout for reboot handler, see how reboot is handled in general_preconfigure_reboot parameter description |

## Example Playbooks<a id="examples"></a>



## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Role was tested only on x86_64 architecture

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
