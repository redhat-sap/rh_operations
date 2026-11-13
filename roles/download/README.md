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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`download_alias`](#parameter-download_alias)
  * [`download_destination`](#parameter-download_destination)
  * [`sap_operations_download_username`](#parameter-sap_operations_download_username)
  * [`sap_operations_download_password`](#parameter-sap_operations_download_password)
  * [`download_username`](#parameter-download_username)
  * [`download_password`](#parameter-download_password)
  * [`download_description`](#parameter-download_description)
  * [`download_infotype`](#parameter-download_infotype)
  * [`download_object_type`](#parameter-download_object_type)
  * [`download_patch_level`](#parameter-download_patch_level)
  * [`download_title`](#parameter-download_title)
  * [`download_release_date`](#parameter-download_release_date)
  * [`download_change_date`](#parameter-download_change_date)
  * [`download_architecture`](#parameter-download_architecture)
  * [`download_system`](#parameter-download_system)
  * [`download_os_family`](#parameter-download_os_family)
  * [`download_validate_certs`](#parameter-download_validate_certs)
  * [`download_timeout`](#parameter-download_timeout)
  * [`download_mode`](#parameter-download_mode)
  * [`download_sort_attribute`](#parameter-download_sort_attribute)
  * [`download_one_file`](#parameter-download_one_file)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role to download SAP software
> Role to download SAP software from SAP Software Download Center (SWDC).
> Username and password to access SAP SWDC are required.
> Role is idemponent - bits that are already downloaded will not be downloaded again.
> Idempotency is working by comparing SHA256 checksum for local files and files to be downloaded.
> Role is checking if there is sufficient space available in destination folder.
> Destination folder (variable `download_destination`) should already exist.
> If destination folder does not exist, not directory or not writeable role will fail
> For each file downloaded there is SHA256 checksum available on SAP SWDC, this checksum will be validated.
> This is ensure that bits are downloaded correctly and were not tampered with.
> SSL certificate is also checked when bits are downloaded, see download_validate_certs variable below.
> By default role will download only one file with latest ReleaseDate, see parameters download_sort_attribute and download_one_file
> Role return variables
> **download_register_last**
> Variable is set by the role and and available after role has been executed.
> Variable contains information about last downloaded SAP alias
> Variable is very useful if one wants to do something with downloaded files - unpack them, for instance.
> See role sap.sap_operations.unpack
> Examples
> "download_register_last": {
> "changed": true,
> "failed": false,
> "files": [
> {
> "DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000001293762023",
> "changed": false,
> "failed": false,
> "filename": "saphostagentrpm_62-80004822.rpm",
> "sha256": "1f7864d97268f505cd2cb7ab75188270590ee11ff8418f54229e0ee32f28f618"
> }
> ]
> }
> Notes for variable ``download_register_last``
> For each downloaded application there might be several elements in ``files`` list.
> For each file that is downloaded, there are two variables ``changed`` and ``failed``.
> If these variables are true, this is translated to higher levels.
> If downloading of one url for an application failed, this is translated to variable ``download_register_application_last.changed`` and
> ``download_register_application_last.failed``
> ``sha256`` provided, because this is checksum from SAP SWDC metadata.
> **download_register**
> Variable is set by the role and and available after role has been executed.
> Variable contains information about all downloaded SAP application. Across several executions of role ``sap.sap_operations.download``
> Variable is very useful if one wants to do something with downloaded files - unpack them, for instance.
> See role sap.sap_operations.unpack
> Examples:
> "download_register": {
> "changed": true,
> "failed": true,
> "files": [
> {
> "DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000000269302024",
> "changed": false,
> "failed": false,
> "filename": "saphostagentrpm_63-80004822.rpm",
> "sha256": "673e39245b22cd5b609d7636de13cea9fdc6cb463c86526af5e523cf5c0c908d"
> },
> {
> "DirectDownloadUrl": "https://softwaredownloads.sap.com/file/0020000001293762023",
> "changed": false,
> "failed": false,
> "filename": "saphostagentrpm_62-80004822.rpm",
> "sha256": "1f7864d97268f505cd2cb7ab75188270590ee11ff8418f54229e0ee32f28f618"
> }
> ]
> }
> Notes for variable ``download_register``:
> With each run of role ``sap.sap_operations.download`` data is added to this variable.
> With 5 runs of role ``sap.sap_operations.download`` ``results`` list will contain list of files downloaded in all 5 runs
> This is a feature of the way how ansible handles variables.

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-download_alias"></a>`download_alias` | `str` | Yes | N/A | Alias of SAP software that will be downloaded.<br>*Choices:* sapcar-7.53, sapcar-7.22, saphostagent-7.22, hana-server, hana-client, hana-cockpit, swpm-1.0, swpm-2.0 |
| <a id="parameter-download_destination"></a>`download_destination` | `path` | Yes | N/A | Folder where bits will be downloaded. Should exists before role execution. Ansible user should have write permission to this destination folder. Role will check if there is sufficient space available on device. If not role will fail with information […] |
| <a id="parameter-sap_operations_download_username"></a>`sap_operations_download_username` | `str` | No | N/A | Collection variable that provides the username (sap support user, suser) for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_USERNAME. Role parameter `download_username` defaults to this collection variable. |
| <a id="parameter-sap_operations_download_password"></a>`sap_operations_download_password` | `str` | No | N/A | Collection variable that provides the password of the username for software downloads. Default value is set to environment variable SAP_OPERATIONS_DOWNLOAD_PASSWORD. Role parameter `download_password` defaults to this collection variable. |
| <a id="parameter-download_username"></a>`download_username` | `str` | Yes | N/A | Username (sap support user, suser) that will be used to download software. By default value is from collection variable `sap_operations_download_username`. Collection variable `sap_operations_download_username` default value is set to environment […] |
| <a id="parameter-download_password"></a>`download_password` | `str` | Yes | N/A | Password of provided username that will be used to download software By default value is from collection variable `sap_operations_download_password`. Collection variable `sap_operations_download_password` default value is set to environment variable […] |
| <a id="parameter-download_description"></a>`download_description` | `str` | No | `""` | All results from SWDC will be filtered "Description" should contain this value |
| <a id="parameter-download_infotype"></a>`download_infotype` | `str` | No | `""` | All results from SWDC will be filtered "Infotype" should contain this value |
| <a id="parameter-download_object_type"></a>`download_object_type` | `str` | No | `""` | All results from SWDC will be filtered "ObjectType" should contain this value |
| <a id="parameter-download_patch_level"></a>`download_patch_level` | `str` | No | `""` | All results from SWDC will be filtered "PatchLevel" should contain this value. Will be converted to string. |
| <a id="parameter-download_title"></a>`download_title` | `str` | No | `""` | All results from SWDC will be filtered "Title" should contain this value |
| <a id="parameter-download_release_date"></a>`download_release_date` | `str` | No | `"0000000000000"` | All results from SWDC will be filtered "ReleaseDate" should be greater or equal to this value |
| <a id="parameter-download_change_date"></a>`download_change_date` | `str` | No | `"0000000000000"` | All results from SWDC will be filtered "ChangeDate" should be greater or equal to this value |
| <a id="parameter-download_architecture"></a>`download_architecture` | `str` | No | `"x86_64"` | Architecture for which SAP software will be downloaded. Not required, if not set will be set to architecture from `ansible_facts['architecture']` One might want to download software for `x86_64` from PowerPC host - in that case this parameter will be […]<br>*Choices:* x86_64, ppc64le, arm64 |
| <a id="parameter-download_system"></a>`download_system` | `str` | No | `"Linux"` | System for which SAP software will be downloaded. Not required, if not set will be set to system from `ansible_facts['system']` One might want to download software for `Linux` from Windows host - in that case this parameter will be useful.<br>*Choices:* Linux |
| <a id="parameter-download_os_family"></a>`download_os_family` | `str` | No | `"Linux"` | OS family for which SAP software will be downloaded, passed to the SWDC query. If not set will be set to `Linux`. |
| <a id="parameter-download_validate_certs"></a>`download_validate_certs` | `bool` | No | `true` | Should be certificates validated (for https calls). Might be required in some environment (for instance with no direct access to the internet) Recommended to set to True. |
| <a id="parameter-download_timeout"></a>`download_timeout` | `int` | No | `3600` | Download timeout (in seconds). |
| <a id="parameter-download_mode"></a>`download_mode` | `str` | No | `"0755"` | Permissions that will be set for downloaded files. |
| <a id="parameter-download_sort_attribute"></a>`download_sort_attribute` | `str` | No | `"ReleaseDate"` | Attribute used to sort list of items to download<br>*Choices:* ReleaseDate, ChangeDate |
| <a id="parameter-download_one_file"></a>`download_one_file` | `bool` | No | `true` | If at most one file has to be downloaded |

## Example Playbooks<a id="examples"></a>

```ansible
- hosts: all
  tasks:
    - name: Download SAP Host Agent
      ansible.builtin.include_role:
        name: sap.sap_operations.download
      vars:
        download_alias: S490000
        download_destination: /tmp/download_destination
        download_username: "{{ sap_operations_download_username }}"
        download_password: "{{ sap_operations_download_password }}"
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
