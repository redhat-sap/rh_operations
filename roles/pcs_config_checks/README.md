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

Run cluster configuration checks

## Requirements

Root access (or privileged access to run pcs commands) is required for the user that will execute this role.

Custom configuration checks can be executed by this role, see role parameters.

Dynamic configuration checks can be executed by this role, see role parameters.

Role collects necessary facts, no need to gather facts for the playbook.

Role can be executed in two modes: `assert` and `debug`. See variable **pcs_config_checks_mode**.
Debug mode is much more verbose and recommended when one wants to debug what is happening, why checks are not working as expected.

## Limitations

Check parameter **cloud_providers* does not do anything at the moment.

<!-- BEGIN: Role Input Parameters -->

## Role Variables

Required parameters:

### pcs_config_checks_architecture

- _Type:_ `str`
- _Required:_ `False`

Overwrite architecture collected by ansible_facts
### pcs_config_checks_custom

- _Type:_ `list`
- _Default:_ `[]`
- _Required:_ `False`

List of custom checks

      - **architectures**<br>
        _Default:_ `['x86_64', 'ppc64le']`<br>
            List of architectures on which check will be executed

      - **cloud_providers**<br>
        _Default:_ `['azure', 'aws', 'gcp']`<br>
            List of cloud providers on which check will be executed

      - **condition**<br>
        _Default:_ `[]`<br>
            Condition to run check

            Conditions should use only variables that are provided in checks execution context.

            ansible_facts and cluster_properties variables are provided in checks execution context.

            ansible_facts are collected for the host where role is executed, so if you are analyzing local xml export of the cluster CIB, ansible_facts will be collected for the host where you are running the role (for instance localhost).

            More variables will be provided in checks execution context.

            Checks are automatically filtered based on the following criteria - 'architecture' variable - either provided as role parameter, or collected from ansible_facts - 'platform' and 'version' variables - either provided as role parameters, or collected from ansible_facts - 'cloud_provider' - not yet supported - Checks filtered out this way will not be even in the main check loop.

            Another way to filter checks is to use tags. See I(pcs_config_checks_tags_exclude) parameter.

            If there is a more complex condition when to execute check and when not, this condition should be provided individually for each check in parameter I(when).

            For instance, this is how to ignore checks on an odd numbered day.

                  name: This check will be executed only on even numbered days and will fail.
                  condition: false
                  when: {% raw %} "{{ ansible_facts['date_time']['day'] | int % 2 == 0 }}" {% endraw %}
                  Check will be marked as skipped and not executed if 'when' condition is C(false).
                  But this check will appear in list of checks.

      - **documentation**<br>
            Documentation for the check

      - **fail_msg**<br>
        _Default:_ `FAILED`<br>
            Message to print if check fails

      - **ignore_errors**<br>
        _Default:_ `False`<br>
            C(True) if errors should be ignored<br>C(False) if errors should be raised

      - **name**<br>
            Name of the check

      - **platforms**<br>
        _Default:_ `[{'name': 'EL', 'version': '7'}, {'name': 'EL', 'version': '8'}, {'name': 'EL', 'version': '9'}]`<br>
            Platform on which check will be executed<br>Platform specification as in ansible collections meta/main.yml file

      - **priority**<br>
        _Default:_ `medium`<br>
            Priority of the check

      - **quiet**<br>
        _Default:_ `True`<br>
            If this is true, the check will be executed quietly

      - **remediation**<br>
            Remediation for the check

      - **severity**<br>
        _Default:_ `warning`<br>
            Severity of the check

      - **success_msg**<br>
        _Default:_ `PASSED`<br>
            Message to print if check succeeds

      - **tags**<br>
        _Default:_ `['cluster', 'pcs']`<br>
            Tags for the check

      - **when**<br>
        _Default:_ `True`<br>
            If this condition is true, the check will be executed

### pcs_config_checks_custom_only

- _Type:_ `bool`
- _Default:_ `False`
- _Required:_ `False`

If this is C(True), only custom checks I(pcs_config_checks_custom) will be executed. If this is C(False), preconfigured and custom checks will be executed

### pcs_config_checks_loop_display

- _Type:_ `str`
- _Default:_ `name`
- _Required:_ `False`

Indicate what will be displayed in loop when executing checks

