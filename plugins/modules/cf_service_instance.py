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
module: cf_service_instance

extends_documentation_fragment:
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin
  - sap.sap_operations.cloud_foundry

author:
  - Kirill Satarin (@kksat)

short_description: Manage Cloud Foundry service instances

description:
    - This plugin allows managing service instances in a Cloud Foundry environment.
    - It can create, delete service instances.
    - Plugin is idempotent it will not create service instance with the same name it is already exists.
    # TODO: add functionality to change service instance configuration
    - Plugin will not change service instance parameters or metadata if service instance already exists (this functionality is planned)

version_added: 1.22.0

options:
    name:
        description: The name of the service instance.
        type: str
        required: True
    service:
        description: The name of the service offering.
        type: str
        required: True
    state:
        description: The desired state of the service instance.
        choices: ['present', 'absent']
        default: 'present'
        type: str
        required: False
    space:
        description: The name of the space in which to manage the service instance.
        type: str
        required: True
    service_plan:
        description: The name of the service plan for the service instance.
        type: str
        required: False
    parameters:
        description: A dictionary containing configuration parameters for the service instance.
        type: dict
        required: False
    metadata:
        description: A dictionary containing metadata for the service instance.
        type: dict
        required: False
"""

EXAMPLES = r"""
---
- name: Create a service instance
  sap.sap_operations.cf_service_instance:
    name: my_service_instance
    service: my_service
    state: present
    space: my_space
    service_plan: my_service_plan
    parameters:
      param1: value1
      param2: value2
    metadata:
      label1: value1
      label2: value2

- name: Delete a service instance
  sap.sap_operations.cf_service_instance:
    name: my_service_instance
    service: my_service
    state: absent
    space: my_space
"""

RETURN = r"""
    """
