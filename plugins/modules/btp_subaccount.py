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
module: btp_subaccount

extends_documentation_fragment:
  - sap.sap_operations.sap_btp_action_plugin
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin

author:
  - Kirill Satarin (@kksat)

short_description: Manage SAP BTP global account subaccounts
version_added: 1.27.0
description:
    - This module allows managing SAP BTP global account subaccounts, including creation and information retrieval.
    - Subaccount will not be updated if there is already subaccount with same subdomain.
    - It is not yet possible to remove existing subaccount with this plugin

options:
    description:
        description:
            - Description of the subaccount to be created or managed.
        required: true
        type: str
    beta_enabled:
        description:
            - Specifies if the subaccount should have beta features enabled.
        required: false
        default: true
        type: bool
    display_name:
        description:
            - The display name for the subaccount.
        required: true
        type: str
    region:
        description:
            - The region where the subaccount will be created.
        required: true
        type: str
    subaccount_admins:
        description:
            - A list of emails for the subaccount administrators.
        required: true
        type: list
        elements: str
    subdomain:
        description:
            - The subdomain for the subaccount
            - Should be globally unique
        required: true
        type: str
"""

EXAMPLES = r"""
---
- name: Create a new subaccount in SAP BTP
  sap.sap_operations.btp_subaccount:
    description: "Development environment"
    beta_enabled: true
    display_name: "Dev Environment"
    region: "eu10"
    subaccount_admins:
      - "admin@example.com"
    subdomain: "dev-env"
"""


RETURN = r"""
---
btp_subaccount:
  description: The result of the Ansible plugin operation, containing details about the subaccount.
  returned: success
  type: dict
  sample:
    betaEnabled: true
    contentAutomationState: null
    contentAutomationStateDetails: null
    createdBy: null
    createdDate: 1713452527495
    description: "Subaccount managed by ansible"
    displayName: "ansible-subaccount-1775088641"
    globalAccountGUID: "7hbf5926-fh9a-4b7e-9b5a-cf3hls6s7"
    guid: "42fss8ec-r75b-4n0l-b5;e-c8b40dd9d839"
    modifiedDate: 1713452550559
    parentGUID: "7hbf5926-4hda-4b7e-9b5a-cfl8ls6s7"
    parentType: "ROOT"
    region: "us10"
    state: "OK"
    stateMessage: "Subaccount created."
    subdomain: "ansible-subdomain-1775088641"
    technicalName: "42fss8ec-r75b-4n0l-b5;e-c8b40dd9d839"
    usedForProduction: "USED_FOR_PRODUCTION"
  contains:
    betaEnabled:
      description: Indicates if the beta features are enabled for the subaccount.
      returned: always
      type: bool
    contentAutomationState:
      description: The state of content automation for the subaccount, if applicable.
      returned: when applicable
      type: str
    createdBy:
      description: The identifier of the user who created the subaccount.
      returned: when available
      type: str
    createdDate:
      description: The timestamp when the subaccount was created.
      returned: always
      type: str
    description:
      description: A brief description of the subaccount.
      returned: always
      type: str
    displayName:
      description: The display name of the subaccount.
      returned: always
      type: str
    globalAccountGUID:
      description: The GUID of the global account to which the subaccount belongs.
      returned: always
      type: str
    guid:
      description: The unique identifier of the subaccount.
      returned: always
      type: str
    modifiedDate:
      description: The timestamp when the subaccount was last modified.
      returned: always
      type: str
    parentGUID:
      description: The GUID of the parent account.
      returned: always
      type: str
    parentType:
      description: The type of the parent account.
      returned: always
      type: str
    region:
      description: The region in which the subaccount is located.
      returned: always
      type: str
    state:
      description: The current state of the subaccount.
      returned: always
      type: str
    stateMessage:
      description: A message providing additional details about the state of the subaccount.
      returned: always
      type: str
    subdomain:
      description: The subdomain assigned to the subaccount.
      returned: always
      type: str
    technicalName:
      description: The technical name of the subaccount.
      returned: always
      type: str
    usedForProduction:
      description: Indicates whether the subaccount is used for production purposes.
      returned: always
      type: str
"""
