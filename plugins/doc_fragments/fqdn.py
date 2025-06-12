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
short_description: Verify that value provided is valid fqdn
description:
    - Verify that value provided is valid fqdn (fully qualified domain name)
    - Valid fqdn is not longer than 253 characters
    - Valid fqdn if split by '.' contains list of valid hostnames
    - Each hostname that valid fqdn contains is not longer than 63 characters
    - Each hostname that valid fqdn contains is valid hostname
options:
    value:
        description: Value to check if valid fqdn
        type: str
        required: True
  """
