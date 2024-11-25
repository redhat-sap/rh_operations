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
        pcs_resources_by_id_from_cib,
    )
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
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        get_pcs_resource_agent_class_from_cib,
    )
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        get_pcs_resource_agent_provider_from_cib,
    )
    from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import (
        get_pcs_resource_agent_type_from_cib,
    )
except ImportError as import_exception:
    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = import_exception
else:
    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = None


DOCUMENTATION = """

name: pcs_resources

author: Kirill Satarin (@kksat)

extends_documentation_fragment: sap.sap_operations.experimental

version_added: 1.6.0-galaxy

short_description: Get pcs cluster resources lists

description:
  - Get pcs cluster resources lists from sap.sap_operations.pcs_cib_info or sap.sap_operations.pcs_status result
  - Depending on parameters provided, this filter will return list of pcs resources
  - Output of this filter is different for pcs_cib_info and pcs_status result
  - Primitive, clone and group resources are supported
  - |
    Several parameters can be provided to filter pcs resources at once, for instance:
    List all pcs resources with id that contains 'HANA'
    sap.sap_operations.pcs_resources(id_contains='HANA', resource_agent_class='ocf')


options:
  value:
    description: Result of sap.sap_operations.pcs_cib_info or sap.sap_operations.pcs_status execution
    type: dict
    required: True

  id:
    description:
      - Id of the pcs resource.
      - All resources with this id will be returned.
    type: str
    required: False

  id_contains:
    description:
      - String that should be contained in pcs resource id.
      - All resources with id that contains this string will be returned.
    type: str
    required: False

  resource_agent_type:
    description:
      - Type of resource agent for pcs resource.
      - All resources with resource agent type will be returned.
    type: str
    required: False

  resource_agent_provider:
    description:
      - Provider of resource agent for pcs resource.
      - All resources with resource agent provider will be returned.
    type: str
    required: False

  resource_agent_class:
    description:
      - Class of resource agent for pcs resource
      - All resources with resource agent class will be returned.
    type: str
    required: False

"""

EXAMPLES = r"""
- name: Get cluster CIB
  sap.sap_operations.pcs_cib_info:
  register: pcs_cib_info

- name: Get cluster status
  sap.sap_operations.pcs_status_info:
  register: pcs_status_info

- name: Print pcs_resources
  ansible.builtin.debug:
    msg:
      - "{{ pcs_cib_info | sap.sap_operations.pcs_resources }}"
      - "{{ pcs_cib_info | sap.sap_operations.pcs_resources(id='dummy') }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_resources }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_resources(id_contains='dummy') }}"
"""

RETURN = """
data:
  description: List of pcs resources filtered by provided parameters
  returned: Success and when sap.sap_operations.pcs_status_info output is provided
  type: list
  elements: dict
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

data2:
  description: List of pcs resources filtered by provided parameters
  returned: Success and when sap.sap_operations.pcs_cib_info output is provided
  type: list
  elements: dict
  example:
    - "primitive":
        "id": "dummy-resource"
        "class": "ocf"
        "provider": "pacemaker"
        "type": "Dummy"
        "operations":
          - "op":
              "id": "dummy-resource-migrate_from-interval-0s"
              "interval": "0s"
              "name": "migrate_from"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-migrate_to-interval-0s"
              "interval": "0s"
              "name": "migrate_to"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-monitor-interval-10s"
              "interval": "10s"
              "name": "monitor"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-reload-interval-0s"
              "interval": "0s"
              "name": "reload"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-reload-agent-interval-0s"
              "interval": "0s"
              "name": "reload-agent"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-start-interval-0s"
              "interval": "0s"
              "name": "start"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-stop-interval-0s"
              "interval": "0s"
              "name": "stop"
              "timeout": "20s"
    - "primitive":
        "id": "dummy-resource-with-options"
        "attrib":
          "id": "dummy-resource-with-options-meta_attributes"
        "class": "ocf"
        "provider": "pacemaker"
        "type": "Dummy"
        "instance_attributes":
          - "nvpair":
              "id": "dummy-resource-with-options-instance_attributes-fake"
              "name": "fake"
              "value": "fake-value"
          - "nvpair":
              "id": "dummy-resource-with-options-instance_attributes-passwd"
              "name": "passwd"
              "value": "passwd-value"
        "meta_attributes":
          - "nvpair":
              "id": "dummy-resource-with-options-meta_attributes-is-managed"
              "name": "is-managed"
              "value": "true"
          - "nvpair":
              "id": "dummy-resource-with-options-meta_attributes-target-role"
              "name": "target-role"
              "value": "Started"
        "operations":
          - "op":
              "id": "dummy-resource-with-options-migrate_from-interval-0s"
              "interval": "0s"
              "name": "migrate_from"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-with-options-migrate_to-interval-0s"
              "interval": "0s"
              "name": "migrate_to"
              "timeout": "20s"
          - "op":
              "id": "dummy-resource-with-options-monitor-interval-1min"
              "interval": "1min"
              "name": "monitor"
              "timeout": "5"
          - "op":
              "id": "dummy-resource-with-options-reload-interval-0s"
              "interval": "0s"
              "name": "reload"
              "timeout": "20s"
"""


def pcs_resources(  # noqa: C901
    data,
    id=None,
    id_contains=None,
    resource_agent_type: str = None,
    resource_agent_provider: str = None,
    resource_agent_class: str = None,
):
    if SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR:
        return []

    if not data.__dir__().__contains__("get"):
        return []
    if data.get("pacemaker_cib_xml"):
        try:
            pcs_config_tree = ET.fromstring(data.get("pacemaker_cib_xml"))  # nosec B314
            if not pcs_config_tree:
                return []
        except Exception:
            return []
        filtered_resources = pcs_resources_by_id_from_cib(pcs_config_tree)
        get_pcs_resource_agent_class = get_pcs_resource_agent_class_from_cib
        get_pcs_resource_agent_provider = get_pcs_resource_agent_provider_from_cib
        get_pcs_resource_agent_type = get_pcs_resource_agent_type_from_cib

    elif data.get("pacemaker_status_xml"):
        try:
            pcs_status_tree = ET.fromstring(
                data.get("pacemaker_status_xml")
            )  # nosec B314
            if not pcs_status_tree:
                return []
        except Exception:
            return []
        filtered_resources = pcs_resources_by_id_from_status(pcs_status_tree)
        get_pcs_resource_agent_class = get_pcs_resource_agent_class_from_status
        get_pcs_resource_agent_provider = get_pcs_resource_agent_provider_from_status
        get_pcs_resource_agent_type = get_pcs_resource_agent_type_from_status
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

    if resource_agent_class:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if get_pcs_resource_agent_class(pcs_resource) == resource_agent_class
        ]

    if resource_agent_provider:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if get_pcs_resource_agent_provider(pcs_resource) == resource_agent_provider
        ]

    if resource_agent_type:
        filtered_resources = [
            pcs_resource
            for pcs_resource in filtered_resources
            if get_pcs_resource_agent_type(pcs_resource) == resource_agent_type
        ]

    return [Element2Dict(pcs_resource) for pcs_resource in filtered_resources]


class FilterModule(object):
    def filters(self):
        return {
            "pcs_resources": pcs_resources,
        }
