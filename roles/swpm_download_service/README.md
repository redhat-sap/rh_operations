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

# swpm_download_service

Use SWPM download service to download binaries for maintenance plan.


Use SWPM download service to download binaries for maintenance plan.
Role is not idempotent it will call sapinst binary and try to download binaries from Maintenance planner plan id every time it is executed
Role expects that SAP SWPM already installed in default location. 
How to install SAP SWPM see role sap.sap_operations.swpm
For non default locations see role sap.sap_operations.sapinst

Role expects that user group 'sapinst' already exists, it will fail if not.



## Role Variables

### Required parameters:


- [swpm_download_service_username](#swpm_download_service_username)

- [swpm_download_service_password](#swpm_download_service_password)

- [swpm_download_service_plan_id](#swpm_download_service_plan_id)

- [swpm_download_service_directory](#swpm_download_service_directory)
 

#### swpm_download_service_username


_Type:_ `str`


_Required:_ `True`
_Description:_
Username (sap support user, suser) that will be used to download software.
This should be suser id (S000) not email.
By default value is from collection variable `sap_operations_download_username`.
Collection variable `sap_operations_download_username` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME


 

#### swpm_download_service_password


_Type:_ `str`


_Required:_ `True`
_Description:_
Password of provided username that will be used to download software
By default value is from collection variable `sap_operations_download_password`.
Collection variable `sap_operations_download_password` default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD


 

#### swpm_download_service_plan_id


_Type:_ `str`


_Required:_ `True`
_Description:_
Maintenance planner plan id. All binaries in that plan will be downloaded.


 

#### swpm_download_service_directory


_Type:_ `path`


_Required:_ `True`
_Description:_
Directory where all binaries will be downloaded. 
Should be writable.


 
 

## Limitations


## Dependencies

Role executes sap.sap_operations.sapinst role.
Role expects that SAP SWPM is already installed in default location, see role sap.sap_operations.sapinst and sap.sap_operations.swpm

## Example Playbooks


- name: Run role swpm_download_service
  ansible.builtin.include_role:
    name: sap.sap_operations.swpm_download_service
  vars:
    swpm_download_service_directory: /tmp/
    swpm_download_service_plan_id: '1002099834'


## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
