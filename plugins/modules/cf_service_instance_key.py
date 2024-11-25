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
module: cf_service_instance_key

extends_documentation_fragment:
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin
  - sap.sap_operations.cloud_foundry

author:
  - Kirill Satarin (@kksat)

version_added: 1.25.0

short_description: Manage Cloud Foundry Service Instance Keys
description:
    - This module allows managing service instance keys in Cloud Foundry
    - It can create or delete service instance keys based on the state provided
options:
    service_instance_name:
        description:
            - The name of the service instance for which to manage keys.
        required: false
        type: str
    service_instance_guid:
        description:
            - The GUID of the service instance for which to manage keys.
        required: false
        type: str
    key_name:
        description:
            - The name of the service instance key to manage.
        required: true
        type: str
        aliases: [ service_instance_key_name ]
    state:
        description:
            - The desired state of the service instance key.
        required: false
        default: "present"
        choices: [ "present", "absent" ]
        type: str
"""

EXAMPLES = """
---
- name: Create a service instance key
  sap.sap_operations.cf_service_instance_key:
    username: "admin"
    password: "password"
    api_endpoint: "https://api.example.com"
    service_instance_name: "my-service-instance"
    key_name: "my-service-key"
    state: "present"

- name: Delete a service instance key
  sap.sap_operations.cf_service_instance_key:
    username: "admin"
    password: "password"
    api_endpoint: "https://api.example.com"
    service_instance_guid: "12345678-1234-1234-1234-123456789012"
    key_name: "my-service-key"
    state: "absent"
"""


RETURN = """
---
cf_service_instance_key:
  description: A service keys details
  returned: success and state is present
  type: dict
  contains:
    entity:
      description: The entity details of the service key.
      type: dict
      contains:
        credentials:
          description: The credentials and related URLs for the service.
          type: dict
          contains:
            endpoints:
              description: Various service URLs.
              type: dict
              contains:
                account_context_service_url:
                  description: URL for the account context service.
                  type: str
                accounts_service_url:
                  description: URL for the accounts service.
                  type: str
                cloud_automation_url:
                  description: URL for the cloud automation service.
                  type: str
                entitlements_service_url:
                  description: URL for the entitlements service.
                  type: str
                events_service_url:
                  description: URL for the events service.
                  type: str
                external_provider_registry_url:
                  description: URL for the external provider registry service.
                  type: str
                metadata_service_url:
                  description: URL for the metadata service.
                  type: str
                order_processing_url:
                  description: URL for the order processing service.
                  type: str
                provisioning_service_url:
                  description: URL for the provisioning service.
                  type: str
                saas_registry_service_url:
                  description: URL for the SaaS registry service.
                  type: str
            grant_type:
              description: The grant type for authentication.
              type: str
            "sap.cloud.service":
              description: SAP cloud service identifier.
              type: str
            uaa:
              description: Details about the UAA (User Account and Authentication).
              type: dict
              contains:
                apiurl:
                  description: API URL for the UAA service.
                  type: str
                clientid:
                  description: Client ID for authentication.
                  type: str
                clientsecret:
                  description: Client secret for authentication.
                  type: str
                identityzone:
                  description: Identity zone for the UAA service.
                  type: str
                url:
                  description: URL for the UAA service.
                  type: str
                verificationkey:
                  description: Public verification key.
                  type: str
        name:
          description: The name of the service key.
          type: str
        service_instance_guid:
          description: GUID of the service instance.
          type: str
        service_instance_url:
          description: URL of the service instance.
          type: str
        service_key_parameters_url:
          description: URL for the service key parameters.
          type: str
    metadata:
      description: Metadata related to the service key.
      type: dict
      contains:
        created_at:
          description: Creation timestamp of the service key.
          type: str
        guid:
          description: GUID of the service key.
          type: str
        updated_at:
          description: Last update timestamp of the service key.
          type: str
        url:
          description: URL of the service key.
          type: str
"""
