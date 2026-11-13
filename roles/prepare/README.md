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

# prepare

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`prepare_assert`](#parameter-prepare_assert)
* [Requirements](#requirements)
* [Playbook examples](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Prepare RHEL managed host to run content from sap.sap_operations
> Role ensures that all collection sap.sap_operations prerequisites are met.
> Role works in two modes - normal and assert.
> In normal mode it ensures that all prerequisites to run content from collection sap.sap_operations are met.
> In assert mode it fails if collection prerequisites are not met on the host.
> Role will only collect facts if OS distribution is not RedHat.

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-prepare_assert"></a>`prepare_assert` | `bool` | No | `false` | If set to True role will only assert that all sap.sap_operations collection prerequisites are met.<br><br>Is set to False (default) will ensure that all sap.sap_operations collection prerequisites are met (root access required) |

## Requirements<a id="requirements"></a>

Role requires root access in order to install necessary packages and other sap.sap_operations collection prerequisites (normal mode).

## Playbook examples<a id="examples"></a>


```ansible
- hosts: all
  roles:
    - role: sap.sap_operations.prepare
```

```ansible
- hosts: all
  vars:
    prepare_assert: true
  roles:
    - role: sap.sap_operations.prepare
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
