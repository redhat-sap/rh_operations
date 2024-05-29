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

# cloudconnector

Role to manage SAP cloud connector


Role to manage SAP cloud connector
Role will download necessary binaries from tools.hana.ondemand.com
Role can install both rpm and portable versions of SAP Cloud Connector, see role documentation
Portable version is installed via copy of downloaded archive content, removed via removing installation directory
RPM version installation requires root access
Cloud connector requires SAP JVM to be installed, see SAP documentation.
SAP JVM can be installed with role sap.sap_operations.sapjvm
Role will use ansible_facts to determine current host os system and architecture to download correct binaries
By using this role and downloading SAP software from tools.hana.ondemand.com you accept SAP developer license agreement
One can find more details on tools.hana.ondemand.com



## Role Variables

### Required parameters:


- [cloudconnector_version](#cloudconnector_version)
 

#### cloudconnector_version


_Type:_ `str`


_Required:_ `True`
_Description:_
Cloud connector version

 

#### cloudconnector_state


_Type:_ `str`


_Required:_ `False`
_Choices:_
- present
- absent
_Description:_
SAP cloud connector state

 

#### cloudconnector_download_filename


_Type:_ `str`


_Required:_ `False`
_Description:_
Filename of downloaded SAP cloud connector binaries,
By default Filename is  sapcc-{{ cloudconnector_version }}-{{ cloudconnector_system }}-{{ cloudconnector_architecture }}.{{ cloudconnector_archive_extension }} 
See definition of variables in defaults/main.yml and vars/main.yml

 

#### cloudconnector_download_filepath


_Type:_ `str`


_Required:_ `False`
_Description:_
Complete path to file where SAP cloud connector binary will be downloaded
by default is {{ cloudconnector_download_destination }}/{{ cloudconnector_download_filename }}, see other variables
If this is set it will overwrite cloudconnector_download_destination and cloudconnector_download_filename variable values

 

#### cloudconnector_download_timeout_seconds


_Type:_ `int`

_Default:_ `3600`

_Required:_ `False`
_Description:_
Timeout set for download SAP cloud connector task

 

#### cloudconnector_portable_install_destination


_Type:_ `path`

_Default:_ `/opt/sap/scc`

_Required:_ `False`
_Description:_
Folder where SAP cloud connector binary will be installed, only relevant for portable installations

 

#### cloudconnector_architecture


_Type:_ `str`


_Required:_ `False`
_Choices:_
- x64
- ppc64le
- aarch64
_Description:_
Cloud connector architecture
If not specified, it will be detected automatically using ansible_facts['architecture']
No need to collect facts before running this role. It will be done automatically.
If ansible_facts['architecture'] is not defined, default value C(x64) will be used.


 

#### cloudconnector_download_destination


_Type:_ `str`

_Default:_ `/tmp`

_Required:_ `False`
_Description:_
Cloud connector download destination

 

#### cloudconnector_unpack_destination


_Type:_ `str`

_Default:_ `/tmp/cloudconnector_unpacked`

_Required:_ `False`
_Description:_
Cloud connector unpack destination

 

#### cloudconnector_system


_Type:_ `str`

_Default:_ `linux`

_Required:_ `False`
_Choices:_
- linux
- darwin
_Description:_
Cloud connector OS system
If not specified, it will be detected automatically using ansible_facts['system']
No need to collect facts before running this role. It will be done automatically.
If ansible_facts['system'] is not defined, default value C(linux) will be used.


 

#### cloudconnector_portable


_Type:_ `bool`

_Default:_ `False`

_Required:_ `False`
_Description:_
Bool to define if cloud connector should be installed in portable mode

 

#### cloudconnector_eula


_Type:_ `str`

_Default:_ `eula_3_2_agreed=tools.hana.ondemand.com/developer-license-3_2.txt`

_Required:_ `False`
_Description:_
Confirms that you are agree to SAP developer license

 
 

## Limitations

None

## Dependencies

Role has no dependencies to other roles.

## Example Playbooks

```ansible
- hosts: all
  tasks:
    - name: Make sure that portable cloud connector present
      ansible.builtin.include_role:
        name: sap.sap_operations.cloudconnector
      vars:
        cloudconnector_version: 2.16.2
        cloudconnector_portable: false
```

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
