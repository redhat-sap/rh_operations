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
name: any
author: Kirill Satarin (@kksat)
extends_documentation_fragment: sap.sap_operations.community
version_added: 1.7.0-galaxy
short_description: Return true if any element in the iterable is truthy.
description:
  - Return true if any element in the iterable is truthy.
  - If not iterable, return the truthyness of value provided.
  - Returns False if the iterable is empty (empty list, or empty string).
  - Behaves like the Python builtin any function (for Iterable)
  - If not Iterable provided, behaves like the Python builtin bool function (for value)
options:
  value:
    description: Iterable to check, if not iterable, return the truthyness of value provided.
    required: true
"""  # noqa: E501

EXAMPLES = r"""
- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ [true, true] is sap.sap_operations.any }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ ['true', 'false'] is sap.sap_operations.any }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ [1, 1] is sap.sap_operations.any }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ ([1, 0] is sap.sap_operations.any) }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ ['1', '0'] is sap.sap_operations.any }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ 1 is sap.sap_operations.any }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ not ( 0 is sap.sap_operations.any ) }}"

- name: wer  Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ not ( '' is sap.sap_operations.any ) }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ ' ' is sap.sap_operations.any }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ {1: 2} is sap.sap_operations.any }}"

- name: Test 'any' test plugin, this assertion is True
  ansible.builtin.assert:
    that: "{{ not ( None is sap.sap_operations.any ) }}"
"""  # noqa: E501

RETURN = """
_value:
  type: boolean
  description: True if any element in the iterable is truthy or value provided is truthy.
  example: true
"""  # noqa: E501


from ansible_collections.sap.sap_operations.plugins.filter.any import any_filter  # noqa: E501


class TestModule(object):
    def tests(self):
        return {
            "any": any_filter,
        }
