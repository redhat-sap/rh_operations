# -*- coding: utf-8 -*-

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
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.sap.sap_operations.plugins.module_utils.valid_sid import (
    valid_sid,
)


DOCUMENTATION = """
    name: valid_sid
    author: <https://github.com/kksat>
    version_added: 1.1.0
    short_description: Verify that SAP system ID (SID) is valid.
    description:
        -  |
          Check if SAP system ID (sid) is valid as per SAP notes
          1979280 - Reserved SAP System Identifiers (SAPSID) with Software Provisioning Manager
          2952755 - What to enter for System ID while creating a system and/or license keys?
        - Expects that sid is in uppercase, all lowercase considered not valid.
    options:
        _input:
            description: |
              System ID ( SID ) to check if valid.
            type: str
            required: True
"""

EXAMPLES = r"""
- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: ('ABC' is sap.sap_operations.valid_sid)

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: ('AbC' is not sap.sap_operations.valid_sid)

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: ('ADD' is not sap.sap_operations.valid_sid)

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: ('1BC' is not sap.sap_operations.valid_sid)

- name: Test filter `valid_sid`, this assertion is True
  ansible.builtin.assert:
    that: ('A?C' is not sap.sap_operations.valid_sid)
"""

RETURN = """
  _value:
    description: Whether the tested string is valid SAP system ID (SID) or not
    type: boolean
"""


class TestModule(object):
    def tests(self):
        return {
            "valid_sid": valid_sid,
        }
