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

Role to run sapinst to install SAP applications


Role to run sapinst to install SAP applications
This role should not be called directly, but rather from other roles that install SAP products
(like role smda for Solution Manager Diagnostic Agent installation)




## Role Variables

### Required parameters:


- [sapinst_product_id](#sapinst_product_id)

- [sapinst_params](#sapinst_params)
 

#### sapinst_product_id


_Type:_ `str`


_Required:_ `True`
_Choices:_
- NW_DiagnosticsAgent:GENERIC.IND.PD
- NW_Uninstall:GENERIC.IND.PD
- download_service_toplevel:GENERIC.IND.PD
_Description:_
Product id

 

#### sapinst_params


_Type:_ `dict`


_Required:_ `True`
_Description:_
Dictionary of sapinst parameters, will be converted to inifile.params for installation

 

#### sapinst_folder


_Type:_ `path`

_Default:_ `/usr/sap/swpm`

_Required:_ `False`
_Description:_
Folder where sapinst binary is located

 

#### sapinst_allow_direct_usage


_Type:_ `bool`

_Default:_ `False`

_Required:_ `False`
_Description:_
Set true to allow direct call of this role, not recommended

 

#### sapinst_skip_errorstep


_Type:_ `bool`

_Default:_ `False`

_Required:_ `False`
_Description:_
If set to 'true', the first step with status ERROR is skipped; step status is set to 'OK'.
See sapinst documentation for parameter SAPINST_SKIP_ERRORSTEP.


 

#### sapinst_message_console_threshold


_Type:_ `str`

_Default:_ `error`

_Required:_ `False`
_Choices:_
- flow_trace
- trace
- info
- phase
- warning
- error
- external
_Description:_
sapinst parameter SAPINST_MESSAGE_CONSOLE_THRESHOLD
Trace level console
See sapinst documentation
SAP default value is warning.
This role uses default value error to limit sapinst console output


 

#### sapinst_directory_path


_Type:_ `path`

_Default:_ `/tmp`

_Required:_ `False`
_Description:_
Directory where temp sapinst_directory will be created

 

#### sapinst_prefix


_Type:_ `str`

_Default:_ `sapinst`

_Required:_ `False`
_Description:_
Prefix for temp directory sapinst_directory

 

#### sapinst_suffix


_Type:_ `str`


_Required:_ `False`
_Description:_
Suffix for temp directory sapinst_directory

 
 

## Limitations

Only tested in certain scenarios

## Dependencies

Role has no dependencies to other roles

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
