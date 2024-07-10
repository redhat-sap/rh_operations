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

Manage SAP SWPM (download / install / uninstall)


Manage SAP SWPM
Role will download SAP SWPM binary from SAP SWDC (software download center)
Role will use ansible_facts to determine current host os system and architecture to download correct binary
Role will download latest SP available from SAP SWDC web site in that sense role is not idempotent,
because next time one will run this role, there might be new SP of SAP SWPM

Role will not do anything if swpm_state='present' and file sapinst exists in swpm_unpack_destination



## Role Variables

### Required parameters:


- [swpm_download_username](#swpm_download_username)

- [swpm_download_password](#swpm_download_password)
 

#### swpm_download_username


_Type:_ `str`


_Required:_ `True`
_Description:_
Username (sap support user, suser) that will be used to download software.
By default value is from collection variable `sap_operations_download_username`.
Collection variable `sap_operations_download_username` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME


 

#### swpm_download_password


_Type:_ `str`


_Required:_ `True`
_Description:_
Password of provided username that will be used to download software
By default value is from collection variable `sap_operations_download_password`.
Collection variable `sap_operations_download_password` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD


 

#### swpm_state


_Type:_ `str`

_Default:_ `present`

_Required:_ `False`
_Choices:_
- present
- downloaded
- absent
_Description:_
State for SAP SWPM
present - role will ensure that executable will downloaded and installed (copied to swpm_unpack_destination)
present - will do any changes only if file sapinst in swpm_unpack_destination does not exists
absent - role will ensure that SAP SWPM is absent, swpm_unpack_destination directory will be removed
downloaded - role will only download SAP SWPM binary archive

 

#### swpm_unpack_destination


_Type:_ `path`

_Default:_ `/usr/sap/swpm`

_Required:_ `False`
_Description:_
Path there SAP SWPM binary archive will be unpacked (in case of swpm_state='present')
Role will not create swpm_unpack_destination folder or any folders above it. It has to exists

 

#### swpm_download_destination


_Type:_ `path`

_Default:_ `/tmp/`

_Required:_ `False`
_Description:_
Path there SAP SWPM binary archive will be downloaded (in case of swpm_state='present' or swpm_state='downloaded')
Role will not create swpm_download_destination folder or any folders above it. It has to exists

 

#### swpm_version


_Type:_ `str`

_Default:_ `2.0`

_Required:_ `False`
_Choices:_
- 2.0
- 1.0
_Description:_
SAP SWPM version that will be downloaded and / or installed
Role will always download SP version that was changed last on SAP SWDC (software download center)

 
 

## Limitations

Tested only on RHEL 8 and 9
Tested only on x86_64 architecture

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks



## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
