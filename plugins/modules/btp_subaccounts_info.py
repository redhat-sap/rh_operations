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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: btp_subaccounts_info

extends_documentation_fragment:
  - sap.sap_operations.sap_btp_action_plugin
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin

author:
  - Kirill Satarin (@kksat)

short_description: Fetches information about SAP BTP subaccounts
version_added: 1.27.0
description:
  - This module fetches information about SAP Business Technology Platform (BTP) subaccounts.
  - It uses the BTP Accounts Service API to retrieve the information.
options:
  include_auto_managed_plans:
    description:
      - Whether to include subaccounts with auto-managed plans in the results.
    type: bool
    required: false
    default: false
  entitled_services_only:
    description:
      - Whether to return only subaccounts that are entitled to use services.
    type: bool
    required: false
    default: false
"""

EXAMPLES = r"""
---
- name: Fetch BTP subaccounts information
  sap.sap_operations.btp_subaccounts_info:
    include_auto_managed_plans: true
    entitled_services_only: false
"""


RETURN = r"""
---
btp_subaccounts_info:
  description: A list of subaccounts with their details.
  returned: success
  type: list
  elements: dict
  contains:
    betaEnabled:
      description: Indicates if the beta features are enabled for the subaccount.
      type: bool
    contentAutomationState:
      description: The state of content automation, if applicable.
      returned: if exists
      type: str
    contentAutomationStateDetails:
      description: Detailed information about the content automation state, if applicable.
      returned: if exists
      type: str
    createdBy:
      description: The identifier of the user who created the subaccount, if available.
      returned: if exists
      type: str
    createdDate:
      description: The creation date of the subaccount in milliseconds since epoch.
      type: int
    description:
      description: A description of the subaccount.
      type: str
    displayName:
      description: The display name of the subaccount.
      type: str
    globalAccountGUID:
      description: The GUID of the global account to which the subaccount belongs.
      type: str
    guid:
      description: The unique identifier of the subaccount.
      type: str
    modifiedDate:
      description: The last modification date of the subaccount in milliseconds since epoch.
      type: int
    parentGUID:
      description: The GUID of the parent entity of the subaccount.
      type: str
    parentType:
      description: The type of the parent entity (e.g., ROOT).
      type: str
    region:
      description: The region where the subaccount is located.
      type: str
    state:
      description: The current state of the subaccount (e.g., OK).
      type: str
    stateMessage:
      description: A message providing more details about the state of the subaccount.
      type: str
    subdomain:
      description: The subdomain assigned to the subaccount.
      type: str
    technicalName:
      description: The technical name of the subaccount.
      type: str
    usedForProduction:
      description: Indicates if the subaccount is used for production purposes.
      type: str
      sample: 'USED_FOR_PRODUCTION'
"""
