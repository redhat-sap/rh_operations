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


from ansible_collections.sap.sap_operations.plugins.module_utils.valid_sid import (
    valid_sid,
)


DOCUMENTATION = """
name: valid_sid
author: Kirill Satarin (@kksat)
version_added: 1.0.4
short_description: Verify that SAP system ID (SID) is valid.
description:
    -  |
      Check if SAP system ID (sid) is valid as per SAP notes
      1979280 - Reserved SAP System Identifiers (SAPSID) with Software Provisioning Manager
      2952755 - What to enter for System ID while creating a system and/or license keys?
    - Expects that sid is in uppercase, all lowercase considered not valid.
options:
    value:
        description: |
          System ID (SID) to check if valid.
        type: str
        required: True
"""

EXAMPLES = r"""
- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: ( 'ABC'| sap.sap_operations.valid_sid )

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: not ( 'AbC'| sap.sap_operations.valid_sid )

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: not ( 'ADD'| sap.sap_operations.valid_sid )

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: not ( '1BC'| sap.sap_operations.valid_sid )

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: not ( 'A?C'| sap.sap_operations.valid_sid )
"""

RETURN = """
  data:
    type: bool
    description:
      - True if valid SID is provided
      - False if non valid SID is provided
"""


# ---- Ansible filters ----
class FilterModule(object):
    def filters(self):
        return {"valid_sid": valid_sid}
