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

__metaclass__ = type


DOCUMENTATION = """
---
name: inifile_params
author: Kirill Satarin (@kksat)
extends_documentation_fragment: sap.sap_operations.community
version_added: 2.8.0
short_description: Convert multilevel dictionary to the inifile params plain text
description:
  - Convert multilevel dictionary to the inifile params plain text

options:
  value:
    description: Dictionary to convert.
    type: dict
    required: true
  prefix:
    description: Prefix for all lines
    type: str
    required: false
    default: ""
  kvseparator:
    description: Separator between key and value
    type: str
    required: false
    default: " = "
  levelseparator:
    description: Separator between dictionary levels
    type: str
    required: false
    default: "."
"""

EXAMPLES = """
---
- name: Test filter inifile_params
  hosts: localhost
  gather_facts: false
  vars:
    inifile_params:
      DiagnosticsAgent:
        SAPJVMVersion: SAPJVM8
        InstanceNumber: 98
        SID: DAA
      archives:
        downloadBasket: /tmp
    inifile_params_text: |-
      DiagnosticsAgent.SAPJVMVersion = SAPJVM8
      DiagnosticsAgent.InstanceNumber = 98
      DiagnosticsAgent.SID = DAA
      archives.downloadBasket = /tmp
  tasks:
    - name: Test filter inifile_params
      ansible.builtin.assert:
        that:
          - inifile_params | sap.sap_operations.inifile_params == inifile_params_text
"""

RETURN = """
---
  data:
    type: str
    description:
      - multiline string in inifile.params format
    sample: |-
      DiagnosticsAgent.SAPJVMVersion = SAPJVM8
      DiagnosticsAgent.InstanceNumber = 98
      DiagnosticsAgent.SID = DAA
      archives.downloadBasket = /tmp
"""


def dict_to_lines(dictionary, prefix="", kvseparator=" = ", levelseparator="."):
    lines = []
    for key, value in dictionary.items():
        if isinstance(value, dict):
            lines.extend(
                dict_to_lines(
                    value,
                    prefix=f"{prefix}{key}{levelseparator}",
                    kvseparator=kvseparator,
                    levelseparator=levelseparator,
                )
            )
        else:
            lines.append(f"{prefix}{key}{kvseparator}{value}")
    return lines


def dict_to_text(dictionary, prefix="", kvseparator=" = ", levelseparator="."):
    return "\n".join(
        dict_to_lines(
            dictionary,
            prefix=prefix,
            kvseparator=kvseparator,
            levelseparator=levelseparator,
        )
    )


def inifile_params(
    value: dict, prefix: str = "", kvseparator: str = " = ", levelseparator="."
):
    if value is None:
        return ""
    if isinstance(value, dict):
        return dict_to_text(value)
    return ""


class FilterModule(object):
    def filters(self):
        return {"inifile_params": inifile_params}
