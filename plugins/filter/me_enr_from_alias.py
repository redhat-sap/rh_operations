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
from ansible_collections.sap.sap_operations.plugins.module_utils.me_helpers import enr_from_alias  # noqa: E501


DOCUMENTATION = """
name: me_enr_from_alias
author: Kirill Satarin (@kksat)
extends_documentation_fragment: sap.sap_operations.community
version_added: 1.10.0
short_description: Return the ENR from alias.
description:
  - Return the ENR from alias.
  - If alias is not correct None will be returned.

options:
  value:
    description: Alias to convert.
    type: str
    required: true
"""

EXAMPLES = r"""
- name: Example 'me_enr_from_alias' filter, this assertion is True
  ansible.builtin.assert:
    that:
      - "{{ ( 'sapcar' | sap.sap_operations.me_enr_from_alias ) is defined }}"
      - "{{  'sapcar-7.22' | sap.sap_operations.me_enr_from_alias == '73555000100200014919' }}"
"""  # noqa: E501

RETURN = """
data:
  type: string
  description: ENR for provided alias or None if alias is not correct.
  sample: '73555000100200014919'
"""


def me_enr_from_alias(value):
    return enr_from_alias.get(value, None)


class FilterModule(object):
    def filters(self):
        return {"me_enr_from_alias": me_enr_from_alias}
