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
from ansible_collections.sap.sap_operations.plugins.module_utils.compat import (
    dict_union,
)

__metaclass__ = type


DOCUMENTATION = """
name: combine_default
author: Kirill Satarin (@kksat)
version_added: 1.11.0
short_description: Combine two dictionaries, second dictionary will be used as default.
description:
  - Combine two dictionaries, second dictionary will be used as default.
  - If key is present in both dictionaries, value from first dictionary (not value from default) will be used.
  - If value is not dictionary, it will be returned as is.
  - If value is None, default will be returned.
  - This is expected to work only with one level of nesting for dictionaries.

options:
  value:
    description: Dictionary to combine with default.
    type: dict
    required: True
  default:
    description: Dictionary to use as default.
    type: dict
    required: False
"""

EXAMPLES = r"""
- name: Test filter `combine_default`, this assertion is True
  ansible.builtin.assert:
    that:
      - ( 'ABC' | sap.sap_operations.combine_default('DEF') ) == 'ABC'
      - ( 123 | sap.sap_operations.combine_default('DEF') ) == 123
      - ( [1, 2, 3] | sap.sap_operations.combine_default('DEF') ) == [1, 2, 3]
      - ( {"key":"value"} | sap.sap_operations.combine_default('DEF') ) == {"key":"value"}
      - True | sap.sap_operations.combine_default('DEF') == True
      - False | sap.sap_operations.combine_default('DEF') == False
      - 0 | sap.sap_operations.combine_default('DEF') == 0
      - 1 | sap.sap_operations.combine_default('DEF') == 1
      - None | sap.sap_operations.combine_default('DEF') == 'DEF'
      - value | sap.sap_operations.combine_default(default) == result1
      - default | sap.sap_operations.combine_default(value) == result2
  vars:
    value:
      key1: value1
      key2: value2
    default:
      key2: new_value2
      key3: value3
    result1:
      key1: value1
      key2: value2
      key3: value3
    result2:
      key1: value1
      key2: new_value2
      key3: value3
"""

RETURN = """
  data:
    type: dict
    description:
      - Combined dictionary.
      - If key is present in both dictionaries, value from first dictionary (not value from default) will be used.
      - If value is not dictionary, it will be returned as is.
      - If value is None, default will be returned.
"""


def combine_default(value, default=None):
    if isinstance(value, dict) and isinstance(default, dict):
        return dict_union(default, value)
    if value is None:
        return default
    return value


# ---- Ansible filters ----
class FilterModule(object):
    def filters(self):
        return {"combine_default": combine_default}
