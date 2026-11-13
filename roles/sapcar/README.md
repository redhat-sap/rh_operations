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

# sapcar

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`sap_operations_sapcar_exe_path`](#parameter-sap_operations_sapcar_exe_path)
  * [`sapcar_exe_path`](#parameter-sapcar_exe_path)
  * [`sapcar_state`](#parameter-sapcar_state)
  * [`sapcar_download_destination`](#parameter-sapcar_download_destination)
  * [`sapcar_patch_level`](#parameter-sapcar_patch_level)
  * [`sapcar_mode`](#parameter-sapcar_mode)
  * [`sapcar_owner`](#parameter-sapcar_owner)
  * [`sapcar_version`](#parameter-sapcar_version)
  * [`sap_operations_download_username`](#parameter-sap_operations_download_username)
  * [`sap_operations_download_password`](#parameter-sap_operations_download_password)
  * [`sapcar_download_username`](#parameter-sapcar_download_username)
  * [`sapcar_download_password`](#parameter-sapcar_download_password)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role to manage sapcar
> Role to manage sapcar binary

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-sap_operations_sapcar_exe_path"></a>`sap_operations_sapcar_exe_path` | `path` | No | `"/usr/sap/sapcar/sapcar"` | Collection variable that provides the path to the sapcar executable file.<br><br>Role parameter `sapcar_exe_path` defaults to this collection variable. |
| <a id="parameter-sapcar_exe_path"></a>`sapcar_exe_path` | `path` | No | `"/usr/sap/sapcar/sapcar"` | Path to sapcar executable file<br><br>Default value is from collection variable sap_operations_sapcar_exe_path<br><br>All parent directories to directory where sapcar executable should be located should exists and be writable for ansible […] |
| <a id="parameter-sapcar_state"></a>`sapcar_state` | `str` | No | `"present"` | State for sapcar executable<br><br>present - role will ensure that executable will downloaded and installed (copied to sapcar_exe_path)<br><br>present - will do any changes only if file sapcar_exe_path does not exists<br><br>absent - role will ensure […]<br>*Choices:* present, absent |
| <a id="parameter-sapcar_download_destination"></a>`sapcar_download_destination` | `path` | No | `"/tmp/sapcar_download_destination"` | Path there sapcar binary will be downloaded (in case of sapcar_state='present')<br><br>Role will ensure that this folder exists |
| <a id="parameter-sapcar_patch_level"></a>`sapcar_patch_level` | `str` | No | `""` | Patch level that will be downloaded and installed if sapcar_state='present'<br><br>sap.sap_operations.download role will be used to download sapcar binaries<br><br>sap.sap_operations.download role by default will download patch level with latest […] |
| <a id="parameter-sapcar_mode"></a>`sapcar_mode` | `str` | No | `"0755"` | Permissions mode that will be used for all folders that are created by the role (sapcar_download_destination and sapcar_exe_path) and sapcar executable destination sapcar_exe_path |
| <a id="parameter-sapcar_owner"></a>`sapcar_owner` | `str` | No | N/A | Owner that will be used for all folders that are created by the role (sapcar_download_destination and sapcar_exe_path) and sapcar executable destination sapcar_exe_path<br><br>By default is set to omit special variable - meaning current ansible_user […] |
| <a id="parameter-sapcar_version"></a>`sapcar_version` | `str` | No | N/A | Sapcar version that has to be downloaded and installed<br><br>By default will be automatically calculated as highest version available among all sapcar versions from sap.sap_operations.me_aliases filter |
| <a id="parameter-sap_operations_download_username"></a>`sap_operations_download_username` | `str` | No | N/A | Collection variable that provides the username (sap support user, suser) for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME. Role parameter `sapcar_download_username` defaults to this collection […] |
| <a id="parameter-sap_operations_download_password"></a>`sap_operations_download_password` | `str` | No | N/A | Collection variable that provides the password of the username for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD. Role parameter `sapcar_download_password` defaults to this collection variable. |
| <a id="parameter-sapcar_download_username"></a>`sapcar_download_username` | `str` | Yes | N/A | Username (sap support user, suser) that will be used to download software. By default value is from collection variable `sap_operations_download_username`. Collection variable `sap_operations_download_username` default value is set to environment […] |
| <a id="parameter-sapcar_download_password"></a>`sapcar_download_password` | `str` | Yes | N/A | Password of provided username that will be used to download software By default value is from collection variable `sap_operations_download_password`. Collection variable `sap_operations_download_password` default value is set to environment variable […] |

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Username has to be email of SAP UID with only one Suser assigned. If more than one Suser is assigned to UID download will fail.

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
