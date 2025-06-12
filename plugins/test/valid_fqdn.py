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
name: valid_fqdn
author: Kirill Satarin (@kksat)
version_added: 2.14.0
extends_documentation_fragment:
    - sap.sap_operations.community
    - sap.sap_operations.fqdn
"""

EXAMPLES = """
---
- name: This is valid fqdn
  ansible.builtin.assert:
    that: ('hostname13.domain.com' is sap.sap_operations.valid_fqdn)

- name: Valid hostname is also valid fqdn
  ansible.builtin.assert:
    that: ('hostname13' is sap.sap_operations.valid_fqdn)

- name: Valid hostname is also valid fqdn, but it can be up to 63 characters
  ansible.builtin.assert:
    that: ('hostname1234567890123456789012345678901234567890' is sap.sap_operations.valid_fqdn)

- name: Fqdn cannot contain two dots in a sequence
  ansible.builtin.assert:
    that: ('hostname13..domain.com' is not sap.sap_operations.valid_fqdn)

- name: This is not valid fqdn
  ansible.builtin.assert:
    that: ('hostname13-.domain.com' is not sap.sap_operations.valid_fqdn)

- name: Fqdn cannot end in dot
  ansible.builtin.assert:
    that: ('hostname13.domain.com.' is not sap.sap_operations.valid_fqdn)
"""

RETURN = """
---
_value:
  type: boolean
  description: True if value provided is valid sap fqdn

"""


from ansible_collections.sap.sap_operations.plugins.module_utils.hostname import (
    valid_fqdn,
)  # noqa: E501


class TestModule(object):
    def tests(self):
        return {
            "valid_fqdn": valid_fqdn,
        }
