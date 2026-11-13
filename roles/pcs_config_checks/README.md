<!--
SPDX-License-Identifier: GPL-3.0-only
SPDX-FileCopyrightText: 2023 Red Hat, Project Atmosphere

Copyright 2023 Red Hat, Project Atmosphere

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

# pcs_config_checks

<!-- ANSIBLE DOCSMITH MAIN START -->

* [Role overview](#role-overview)
* [Role variables](#variables)
  * [`pcs_config_checks_custom`](#parameter-pcs_config_checks_custom)
    * [`pcs_config_checks_custom['condition']`](#parameter-pcs_config_checks_custom/condition)
    * [`pcs_config_checks_custom['name']`](#parameter-pcs_config_checks_custom/name)
    * [`pcs_config_checks_custom['documentation']`](#parameter-pcs_config_checks_custom/documentation)
    * [`pcs_config_checks_custom['remediation']`](#parameter-pcs_config_checks_custom/remediation)
    * [`pcs_config_checks_custom['fail_msg']`](#parameter-pcs_config_checks_custom/fail_msg)
    * [`pcs_config_checks_custom['success_msg']`](#parameter-pcs_config_checks_custom/success_msg)
    * [`pcs_config_checks_custom['priority']`](#parameter-pcs_config_checks_custom/priority)
    * [`pcs_config_checks_custom['severity']`](#parameter-pcs_config_checks_custom/severity)
    * [`pcs_config_checks_custom['when']`](#parameter-pcs_config_checks_custom/when)
    * [`pcs_config_checks_custom['quiet']`](#parameter-pcs_config_checks_custom/quiet)
    * [`pcs_config_checks_custom['tags']`](#parameter-pcs_config_checks_custom/tags)
    * [`pcs_config_checks_custom['architectures']`](#parameter-pcs_config_checks_custom/architectures)
    * [`pcs_config_checks_custom['platforms']`](#parameter-pcs_config_checks_custom/platforms)
    * [`pcs_config_checks_custom['cloud_providers']`](#parameter-pcs_config_checks_custom/cloud_providers)
    * [`pcs_config_checks_custom['ignore_errors']`](#parameter-pcs_config_checks_custom/ignore_errors)
  * [`pcs_config_checks_preconfigured`](#parameter-pcs_config_checks_preconfigured)
    * [`pcs_config_checks_preconfigured['condition']`](#parameter-pcs_config_checks_preconfigured/condition)
    * [`pcs_config_checks_preconfigured['name']`](#parameter-pcs_config_checks_preconfigured/name)
    * [`pcs_config_checks_preconfigured['documentation']`](#parameter-pcs_config_checks_preconfigured/documentation)
    * [`pcs_config_checks_preconfigured['remediation']`](#parameter-pcs_config_checks_preconfigured/remediation)
    * [`pcs_config_checks_preconfigured['fail_msg']`](#parameter-pcs_config_checks_preconfigured/fail_msg)
    * [`pcs_config_checks_preconfigured['success_msg']`](#parameter-pcs_config_checks_preconfigured/success_msg)
    * [`pcs_config_checks_preconfigured['priority']`](#parameter-pcs_config_checks_preconfigured/priority)
    * [`pcs_config_checks_preconfigured['severity']`](#parameter-pcs_config_checks_preconfigured/severity)
    * [`pcs_config_checks_preconfigured['when']`](#parameter-pcs_config_checks_preconfigured/when)
    * [`pcs_config_checks_preconfigured['quiet']`](#parameter-pcs_config_checks_preconfigured/quiet)
    * [`pcs_config_checks_preconfigured['tags']`](#parameter-pcs_config_checks_preconfigured/tags)
    * [`pcs_config_checks_preconfigured['architectures']`](#parameter-pcs_config_checks_preconfigured/architectures)
    * [`pcs_config_checks_preconfigured['platforms']`](#parameter-pcs_config_checks_preconfigured/platforms)
    * [`pcs_config_checks_preconfigured['cloud_providers']`](#parameter-pcs_config_checks_preconfigured/cloud_providers)
    * [`pcs_config_checks_preconfigured['ignore_errors']`](#parameter-pcs_config_checks_preconfigured/ignore_errors)
  * [`pcs_config_checks_platform`](#parameter-pcs_config_checks_platform)
    * [`pcs_config_checks_platform['name']`](#parameter-pcs_config_checks_platform/name)
    * [`pcs_config_checks_platform['version']`](#parameter-pcs_config_checks_platform/version)
  * [`pcs_config_checks_architecture`](#parameter-pcs_config_checks_architecture)
  * [`pcs_config_checks_mode`](#parameter-pcs_config_checks_mode)
  * [`pcs_config_checks_verbose`](#parameter-pcs_config_checks_verbose)
  * [`pcs_config_checks_tags_exclude`](#parameter-pcs_config_checks_tags_exclude)
  * [`pcs_config_checks_priority`](#parameter-pcs_config_checks_priority)
  * [`pcs_config_checks_severity`](#parameter-pcs_config_checks_severity)
  * [`pcs_config_checks_custom_only`](#parameter-pcs_config_checks_custom_only)
  * [`pcs_config_checks_loop_display`](#parameter-pcs_config_checks_loop_display)
* [Example Playbooks](#examples)
* [Dependencies](#dependencies)
* [Limitations](#limitations)
* [License](#license)
* [Author Information](#author)

## Role overview<a id="role-overview"></a>

> Run pcs cluster checks

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| <a id="parameter-pcs_config_checks_custom"></a>`pcs_config_checks_custom` | `list of dict` | No | `[]` | List of custom checks |
| <a id="parameter-pcs_config_checks_custom/condition"></a>`pcs_config_checks_custom['condition']` | `list of str` | No | `[]` | Condition to run check<br><br>Conditions should use only variables that are provided in checks execution context.<br><br>ansible_facts and cluster_properties variables are provided in checks execution context.<br><br>ansible_facts are collected for […] |
| <a id="parameter-pcs_config_checks_custom/name"></a>`pcs_config_checks_custom['name']` | `str` | Yes | N/A | Name of the check |
| <a id="parameter-pcs_config_checks_custom/documentation"></a>`pcs_config_checks_custom['documentation']` | `str` | No | N/A | Documentation for the check |
| <a id="parameter-pcs_config_checks_custom/remediation"></a>`pcs_config_checks_custom['remediation']` | `str` | No | N/A | Remediation for the check |
| <a id="parameter-pcs_config_checks_custom/fail_msg"></a>`pcs_config_checks_custom['fail_msg']` | `str` | No | `"FAILED"` | Message to print if check fails |
| <a id="parameter-pcs_config_checks_custom/success_msg"></a>`pcs_config_checks_custom['success_msg']` | `str` | No | `"PASSED"` | Message to print if check succeeds |
| <a id="parameter-pcs_config_checks_custom/priority"></a>`pcs_config_checks_custom['priority']` | `str` | No | `"medium"` | Priority of the check<br>*Choices:* high, medium, low |
| <a id="parameter-pcs_config_checks_custom/severity"></a>`pcs_config_checks_custom['severity']` | `str` | No | `"warning"` | Severity of the check<br>*Choices:* error, warning, info |
| <a id="parameter-pcs_config_checks_custom/when"></a>`pcs_config_checks_custom['when']` | `bool` | No | `true` | If this condition is true, the check will be executed |
| <a id="parameter-pcs_config_checks_custom/quiet"></a>`pcs_config_checks_custom['quiet']` | `bool` | No | `true` | If this is true, the check will be executed quietly |
| <a id="parameter-pcs_config_checks_custom/tags"></a>`pcs_config_checks_custom['tags']` | `list of str` | No | `['cluster', 'pcs']` | Tags for the check |
| <a id="parameter-pcs_config_checks_custom/architectures"></a>`pcs_config_checks_custom['architectures']` | `list of str` | No | `['x86_64', 'ppc64le']` | List of architectures on which check will be executed |
| <a id="parameter-pcs_config_checks_custom/platforms"></a>`pcs_config_checks_custom['platforms']` | `list of dict` | No | `[{'name': 'EL', 'version': '7'}, {'name': 'EL', 'version': '8'}, {'name': 'EL', 'version': '9'}]` | Platform on which check will be executed<br><br>Platform specification as in ansible collections meta/main.yml file |
| <a id="parameter-pcs_config_checks_custom/cloud_providers"></a>`pcs_config_checks_custom['cloud_providers']` | `list of str` | No | `['azure', 'aws', 'gcp']` | List of cloud providers on which check will be executed |
| <a id="parameter-pcs_config_checks_custom/ignore_errors"></a>`pcs_config_checks_custom['ignore_errors']` | `bool` | No | `false` | `True` if errors should be ignored<br><br>`False` if errors should be raised |
| <a id="parameter-pcs_config_checks_preconfigured"></a>`pcs_config_checks_preconfigured` | `list of dict` | No | `[]` | List of preconfigured checks |
| <a id="parameter-pcs_config_checks_preconfigured/condition"></a>`pcs_config_checks_preconfigured['condition']` | `list of str` | No | `[]` | Condition to run check<br><br>Conditions should use only variables that are provided in checks execution context.<br><br>ansible_facts and cluster_properties variables are provided in checks execution context.<br><br>ansible_facts are collected for […] |
| <a id="parameter-pcs_config_checks_preconfigured/name"></a>`pcs_config_checks_preconfigured['name']` | `str` | Yes | N/A | Name of the check |
| <a id="parameter-pcs_config_checks_preconfigured/documentation"></a>`pcs_config_checks_preconfigured['documentation']` | `str` | No | N/A | Documentation for the check |
| <a id="parameter-pcs_config_checks_preconfigured/remediation"></a>`pcs_config_checks_preconfigured['remediation']` | `str` | No | N/A | Remediation for the check |
| <a id="parameter-pcs_config_checks_preconfigured/fail_msg"></a>`pcs_config_checks_preconfigured['fail_msg']` | `str` | No | `"FAILED"` | Message to print if check fails |
| <a id="parameter-pcs_config_checks_preconfigured/success_msg"></a>`pcs_config_checks_preconfigured['success_msg']` | `str` | No | `"PASSED"` | Message to print if check succeeds |
| <a id="parameter-pcs_config_checks_preconfigured/priority"></a>`pcs_config_checks_preconfigured['priority']` | `str` | No | `"medium"` | Priority of the check<br>*Choices:* high, medium, low |
| <a id="parameter-pcs_config_checks_preconfigured/severity"></a>`pcs_config_checks_preconfigured['severity']` | `str` | No | `"warning"` | Severity of the check<br>*Choices:* error, warning, info |
| <a id="parameter-pcs_config_checks_preconfigured/when"></a>`pcs_config_checks_preconfigured['when']` | `bool` | No | `true` | If this condition is true, the check will be executed |
| <a id="parameter-pcs_config_checks_preconfigured/quiet"></a>`pcs_config_checks_preconfigured['quiet']` | `bool` | No | `true` | If this is true, the check will be executed quietly |
| <a id="parameter-pcs_config_checks_preconfigured/tags"></a>`pcs_config_checks_preconfigured['tags']` | `list of str` | No | `['cluster', 'pcs']` | Tags for the check |
| <a id="parameter-pcs_config_checks_preconfigured/architectures"></a>`pcs_config_checks_preconfigured['architectures']` | `list of str` | No | `['x86_64', 'ppc64le']` | List of architectures on which check will be executed |
| <a id="parameter-pcs_config_checks_preconfigured/platforms"></a>`pcs_config_checks_preconfigured['platforms']` | `list of dict` | No | `[{'name': 'EL', 'version': '7'}, {'name': 'EL', 'version': '8'}, {'name': 'EL', 'version': '9'}]` | Platform on which check will be executed<br><br>Platform specification as in ansible collections meta/main.yml file |
| <a id="parameter-pcs_config_checks_preconfigured/cloud_providers"></a>`pcs_config_checks_preconfigured['cloud_providers']` | `list of str` | No | `['azure', 'aws', 'gcp']` | List of cloud providers on which check will be executed |
| <a id="parameter-pcs_config_checks_preconfigured/ignore_errors"></a>`pcs_config_checks_preconfigured['ignore_errors']` | `bool` | No | `false` | `True` if errors should be ignored<br><br>`False` if errors should be raised |
| <a id="parameter-pcs_config_checks_platform"></a>`pcs_config_checks_platform` | `dict` | No | N/A | Overwrite platform collected by ansible_facts |
| <a id="parameter-pcs_config_checks_platform/name"></a>`pcs_config_checks_platform['name']` | `str` | Yes | N/A | Name of the platform<br>*Choices:* EL |
| <a id="parameter-pcs_config_checks_platform/version"></a>`pcs_config_checks_platform['version']` | `str` | Yes | N/A | Version of the platform<br>*Choices:* 7, 8, 9 |
| <a id="parameter-pcs_config_checks_architecture"></a>`pcs_config_checks_architecture` | `str` | No | N/A | Overwrite architecture collected by ansible_facts<br>*Choices:* x86_64, ppc64le |
| <a id="parameter-pcs_config_checks_mode"></a>`pcs_config_checks_mode` | `str` | No | `"assert"` | Role execution mode<br><br>Debug provides more information about the checks and execution context<br><br>Assert is the default mode<br>*Choices:* assert, debug |
| <a id="parameter-pcs_config_checks_verbose"></a>`pcs_config_checks_verbose` | `bool` | No | `false` | If this `True`, more information will be provided in output.<br><br>Affects both debug and assert modes<br><br>If set to `True` quiet parameter for all checks will be ignored, effectively making check.quiet false for all checks.<br><br>If set to […] |
| <a id="parameter-pcs_config_checks_tags_exclude"></a>`pcs_config_checks_tags_exclude` | `list of str` | No | `['skip']` | List of tags to exclude<br><br>If check has tag from this list, it will not run<br><br>Checks with tag 'skip' will never run<br><br>Only first **five** elements from this list are used, all other are ignored |
| <a id="parameter-pcs_config_checks_priority"></a>`pcs_config_checks_priority` | `list of str` | No | `['low', 'medium', 'high']` | List of check priorities that will be executed<br><br>Checks with priority not in this list will be skipped |
| <a id="parameter-pcs_config_checks_severity"></a>`pcs_config_checks_severity` | `list of str` | No | `['error', 'warning', 'info']` | List of check severities that will be executed<br><br>Checks with severity not in this list will be skipped |
| <a id="parameter-pcs_config_checks_custom_only"></a>`pcs_config_checks_custom_only` | `bool` | No | `false` | If this is `True`, only custom checks *pcs_config_checks_custom* will be executed<br><br>If this is `False`, preconfigured and custom checks will be executed |
| <a id="parameter-pcs_config_checks_loop_display"></a>`pcs_config_checks_loop_display` | `str` | No | `"name"` | Indicate what will be displayed in loop when executing checks<br>*Choices:* name, condition, documentation, remediation, fail_msg, success_msg, priority, severity, when, quiet, tags, architectures, platforms, cloud_providers |

## Example Playbooks<a id="examples"></a>

```ansible
- hosts: all
  tasks:
    - name: Run pcs cluster checks
      ansible.builtin.include_role:
        name: sap.sap_operations.pcs_config_checks
```


## Dependencies<a id="dependencies"></a>

Role has no dependencies to other roles.

## Limitations<a id="limitations"></a>

Check parameter cloud_providers does not do anything at the moment.

## License<a id="license"></a>

GPL-3.0-only

## Author Information<a id="author"></a>

Kirill Satarin (@kksat)


<!-- ANSIBLE DOCSMITH MAIN END -->
