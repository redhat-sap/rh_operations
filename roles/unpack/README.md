<!--
SPDX-License-Identifier: GPL-3.0-only
SPDX-FileCopyrightText: 2023 Red Hat, Project Atmosphere

Copyright 2023 Red Hat, Project Atmosphere

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

# unpack

Unpack SAP binaries from \*.zip and \*.sar archives

## Requirements

Role requires 'unzip' command to be installed. Role uses module 'ansible.builtin.unarchive', see documentation for that module.

SAPCAR should be installed in location 'unpack_sapcar_exe_path' (collection variable 'sap_operations_sapcar_exe_path'). Variable 'unpack_sapcar_exe_path' has precedence over 'sap_operations_sapcar_exe_path', if variable 'unpack_sapcar_exe_path' is set, value of variable 'sap_operations_sapcar_exe_path' is ignored.

<!-- BEGIN: Role Input Parameters -->

## Role Variables

Required parameters:

- [unpack_destination](#unpack_destination)

- [unpack_source](#unpack_source)

### unpack_destination

- _Type:_ `str`
- _Required:_ `True`

Folder where files will be unpacked.
If folder does not exist, it will be created.
Ansible user has to have permissions to create the folder and write to the folder if it already exists.

### unpack_source

- _Type:_ `list`
- _Required:_ `True`

List or str value - files and/or folders that should be unpacked.
Folder and/or files that are missing or cannot be accessed will be ignored.
Only files on first level in directory will be processed, role does not look recursively in the directory.

### unpack_manifest

- _Type:_ `bool`
- _Default:_ `True`
- _Required:_ `False`

Flag to unpack SAPCAR archives using option "-manifest SIGNATURE.SMF".
If set to true option "-manifest SIGNATURE.SMF" will be used

### unpack_sapcar_exe_path

- _Type:_ `str`
- _Default:_ `/usr/sap/sapcar/sapcar`
- _Required:_ `False`

Path to SAPCAR executable file. SAPCAR should be installed as a prerequisite for this role.

This variable is equivalent to sap_operations collection variable 'sap_operations_sapcar_exe_path'.

<!-- END: Role Input Parameters -->

## Dependencies

Role has no dependencies to other roles.

## Example Playbook

```ansible
    - hosts: all
      roles:
         - role: sap.sap_operations.unpack
      vars:
        unpack_source:
          - /tmp
          - /path/to/file.zip
          - /path/to/file.sar
          - /this/file/will/be/ignored.xyz
          - /this/file/will/also/be/ignored
          - /directories/that/do/not/exist/will/be/ignored
        unpack_destination: /unpacked
        unpack_sapcar_exe_path: /usr/sap/sapcar/sapcar
```

'unpack_source' can be list of paths to folders and/or files.

Another options is to set 'unpack_source' value to file or folder.

```ansible
    - hosts: all
      roles:
         - role: sap.sap_operations.unpack
      vars:
        unpack_source: /path/to/file.zip
        unpack_destination: /unpacked
        unpack_sapcar_exe_path: /usr/sap/sapcar/sapcar
```

## License

Apache 2

## Author Information

kksat
