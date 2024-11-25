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


DOCUMENTATION = """
name: me_valid_alias
author: Kirill Satarin (@kksat)
extends_documentation_fragment: sap.sap_operations.community
version_added: 1.10.0
short_description: Return true if string provided is valid software alias.
description:
  - Return true if string provided is valid software alias.
options:
  value:
    description: Value to check.
    required: true
    type: str
"""

EXAMPLES = r"""

- name: Test 'me_valid_alias' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ 'saphostagent' is sap.sap_operations.me_valid_alias }}"

- name: Test 'me_valid_alias' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ 'hana-client' is sap.sap_operations.me_valid_alias }}"

- name: Test 'me_valid_alias' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ 'does_not_exist' is not sap.sap_operations.me_valid_alias }}"
"""

RETURN = """
_value:
  type: boolean
  description: True if value provided is valid alias.

"""


from ansible_collections.sap.sap_operations.plugins.module_utils.me_helpers import (
    enr_from_alias,
)  # noqa: E501


def me_valid_alias(value):
    return value in enr_from_alias.keys()


class TestModule(object):
    def tests(self):
        return {
            "me_valid_alias": me_valid_alias,
        }
