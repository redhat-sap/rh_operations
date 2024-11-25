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
module: pcs_cib_info

extends_documentation_fragment: sap.sap_operations.community

author: Kirill Satarin (@kksat)

short_description: Get pacemaker CIB (configuration information base) information

description:
  - Get pacemaker CIB (configuration information base) information
  - This module will execute command C(cibadmin --query) and process results to present them nicely in Ansible
  - If pacemaker is not running, or ansible user does not have authorizations to execution C(cibadmin --query) command, module will fail
  - Recommended to use C(root) user

options: {}

version_added: 1.4.0-galaxy

"""

EXAMPLES = r"""
- name: Get pacemaker configuration
  sap.sap_operations.pcs_cib_info:
  become: true
  become_user: root
"""

RETURN = r"""
pacemaker_cib:
    description: Pacemaker CIB (configuration information base)
    type: dict
    returned: success
    sample: |-
        {
            "cib": {
                "admin_epoch": "0",
                "cib-last-written": "Tue May  9 10:12:45 2023",
                "configuration": {
                    "constraints": [
                        {
                            "rsc_order": {
                                "first": "SAPHanaTopology_HAN_00-clone",
                                "first-action": "start",
                                "id": "order-SAPHanaTopology_HAN_00-clone-SAPHana_HAN_00-clone-mandatory",
                                "symmetrical": "false",
                                "then": "SAPHana_HAN_00-clone",
                                "then-action": "start"
                            }
                        },
                        {
                            "rsc_colocation": {
                                "id": "colocation-vip_HAN_00-SAPHana_HAN_00-clone-2000",
                                "rsc": "vip_HAN_00",
                                "rsc-role": "Started",
                                "score": "2000",
                                "with-rsc": "SAPHana_HAN_00-clone",
                                "with-rsc-role": "Master"
                            }
                        },
                        {
                            "rsc_order": {
                                "first": "SAPHana_HAN_00-clone",
                                "first-action": "promote",
                                "id": "order-SAPHana_HAN_00-clone-vip_HAN_00-mandatory",
                                "then": "vip_HAN_00",
                                "then-action": "start"
                            }
                        }
                    ],
                    "crm_config": {
                        "cluster_property_set": [
                            {
                                "nvpair": {
                                    "id": "cib-bootstrap-options-have-watchdog",
                                    "name": "have-watchdog",
                                    "value": "false"
                                }
                            },
                            {
                                "nvpair": {
                                    "id": "cib-bootstrap-options-dc-version",
                                    "name": "dc-version",
                                    "value": "2.1.2-4.el8_6.5-ada5c3b36e2"
                                }
                            },
                            {
                                "nvpair": {
                                    "id": "cib-bootstrap-options-cluster-infrastructure",
                                    "name": "cluster-infrastructure",
                                    "value": "corosync"
                                }
                            },
                            {
                                "nvpair": {
                                    "id": "cib-bootstrap-options-cluster-name",
                                    "name": "cluster-name",
                                    "value": "hana_scale-up_azure"
                                }
                            },
                            {
                                "nvpair": {
                                    "id": "cib-bootstrap-options-concurrent-fencing",
                                    "name": "concurrent-fencing",
                                    "value": "true"
                                }
                            },
                            {
                                "nvpair": {
                                    "id": "cib-bootstrap-options-stonith-timeout",
                                    "name": "stonith-timeout",
                                    "value": "900"
                                }
                            },
                            {
                                "nvpair": {
                                    "id": "cib-bootstrap-options-stonith-enabled",
                                    "name": "stonith-enabled",
                                    "value": "true"
                                }
                            }
                        ]
                    },
                    "nodes": [
                        {
                            "node": {
                                "id": "1",
                                "instance_attributes": [
                                    {
                                        "nvpair": {
                                            "id": "nodes-1-hana_han_vhost",
                                            "name": "hana_han_vhost",
                                            "value": "host1"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-1-hana_han_site",
                                            "name": "hana_han_site",
                                            "value": "DC1"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-1-hana_han_srmode",
                                            "name": "hana_han_srmode",
                                            "value": "sync"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-1-hana_han_remoteHost",
                                            "name": "hana_han_remoteHost",
                                            "value": "host2"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-1-hana_han_op_mode",
                                            "name": "hana_han_op_mode",
                                            "value": "logreplay"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-1-lpa_han_lpt",
                                            "name": "lpa_han_lpt",
                                            "value": "1683627165"
                                        }
                                    }
                                ],
                                "uname": "host1"
                            }
                        },
                        {
                            "node": {
                                "id": "2",
                                "instance_attributes": [
                                    {
                                        "nvpair": {
                                            "id": "nodes-2-hana_han_vhost",
                                            "name": "hana_han_vhost",
                                            "value": "host2"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-2-hana_han_remoteHost",
                                            "name": "hana_han_remoteHost",
                                            "value": "host1"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-2-hana_han_site",
                                            "name": "hana_han_site",
                                            "value": "DC2"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-2-hana_han_srmode",
                                            "name": "hana_han_srmode",
                                            "value": "sync"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-2-lpa_han_lpt",
                                            "name": "lpa_han_lpt",
                                            "value": "30"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "nodes-2-hana_han_op_mode",
                                            "name": "hana_han_op_mode",
                                            "value": "logreplay"
                                        }
                                    }
                                ],
                                "uname": "host2"
                            }
                        }
                    ],
                    "resources": [
                        {
                            "primitive": {
                                "class": "stonith",
                                "id": "rsc_st_azure",
                                "instance_attributes": [
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-msi",
                                            "name": "msi",
                                            "value": "true"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-pcmk_action_limit",
                                            "name": "pcmk_action_limit",
                                            "value": "3"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-pcmk_delay_max",
                                            "name": "pcmk_delay_max",
                                            "value": "15"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-pcmk_monitor_retries",
                                            "name": "pcmk_monitor_retries",
                                            "value": "4"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-pcmk_monitor_timeout",
                                            "name": "pcmk_monitor_timeout",
                                            "value": "120"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-pcmk_reboot_timeout",
                                            "name": "pcmk_reboot_timeout",
                                            "value": "900"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-power_timeout",
                                            "name": "power_timeout",
                                            "value": "240"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-resourceGroup",
                                            "name": "resourceGroup",
                                            "value": "molecule"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "rsc_st_azure-instance_attributes-subscriptionId",
                                            "name": "subscriptionId",
                                            "value": "6a73742d-8c0a-4b2d-9c60-67c592a0df50"
                                        }
                                    }
                                ],
                                "operations": [
                                    {
                                        "op": {
                                            "id": "rsc_st_azure-monitor-interval-3600",
                                            "interval": "3600",
                                            "name": "monitor"
                                        }
                                    }
                                ],
                                "type": "fence_azure_arm"
                            }
                        },
                        {
                            "clone": {
                                "id": "SAPHanaTopology_HAN_00-clone",
                                "meta_attributes": [
                                    {
                                        "nvpair": {
                                            "id": "SAPHanaTopology_HAN_00-clone-meta_attributes-clone-max",
                                            "name": "clone-max",
                                            "value": "2"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "SAPHanaTopology_HAN_00-clone-meta_attributes-clone-node-max",
                                            "name": "clone-node-max",
                                            "value": "1"
                                        }
                                    },
                                    {
                                        "nvpair": {
                                            "id": "SAPHanaTopology_HAN_00-clone-meta_attributes-interleave",
                                            "name": "interleave",
                                            "value": "true"
                                        }
                                    }
                                ],
                                "primitive": {
                                    "class": "ocf",
                                    "id": "SAPHanaTopology_HAN_00",
                                    "instance_attributes": [
                                        {
                                            "nvpair": {
                                                "id": "SAPHanaTopology_HAN_00-instance_attributes-InstanceNumber",
                                                "name": "InstanceNumber",
                                                "value": "00"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHanaTopology_HAN_00-instance_attributes-SID",
                                                "name": "SID",
                                                "value": "HAN"
                                            }
                                        }
                                    ],
                                    "operations": [
                                        {
                                            "op": {
                                                "id": "SAPHanaTopology_HAN_00-methods-interval-0s",
                                                "interval": "0s",
                                                "name": "methods",
                                                "timeout": "5"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHanaTopology_HAN_00-monitor-interval-10",
                                                "interval": "10",
                                                "name": "monitor",
                                                "timeout": "600"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHanaTopology_HAN_00-reload-interval-0s",
                                                "interval": "0s",
                                                "name": "reload",
                                                "timeout": "5"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHanaTopology_HAN_00-start-interval-0s",
                                                "interval": "0s",
                                                "name": "start",
                                                "timeout": "600"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHanaTopology_HAN_00-stop-interval-0s",
                                                "interval": "0s",
                                                "name": "stop",
                                                "timeout": "300"
                                            }
                                        }
                                    ],
                                    "provider": "heartbeat",
                                    "type": "SAPHanaTopology"
                                }
                            }
                        },
                        {
                            "clone": {
                                "id": "SAPHana_HAN_00-clone",
                                "meta_attributes": [
                                    {
                                        "nvpair": {
                                            "id": "SAPHana_HAN_00-clone-meta_attributes-promotable",
                                            "name": "promotable",
                                            "value": "true"
                                        }
                                    }
                                ],
                                "primitive": {
                                    "class": "ocf",
                                    "id": "SAPHana_HAN_00",
                                    "instance_attributes": [
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-instance_attributes-AUTOMATED_REGISTER",
                                                "name": "AUTOMATED_REGISTER",
                                                "value": "true"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-instance_attributes-DUPLICATE_PRIMARY_TIMEOUT",
                                                "name": "DUPLICATE_PRIMARY_TIMEOUT",
                                                "value": "7200"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-instance_attributes-InstanceNumber",
                                                "name": "InstanceNumber",
                                                "value": "00"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-instance_attributes-PREFER_SITE_TAKEOVER",
                                                "name": "PREFER_SITE_TAKEOVER",
                                                "value": "true"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-instance_attributes-SID",
                                                "name": "SID",
                                                "value": "HAN"
                                            }
                                        }
                                    ],
                                    "meta_attributes": [
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-meta_attributes-clone-max",
                                                "name": "clone-max",
                                                "value": "2"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-meta_attributes-clone-node-max",
                                                "name": "clone-node-max",
                                                "value": "1"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-meta_attributes-interleave",
                                                "name": "interleave",
                                                "value": "true"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "SAPHana_HAN_00-meta_attributes-notify",
                                                "name": "notify",
                                                "value": "true"
                                            }
                                        }
                                    ],
                                    "operations": [
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-demote-interval-0s",
                                                "interval": "0s",
                                                "name": "demote",
                                                "timeout": "3600"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-methods-interval-0s",
                                                "interval": "0s",
                                                "name": "methods",
                                                "timeout": "5"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-monitor-interval-121",
                                                "interval": "121",
                                                "name": "monitor",
                                                "role": "Slave",
                                                "timeout": "1400"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-monitor-interval-119",
                                                "interval": "119",
                                                "name": "monitor",
                                                "role": "Master",
                                                "timeout": "1400"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-promote-interval-0s",
                                                "interval": "0s",
                                                "name": "promote",
                                                "timeout": "3600"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-reload-interval-0s",
                                                "interval": "0s",
                                                "name": "reload",
                                                "timeout": "5"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-start-interval-0s",
                                                "interval": "0s",
                                                "name": "start",
                                                "timeout": "3600"
                                            }
                                        },
                                        {
                                            "op": {
                                                "id": "SAPHana_HAN_00-stop-interval-0s",
                                                "interval": "0s",
                                                "name": "stop",
                                                "timeout": "3600"
                                            }
                                        }
                                    ],
                                    "provider": "heartbeat",
                                    "type": "SAPHana"
                                }
                            }
                        },
                        {
                            "primitive": {
                                "class": "ocf",
                                "id": "vip_HAN_00",
                                "instance_attributes": [
                                    {
                                        "nvpair": {
                                            "id": "vip_HAN_00-instance_attributes-ip",
                                            "name": "ip",
                                            "value": "10.0.0.111"
                                        }
                                    }
                                ],
                                "operations": [
                                    {
                                        "op": {
                                            "id": "vip_HAN_00-monitor-interval-10s",
                                            "interval": "10s",
                                            "name": "monitor",
                                            "timeout": "20s"
                                        }
                                    },
                                    {
                                        "op": {
                                            "id": "vip_HAN_00-start-interval-0s",
                                            "interval": "0s",
                                            "name": "start",
                                            "timeout": "20s"
                                        }
                                    },
                                    {
                                        "op": {
                                            "id": "vip_HAN_00-stop-interval-0s",
                                            "interval": "0s",
                                            "name": "stop",
                                            "timeout": "20s"
                                        }
                                    }
                                ],
                                "provider": "heartbeat",
                                "type": "IPaddr2"
                            }
                        }
                    ]
                },
                "crm_feature_set": "3.13.0",
                "dc-uuid": "2",
                "epoch": "38",
                "have-quorum": "1",
                "num_updates": "0",
                "status": [
                    {
                        "node_state": {
                            "crm-debug-origin": "do_state_transition",
                            "crmd": "online",
                            "expected": "member",
                            "id": "2",
                            "in_ccm": "true",
                            "join": "member",
                            "lrm": {
                                "id": "2",
                                "lrm_resources": [
                                    {
                                        "lrm_resource": {
                                            "class": "ocf",
                                            "id": "SAPHana_HAN_00",
                                            "lrm_rsc_op": {
                                                "call-id": "20",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "3064",
                                                "exit-reason": "",
                                                "id": "SAPHana_HAN_00_monitor_121000",
                                                "interval": "121000",
                                                "last-rc-change": "1683625935",
                                                "on_node": "host2",
                                                "op-digest": "5e5c436515be36a83224be31e615f496",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "SAPHana_HAN_00_monitor_121000",
                                                "queue-time": "0",
                                                "rc-code": "0",
                                                "transition-key": "16:20:0:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:0;16:20:0:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "provider": "heartbeat",
                                            "type": "SAPHana"
                                        }
                                    },
                                    {
                                        "lrm_resource": {
                                            "class": "ocf",
                                            "id": "SAPHanaTopology_HAN_00",
                                            "lrm_rsc_op": {
                                                "call-id": "14",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "5468",
                                                "exit-reason": "",
                                                "id": "SAPHanaTopology_HAN_00_monitor_10000",
                                                "interval": "10000",
                                                "last-rc-change": "1683624000",
                                                "on_node": "host2",
                                                "op-digest": "430591688d36fc4a519062e5d3d57a59",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "SAPHanaTopology_HAN_00_monitor_10000",
                                                "queue-time": "0",
                                                "rc-code": "0",
                                                "transition-key": "7:3:0:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:0;7:3:0:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "provider": "heartbeat",
                                            "type": "SAPHanaTopology"
                                        }
                                    },
                                    {
                                        "lrm_resource": {
                                            "class": "stonith",
                                            "id": "rsc_st_azure",
                                            "lrm_rsc_op": {
                                                "call-id": "7",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "487",
                                                "exit-reason": "",
                                                "id": "rsc_st_azure_monitor_3600000",
                                                "interval": "3600000",
                                                "last-rc-change": "1683623435",
                                                "on_node": "host2",
                                                "op-digest": "07adc72ccacd3f2b550f146d8eea6ece",
                                                "op-secure-digest": "f2e14860373472ee63eba393414dc818",
                                                "op-secure-params": "  password passwd  ",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "rsc_st_azure_monitor_3600000",
                                                "queue-time": "0",
                                                "rc-code": "0",
                                                "transition-key": "2:0:0:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:0;2:0:0:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "type": "fence_azure_arm"
                                        }
                                    },
                                    {
                                        "lrm_resource": {
                                            "class": "ocf",
                                            "id": "vip_HAN_00",
                                            "lrm_rsc_op": {
                                                "call-id": "24",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "41",
                                                "exit-reason": "",
                                                "id": "vip_HAN_00_last_0",
                                                "interval": "0",
                                                "last-rc-change": "1683626082",
                                                "on_node": "host2",
                                                "op-digest": "39edfbcab03ce04bc05bcc06663f9d9f",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "vip_HAN_00_monitor_0",
                                                "queue-time": "0",
                                                "rc-code": "7",
                                                "transition-key": "7:25:7:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:7;7:25:7:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "provider": "heartbeat",
                                            "type": "IPaddr2"
                                        }
                                    }
                                ]
                            },
                            "transient_attributes": [
                                {
                                    "instance_attributes": [
                                        {
                                            "nvpair": {
                                                "id": "status-2-hana_han_version",
                                                "name": "hana_han_version",
                                                "value": "2.00.059.05.1662044871"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-2-hana_han_roles",
                                                "name": "hana_han_roles",
                                                "value": "4:S:master1:master:worker:master"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-2-hana_han_clone_state",
                                                "name": "hana_han_clone_state",
                                                "value": "DEMOTED"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-2-master-SAPHana_HAN_00",
                                                "name": "master-SAPHana_HAN_00",
                                                "value": "100"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-2-hana_han_sync_state",
                                                "name": "hana_han_sync_state",
                                                "value": "SOK"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "uname": "host2"
                        }
                    },
                    {
                        "node_state": {
                            "crm-debug-origin": "do_state_transition",
                            "crmd": "online",
                            "expected": "member",
                            "id": "1",
                            "in_ccm": "true",
                            "join": "member",
                            "lrm": {
                                "id": "1",
                                "lrm_resources": [
                                    {
                                        "lrm_resource": {
                                            "class": "ocf",
                                            "id": "SAPHana_HAN_00",
                                            "lrm_rsc_op": {
                                                "call-id": "19",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "3715",
                                                "exit-reason": "",
                                                "id": "SAPHana_HAN_00_monitor_119000",
                                                "interval": "119000",
                                                "last-rc-change": "1683625942",
                                                "on_node": "host1",
                                                "op-digest": "5e5c436515be36a83224be31e615f496",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "SAPHana_HAN_00_monitor_119000",
                                                "queue-time": "0",
                                                "rc-code": "8",
                                                "transition-key": "21:21:8:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:8;21:21:8:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "provider": "heartbeat",
                                            "type": "SAPHana"
                                        }
                                    },
                                    {
                                        "lrm_resource": {
                                            "class": "ocf",
                                            "id": "SAPHanaTopology_HAN_00",
                                            "lrm_rsc_op": {
                                                "call-id": "12",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "5377",
                                                "exit-reason": "",
                                                "id": "SAPHanaTopology_HAN_00_monitor_10000",
                                                "interval": "10000",
                                                "last-rc-change": "1683624000",
                                                "on_node": "host1",
                                                "op-digest": "430591688d36fc4a519062e5d3d57a59",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "SAPHanaTopology_HAN_00_monitor_10000",
                                                "queue-time": "0",
                                                "rc-code": "0",
                                                "transition-key": "5:3:0:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:0;5:3:0:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "provider": "heartbeat",
                                            "type": "SAPHanaTopology"
                                        }
                                    },
                                    {
                                        "lrm_resource": {
                                            "class": "stonith",
                                            "id": "rsc_st_azure",
                                            "lrm_rsc_op": {
                                                "call-id": "5",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "1",
                                                "exit-reason": "",
                                                "id": "rsc_st_azure_last_0",
                                                "interval": "0",
                                                "last-rc-change": "1683623453",
                                                "on_node": "host1",
                                                "op-digest": "ef94f90261c5b27235fa13d790d77830",
                                                "op-secure-digest": "f2e14860373472ee63eba393414dc818",
                                                "op-secure-params": "  password passwd  ",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "rsc_st_azure_monitor_0",
                                                "queue-time": "0",
                                                "rc-code": "7",
                                                "transition-key": "2:1:7:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:7;2:1:7:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "type": "fence_azure_arm"
                                        }
                                    },
                                    {
                                        "lrm_resource": {
                                            "class": "ocf",
                                            "id": "vip_HAN_00",
                                            "lrm_rsc_op": {
                                                "call-id": "25",
                                                "crm-debug-origin": "build_active_RAs",
                                                "crm_feature_set": "3.13.0",
                                                "exec-time": "38",
                                                "exit-reason": "",
                                                "id": "vip_HAN_00_monitor_10000",
                                                "interval": "10000",
                                                "last-rc-change": "1683626082",
                                                "on_node": "host1",
                                                "op-digest": "9338a88e9b18f024dbad86a1190733cf",
                                                "op-status": "0",
                                                "operation": "monitor",
                                                "operation_key": "vip_HAN_00_monitor_10000",
                                                "queue-time": "0",
                                                "rc-code": "0",
                                                "transition-key": "33:25:0:507e2249-ffd4-436b-b83f-55d0676ffa3e",
                                                "transition-magic": "0:0;33:25:0:507e2249-ffd4-436b-b83f-55d0676ffa3e"
                                            },
                                            "provider": "heartbeat",
                                            "type": "IPaddr2"
                                        }
                                    }
                                ]
                            },
                            "transient_attributes": [
                                {
                                    "instance_attributes": [
                                        {
                                            "nvpair": {
                                                "id": "status-1-hana_han_version",
                                                "name": "hana_han_version",
                                                "value": "2.00.059.05.1662044871"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-1-hana_han_roles",
                                                "name": "hana_han_roles",
                                                "value": "4:P:master1:master:worker:master"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-1-master-SAPHana_HAN_00",
                                                "name": "master-SAPHana_HAN_00",
                                                "value": "150"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-1-hana_han_clone_state",
                                                "name": "hana_han_clone_state",
                                                "value": "PROMOTED"
                                            }
                                        },
                                        {
                                            "nvpair": {
                                                "id": "status-1-hana_han_sync_state",
                                                "name": "hana_han_sync_state",
                                                "value": "PRIM"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "uname": "host1"
                        }
                    }
                ],
                "update-client": "crm_attribute",
                "update-origin": "host1",
                "update-user": "root",
                "validate-with": "pacemaker-3.8"
            }
        }
"""

import xml.etree.ElementTree as ET  # nosec B405

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import Element2Dict
from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import get_pacemaker_cib_query_xml


def main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    pcs_cib_query_xml_string = get_pacemaker_cib_query_xml(module)
    pacemaker_cib = Element2Dict(ET.fromstring(pcs_cib_query_xml_string))  # nosec B314
    module.exit_json(
        changed=False,
        pacemaker_cib=pacemaker_cib,
        pacemaker_cib_xml=pcs_cib_query_xml_string,
    )


if __name__ == "__main__":
    main()
