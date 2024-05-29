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

Manage SAP JVM (download / install / uninstall)


Manage SAP JVM
Role will download SAP JVM binary from tools.hana.ondemand.com
Role can install both rpm and portable versions of SAP JVM, see role documentation
Portable version is installed via copy of downloaded archive content, removed via removing installation directory
RPM version installation requires root access
Role will use ansible_facts to determine current host os system and architecture to download correct SAP JVM binary
By using this role and downloading SAP software from tools.hana.ondemand.com you accept SAP developer license agreement
One can find more details on tools.hana.ondemand.com



## Role Variables

### Required parameters:


- [sapjvm_version](#sapjvm_version)
 

#### sapjvm_version


_Type:_ `str`


_Required:_ `True`
_Description:_
Version of SAP JVM to download and install
This version must exists on tools.hana.ondemand.com, it does not role will fail

 

#### sapjvm_state


_Type:_ `str`

_Default:_ `present`

_Required:_ `False`
_Choices:_
- present
- absent
_Description:_
SAP JVM state

 

#### sapjvm_download_destination


_Type:_ `path`

_Default:_ `/tmp/sapjvm`

_Required:_ `False`
_Description:_
Folder where SAP JVM binary will be downloaded

 

#### sapjvm_download_filename


_Type:_ `str`


_Required:_ `False`
_Description:_
Filename of downloaded SAP JVM binaries,
By default Filename is sapjvm-{{ sapjvm_version }}-{{ sapjvm_system }}-{{ sapjvm_architecture }}.{{ sapjvm_archive_extension }}
See definition of variables in defaults/main.yml and vars/main.yml

 

#### sapjvm_download_filepath


_Type:_ `path`


_Required:_ `False`
_Description:_
Complete path to file where SAP JVM binary will be downloaded
by default is {{ sapjvm_download_destination }}/{{ sapjvm_download_filename }}, see other variables
If this is set it will overwrite sapjvm_download_destination and sapjvm_download_filename variable values

 

#### sapjvm_download_timeout_seconds


_Type:_ `int`

_Default:_ `3600`

_Required:_ `False`
_Description:_
Timeout set for download SAP JVM task

 

#### sapjvm_unpack_destination


_Type:_ `path`

_Default:_ `/tmp/sapjvm_unpacked`

_Required:_ `False`
_Description:_
Folder where SAP JVM binary will be unpacked

 

#### sapjvm_portable_install_destination


_Type:_ `path`

_Default:_ `/opt/`

_Required:_ `False`
_Description:_
Folder where SAP JVM binary will be installed, only relevant for portable installations

 

#### sapjvm_portable_uninstall_destination


_Type:_ `path`

_Default:_ `/opt/sapjvm_8`

_Required:_ `False`
_Description:_
Folder that will be deleted, if SAP JVM portable version is uninstalled

 

#### sapjvm_system


_Type:_ `path`

_Default:_ `linux`

_Required:_ `False`
_Choices:_
- linux
- darwin
_Description:_
SAP JVM is supported on linux, macos, windows. By default role will determine system using ansible_facts.
This variable to overwrite system determined by ansible_facts

 

#### sapjvm_architecture


_Type:_ `str`

_Default:_ `x64`

_Required:_ `False`
_Choices:_
- x64
- ppc64le
- aarch64
_Description:_
Architecture that for what SAP JVM will be installed
By default will be determined from ansible_facts

 

#### sapjvm_portable


_Type:_ `bool`

_Default:_ `False`

_Required:_ `False`
_Description:_
If portable version of SAP JVM has to be downloaded and installed / removed

 

#### sapjvm_eula


_Type:_ `str`

_Default:_ `eula_3_2_agreed=tools.hana.ondemand.com/developer-license-3_2.txt`

_Required:_ `False`
_Description:_
Confirms that you are agree to SAP developer license

 
 

## Limitations

Only supported on linux and darwin (macos) systems
root access required if rpm version is installed, sudo package has to be installed
packages required zip, tar (to unpack downloaded archives)

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks

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

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
