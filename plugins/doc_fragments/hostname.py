# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2025 Red Hat, Project Atmosphere
#
# Copyright 2025 Red Hat, Project Atmosphere
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
# If not, see <https://www.gnu.org/licenses/>

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = """
---
short_description: Return true if string provided is valid sap hostname as per SAP note 611361
description:
  - Return true if string provided is valid sap hostname as per SAP note 611361
  - Description in the SAP note 611361 is a bit ambiguous, so here are the rules that define valid hostname.
  - Valid hostname should only contain alphanumeric characters and '-'
  - Valid hostname should be lowercase (by default, see all_lowercase parameter and examples)
  - Valid hostname does not start with a number
  - Valid hostname does not end with a '-'
  - Valid hostname is no longer than 13 characters (see parameter le and examples below)
  - Valid hostname is at least on character long (see parameter ge)
options:
  value:
    description: Value to check
    required: true
    type: str
  ge:
    description: Minimum length of the hostname (ge = greater of equal)
    required: false
    type: int
    default: 1
  le:
    description: Maximum length of the hostname (le = less or equal)
    required: false
    type: int
    default: 13
  all_lowercase:
    description: Check if hostname is all lowercase
    required: false
    type: bool
    default: true
  """
