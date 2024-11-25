#!/usr/bin/python

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

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
module: pcs_status_info

extends_documentation_fragment: sap.sap_operations.community

author: Kirill Satarin (@kksat)

short_description: Get pacemaker status information

description:
  - Get pacemaker status information
  - This module will execute command C(pcs status xml) and process results to present them nicely in Ansible
  - If pacemaker is not running, or ansible user does not have authorizations to execution C(pcs status xml) command, module will fail
  - Recommended to use C(root) user

options: {}

version_added: 1.4.0-galaxy

"""

EXAMPLES = r"""
- name: Get pacemaker status
  sap.sap_operations.pcs_status_info:
  become: true
  become_user: root
"""

RETURN = r"""
pacemaker_status:
    description: Pacemaker status information in a dictionary
    type: dict
    returned: success
    sample: |-
        {
        "crm_mon": {
            "nodes": [
                {
                    "node": {
                        "expected_up": "true",
                        "id": "1",
                        "is_dc": "false",
                        "maintenance": "false",
                        "name": "host1",
                        "online": "true",
                        "pending": "false",
                        "resources_running": "0",
                        "shutdown": "false",
                        "standby": "false",
                        "standby_onfail": "false",
                        "type": "member",
                        "unclean": "false"
                    }
                },
                {
                    "node": {
                        "expected_up": "true",
                        "id": "2",
                        "is_dc": "true",
                        "maintenance": "false",
                        "name": "host2",
                        "online": "true",
                        "pending": "false",
                        "resources_running": "0",
                        "shutdown": "false",
                        "standby": "false",
                        "standby_onfail": "false",
                        "type": "member",
                        "unclean": "false"
                    }
                }
            ],
            "summary": {
                "cluster_options": {
                    "maintenance-mode": "false",
                    "no-quorum-policy": "stop",
                    "priority-fencing-delay-ms": "0",
                    "stonith-enabled": "true",
                    "stonith-timeout-ms": "60000",
                    "stop-all-resources": "false",
                    "symmetric-cluster": "true"
                },
                "current_dc": {
                    "id": "2",
                    "name": "host2",
                    "present": "true",
                    "version": "2.1.2-4.el8_6.5-ada5c3b36e2",
                    "with_quorum": "true"
                },
                "last_change": {
                    "client": "crmd",
                    "origin": "host1",
                    "time": "Wed May  3 18:13:41 2023",
                    "user": "hacluster"
                },
                "last_update": {
                    "time": "Thu May  4 09:47:15 2023"
                },
                "nodes_configured": {
                    "number": "2"
                },
                "resources_configured": {
                    "blocked": "0",
                    "disabled": "0",
                    "number": "0"
                },
                "stack": {
                    "type": "corosync"
                }
            },
            "version": "2.1.2-4.el8_6.5"
            }
        }

"""

import xml.etree.ElementTree as ET  # nosec B405

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import Element2Dict
from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import get_pacemaker_status_xml


def main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    pacemaker_status_xml = get_pacemaker_status_xml(module)
    pacemaker_status = Element2Dict(ET.fromstring(pacemaker_status_xml))  # nosec B314
    module.exit_json(
        changed=False,
        pacemaker_status=pacemaker_status,
        pacemaker_status_xml=pacemaker_status_xml,
    )


if __name__ == "__main__":
    main()
