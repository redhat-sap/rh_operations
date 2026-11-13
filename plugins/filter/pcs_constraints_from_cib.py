# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2026 Kirill Satarin (@kksat)
#
# Copyright 2026 Kirill Satarin (@kksat)
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

SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR = None

DOCUMENTATION = """
name: pcs_constraints_from_cib
author: Kirill Satarin (@kksat)
version_added: 2.18.0
short_description: Return constraints from pcs_cib_info result
description:
  - Returns location, colocation and order constraints from the cluster CIB
  - Input is the result of M(sap.sap_operations.pcs_cib_info)
  - Each constraint is returned as a dictionary with its XML attributes plus
    a C(_kind) field set to C(location), C(colocation) or C(order)
options:
  value:
    description: Result of sap.sap_operations.pcs_cib_info module execution
    type: dict
    required: true
  kind:
    description: Optional constraint kind filter - one of location, colocation, order
    type: str
    required: false
  rsc:
    description: Optional filter by rsc attribute (matches location or colocation)
    type: str
    required: false
  node:
    description: Optional filter by node attribute (location constraints only)
    type: str
    required: false
  score:
    description: Optional filter by score value
    type: str
    required: false
"""

EXAMPLES = r"""
- name: Constraints that block a node from running a resource (fencing avoid)
  ansible.builtin.debug:
    msg: "{{ pcs_cib_info | sap.sap_operations.pcs_constraints_from_cib(kind='location', score='-INFINITY') }}"
"""

RETURN = """
data:
  description: List of constraints as dicts. Empty list on any failure.
  returned: Success
  type: list
  elements: dict
  example:
    - _kind: location
      id: cli-ban-dummy-on-host1
      node: host1
      role: Started
      rsc: dummy
      score: -INFINITY
    - _kind: colocation
      id: colocation-vip_HAN_00-SAPHana_HAN_00-clone-2000
      rsc: vip_HAN_00
      rsc-role: Started
      score: "2000"
      with-rsc: SAPHana_HAN_00-clone
      with-rsc-role: Master
    - _kind: order
      id: order-SAPHana_HAN_00-clone-vip_HAN_00-mandatory
      first: SAPHana_HAN_00-clone
      first-action: promote
      then: vip_HAN_00
      then-action: start
"""


_KIND_TAG = {
    "location": "rsc_location",
    "colocation": "rsc_colocation",
    "order": "rsc_order",
}


def _build_all(tree):
    out = []
    for kind, tag in _KIND_TAG.items():
        for elem in tree.findall(".//constraints/{0}".format(tag)):
            d = dict(elem.attrib)
            d["_kind"] = kind
            out.append(d)
    return out


def pcs_constraints_from_cib(data, kind=None, rsc=None, node=None, score=None):
    if SAP_OPERATIONS_MODULE_UTILS_PACEMAKER_LIBRARY_IMPORT_ERROR:
        return []
    if not hasattr(data, "get"):
        return []
    xml = data.get("pacemaker_cib_xml")
    if not xml:
        return []
    try:
        tree = ET.fromstring(xml)  # nosec B314
    except Exception:
        return []

    items = _build_all(tree)
    if kind:
        items = [i for i in items if i.get("_kind") == kind]
    if rsc:
        items = [i for i in items if i.get("rsc") == rsc]
    if node:
        items = [i for i in items if i.get("node") == node]
    if score:
        items = [i for i in items if i.get("score") == score]
    return items


class FilterModule(object):
    def filters(self):
        return {"pcs_constraints_from_cib": pcs_constraints_from_cib}
