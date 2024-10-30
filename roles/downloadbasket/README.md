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

# downloadbasket

Role to download SAP SWDC download basket content


Role is idemponent - bits that are already downloaded will not be overwritten again.
Role is checking if there is sufficient space available in destination folder and failing if there is not enough space on mount point
For each file downloaded there is SHA256 checksum available on SAP SWDC, this checksum will be validated.
This is ensure that bits are downloaded correctly and were not tampered with.
Checksum and filename will be used to skip files with same filename and sha256 checksum if they are already available in downloadbasket_destination

Role return variables:
**downloadbasket_register**
Variable is set (using set_fact) by the role and and available after role has been executed.
Variable contains information about last downloaded content from SAP SWDC download basket
This variable will contain results of all executions of downloadbasket role, for instance
when role executed with different usernames.
Variable is very useful if one wants to do something with downloaded files - unpack them, for instance.
See role sap.sap_operations.unpack

Examples:
"downloadbasket_register": {
"changed": true,
"failed": false,
"files": [
{
"DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000000098712022",
"changed": false,
"failed": false,
"filename": "SAPCAR_1115-70006237.EXE",
"sha256": "f362f57ebdc7f8c2e2a2d5532a53e5f2dce26583c1b8c619fe3ed884d979794e"
},
{
"DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000000098732022",
"changed": false,
"failed": false,
"filename": "SAPCAR_1115-70006234.EXE",
"sha256": "d2fddbe1b7e7858da01864837a05a68f2461fad5f01877e4fa9e07b85e9404e6"
},
{
"DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000000099952022",
"changed": false,
"failed": false,
"filename": "SAPCAR_1115-70006239.EXE",
"sha256": "fe2f7ee00ff6d9f7ed7086cae75e66ebe9cc37eb1bf667666c0d7a8cee110cb5"
}
]
}
Notes for variable ``downloadbasket_register``:
With each run of role ``sap.sap_operations.downloadbasket`` data is added to this variable.
With 5 runs of role ``sap.sap_operations.download`` ``files`` list will contain information about downloaded files from all 5 runs
This is a feature of the way how ansible handles variables.




## Role Variables

### Required parameters:


- [downloadbasket_destination](#downloadbasket_destination)

- [downloadbasket_username](#downloadbasket_username)

- [downloadbasket_password](#downloadbasket_password)
 

#### downloadbasket_destination


_Type:_ `path`


_Required:_ `True`
_Description:_
Path where bits will be downloaded.
Should exists before role execution.
Ansible user should have write permission to this destination folder.
Role will check if there is sufficient space available on device.
If not role will fail with information about space requirements.
Please be mindful and avoid race condition when this destination is shared folder among several hosts
- ansible tasks are executed in parallel by default and it might have undesirable consequences.


 

#### downloadbasket_username


_Type:_ `str`


_Required:_ `True`
_Description:_
Username (sap support user, suser) that will be used to download software.
By default value is from collection variable `sap_operations_download_username`.
Collection variable `sap_operations_download_username` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME


 

#### downloadbasket_password


_Type:_ `str`


_Required:_ `True`
_Description:_
Password of provided username that will be used to download software
By default value is from collection variable `sap_operations_download_password`.
Collection variable `sap_operations_download_password` default value is set\
to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD


 

#### downloadbasket_validate_certs


_Type:_ `bool`

_Default:_ `True`

_Required:_ `False`
_Description:_
Should be certificates validated (for https calls).
Might be required in some environment (for instance with no direct access to the internet)
Recommended to set to True.


 

#### downloadbasket_timeout


_Type:_ `int`

_Default:_ `3600`

_Required:_ `False`
_Description:_
Download timeout (in seconds).


 

#### downloadbasket_mode


_Type:_ `str`

_Default:_ `0755`

_Required:_ `False`
_Description:_
Permissions that will be set for downloaded files.


 
 
