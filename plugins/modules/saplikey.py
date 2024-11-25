#!/usr/bin/python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2023 Kirill Satarin (@kksat)
#
# Copyright 2023 Kirill Satarin (@kksat)
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = r"""

module: saplikey

extends_documentation_fragment:
  - sap.sap_operations.experimental
  - sap.sap_operations.saplikey_common

author:
  - Kirill Satarin (@kksat)

short_description: Manage sap license keys for SAP application instance with saplikey program.

description:
  - Manage sap license keys for SAP application instance with saplikey program.
  - Either O(filename) or O(license_content) should be provided. Filename is a path on the target host where license file is located.
  - If O(license_content) provided, it will be copied to temporary local file and then used for installation. File deleted afterwards.
  - If state is C(absent), O(system), O(hardware_key) and O(product) parameters are required.
  - |
    In order to use asterisk as a wildcard in O(system), O(hardware_key) and O(product) parameters, set O(allow_asterisk) to true.
    This is to prevent accidental deletion of licenses.

version_added: 1.8.0-galaxy

options:

  filename:
    description:
      - Path to the license file to install or remove.
    type: path
    required: false

  license_content:
    description:
      - The content of the license file to install or remove.
      - This parameter is not logged.
    type: str
    required: false

  state:
    description:
      - Whether the license should be present or absent.
    type: str
    required: false
    default: present
    choices:
      - present
      - absent

  system:
    description:
      - The system ID of the SAP system.
      - Or a wildcard asterisk C(*).
    type: str
    required: false
    aliases:
      - sid
      - system_id

  hardware_key:
    description:
      - The hardware key of the SAP system.
    type: str
    required: false

  product:
    description:
      - The product ID of the SAP system.
    type: str
    required: false

  allow_asterisk:
    description:
      - Whether to allow the use of asterisks as wildcards in the system, hardware_key, and product parameters.
      - This is to prevent accidental deletion of licenses.
    type: bool
    required: false
    default: false

seealso:
  - name: SAP Note 181543 - License key for high availability environment
    description: SAP Note 181543 - License key for high availability environment
    link: https://me.sap.com/notes/181543

  - name: SAP Note 2755234 - Couldn't load SAPSECULIB, first temporary license cannot be created by installer
    description: SAP Note 2755234 - Couldn't load SAPSECULIB, first temporary license cannot be created by installer
    link: https://me.sap.com/notes/2755234

"""  # noqa: E501

EXAMPLES = r"""

- name: Ensure license keys absent (with asterisks)
  sap.sap_operations.saplikey:
    state: absent
    system: '*'
    hardware_key: '*'
    product: NetWeaver_SYB
    allow_asterisk: true
  become: true
  become_user: <sid>adm
  become_flags: '-i'

- name: Ensure license key present
  sap.sap_operations.saplikey:
    license_content: |
      ----- Begin SAP License -----
  become: true
  become_user: <sid>adm
  become_flags: '-i'

- name: Ensure license key absent that does not exists
  sap.sap_operations.saplikey:
    state: absent
    system: AAA
    hardware_key: doesnotexists
    product: doesnotexists
  become: true
  become_user: <sid>adm
  become_flags: '-i'
"""

RETURN = r"""

rc:
  description: Return code of the saplikey program execution.
  returned: always
  type: int
  sample: 0

stdout:
  description: The standard output of the saplikey program execution.
  returned: always
  type: str
  sample: |
    SAP License Key Administration  -  Copyright (C) 2003 - 2012 SAP AG

    1 SAP license key(s) successfully installed.

stderr:
  description: The standard error of the saplikey program execution.
  returned: always
  type: str
  sample: ""

license_keys:
  description:
    - The list of installed license keys.
    - Please pay attention that all dates are in format YYYYMMDD.
    - Please pay attention that all numeric values are returned as strings.
  returned: always
  type: list
  elements: dict
  sample:
    - begin_of_validity: '20230111'
      end_of_validity: '20240712'
      hardware_key: D1111111111
      installation_number: '0000000000'
      last_successful_check: '20231016'
      software_product: NetWeaver_SYB
      software_product_limit: '2000000000'
      system_id: AAA
      system_number: '000000000000000000'
      type_of_license_key: permanent
      validity: valid
    - begin_of_validity: '20230111'
      end_of_validity: '20240712'
      hardware_key: D1111111111
      installation_number: '0000000000'
      last_successful_check: '00000000'
      software_product: Maintenance_SYB
      software_product_limit: '2000000000'
      system_id: AAA
      system_number: '000000000000000000'
      type_of_license_key: permanent
      validity: valid

"""


from ansible_collections.sap.sap_operations.plugins.module_utils.saplikey import (  # noqa: E501
    AnsibleModule_saplikey,
    get_license_keys_from_stdout,
)
import tempfile


def main():
    argument_spec = dict(
        filename=dict(type="path", required=False),
        license_content=dict(type="str", required=False, no_log=True),
        state=dict(
            type="str",
            required=False,
            default="present",
            choices=["present", "absent"],
        ),
        system=dict(type="str", required=False, aliases=["sid", "system_id"]),
        hardware_key=dict(type="str", required=False, no_log=False),
        product=dict(type="str", required=False),
        allow_asterisk=dict(type="bool", required=False, default=False),
    )
    mutually_exclusive = (["filename", "license_content"],)
    required_together = (["system", "hardware_key", "product"],)
    required_if = (
        ["state", "absent", ["system", "hardware_key", "product"]],
        ["state", "present", ["filename", "license_content"], True],
    )
    required_by = {
        "system": ("hardware_key", "product"),
        "hardware_key": ("system", "product"),
        "product": ("system", "hardware_key"),
    }

    module = AnsibleModule_saplikey(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_together=required_together,
        required_if=required_if,
        required_by=required_by,
        supports_check_mode=False,
    )
    _ignore, stdout_show, _ignore = module.run_saplikey_command(
        ["-show"], check_rc=True
    )
    license_keys_before = get_license_keys_from_stdout(stdout_show)

    if module.params["state"] == "absent":
        system = module.params.get("system")
        hardware_key = module.params.get("hardware_key")
        product = module.params.get("product")
        allow_asterisk = module.params.get("allow_asterisk")
        if not allow_asterisk:
            if hardware_key == "*" or product == "*" or system == "*":
                module.fail_json(
                    msg="Make sure you set parameter allow_asterisk\
                    to true if you want to use asterisk as a wildcard"
                )

        rc, stdout, stderr = module.run_saplikey_command(
            [
                "-delete",
                "{0}".format(system),
                "{0}".format(hardware_key),
                "{0}".format(product),
            ]
        )

    if module.params["state"] == "present":
        filename = module.params.get("filename")
        if filename:
            rc, stdout, stderr = module.run_saplikey_command(
                ["-install", "{0}".format(filename)]
            )
        else:
            license_content = module.params.get("license_content")
        with tempfile.NamedTemporaryFile(mode="w", delete=True) as temp_file:
            temp_file.write(license_content)
            temp_file.flush()
            rc, stdout, stderr = module.run_saplikey_command(
                ["-install", temp_file.name]
            )

    _ignore, stdout_show, _ignore = module.run_saplikey_command(
        ["-show"], check_rc=True
    )
    license_keys_after = get_license_keys_from_stdout(stdout_show)
    changed = len(license_keys_after) != len(license_keys_before)

    module.exit_json(
        changed=changed,
        rc=rc,
        stdout=stdout,
        stderr=stderr,
        license_keys=license_keys_after,
    )


if __name__ == "__main__":
    main()
