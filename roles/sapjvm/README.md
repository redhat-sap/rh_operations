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

# sapjvm

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`sapjvm_version`](#parameter-sapjvm_version)
  * [`sapjvm_state`](#parameter-sapjvm_state)
  * [`sapjvm_download_destination`](#parameter-sapjvm_download_destination)
  * [`sapjvm_download_filename`](#parameter-sapjvm_download_filename)
  * [`sapjvm_download_filepath`](#parameter-sapjvm_download_filepath)
  * [`sapjvm_download_timeout_seconds`](#parameter-sapjvm_download_timeout_seconds)
  * [`sapjvm_unpack_destination`](#parameter-sapjvm_unpack_destination)
  * [`sapjvm_portable_install_destination`](#parameter-sapjvm_portable_install_destination)
  * [`sapjvm_portable_uninstall_destination`](#parameter-sapjvm_portable_uninstall_destination)
  * [`sapjvm_system`](#parameter-sapjvm_system)
  * [`sapjvm_architecture`](#parameter-sapjvm_architecture)
  * [`sapjvm_portable`](#parameter-sapjvm_portable)
  * [`sapjvm_eula`](#parameter-sapjvm_eula)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Manage SAP JVM (download / install / uninstall)
> Manage SAP JVM
> Role will download SAP JVM binary from tools.hana.ondemand.com
> Role can install both rpm and portable versions of SAP JVM, see role documentation
> Portable version is installed via copy of downloaded archive content, removed via removing installation directory
> RPM version installation requires root access
> Role will use ansible_facts to determine current host os system and architecture to download correct SAP JVM binary
> By using this role and downloading SAP software from tools.hana.ondemand.com you accept SAP developer license agreement
> One can find more details on tools.hana.ondemand.com

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-sapjvm_version"></a>`sapjvm_version` | `str` | Yes | N/A | Version of SAP JVM to download and install<br><br>This version must exists on tools.hana.ondemand.com, it does not role will fail |
| <a id="parameter-sapjvm_state"></a>`sapjvm_state` | `str` | No | `"present"` | SAP JVM state<br>*Choices:* present, absent |
| <a id="parameter-sapjvm_download_destination"></a>`sapjvm_download_destination` | `path` | No | `"/tmp/sapjvm"` | Folder where SAP JVM binary will be downloaded |
| <a id="parameter-sapjvm_download_filename"></a>`sapjvm_download_filename` | `str` | No | N/A | Filename of downloaded SAP JVM binaries,<br><br>By default Filename is {% raw %}sapjvm-{{ sapjvm_version }}-{{ sapjvm_system }}-{{ sapjvm_architecture }}.{{ sapjvm_archive_extension }}{% endraw %}<br><br>See definition of variables in […] |
| <a id="parameter-sapjvm_download_filepath"></a>`sapjvm_download_filepath` | `path` | No | N/A | Complete path to file where SAP JVM binary will be downloaded<br><br>by default is {% raw %}{{ sapjvm_download_destination }}/{{ sapjvm_download_filename }}{% endraw %}, see other variables<br><br>If this is set it will overwrite […] |
| <a id="parameter-sapjvm_download_timeout_seconds"></a>`sapjvm_download_timeout_seconds` | `int` | No | `3600` | Timeout set for download SAP JVM task |
| <a id="parameter-sapjvm_unpack_destination"></a>`sapjvm_unpack_destination` | `path` | No | `"/tmp/sapjvm_unpacked"` | Folder where SAP JVM binary will be unpacked |
| <a id="parameter-sapjvm_portable_install_destination"></a>`sapjvm_portable_install_destination` | `path` | No | `"/opt/"` | Folder where SAP JVM binary will be installed, only relevant for portable installations |
| <a id="parameter-sapjvm_portable_uninstall_destination"></a>`sapjvm_portable_uninstall_destination` | `path` | No | `"/opt/sapjvm_8"` | Folder that will be deleted, if SAP JVM portable version is uninstalled |
| <a id="parameter-sapjvm_system"></a>`sapjvm_system` | `path` | No | `"linux"` | SAP JVM is supported on linux, macos, windows. By default role will determine system using ansible_facts.<br><br>This variable to overwrite system determined by ansible_facts<br>*Choices:* linux, darwin |
| <a id="parameter-sapjvm_architecture"></a>`sapjvm_architecture` | `str` | No | `"x64"` | Architecture that for what SAP JVM will be installed<br><br>By default will be determined from ansible_facts<br>*Choices:* x64, ppc64le, aarch64 |
| <a id="parameter-sapjvm_portable"></a>`sapjvm_portable` | `bool` | No | `false` | If portable version of SAP JVM has to be downloaded and installed / removed |
| <a id="parameter-sapjvm_eula"></a>`sapjvm_eula` | `str` | No | `"eula_3_2_agreed=tools.hana.ondemand.com/developer-license-3_2.txt"` | Confirms that you are agree to SAP developer license |

## Example Playbooks<a id="examples"></a>

- name: Test SAP JVM portable installation
  hosts: all
  gather_facts: false
  tasks:
    - name: Make sure that portable SAP JVM present
      ansible.builtin.include_role:
        name: sap.sap_operations.sapjvm
      vars:
        sapjvm_version: 8.1.097
        sapjvm_portable: true

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Only supported on linux and darwin (macos) systems

root access required if rpm version is installed, sudo package has to be installed

packages required zip, tar (to unpack downloaded archives)

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
