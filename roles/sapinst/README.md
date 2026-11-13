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

# sapinst

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`sapinst_product_id`](#parameter-sapinst_product_id)
  * [`sapinst_params`](#parameter-sapinst_params)
  * [`sapinst_folder`](#parameter-sapinst_folder)
  * [`sapinst_allow_direct_usage`](#parameter-sapinst_allow_direct_usage)
  * [`sapinst_skip_errorstep`](#parameter-sapinst_skip_errorstep)
  * [`sapinst_message_console_threshold`](#parameter-sapinst_message_console_threshold)
  * [`sapinst_directory_path`](#parameter-sapinst_directory_path)
  * [`sapinst_prefix`](#parameter-sapinst_prefix)
  * [`sapinst_suffix`](#parameter-sapinst_suffix)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Role to run sapinst to install SAP applications
> This role should not be called directly, but rather from other roles that install SAP products
> (like role smda for Solution Manager Diagnostic Agent installation)

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-sapinst_product_id"></a>`sapinst_product_id` | `str` | Yes | N/A | Product id<br>*Choices:* NW_DiagnosticsAgent:GENERIC.IND.PD, NW_Uninstall:GENERIC.IND.PD, download_service_toplevel:GENERIC.IND.PD |
| <a id="parameter-sapinst_params"></a>`sapinst_params` | `dict` | Yes | N/A | Dictionary of sapinst parameters, will be converted to inifile.params for installation |
| <a id="parameter-sapinst_folder"></a>`sapinst_folder` | `path` | No | `"/usr/sap/swpm"` | Folder where sapinst binary is located |
| <a id="parameter-sapinst_allow_direct_usage"></a>`sapinst_allow_direct_usage` | `bool` | No | `false` | Set true to allow direct call of this role, not recommended |
| <a id="parameter-sapinst_skip_errorstep"></a>`sapinst_skip_errorstep` | `bool` | No | `false` | If set to 'true', the first step with status ERROR is skipped; step status is set to 'OK'. See sapinst documentation for parameter SAPINST_SKIP_ERRORSTEP. |
| <a id="parameter-sapinst_message_console_threshold"></a>`sapinst_message_console_threshold` | `str` | No | `"error"` | sapinst parameter SAPINST_MESSAGE_CONSOLE_THRESHOLD Trace level console See sapinst documentation SAP default value is warning. This role uses default value error to limit sapinst console output<br>*Choices:* flow_trace, trace, info, phase, warning, error, external |
| <a id="parameter-sapinst_directory_path"></a>`sapinst_directory_path` | `path` | No | `"/tmp"` | Directory where temp sapinst_directory will be created |
| <a id="parameter-sapinst_prefix"></a>`sapinst_prefix` | `str` | No | `"sapinst"` | Prefix for temp directory sapinst_directory |
| <a id="parameter-sapinst_suffix"></a>`sapinst_suffix` | `str` | No | `""` | Suffix for temp directory sapinst_directory |

## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles

## Limitations<a id="limitations"></a>

Only tested in certain scenarios

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
