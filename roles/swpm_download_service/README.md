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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`sap_operations_download_username`](#parameter-sap_operations_download_username)
  * [`sap_operations_download_password`](#parameter-sap_operations_download_password)
  * [`swpm_download_service_username`](#parameter-swpm_download_service_username)
  * [`swpm_download_service_password`](#parameter-swpm_download_service_password)
  * [`swpm_download_service_plan_id`](#parameter-swpm_download_service_plan_id)
  * [`swpm_download_service_directory`](#parameter-swpm_download_service_directory)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Use SWPM download service to download binaries for maintenance plan.
> Role is not idempotent it will call sapinst binary and try to download binaries from Maintenance planner plan id every time it is executed
> Role expects that SAP SWPM already installed in default location.
> How to install SAP SWPM see role sap.sap_operations.swpm
> For non default locations see role sap.sap_operations.sapinst
> Role expects that user group 'sapinst' already exists, it will fail if not.

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-sap_operations_download_username"></a>`sap_operations_download_username` | `str` | No | N/A | Collection variable that provides the username (sap support user, suser) for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME. Role parameter `swpm_download_service_username` defaults to this […] |
| <a id="parameter-sap_operations_download_password"></a>`sap_operations_download_password` | `str` | No | N/A | Collection variable that provides the password of the username for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD. Role parameter `swpm_download_service_password` defaults to this collection […] |
| <a id="parameter-swpm_download_service_username"></a>`swpm_download_service_username` | `str` | Yes | N/A | Username (sap support user, suser) that will be used to download software. This should be suser id (S000) not email. By default value is from collection variable `sap_operations_download_username`. Collection variable […] |
| <a id="parameter-swpm_download_service_password"></a>`swpm_download_service_password` | `str` | Yes | N/A | Password of provided username that will be used to download software By default value is from collection variable `sap_operations_download_password`. Collection variable `sap_operations_download_password` default value is set to environment variable […] |
| <a id="parameter-swpm_download_service_plan_id"></a>`swpm_download_service_plan_id` | `str` | Yes | N/A | Maintenance planner plan id. All binaries in that plan will be downloaded. |
| <a id="parameter-swpm_download_service_directory"></a>`swpm_download_service_directory` | `path` | Yes | N/A | Directory where all binaries will be downloaded. Should be writable. |

## Example Playbooks<a id="examples"></a>


- name: Run role swpm_download_service
  ansible.builtin.include_role:
    name: sap.sap_operations.swpm_download_service
  vars:
    swpm_download_service_directory: /tmp/
    swpm_download_service_plan_id: '1002099834'


## Dependencies<a id="dependencies"></a>

Role executes sap.sap_operations.sapinst role.

Role expects that SAP SWPM is already installed in default location, see role sap.sap_operations.sapinst and sap.sap_operations.swpm

## Limitations<a id="limitations"></a>



## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
