# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2023 Red Hat, Project Atmosphere
#
# Copyright 2023 Red Hat, Project Atmosphere
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


DOCUMENTATION = """

name: license_content

author:
  - Kirill Satarin (@kksat)

extends_documentation_fragment:
  - sap.sap_operations.experimental

version_added: 1.8.0-galaxy

short_description: Get sap license attributes from sap license file

description:
  - Get sap license attributes from sap license file
  - This filter will parse sap license file and return dictionary with license attributes
  - If no line '----- Begin SAP License -----' found, filter will return empty list

options:
  value:
    description: Content of the sap license file
    type: dict
    required: true
"""  # noqa: E501

EXAMPLES = r"""

- name: Get sap license attributes from sap license file
  ansible.builtin.debug:
    msg: "{{ lookup('file', '/usr/sap/AAA/SYS/saplicense') | license_content }}"
"""  # noqa: E501
# spell-checker: disable
RETURN = """
data:
  type: list
  elements: dict
  returned: Success
  description:
    - List of dictionaries with sap license attributes
  example:
    - "begin_of_validity": "20200107"
      "end_of_validity": "99991231"
      "hardware_key": "D1111111111"
      "installation_number": "0000000000"
      "license_key": "MIIBOgYJ"
      "software_product": "NetWeaver_SYB"
      "software_product_limit": "2000000000"
      "system_id": "AAA"
      "system_number": "000000000000000000"
    - "begin_of_validity": "20200107"
      "end_of_validity": "20200408"
      "hardware_key": "D1111111111"
      "installation_number": "0000000000"
      "license_key": "MIIBOwY..."
      "software_product": "Maintenance_SYB"
      "software_product_limit": "2000000000"
      "system_id": "AAA"
      "system_number": "000000000000000000"
"""
# spell-checker:enable

from ansible_collections.sap.sap_operations.plugins.module_utils.saplikey import (
    get_license_keys_from_stdout,
)  # noqa: E501


def license_content(text):
    return get_license_keys_from_stdout(text)


class FilterModule(object):
    def filters(self):
        return {"license_content": license_content}
