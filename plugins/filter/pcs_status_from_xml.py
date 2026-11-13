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

from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import Element2Dict

DOCUMENTATION = """
name: pcs_status_from_xml
author: Kirill Satarin (@kksat)
version_added: 2.18.0
short_description: Parse pacemaker status XML into a dict (same shape as pcs_status_info)
description:
  - Parses the XML returned by C(pcs status xml) and returns a dict with the
    same structure as M(sap.sap_operations.pcs_status_info) produces in
    C(pacemaker_status).
  - Useful for offline tests where the XML is loaded from a file rather than
    collected live.
options:
  value:
    description: pacemaker status XML string
    type: str
    required: true
"""

EXAMPLES = r"""
- ansible.builtin.debug:
    var: lookup('file', 'pcs_status.xml') | sap.sap_operations.pcs_status_from_xml
"""

RETURN = """
data:
  description: Dict representation of the pacemaker status XML. Empty dict on parse failure.
  returned: Success
  type: dict
"""


def pcs_status_from_xml(xml_string):
    if not isinstance(xml_string, str) or not xml_string.strip():
        return {}
    try:
        root = ET.fromstring(xml_string)  # nosec B314
    except Exception:
        return {}
    return Element2Dict(root)


class FilterModule(object):
    def filters(self):
        return {"pcs_status_from_xml": pcs_status_from_xml}
