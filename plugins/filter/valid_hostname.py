# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2025 Kirill Satarin (@kksat)
#
# Copyright 2025 Kirill Satarin (@kksat)
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
---
name: valid_hostname
author: Kirill Satarin (@kksat)
version_added: 2.14.0
extends_documentation_fragment:
    - sap.sap_operations.community
    - sap.sap_operations.hostname
"""

EXAMPLES = """
---
- name: Hostname with alphanumeric characters is valid
  ansible.builtin.assert:
    that: ('hostname13' | sap.sap_operations.valid_hostname)

- name: Very long hostname is not valid
  ansible.builtin.assert:
    that: not ('this-is-longer-than13' | sap.sap_operations.valid_hostname)

- name: Very long hostname is not valid unless you say so
  ansible.builtin.assert:
    that: ('this-is-longer-than13' | sap.sap_operations.valid_hostname(le=140))

- name: Hostname with capital letters is not considered valid by default
  ansible.builtin.assert:
    that: not ('Hostname' | sap.sap_operations.valid_hostname)

- name: Hostname with capital letters can also be valid
  ansible.builtin.assert:
    that: ('Hostname' | sap.sap_operations.valid_hostname(all_lowercase=False))

- name: Hostname cannot start with a number
  ansible.builtin.assert:
    that: not ('1hostname' | sap.sap_operations.valid_hostname)

- name: Hostname cannot end with '-'
  ansible.builtin.assert:
    that: not ('hostname-' | sap.sap_operations.valid_hostname)

- name: Hostname should contain only alphanumeric characters and '-'
  ansible.builtin.assert:
    that: not ('host?name' | sap.sap_operations.valid_hostname)

- name: Hostname should contain only alphanumeric characters and '-'
  ansible.builtin.assert:
    that: not ('host.name' | sap.sap_operations.valid_hostname)

- name: Empty string is not valid hostname
  ansible.builtin.assert:
    that: not ('' | sap.sap_operations.valid_hostname)
"""

RETURN = """
---
_value:
  type: boolean
  description: True if value provided is valid sap hostname

"""


from ansible_collections.sap.sap_operations.plugins.module_utils.hostname import (
    valid_hostname,
)  # noqa: E501


class FilterModule(object):
    def filters(self):
        return {
            "valid_hostname": valid_hostname,
        }
