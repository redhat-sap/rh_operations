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

# swpm

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`swpm_state`](#parameter-swpm_state)
  * [`sap_operations_swpm_unpack_destination`](#parameter-sap_operations_swpm_unpack_destination)
  * [`swpm_unpack_destination`](#parameter-swpm_unpack_destination)
  * [`swpm_download_destination`](#parameter-swpm_download_destination)
  * [`swpm_version`](#parameter-swpm_version)
  * [`sap_operations_download_username`](#parameter-sap_operations_download_username)
  * [`sap_operations_download_password`](#parameter-sap_operations_download_password)
  * [`swpm_download_username`](#parameter-swpm_download_username)
  * [`swpm_download_password`](#parameter-swpm_download_password)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Manage SAP SWPM (download / install / uninstall)
> Manage SAP SWPM
> Role will download SAP SWPM binary from SAP SWDC (software download center)
> Role will use ansible_facts to determine current host os system and architecture to download correct binary
> Role will download latest SP available from SAP SWDC web site in that sense role is not idempotent,
> because next time one will run this role, there might be new SP of SAP SWPM
> Role will not do anything if swpm_state='present' and file sapinst exists in swpm_unpack_destination

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-swpm_state"></a>`swpm_state` | `str` | No | `"present"` | State for SAP SWPM<br><br>present - role will ensure that executable will downloaded and installed (copied to swpm_unpack_destination)<br><br>present - will do any changes only if file sapinst in swpm_unpack_destination does not exists<br><br>absent […]<br>*Choices:* present, downloaded, absent |
| <a id="parameter-sap_operations_swpm_unpack_destination"></a>`sap_operations_swpm_unpack_destination` | `path` | No | `"/usr/sap/swpm"` | Collection variable that provides the path where SAP SWPM binary archive will be unpacked.<br><br>Role parameter `swpm_unpack_destination` defaults to this collection variable. |
| <a id="parameter-swpm_unpack_destination"></a>`swpm_unpack_destination` | `path` | No | `"/usr/sap/swpm"` | Path there SAP SWPM binary archive will be unpacked (in case of swpm_state='present')<br><br>Role will not create swpm_unpack_destination folder or any folders above it. It has to exists |
| <a id="parameter-swpm_download_destination"></a>`swpm_download_destination` | `path` | No | `"/tmp/"` | Path there SAP SWPM binary archive will be downloaded (in case of swpm_state='present' or swpm_state='downloaded')<br><br>Role will not create swpm_download_destination folder or any folders above it. It has to exists |
| <a id="parameter-swpm_version"></a>`swpm_version` | `str` | No | `"2.0"` | SAP SWPM version that will be downloaded and / or installed<br><br>Role will always download SP version that was changed last on SAP SWDC (software download center)<br>*Choices:* 2.0, 1.0 |
| <a id="parameter-sap_operations_download_username"></a>`sap_operations_download_username` | `str` | No | N/A | Collection variable that provides the username (sap support user, suser) for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME. Role parameter `swpm_download_username` defaults to this collection […] |
| <a id="parameter-sap_operations_download_password"></a>`sap_operations_download_password` | `str` | No | N/A | Collection variable that provides the password of the username for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD. Role parameter `swpm_download_password` defaults to this collection variable. |
| <a id="parameter-swpm_download_username"></a>`swpm_download_username` | `str` | Yes | N/A | Username (sap support user, suser) that will be used to download software. By default value is from collection variable `sap_operations_download_username`. Collection variable `sap_operations_download_username` default value is set to environment […] |
| <a id="parameter-swpm_download_password"></a>`swpm_download_password` | `str` | Yes | N/A | Password of provided username that will be used to download software By default value is from collection variable `sap_operations_download_password`. Collection variable `sap_operations_download_password` default value is set to environment variable […] |

## Example Playbooks<a id="examples"></a>



## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Tested only on RHEL 8 and 9

Tested only on x86_64 architecture

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
