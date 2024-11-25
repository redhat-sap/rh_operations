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

from typing import Iterable


DOCUMENTATION = """
name: all
author: Kirill Satarin (@kksat)
extends_documentation_fragment: sap.sap_operations.community
version_added: 1.7.0-galaxy
short_description: Return true if all elements in the iterable are truthy.
description:
  - Return true if all elements in the iterable are truthy.
  - If not iterable, return the truthyness of value provided.
  - Returns True if the iterable is empty (empty list, or empty string).
  - Behaves like the Python builtin all function (for Iterable)
  - If not Iterable provided, behaves like the Python builtin bool function (for value)
options:
  value:
    description: Iterable to check, if not iterable, return the truthyness of value provided.
    required: true
"""  # noqa: E501

EXAMPLES = r"""
- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ [true, true] | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ ['true', 'false'] | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ [1, 1] | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ not ([1, 0] | sap.sap_operations.all) }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ ['1', '0'] | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ 1 | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ not ( 0 | sap.sap_operations.all ) }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ '' | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ ' ' | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ {1: 2} | sap.sap_operations.all }}"

- name: Test 'all' filter, this assertion is True
  ansible.builtin.assert:
    that: "{{ not ( None | sap.sap_operations.all ) }}"
"""  # noqa: E501

RETURN = """
data:
  type: boolean
  description: True if all elements in the iterable are truthy or value provided is truthy.
  example: true
"""  # noqa: E501


def all_filter(value):
    if isinstance(value, Iterable):
        return all(value)
    else:
        return bool(value)


class FilterModule(object):
    def filters(self):
        return {"all": all_filter}
