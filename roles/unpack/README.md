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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`unpack_source`](#parameter-unpack_source)
  * [`unpack_destination`](#parameter-unpack_destination)
  * [`unpack_manifest`](#parameter-unpack_manifest)
  * [`unpack_sapcar_exe_path`](#parameter-unpack_sapcar_exe_path)
  * [`sap_operations_sapcar_exe_path`](#parameter-sap_operations_sapcar_exe_path)
  * [`unpack_sapcar_extension`](#parameter-unpack_sapcar_extension)
  * [`unpack_zip_extension`](#parameter-unpack_zip_extension)
* [Requirements](#requirements)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role to unpack *.sar and *.zip files.
> This role is NOT idempotent for *.sar files.
> Meaning it will unpack all the *.sar files every time role is executed.
> For unpacking *.zip files Ansible module ansible.builtin.unarchive is used and this module is idempotent.
> Role prerequisites:
>   * 'unzip' is installed (will not be installed by this role), if 'unzip' command is missing, role will fail.
>   * SAPCAR should be installed in 'sap_operations_sapcar_exe_path' (default value /usr/sap/sapcar/sapcar).
>   If SAPCAR is not installed at 'sap_operations_sapcar_exe_path' role will fail.
>   Ansible user has to have permissions to execute SAPCAR.

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-unpack_source"></a>`unpack_source` | `list` | Yes | N/A | List or str value - files and/or folders that should be unpacked. Folder and/or files that are missing or cannot be accessed will be ignored. Only files on first level in directory will be processed, role does not look recursively in the directory. |
| <a id="parameter-unpack_destination"></a>`unpack_destination` | `str` | Yes | N/A | Folder where files will be unpacked. If folder does not exist, it will be created. Ansible user has to have permissions to create the folder and write to the folder if it already exists. |
| <a id="parameter-unpack_manifest"></a>`unpack_manifest` | `bool` | No | `true` | Flag to unpack SAPCAR archives using option "-manifest SIGNATURE.SMF". If set to true option "-manifest SIGNATURE.SMF" will be used |
| <a id="parameter-unpack_sapcar_exe_path"></a>`unpack_sapcar_exe_path` | `str` | No | `"/usr/sap/sapcar/sapcar"` | Path to SAPCAR executable file. SAPCAR should be installed as a prerequisite for this role.<br><br>This variable is equivalent to sap_operations collection variable 'sap_operations_sapcar_exe_path'. |
| <a id="parameter-sap_operations_sapcar_exe_path"></a>`sap_operations_sapcar_exe_path` | `str` | No | `"/usr/sap/sapcar/sapcar"` | Collection variable that provides the path to the SAPCAR executable file. Role parameter `unpack_sapcar_exe_path` defaults to this collection variable. |
| <a id="parameter-unpack_sapcar_extension"></a>`unpack_sapcar_extension` | `str` | No | `"sar"` | Extension of SAPCAR archive files that will be unpacked. Only files with this extension will be processed as *.sar files. |
| <a id="parameter-unpack_zip_extension"></a>`unpack_zip_extension` | `str` | No | `"zip"` | Extension of zip archive files that will be unpacked. Only files with this extension will be processed as *.zip files. |

## Requirements<a id="requirements"></a>

unzip is installed (will not be installed by this role), if unzip command is missing, role will fail

SAPCAR should be installed in sap_operations_sapcar_exe_path (default value /usr/sap/sapcar/sapcar)

## Example Playbooks<a id="examples"></a>

```ansible
- hosts: all
  tasks:
    - name: Unpack archives
      ansible.builtin.include_role:
        name: sap.sap_operations.unpack
      vars:
        unpack_source:
          - /tmp
          - /path/to/file.zip
          - /path/to/file.sar
        unpack_destination: /unpacked
```


## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

None

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
