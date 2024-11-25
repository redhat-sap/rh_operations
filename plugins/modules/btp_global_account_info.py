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
module: btp_global_account_info

extends_documentation_fragment:
  - sap.sap_operations.sap_btp_action_plugin
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin

author:
  - Kirill Satarin (@kksat)

short_description: Get information about a SAP BTP global account.

description:
  - Get information about a SAP BTP global account.

version_added: 1.26.0

options:
  expand:
    description: Expand the response with additional information.
    required: false
    default: True
    type: bool
"""

EXAMPLES = r"""
---
- name: Get SAP BTP global account information
  sap.sap_operations.btp_global_account_info:
    login: username@host.com
    password: SecretPassword ## not secret
    api_endpoint: https://accounts-service.cfapps.eu10.hana.ondemand.com
    client_id: "{{ lookup('env', 'BTP_CLIENT_ID') }}"
    client_secret: "{{ lookup('env', 'BTP_CLIENT_SECRET') }}"
    authorize_service_url: 'https://accounts-service.cfapps.eu10.hana.ondemand.com/oauth/authorize'
    token_service_url: 'https://example-global-account.authentication.eu10.hana.ondemand.com/oauth/token'
    expand: true
"""

RETURN = r"""
---
btp_global_account_info:
  description: Dictionary with SAP BTP global account information.
  returned: success
  type: dict
  sample:
    commercialModel: Subscription
    consumptionBased: false
    contractStatus: ACTIVE
    createdDate: 1701277726166
    displayName: Trial global account
    entityState: OK
    geoAccess: STANDARD
    guid: 32864b5f-guid-guid-guid-eb27a837c2f2
    licenseType: TRIAL
    modifiedDate: 1704803656733
    renewalDate: 1706461726145
    stateMessage: Global account created.
    subdomain: subdomaintrial-ga
  contains:
    commercialModel:
        description: The commercial model of the account.
        returned: always
        type: str
        sample: Subscription
    consumptionBased:
        description: Indicates if the account is consumption based.
        returned: always
        type: bool
        sample: false
    contractStatus:
        description: The status of the account contract.
        returned: always
        type: str
        sample: ACTIVE
    createdDate:
        description: The timestamp when the account was created.
        returned: always
        type: int
        sample: 1710931123147
    displayName:
        description: The display name of the account.
        returned: always
        type: str
        sample: 470ae534trial
    entityState:
        description: The state of the account entity.
        returned: always
        type: str
        sample: OK
    geoAccess:
        description: The geographical access level of the account.
        returned: always
        type: str
        sample: STANDARD
    guid:
        description: The globally unique identifier of the account.
        returned: always
        type: str
        sample: 7abf6926-f5da-467e-975a-cf2473680127
    licenseType:
        description: The type of license the account holds.
        returned: always
        type: str
        sample: TRIAL
    modifiedDate:
        description: The timestamp when the account was last modified.
        returned: always
        type: int
        sample: 1711622755495
    renewalDate:
        description: The timestamp when the account is due for renewal.
        returned: always
        type: int
        sample: 1713523123127
    stateMessage:
        description: A message describing the state of the account.
        returned: always
        type: str
        sample: Global account created.
    subaccounts:
        description: A list of subaccounts associated with the account.
        returned: always
        type: list
        elements: dict
        contains:
            betaEnabled:
                description: Indicates if beta features are enabled for the subaccount.
                returned: always
                type: bool
                sample: false
            createdDate:
                description: The timestamp when the subaccount was created.
                returned: always
                type: int
                sample: 1710931140438
            displayName:
                description: The display name of the subaccount.
                returned: always
                type: str
                sample: trial
            globalAccountGUID:
                description: The globally unique identifier for the parent account.
                returned: always
                type: str
                sample: 7abd69g6-f5dg-46fe-975a-cf2473680127
            guid:
                description: globally unique identifier for the subaccount.
                returned: always
                type: str
                sample: 4et23db7-bb09-40da-938c-a17e98ea4ce
            region:
                description: The region where the subaccount is located.
                returned: always
                type: str
                sample: us10
            state:
                description: The state of the subaccount.
                returned: always
                type: str
                sample: OK
            subdomain:
                description: The subdomain assigned to the subaccount.
                returned: always
                type: str
                sample: 470ae534trial
    subdomain:
        description: The subdomain assigned to the global account.
        returned: always
        type: str
        sample: 470ae534trial-ga
    children:
      description: List with SAP BTP global account directories [Feature Set B]
      returned: only if the are subdirectories in the global directory
      type: list
      elements: dict
      sample:
        - consumptionBased: false
          contractStatus: ACTIVE
          createdBy: username@host.com
          createdDate: 1705414050315
          directoryFeatures:
            - DEFAULT
          directoryType: FOLDER
          displayName: test
          entityState: OK
          globalAccountGUID: 32864b5f-guid-guid-guid-eb27a837c2f2
          guid: 4c71c790-guid-guid-guid-b56c6754f8e4
          modifiedDate: 1705414050315
          parentGUID: 32864b5f-guid-guid-guid-eb27a837c2f2
          parentGuid: 32864b5f-guid-guid-guid-eb27a837c2f2
          parentType: ROOT
          stateMessage: Directory created.
          subaccounts:
            - betaEnabled: false
              contentAutomationState:
              contentAutomationStateDetails:
              createdBy: username@host.com
              createdDate: 1705414070346
              description:
              displayName: test
              globalAccountGUID: 32864b5f-guid-guid-guid-eb27a837c2f2
              guid: eb4aac50-guid-guid-guid-a3364d6b6c16
              modifiedDate: 1705414085650
              parentFeatures:
                - DEFAULT
              parentGUID: 4c71c790-guid-guid-guid-b56c6754f8e4
              parentType: FOLDER
              region: us10
              sapManagedType:
              state: OK
              stateMessage: Subaccount created.
              subdomain: test-subdomain
              technicalName: eb4aac50-guid-guid-guid-a3364d6b6c16
              usedForProduction: UNSET
"""
