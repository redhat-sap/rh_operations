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

# download

Role to download SAP software


Role to download SAP software from SAP Software Download Center (SWDC).
Username and password to access SAP SWDC are required.
Role is idemponent - bits that are already downloaded will not be downloaded again.
Idempotency is working by comparing SHA256 checksum for local files and files to be downloaded.
Role is checking if there is sufficient space available in destination folder.
Destination folder (variable `download_destination`) should already exist.
If destination folder does not exist, not directory or not writeable role will fail
For each file downloaded there is SHA256 checksum available on SAP SWDC, this checksum will be validated.
This is ensure that bits are downloaded correctly and were not tampered with.
SSL certificate is also checked when bits are downloaded, see download_validate_certs variable below.

By default role will download only one file with latest ReleaseDate, see parameters download_sort_attribute and download_one_file
Role return variables
**download_register_last**
Variable is set by the role and and available after role has been executed.
Variable contains information about last downloaded SAP alias
Variable is very useful if one wants to do something with downloaded files - unpack them, for instance.
See role sap.sap_operations.unpack
Examples
"download_register_last": {
"changed": true,
"failed": false,
"files": [
{
"DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000001293762023",
"changed": false,
"failed": false,
"filename": "saphostagentrpm_62-80004822.rpm",
"sha256": "1f7864d97268f505cd2cb7ab75188270590ee11ff8418f54229e0ee32f28f618"
}
]
}

Notes for variable ``download_register_last``
For each downloaded application there might be several elements in ``files`` list.
For each file that is downloaded, there are two variables ``changed`` and ``failed``.
If these variables are true, this is translated to higher levels.
If downloading of one url for an application failed, this is translated to variable ``download_register_application_last.changed`` and
``download_register_application_last.failed``

``sha256`` provided, because this is checksum from SAP SWDC metadata.
**download_register**
Variable is set by the role and and available after role has been executed.
Variable contains information about all downloaded SAP application. Across several executions of role ``sap.sap_operations.download``
Variable is very useful if one wants to do something with downloaded files - unpack them, for instance.
See role sap.sap_operations.unpack
Examples:
"download_register": {
"changed": true,
"failed": true,
"files": [
{
"DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000000269302024",
"changed": false,
"failed": false,
"filename": "saphostagentrpm_63-80004822.rpm",
"sha256": "673e39245b22cd5b609d7636de13cea9fdc6cb463c86526af5e523cf5c0c908d"
},
{
"DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000001293762023",
"changed": false,
"failed": false,
"filename": "saphostagentrpm_62-80004822.rpm",
"sha256": "1f7864d97268f505cd2cb7ab75188270590ee11ff8418f54229e0ee32f28f618"
}
]
}

Notes for variable ``download_register``:

With each run of role ``sap.sap_operations.download`` data is added to this variable.
With 5 runs of role ``sap.sap_operations.download`` ``results`` list will contain list of files downloaded in all 5 runs
This is a feature of the way how ansible handles variables.




## Role Variables

### Required parameters:


- [download_alias](#download_alias)

- [download_destination](#download_destination)

- [download_username](#download_username)

- [download_password](#download_password)
 

#### download_alias


_Type:_ `str`


_Required:_ `True`
_Choices:_
- sapcar-7.53
- sapcar-7.22
- saphostagent-7.22
- hana-server
- hana-client
- hana-cockpit
- swpm-1.0
- swpm-2.0
_Description:_
Alias of SAP software that will be downloaded.


 

#### download_destination


_Type:_ `path`


_Required:_ `True`
_Description:_
Folder where bits will be downloaded.
Should exists before role execution.
Ansible user should have write permission to this destination folder.
Role will check if there is sufficient space available on device.
If not role will fail with information about space requirements.
Ansible module ansible.builtin.uri is used to download SAP software from SWDC
This module downloads temp files to ansible_remote_tmp folder,
this folder has to have space to download largest file, if not - not enough space
error will be raised by Ansible.
See https://docs.ansible.com/ansible/latest/collections/ansible/builtin/sh_shell.html#parameter-remote_tmp
and https://docs.ansible.com/ansible/latest/collections/ansible/builtin/sh_shell.html#parameter-system_tmpdirs


 

#### download_username


_Type:_ `str`


_Required:_ `True`
_Description:_
Username (sap support user, suser) that will be used to download software.
By default value is from collection variable `sap_operations_download_username`.
Collection variable `sap_operations_download_username` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME


 

#### download_password


_Type:_ `str`


_Required:_ `True`
_Description:_
Password of provided username that will be used to download software
By default value is from collection variable `sap_operations_download_password`.
Collection variable `sap_operations_download_password` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD


 

#### download_description


_Type:_ `str`


_Required:_ `False`
_Description:_
All results from SWDC will be filtered "Description" should contain this value

 

#### download_infotype


_Type:_ `str`


_Required:_ `False`
_Description:_
All results from SWDC will be filtered "Infotype" should contain this value

 

#### download_object_type


_Type:_ `str`


_Required:_ `False`
_Description:_
All results from SWDC will be filtered "ObjectType" should contain this value

 

#### download_patch_level


_Type:_ `str`


_Required:_ `False`
_Description:_
All results from SWDC will be filtered "PatchLevel" should contain this value. Will be converted to string.

 

#### download_title


_Type:_ `str`


_Required:_ `False`
_Description:_
All results from SWDC will be filtered "Title" should contain this value

 

#### download_architecture


_Type:_ `str`

_Default:_ `x86_64`

_Required:_ `False`
_Choices:_
- x86_64
- ppc64le
- arm64
_Description:_
Architecture for which SAP software will be downloaded.
Not required, if not set will be set to architecture from `ansible_facts['architecture']`
One might want to download software for `x86_64` from PowerPC host - in that case this parameter will be useful.


 

#### download_system


_Type:_ `str`

_Default:_ `Linux`

_Required:_ `False`
_Choices:_
- Linux
_Description:_
System for which SAP software will be downloaded.
Not required, if not set will be set to system from `ansible_facts['system']`
One might want to download software for `Linux` from Windows host - in that case this parameter will be useful.


 

#### download_validate_certs


_Type:_ `bool`

_Default:_ `True`

_Required:_ `False`
_Description:_
Should be certificates validated (for https calls).
Might be required in some environment (for instance with no direct access to the internet)
Recommended to set to True.


 

#### download_timeout


_Type:_ `int`

_Default:_ `3600`

_Required:_ `False`
_Description:_
Download timeout (in seconds).

 

#### download_mode


_Type:_ `str`

_Default:_ `0755`

_Required:_ `False`
_Description:_
Permissions that will be set for downloaded files.

 

#### download_sort_attribute


_Type:_ `str`

_Default:_ `ReleaseDate`

_Required:_ `False`
_Choices:_
- ReleaseDate
- ChangeDate
_Description:_
Attribute used to sort list of items to download

 

#### download_one_file


_Type:_ `bool`

_Default:_ `True`

_Required:_ `False`
_Description:_
If at most one file has to be downloaded

 
 
