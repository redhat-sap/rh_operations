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

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`cloudconnector_state`](#parameter-cloudconnector_state)
  * [`cloudconnector_download_filename`](#parameter-cloudconnector_download_filename)
  * [`cloudconnector_download_filepath`](#parameter-cloudconnector_download_filepath)
  * [`cloudconnector_download_timeout_seconds`](#parameter-cloudconnector_download_timeout_seconds)
  * [`cloudconnector_portable_install_destination`](#parameter-cloudconnector_portable_install_destination)
  * [`cloudconnector_architecture`](#parameter-cloudconnector_architecture)
  * [`cloudconnector_version`](#parameter-cloudconnector_version)
  * [`cloudconnector_download_destination`](#parameter-cloudconnector_download_destination)
  * [`cloudconnector_unpack_destination`](#parameter-cloudconnector_unpack_destination)
  * [`cloudconnector_system`](#parameter-cloudconnector_system)
  * [`cloudconnector_portable`](#parameter-cloudconnector_portable)
  * [`cloudconnector_eula`](#parameter-cloudconnector_eula)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role to manage SAP cloud connector
> Role will download necessary binaries from tools.hana.ondemand.com
> Role can install both rpm and portable versions of SAP Cloud Connector, see role documentation
> Portable version is installed via copy of downloaded archive content, removed via removing installation directory
> RPM version installation requires root access
> Cloud connector requires SAP JVM to be installed, see SAP documentation.
> SAP JVM can be installed with role sap.sap_operations.sapjvm
> Role will use ansible_facts to determine current host os system and architecture to download correct binaries
> By using this role and downloading SAP software from tools.hana.ondemand.com you accept SAP developer license agreement
> One can find more details on tools.hana.ondemand.com

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-cloudconnector_state"></a>`cloudconnector_state` | `str` | No | N/A | SAP cloud connector state<br>*Choices:* present, absent |
| <a id="parameter-cloudconnector_download_filename"></a>`cloudconnector_download_filename` | `str` | No | N/A | Filename of downloaded SAP cloud connector binaries,<br><br>By default Filename is {% raw %} sapcc-{{ cloudconnector_version }}-{{ cloudconnector_system }}-{{ cloudconnector_architecture }}.{{ cloudconnector_archive_extension }} {% endraw […] |
| <a id="parameter-cloudconnector_download_filepath"></a>`cloudconnector_download_filepath` | `str` | No | N/A | Complete path to file where SAP cloud connector binary will be downloaded<br><br>by default is {% raw %}{{ cloudconnector_download_destination }}/{{ cloudconnector_download_filename }}{% endraw %}, see other variables<br><br>If this is set it will […] |
| <a id="parameter-cloudconnector_download_timeout_seconds"></a>`cloudconnector_download_timeout_seconds` | `int` | No | `3600` | Timeout set for download SAP cloud connector task |
| <a id="parameter-cloudconnector_portable_install_destination"></a>`cloudconnector_portable_install_destination` | `path` | No | `"/opt/sap/scc"` | Folder where SAP cloud connector binary will be installed, only relevant for portable installations |
| <a id="parameter-cloudconnector_architecture"></a>`cloudconnector_architecture` | `str` | No | N/A | Cloud connector architecture If not specified, it will be detected automatically using ansible_facts['architecture'] No need to collect facts before running this role. It will be done automatically. If ansible_facts['architecture'] is not defined, […]<br>*Choices:* x64, ppc64le, aarch64 |
| <a id="parameter-cloudconnector_version"></a>`cloudconnector_version` | `str` | Yes | N/A | Cloud connector version |
| <a id="parameter-cloudconnector_download_destination"></a>`cloudconnector_download_destination` | `str` | No | `"/tmp"` | Cloud connector download destination |
| <a id="parameter-cloudconnector_unpack_destination"></a>`cloudconnector_unpack_destination` | `str` | No | `"/tmp/cloudconnector_unpacked"` | Cloud connector unpack destination |
| <a id="parameter-cloudconnector_system"></a>`cloudconnector_system` | `str` | No | `"linux"` | Cloud connector OS system If not specified, it will be detected automatically using ansible_facts['system'] No need to collect facts before running this role. It will be done automatically. If ansible_facts['system'] is not defined, default value […]<br>*Choices:* linux, darwin |
| <a id="parameter-cloudconnector_portable"></a>`cloudconnector_portable` | `bool` | No | `false` | Bool to define if cloud connector should be installed in portable mode |
| <a id="parameter-cloudconnector_eula"></a>`cloudconnector_eula` | `str` | No | `"eula_3_2_agreed=tools.hana.ondemand.com/developer-license-3_2.txt"` | Confirms that you are agree to SAP developer license |

## Example Playbooks<a id="examples"></a>

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

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

None

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
