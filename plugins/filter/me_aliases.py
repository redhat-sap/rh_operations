# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2024 Kirill Satarin (@kksat)
#
# Copyright 2024 Kirill Satarin (@kksat)
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
from ansible_collections.sap.sap_operations.plugins.module_utils.me_helpers import (
    enr_from_alias,
)  # noqa: E501


DOCUMENTATION = """
---
name: me_aliases
author: Kirill Satarin (@kksat)
extends_documentation_fragment: sap.sap_operations.community
version_added: 1.33.0
short_description: Return all the aliases that are available
description:
  - Return all the aliases that are available

options:
  dummy:
    description: Dummy value to make the module work.
    type: str
    required: false
"""

EXAMPLES = r"""
---
- name: Test 'me_aliases' filter, this assertion is True
  ansible.builtin.assert:
  that:
    - ( 'dummy' | sap.sap_operations.me_aliases ) is defined
    - ( 'dummy' | sap.sap_operations.me_aliases ) is iterable
    - ( 'dummy' | sap.sap_operations.me_aliases ) is contains('sapcar')
    - ( 'dummy' | sap.sap_operations.me_aliases ) is contains('hana-server')
"""

RETURN = """
---
data:
  type: list
  elements: string
  description: List of aliases that are supported by sap.sap_operations collection
  sample:
    - sapcar
    - sapcar-7.53
    - sapcar-7.22
    - saphostagent
    - saphostagent-7.22
    - hana-server
    - hana-client
    - hana-cockpit
    - swpm-1.0
    - swpm-2.0
"""


def me_aliases(value):
    return list(enr_from_alias.keys())


class FilterModule(object):
    def filters(self):
        return {"me_aliases": me_aliases}
