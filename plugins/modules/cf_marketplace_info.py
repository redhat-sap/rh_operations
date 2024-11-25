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
module: cf_marketplace_info

extends_documentation_fragment:
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin
  - sap.sap_operations.cloud_foundry

author:
  - Kirill Satarin (@kksat)

short_description: Fetches Cloud Foundry marketplace service offerings

description:
  - This module fetches the list of available service offerings from the Cloud Foundry marketplace.
  - It uses the Cloud Foundry CLI to interact with the Cloud Foundry API.
  - Cloud Foundry CLI should be installed and available in PATH.

version_added: "1.21.0"

options: {}

notes:
  - This module does not modify any data and is safe to run in check mode.
"""

EXAMPLES = r"""
---
- name: Get Cloud Foundry marketplace services
  sap.sap_operations.cf_marketplace_info:
    username: <SAP BTP user email>
    password: password
    api_endpoint: <SAP BTP API endpoint>
"""

RETURN = r"""
---
cf_marketplace_info:
  description: List of Cloud Foundry marketplace services
  type: list
  elements: dict
  returned: success
  contains:
    available:
      description: Indicates if the service is available.
      returned: always
      type: bool
      sample: true
    broker_catalog:
      description: Contains the broker catalog details.
      returned: always
      type: dict
      contains:
        features:
          description: Features provided by the service.
          returned: always
          type: dict
          contains:
            allow_context_updates:
              description: Indicates if context updates are allowed.
              returned: always
              type: bool
            bindable:
              description: Indicates if the service can be bound to applications.
              returned: always
              type: bool
            bindings_retrievable:
              description: Indicates if bindings are retrievable.
              returned: always
              type: bool
            instances_retrievable:
              description: Indicates if instances are retrievable.
              returned: always
              type: bool
            plan_updateable:
              description: Indicates if the plan is updateable.
              returned: always
              type: bool
        id:
          description: The ID of the service in the broker catalog.
          returned: always
          type: str
        metadata:
          description: Metadata associated with the service.
          returned: always
          type: dict
          contains:
            displayName:
              description: Display name
              returned: always
              type: str
            documentationUrl:
              description: Documentation URL
              returned: always
              type: str
            imageUrl:
              description: Image URL
              returned: always
              type: str
            longDescription:
              description: Long description
              returned: always
              type: str
            serviceInventoryId:
              description: Service inventory ID
              returned: always
              type: str
            sm_offering_id:
              description: SM offering ID
              returned: always
              type: str
    created_at:
      description: The creation date and time of the service.
      returned: always
      type: str
    description:
      description: The description of the service.
      returned: always
      type: str
    documentation_url:
      description: URL to the documentation of the service.
      returned: always
      type: str
    guid:
      description: The globally unique identifier of the service.
      returned: always
      type: str
    links:
      description: Links to related resources.
      returned: always
      type: dict
      contains:
        self:
          description: Display name
          returned: always
          type: dict
          contains:
            href:
              description: URL
              returned: always
              type: str
        service_broker:
          description: Documentation URL
          returned: always
          type: dict
          contains:
            href:
              description: URL
              returned: always
              type: str
        service_plans:
          description: Image URL
          returned: always
          type: dict
          contains:
            href:
              description: URL
              returned: always
              type: str
    metadata:
      description: Additional metadata about the service.
      returned: always
      type: dict
      contains:
        annotations:
          description: Annotations
          returned: always
          type: dict
        labels:
          description: Labels
          returned: always
          type: dict
    name:
      description: The name of the service.
      returned: always
      type: str
    relationships:
      description: Relationships to other entities.
      returned: always
      type: dict
      contains:
        service_broker:
          description: Service broker
          returned: always
          type: dict
          contains:
            data:
              description: Data
              returned: always
              type: dict
              contains:
                guid:
                  description: GUID
                  returned: always
                  type: str
    requires:
      description: Features required by the service.
      returned: always
      type: list
    shareable:
      description: Indicates if the service instance can be shared across spaces.
      returned: always
      type: bool
    tags:
      description: Tags associated with the service.
      returned: always
      type: list
      elements : str
    updated_at:
      description: The last update date and time of the service.
      returned: always
      type: str
"""