### pcs_config_checks_mode

- _Type:_ `str`
- _Default:_ `assert`
- _Required:_ `False`

Role execution mode

Debug provides more information about the checks and execution context

Assert is the default mode

### pcs_config_checks_platform

- _Type:_ `dict`
- _Required:_ `False`

Overwrite platform collected by ansible_facts

  - **name**<br>
            Name of the platform

  - **version**<br>
      Version of the platform

### pcs_config_checks_preconfigured

- _Type:_ `list`
- _Default:_ `[]`
- _Required:_ `False`

List of preconfigured checks

      - **architectures**<br>
        _Default:_ `['x86_64', 'ppc64le']`<br>
            List of architectures on which check will be executed

      - **cloud_providers**<br>
        _Default:_ `['azure', 'aws', 'gcp']`<br>
            List of cloud providers on which check will be executed

      - **condition**<br>
        _Default:_ `[]`<br>

            Condition to run check<br>Conditions should use only variables that are provided in checks execution context.

            ansible_facts and cluster_properties variables are provided in checks execution context.

            ansible_facts are collected for the host where role is executed, so if you are analyzing local xml export of the cluster CIB, ansible_facts will be collected for the host where you are running the role (for instance localhost).

            More variables will be provided in checks execution context.

            Checks are automatically filtered based on the following criteria - 'architecture' variable - either provided as role parameter, or collected from ansible_facts - 'platform' and 'version' variables - either provided as role parameters, or collected from ansible_facts - 'cloud_provider' - not yet supported - Checks filtered out this way will not be even in the main check loop.

            Another way to filter checks is to use tags. See I(pcs_config_checks_tags_exclude) parameter.

            If there is a more complex condition when to execute check and when not, this condition should be provided individually for each check in parameter I(when).

            For instance, this is how to ignore checks on an odd numbered day.
                  name: This check will be executed only on even numbered days and will fail.
                  condition: false
                  when: {% raw %} "{{ ansible_facts['date_time']['day'] | int % 2 == 0 }}" {% endraw %}
            Check will be marked as skipped and not executed if 'when' condition is C(false).
            But this check will appear in list of checks.

      - **documentation**<br>
            Documentation for the check

      - **fail_msg**<br>
        _Default:_ `FAILED`<br>
            Message to print if check fails

      - **ignore_errors**<br>
        _Default:_ `False`<br>
            C(True) if errors should be ignored<br>C(False) if errors should be raised

      - **name**<br>
            Name of the check

      - **platforms**<br>
        _Default:_ `[{'name': 'EL', 'version': '7'}, {'name': 'EL', 'version': '8'}, {'name': 'EL', 'version': '9'}]`<br>
            Platform on which check will be executed<br>Platform specification as in ansible collections meta/main.yml file

      - **priority**<br>
        _Default:_ `medium`<br>
            Priority of the check

      - **quiet**<br>
        _Default:_ `True`<br>
            If this is true, the check will be executed quietly

      - **remediation**<br>
            Remediation for the check

      - **severity**<br>
        _Default:_ `warning`<br>
            Severity of the check

      - **success_msg**<br>
        _Default:_ `PASSED`<br>
            Message to print if check succeeds

      - **tags**<br>
        _Default:_ `['cluster', 'pcs']`<br>
            Tags for the check

      - **when**<br>
        _Default:_ `True`<br>
            If this condition is true, the check will be executed

### pcs_config_checks_tags_exclude

- _Type:_ `list`
- _Default:_ `['skip']`
- _Required:_ `False`

List of tags to excludeIf check has tag from this list, it will not runChecks with tag 'skip' will never runOnly first **five** elements from this list are used, all other are ignored

### pcs_config_checks_verbose

- _Type:_ `bool`
- _Default:_ `False`
- _Required:_ `False`

If this C(True), more information will be provided in output.Affects both debug and assert modesIf set to C(True) quiet parameter for all checks will be ignored,
effectively making check.quiet false for all checks.
If set to C(False) check.quiet parameter will be used.

<!-- END: Role Input Parameters -->

## Example Playbooks

      ```ansible

      - hosts: all
      gather_facts: false
      become: true
      become_user: root
      roles:
      - role: sap.sap_operations.pcs_config_checks

      ```

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
