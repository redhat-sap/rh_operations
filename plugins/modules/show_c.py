#!/usr/bin/python

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

DOCUMENTATION = r"""
---
module: show_c
author: Kirill Satarin (@kksat)
short_description: Show copyright
description: |
    The hypothetical commands `show w' and `show c' should show the appropriate parts of the General Public License.
    Of course, your program's commands might be different; for a GUI interface, you would use an "about box".
version_added: 1.31.0
seealso:
  - module: sap.sap_operations.show_w
    description: Show warranty
  - name: GNU General Public License 3.0
    description: GPL-3.0 license text
    link: https://www.gnu.org/licenses/gpl-3.0.en.html
options: {}
"""

EXAMPLES = r"""
---
- name: Show copyright
  sap.sap_operations.show_c:
"""

RETURN = r"""
---
msg:
  description: always 'Success'
  returned: always
  type: str
  sample: Success
"""
