#!/usr/bin/python
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


DOCUMENTATION = r"""
---
module: cf_spaces_info

extends_documentation_fragment:
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin
  - sap.sap_operations.cloud_foundry

author:
  - Kirill Satarin (@kksat)

short_description: Fetch information about Cloud Foundry spaces

description:
  - Fetch information about Cloud Foundry spaces

version_added: 1.22.0

options: {}
"""

EXAMPLES = r"""
---
- name: Fetch information about spaces
  sap.sap_operations.cf_spaces_info:
    username: user@email.domain
    password: secret
    api_endpoint: <cloud foundry api endpoint>
"""

RETURN = r"""
---
# TODO: add documentation
    """
