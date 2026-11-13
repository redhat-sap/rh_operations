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

DOCUMENTATION = """
name: pcs_alerts_from_cib
author: Kirill Satarin (@kksat)
version_added: 2.18.0
short_description: Return cluster alerts from pcs_cib_info result
description:
  - Returns alerts defined under the C(<alerts>) section of the cluster CIB
  - Input is the result of M(sap.sap_operations.pcs_cib_info)
options:
  value:
    description: Result of sap.sap_operations.pcs_cib_info module execution
    type: dict
    required: true
  path_contains:
    description: Optional substring filter on the alert path attribute (e.g. C(SAPHanaSR-alert-fencing))
    type: str
    required: false
"""

EXAMPLES = r"""
- name: Assert SAPHanaSR fencing alert is configured
  ansible.builtin.assert:
    that:
      - (pcs_cib_info | sap.sap_operations.pcs_alerts_from_cib(path_contains='SAPHanaSR-alert')) | length > 0
"""

RETURN = """
data:
  description: List of alerts as dicts. Empty list on any failure.
  returned: Success
  type: list
  elements: dict
  example:
    - id: alert_ha_dr
      path: /usr/share/pacemaker/alerts/SAPHanaSR-alert-fencing.sh
"""


def pcs_alerts_from_cib(data, path_contains=None):
    if not hasattr(data, "get"):
        return []
    xml = data.get("pacemaker_cib_xml")
    if not xml:
        return []
    try:
        tree = ET.fromstring(xml)  # nosec B314
    except Exception:
        return []
    items = [dict(e.attrib) for e in tree.findall(".//alerts/alert")]
    if path_contains:
        items = [i for i in items if path_contains in (i.get("path") or "")]
    return items


class FilterModule(object):
    def filters(self):
        return {"pcs_alerts_from_cib": pcs_alerts_from_cib}
