# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2025 Kirill Satarin (@kksat)
#
# Copyright 2025 Kirill Satarin (@kksat)
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
        Element2Dict,
        get_pcs_nodes_from_status,
    )

    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = None
except ImportError as import_exception:
    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = import_exception

DOCUMENTATION = """
---
name: pcs_nodes_from_status
author: Kirill Satarin (@kksat)
extends_documentation_fragment:
    - sap.sap_operations.community
    - sap.sap_operations.experimental
version_added: 2.17.0
short_description: Filter pcs cluster nodes from pcs cluster status xml
description:
  - Get pcs nodes list from result of M(sap.sap_operations.pcs_status_info) module
  - Depending on parameters provided, this filter will return list of pcs nodes

options:
  value:
    description: Result of M(sap.sap_operations.pcs_status_info) execution
    type: dict
    required: True

  name:
    description:
      - Name of the node.
    type: str
    required: False

  name_contains:
    description:
      - String that should be contained in pcs node name.
      - All nodes with name that contains this string will be returned.
    type: str
    required: False

  online:
    description:
      - Online state of the node.
      - All nodes with this online state will be returned.
    type: bool
    required: False

  standby:
    description:
      - Standby state of the node.
      - All nodes with this standby state will be returned.
    type: bool
    required: False

  maintenance:
    description:
      - Maintenance state of the node.
      - All nodes with this maintenance state will be returned.
    type: bool
    required: False

"""

EXAMPLES = """
---
- name: Get cluster status
  sap.sap_operations.pcs_status_info:
  register: pcs_status_info

- name: Print pcs_nodes_from_status
  ansible.builtin.debug:
    msg:
      - "{{ pcs_status_info | sap.sap_operations.pcs_nodes_from_status(online=true) }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_nodes_from_status(standby=true) }}"
      - "{{ pcs_status_info | sap.sap_operations.pcs_nodes_from_status(maintenance=true) }}"
"""

RETURN = """
---
data:
  type: list
  returned: Success
  elements: dict
  description:
    - List of pcs nodes filtered by provided parameters
    - Empty list returned on any failure

  example:
    - "node":
        "name": "node-1"
        "online": "true"
        "standby": "false"
        "maintenance": "false"
    - "node":
        "name": "node-2"
        "online": "false"
        "standby": "true"
        "maintenance": "true"
"""


def pcs_node_convert_attribute_to_bool(pcs_node, attribute_name):
    return True if pcs_node.get(attribute_name) == "true" else False


def pcs_nodes_from_status(data, name=None, name_contains=None, online=None, standby=None, maintenance=None):
    if SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR:
        return []

    pcs_status_tree = parse_pacemaker_status(data)
    if not pcs_status_tree:
        return []

    filtered_nodes = get_pcs_nodes_from_status(pcs_status_tree)
    filters = [
        (name, lambda node: node.get("name") == name),
        (name_contains, lambda node: name_contains in node.get("name")),
        (online, lambda node: pcs_node_convert_attribute_to_bool(node, "online") == online),
        (standby, lambda node: pcs_node_convert_attribute_to_bool(node, "standby") == standby),
        (maintenance, lambda node: pcs_node_convert_attribute_to_bool(node, "maintenance") == maintenance),
    ]

    for condition, filter_func in filters:
        if condition is not None:
            filtered_nodes = filter_nodes(filtered_nodes, filter_func)

    return [Element2Dict(node) for node in filtered_nodes]


def parse_pacemaker_status(data):
    if not hasattr(data, "get") or not data.get("pacemaker_status_xml"):
        return None
    try:
        return ET.fromstring(data.get("pacemaker_status_xml"))  # nosec B314
    except Exception:
        return None


def filter_nodes(nodes, filter_func):
    return [node for node in nodes if filter_func(node)]


class FilterModule(object):
    def filters(self):
        return {
            "pcs_nodes_from_status": pcs_nodes_from_status,
        }
