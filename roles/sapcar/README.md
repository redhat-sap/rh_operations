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

Role to manage sapcar


Role to manage sapcar binary



## Role Variables

### Required parameters:


- [sapcar_download_username](#sapcar_download_username)

- [sapcar_download_password](#sapcar_download_password)
 

#### sapcar_download_username


_Type:_ `str`


_Required:_ `True`
_Description:_
Username (sap support user, suser) that will be used to download software.
By default value is from collection variable `sap_operations_download_username`.
Collection variable `sap_operations_download_username` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME


 

#### sapcar_download_password


_Type:_ `str`


_Required:_ `True`
_Description:_
Password of provided username that will be used to download software
By default value is from collection variable `sap_operations_download_password`.
Collection variable `sap_operations_download_password` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD


 

#### sapcar_exe_path


_Type:_ `path`

_Default:_ `/usr/sap/sapcar/sapcar`

_Required:_ `False`
_Description:_
Path to sapcar executable file
Default value is from collection variable sap_operations_sapcar_exe_path
All parent directories to directory where sapcar executable should be located should exists and be writable for ansible user
Role will not create /usr/sap directory and will not set owner and mode for this
Default path is in /usr/sap, role expects that /usr/sap is present and writable for user the role is executed with, otherwise role will fail
As part of the role execution parent directory for sapcar_exe_path will be created

 

#### sapcar_state


_Type:_ `str`

_Default:_ `present`

_Required:_ `False`
_Choices:_
- present
- absent
_Description:_
State for sapcar executable
present - role will ensure that executable will downloaded and installed (copied to sapcar_exe_path)
present - will do any changes only if file sapcar_exe_path does not exists
absent - role will ensure that file at sapcar_exe_path is absent, containing directory will not be removed

 

#### sapcar_download_destination


_Type:_ `path`

_Default:_ `/tmp/sapcar_download_destination`

_Required:_ `False`
_Description:_
Path there sapcar binary will be downloaded (in case of sapcar_state='present')
Role will ensure that this folder exists

 

#### sapcar_patch_level


_Type:_ `str`


_Required:_ `False`
_Description:_
Patch level that will be downloaded and installed if sapcar_state='present'
sap.sap_operations.download role will be used to download sapcar binaries
sap.sap_operations.download role by default will download patch level with latest ReleaseDate,
see download role documentation

This makes this role quasi idempotent if sapcar_patch_level is not set explicitly -
later version of sapcar might be downloaded and installed if role executed in different times

Should be exact patch level available for current sapcar_version, see documentation for
sap.sap_operations.download role, otherwise nothing will be downloaded and installed.

In case there is no such patch level for selected sapcar version, download list will be empty and role will fail

 

#### sapcar_mode


_Type:_ `str`

_Default:_ `0755`

_Required:_ `False`
_Description:_
Permissions mode that will be used for all folders that are created by the role
(sapcar_download_destination and sapcar_exe_path) and sapcar executable destination sapcar_exe_path


 

#### sapcar_owner


_Type:_ `str`


_Required:_ `False`
_Description:_
Owner that will be used for all folders that are created by the role (sapcar_download_destination and sapcar_exe_path)
and sapcar executable destination sapcar_exe_path

By default is set to omit special variable - meaning current ansible_user will be used as owner

 

#### sapcar_version


_Type:_ `str`


_Required:_ `False`
_Description:_
Sapcar version that has to be downloaded and installed
By default will be automatically calculated as highest version available among all sapcar versions from sap.sap_operations.me_aliases filter

 
 

## Limitations

Username has to be email of SAP UID with only one Suser assigned. If more than one Suser is assigned to UID download will fail.

## Dependencies

Role has no dependencies to other roles.

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
