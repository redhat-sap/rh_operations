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
        pcs_cluster_property_set_from_cib,
    )
except ImportError as import_exception:
    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = import_exception
else:
    SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = None

DOCUMENTATION = """

name: pcs_cluster_property_mapping

author: Kirill Satarin (@kksat)

extends_documentation_fragment: sap.sap_operations.experimental

version_added: 1.6.0-galaxy

short_description: Get pcs cluster property from pcs_cib_info result

description:
  - Get pcs cluster property from pcs_cib_info result
  - This module expects result of M(sap.sap_operations.pcs_cib_info) module as input value
  - If property does not exists, empty dictionary will be returned
  - By default this filter will return only cluster properties from 'cib-bootstrap-options' cluster property set

options:
  value:
    description: Result of sap.sap_operations.pcs_cib_info module execution
    type: dict
    required: true

  cluster_property_set_id:
    description: ID of cluster property set to filter
    type: str
    required: false
    default: cib-bootstrap-options

  name:
    description:
      - Name of the cluster property.
    type: str
    required: false

  id:
    description:
      - Id of the cluster property.
    type: str
    required: false
"""

EXAMPLES = r"""
- name: Get cluster CIB
  sap.sap_operations.pcs_cib_info:
  register: pcs_cib_info

- name: Get cluster name from pcs_cib_info several ways
  ansible.builtin.debug:
    msg:
      - "Cluster name - {{ ( pcs_cib_info | sap.sap_operations.pcs_cluster_property_mapping(name='cluster-name') )['cluster-name'] }}"
      - "Cluster name - {{ ( pcs_cib_info | sap.sap_operations.pcs_cluster_property_mapping(id='cib-bootstrap-options-cluster-name') )['cluster-name'] }}"
      - "Cluster name - {{ ( pcs_cib_info | sap.sap_operations.pcs_cluster_property_mapping )['cluster-name'] }}"
      - >
        When you provide some different input result will be empty dictionary.
        See {{ ('not pcs_cib output' | sap.sap_operations.pcs_cluster_property_mapping is mapping) == true }}"
"""  # noqa: E501

RETURN = """
data:
  type: dict
  returned: Success
  description:
    - pcs cluster property object (nvpair)
    - all return value are empty strings if property does not exists
    - empty dictionary will be returned for any failure
  example:
    "cluster-infrastructure": "corosync"
    "cluster-name": "my-cluster"
    "dc-version": "2.1.6-8.el8-6fdc9deea29"
    "have-watchdog": "false"
    "stonith-watchdog-timeout": "0"

"""


def pcs_cluster_property_mapping(  # noqa: C901
    data,
    cluster_property_set_id: str = "cib-bootstrap-options",
    name=None,
    id=None,
    name_contains=None,
    id_contains=None,
):  # noqa: C901
    """This function filters a cluster property set based on the given parameters.

    Args:
      data (dict): A dictionary containing an XML string.
      cluster_property_set_id (str): The ID of the cluster property set to filter.
      name (str): The name of the property to filter by.
      id (str): The ID of the property to filter by.
      name_contains (str): A string that the property name should contain.
      id_contains (str): A string that the property ID should contain.

    Returns:
      A list of dictionaries containing the filtered properties.
    """
    if SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR:
        return []

    if not data.__dir__().__contains__("get"):
        return dict()

    if data.get("pacemaker_cib_xml") is None:
        return dict()
    try:
        pcs_config_tree = ET.fromstring(data.get("pacemaker_cib_xml"))  # nosec B314
        if not pcs_config_tree:
            return dict()

    except Exception:
        return dict()

    pcs_cluster_property_set_all = pcs_cluster_property_set_from_cib(
        pcs_config_tree, cluster_property_set_id=cluster_property_set_id
    )
    pcs_cluster_property_set_filtered = pcs_cluster_property_set_all

    if id is not None:
        pcs_cluster_property_set_filtered = [
            pcs_property
            for pcs_property in pcs_cluster_property_set_filtered
            if pcs_property.get("id") == id
        ]

    if name is not None:
        pcs_cluster_property_set_filtered = [
            pcs_property
            for pcs_property in pcs_cluster_property_set_filtered
            if pcs_property.get("name") == name
        ]

    if name_contains is not None:
        pcs_cluster_property_set_filtered = [
            pcs_property
            for pcs_property in pcs_cluster_property_set_filtered
            if name_contains in pcs_property.get("name")
        ]

    if id_contains is not None:
        pcs_cluster_property_set_filtered = [
            pcs_property
            for pcs_property in pcs_cluster_property_set_filtered
            if id_contains in pcs_property.get("id")
        ]

    if pcs_cluster_property_set_filtered:
        return {
            pcs_property.get("name"): pcs_property.get("value")
            for pcs_property in pcs_cluster_property_set_filtered
        }
    else:
        return dict()


class FilterModule(object):
    def filters(self):
        return {"pcs_cluster_property_mapping": pcs_cluster_property_mapping}
