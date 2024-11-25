# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2023 Kirill Satarin (@kksat)
#
# Copyright 2023 Kirill Satarin (@kksat)
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

import xml.etree.ElementTree as ET  # nosec B405

try:
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        pcs_resources_by_id_from_status,
    )
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        Element2Dict,
    )
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        get_pcs_resource_agent_provider_from_status,
    )
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        get_pcs_resource_agent_type_from_status,
    )
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        get_pcs_resource_agent_class_from_status,
    )
except ImportError as import_exception:
    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = import_exception
else:
    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = None

DOCUMENTATION = """

name: pcs_resources_from_status

author: Kirill Satarin (@kksat)

extends_documentation_fragment: sap.sap_operations.experimental

version_added: 1.6.0-galaxy

short_description: Get pcs cluster resources lists

description:
  - Get pcs resources list from result of sap.sap_operations.pcs_status_info module
  - Depending on parameters provided, this filter will return list of pcs resources
  - Primitive, clone and group resources are supported
  - |
    Several parameters can be provided to filter pcs resources at once, for instance:
    List all pcs resources with id that contains 'HANA'
    sap.sap_operations.pcs_resources(id_contains='HANA', resource_agent_class='ocf')

options:
  value:
    description: Result of pcs_status_info execution
    type: dict
    required: True

  id:
    description:
      - Id of the property.
      - Either one of I(name) or I(id) is required.
    type: str
    required: False

  id_contains:
    description:
      - String that should be contained in pcs resource id.
      - All resources with id that contains this string will be returned.
    type: str
    required: False

  resource_agent:
    description:
      - Resource agent name.
      - All resources with this resource agent will be returned.
    type: str
    required: False

  resource_agent_provider:
    description: Resource agent provider.
    type: str
    required: False

  resource_agent_type:
    description:
      - Resource agent type.
      - All resources with this resource agent type will be returned.
    type: str
    required: False

  resource_agent_class:
    description:
      - Resource agent class.
      - All resources with this resource agent class will be returned.
    type: str
    required: False

  role:
    description:
      - Role of the resource.
      - All resources with this role will be returned.
    type: str
    required: False

  target_role:
    description:
      - Target role of the resource.
      - All resources with this target role will be returned.
    type: str
    required: False

  active:
    description:
      - Active state of the resource.
      - All resources with this active state will be returned.
    type: bool
    required: False

  blocked:
    description:
      - Blocked state of the resource.
      - All resources with this blocked state will be returned.
    type: bool
    required: False

  failed:
    description:
      - Failed state of the resource.
      - All resources with this failed state will be returned.
    type: bool
    required: False

  managed:
    description:
      - Managed state of the resource.
      - All resources with this managed state will be returned.
    type: bool
    required: False

  maintenance:
    description:
      - Maintenance state of the resource.
      - All resources with this maintenance state will be returned.
    type: bool
    required: False

"""

EXAMPLES = r"""
- name: Get cluster status
  sap.sap_operations.pcs_status_info:
  register: pcs_status_info

- name: Print pcs_resources_from_status
  ansible.builtin.debug:
    msg:
      - "{{ pcs_status_info | sap.sap_operations.pcs_resources_from_status(active=true) }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_resources_from_status(blocked=true) }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_resources_from_status(failed=true) }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_resources_from_status(managed=true) }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_resources_from_status(maintenance=true) }}"
"""

RETURN = """
data:
  type: list
  returned: Success
  elements: dict
  description:
    - List of pcs resources filtered by provided parameters
    - Empty list returned on any failure

  example:
    - "resource":
        "active": "false"
        "blocked": "false"
        "failed": "false"
        "failure_ignored": "false"
        "id": "dummy-resource"
        "maintenance": "false"
        "managed": "true"
        "nodes_running_on": "0"
        "orphaned": "false"
        "resource_agent": "ocf::pacemaker:Dummy"
        "role": "Stopped"
    - "resource":
        "active": "false"
        "blocked": "false"
        "failed": "false"
        "failure_ignored": "false"
        "id": "dummy-resource-with-options"
        "maintenance": "false"
        "managed": "true"
        "nodes_running_on": "0"
        "orphaned": "false"
        "resource_agent": "ocf::pacemaker:Dummy"
        "role": "Stopped"
        "target_role": "Started"

"""


def pcs_resource_convert_attribute_to_bool(pcs_resource, attribute_name):
    return True if pcs_resource.get(attribute_name) == "true" else False


def pcs_resources_from_status(  # noqa: C901
    data,
    id=None,
    id_contains=None,
    resource_agent: str = None,
    resource_agent_provider: str = None,
    resource_agent_type: str = None,
    resource_agent_class: str = None,
    role: str = None,
    target_role: str = None,
    active: bool = None,
    blocked: bool = None,
    failed: bool = None,
    managed: bool = None,
    maintenance: bool = None,
):
    if SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR:
        return []

    if not data.__dir__().__contains__("get"):
        return []
    if data.get("pacemaker_status_xml"):
        try:
            pcs_status_tree = ET.fromstring(
                data.get("pacemaker_status_xml")
            )  # nosec B314
            if not pcs_status_tree:
                return []
        except Exception:
            return []
        filtered_resources = pcs_resources_by_id_from_status(pcs_status_tree)
    else:
        return []

    if id:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if id == pcs_resource.get("id")
        ]

    if id_contains:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if id_contains in pcs_resource.get("id")
        ]

    if resource_agent:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource.get("resource_agent") == resource_agent
        ]

    if resource_agent_provider:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if get_pcs_resource_agent_provider_from_status(pcs_resource) == resource_agent_provider
        ]

    if resource_agent_type:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if get_pcs_resource_agent_type_from_status(pcs_resource) == resource_agent_type
        ]

    if resource_agent_class:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if get_pcs_resource_agent_class_from_status(pcs_resource) == resource_agent_class
        ]

    if role:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource.get("role") == role
        ]

    if target_role:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource.get("target_role") == target_role
        ]

    if active:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource_convert_attribute_to_bool(pcs_resource, "active") == active
        ]

    if blocked:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource_convert_attribute_to_bool(pcs_resource, "blocked") == blocked
        ]

    if failed:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource_convert_attribute_to_bool(pcs_resource, "failed") == failed
        ]

    if managed:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource_convert_attribute_to_bool(pcs_resource, "managed") == managed
        ]

    if maintenance:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if pcs_resource_convert_attribute_to_bool(pcs_resource, "maintenance") == maintenance
        ]

    return [Element2Dict(pcs_resource) for pcs_resource in filtered_resources]


class FilterModule(object):
    def filters(self):
        return {
            "pcs_resources_from_status": pcs_resources_from_status,
        }
