#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Red Hat, Inc. Project Atmosphere
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# Copyright (c) 2023 Red Hat, Inc. Project Atmosphere
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.


from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
module: abap_system_info

extends_documentation_fragment:
  - sap.sap_operations.abap_rfc_doc

author:
  - Kirill Satarin (@kksat)

short_description: Fetch SAP ABAP system information

description:
  - Fetch information about SAP ABAP system
  - |
    Information if fetched from SAP ABAP system using following remote enabled RFCs
      OCS_GET_INSTALLED_SWPRODUCTS
      OCS_GET_SFW_COMPONENTS
      TH_GET_VIRT_HOST_DATA
      DELIVERY_GET_INSTALLED_COMPS
      SMLG_GET_DEFINED_GROUPS
      SMLG_GET_DEFINED_SERVERS
      SMLG_GET_SETUP
      SLDAG_GET_COMPUTER_INFO

version_added: 1.2.0
"""

EXAMPLES = r"""
- name: Collection information about SAP ABAP system
  sap.sap_operations.abap_system_info:
  rfc_connection:
      ashost: application-instance-hostname
      client: '000'
      user: DDIC
      passwd: "SecretPa$$word"
      sysnr: '00'
"""

RETURN = r"""
abap_system_info:
    description: ABAP system info
    type: dict
    returned: success
    sample: |-
        {
            "computer_info": {
                "IP_ADDRESS": "10.0.0.234",
                "IP_ADDRESSES": [
                    {
                        "VALUE": "127.0.0.1"
                    },
                    {
                        "VALUE": "10.0.0.234"
                    }
                ],
                "LOCALHOST": "vhcalnplci",
                "LOCALHOSTFULL": "vhcalnplci.dummy.nodomain",
                "OPSYS": "Linux",
                "OPSYS_BITS": "",
                "OPSYS_RELEASE": "4.12.14-197.102-default",
                "PHYS_RAM": "32161"
            },
            "host_data": {
                "HOSTNAME": "vhcalnplci.dummy.nodomain",
                "PORT": "8000"
            },
            "installed_components": {
                "TT_COMPTAB": [
                    {
                        "COMPONENT": "SAP_ABA",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "Cross-Application Component",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "SAP_BASIS",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "SAP Basis Component",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "SAP_BW",
                        "COMP_TYPE": "W",
                        "DESC_TEXT": "SAP Business Warehouse",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "SAP_GWFND",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "SAP Gateway Foundation",
                        "EXTRELEASE": "0000000002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "SAP_UI",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "User Interface Technology",
                        "EXTRELEASE": "0000000002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "ST-PI",
                        "COMP_TYPE": "X",
                        "DESC_TEXT": "SAP Solution Tools Plug-In",
                        "EXTRELEASE": "0006",
                        "LANGU": "E",
                        "RELEASE": "740"
                    }
                ]
            },
            "installed_components_ocs": {
                "ET_COMPLAYER": [
                    {
                        "COMP_TYPE": "S",
                        "LAYER_DESC": "NetWeaver Basis Components",
                        "LAYER_LVL": "01",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "X",
                        "LAYER_DESC": "NetWeaver PlugIns",
                        "LAYER_LVL": "02",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "W",
                        "LAYER_DESC": "NetWeaver Add-Ons",
                        "LAYER_LVL": "03",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "V",
                        "LAYER_DESC": "Application Platform Components",
                        "LAYER_LVL": "04",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "R",
                        "LAYER_DESC": "Application Components",
                        "LAYER_LVL": "05",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "P",
                        "LAYER_DESC": "Application PlugIns",
                        "LAYER_LVL": "06",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "O",
                        "LAYER_DESC": "Common Objects f. Application Extensions",
                        "LAYER_LVL": "07",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "N",
                        "LAYER_DESC": "Application Extensions",
                        "LAYER_LVL": "08",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "I",
                        "LAYER_DESC": "Industry Solutions - Layer 1",
                        "LAYER_LVL": "09",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "H",
                        "LAYER_DESC": "Industry Solutions - Layer 2",
                        "LAYER_LVL": "10",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "G",
                        "LAYER_DESC": "Industry Solutions - Layer 3",
                        "LAYER_LVL": "11",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "F",
                        "LAYER_DESC": "Industry Solutions - Layer 4",
                        "LAYER_LVL": "12",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "E",
                        "LAYER_DESC": "Industry Solutions - Layer 5",
                        "LAYER_LVL": "13",
                        "MODEL_ID": "0000000751"
                    },
                    {
                        "COMP_TYPE": "C",
                        "LAYER_DESC": "Projects",
                        "LAYER_LVL": "14",
                        "MODEL_ID": "0000000751"
                    }
                ],
                "ET_COMPONENTS": [
                    {
                        "ACTIVE": "X",
                        "COMPONENT": "SAP_BASIS",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "SAP Basis Component",
                        "INCMPL_STP": "",
                        "INCMPL_STPLVL": "0000",
                        "MAINT_TYPE": "S",
                        "MASTERCOMP": "",
                        "MASTERREL": "",
                        "PATCHABLE": "X",
                        "RELEASE": "751",
                        "SFW_STATUS": "N",
                        "SP": "SAPK-75102INSAPBASIS",
                        "SPP": "",
                        "SPP_LEVEL": "0000",
                        "SP_LEVEL": "0002",
                        "SUBCOMP_STATUS": ""
                    },
                    {
                        "ACTIVE": "X",
                        "COMPONENT": "SAP_ABA",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "Cross-Application Component",
                        "INCMPL_STP": "",
                        "INCMPL_STPLVL": "0000",
                        "MAINT_TYPE": "S",
                        "MASTERCOMP": "",
                        "MASTERREL": "",
                        "PATCHABLE": "X",
                        "RELEASE": "751",
                        "SFW_STATUS": "N",
                        "SP": "SAPK-75102INSAPABA",
                        "SPP": "",
                        "SPP_LEVEL": "0000",
                        "SP_LEVEL": "0002",
                        "SUBCOMP_STATUS": ""
                    },
                    {
                        "ACTIVE": "X",
                        "COMPONENT": "SAP_GWFND",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "SAP Gateway Foundation",
                        "INCMPL_STP": "",
                        "INCMPL_STPLVL": "0000",
                        "MAINT_TYPE": "P",
                        "MASTERCOMP": "",
                        "MASTERREL": "",
                        "PATCHABLE": "X",
                        "RELEASE": "751",
                        "SFW_STATUS": "N",
                        "SP": "SAPK-75102INSAPGWFND",
                        "SPP": "",
                        "SPP_LEVEL": "0000",
                        "SP_LEVEL": "0002",
                        "SUBCOMP_STATUS": ""
                    },
                    {
                        "ACTIVE": "X",
                        "COMPONENT": "SAP_UI",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "User Interface Technology",
                        "INCMPL_STP": "",
                        "INCMPL_STPLVL": "0000",
                        "MAINT_TYPE": "P",
                        "MASTERCOMP": "",
                        "MASTERREL": "",
                        "PATCHABLE": "X",
                        "RELEASE": "751",
                        "SFW_STATUS": "N",
                        "SP": "SAPK-75102INSAPUI",
                        "SPP": "",
                        "SPP_LEVEL": "0000",
                        "SP_LEVEL": "0002",
                        "SUBCOMP_STATUS": ""
                    },
                    {
                        "ACTIVE": "X",
                        "COMPONENT": "ST-PI",
                        "COMP_TYPE": "X",
                        "DESC_TEXT": "SAP Solution Tools Plug-In",
                        "INCMPL_STP": "",
                        "INCMPL_STPLVL": "0000",
                        "MAINT_TYPE": "S",
                        "MASTERCOMP": "",
                        "MASTERREL": "",
                        "PATCHABLE": "X",
                        "RELEASE": "740",
                        "SFW_STATUS": "N",
                        "SP": "SAPK-74006INSTPI",
                        "SPP": "",
                        "SPP_LEVEL": "0000",
                        "SP_LEVEL": "0006",
                        "SUBCOMP_STATUS": ""
                    },
                    {
                        "ACTIVE": "X",
                        "COMPONENT": "SAP_BW",
                        "COMP_TYPE": "W",
                        "DESC_TEXT": "SAP Business Warehouse",
                        "INCMPL_STP": "",
                        "INCMPL_STPLVL": "0000",
                        "MAINT_TYPE": "S",
                        "MASTERCOMP": "",
                        "MASTERREL": "",
                        "PATCHABLE": "X",
                        "RELEASE": "751",
                        "SFW_STATUS": "N",
                        "SP": "SAPK-75102INSAPBW",
                        "SPP": "",
                        "SPP_LEVEL": "0000",
                        "SP_LEVEL": "0002",
                        "SUBCOMP_STATUS": ""
                    }
                ],
                "ET_CPK": [],
                "ET_CVERS_SUB": [],
                "TT_COMPTAB": [
                    {
                        "COMPONENT": "SAP_BASIS",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "SAP Basis Component",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "SAP_ABA",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "Cross-Application Component",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "SAP_GWFND",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "SAP Gateway Foundation",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "SAP_UI",
                        "COMP_TYPE": "S",
                        "DESC_TEXT": "User Interface Technology",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    },
                    {
                        "COMPONENT": "ST-PI",
                        "COMP_TYPE": "X",
                        "DESC_TEXT": "SAP Solution Tools Plug-In",
                        "EXTRELEASE": "0006",
                        "LANGU": "E",
                        "RELEASE": "740"
                    },
                    {
                        "COMPONENT": "SAP_BW",
                        "COMP_TYPE": "W",
                        "DESC_TEXT": "SAP Business Warehouse",
                        "EXTRELEASE": "0002",
                        "LANGU": "E",
                        "RELEASE": "751"
                    }
                ]
            },
            "smlg_groups": {
                "GROUPS": [
                    {
                        "GROUPNAME": "PUBLIC"
                    }
                ]
            },
            "smlg_servers": {
                "INSTANCES": [
                    {
                        "APPLSERVER": "vhcalnplci_NPL_00"
                    }
                ]
            },
            "smlg_setup": {
                "ERFC_SETUP": [],
                "SETUP": [
                    {
                        "APPLSERVER": "vhcalnplci_NPL_00",
                        "CLASSNAME": "PUBLIC",
                        "GROUPTYPE": "",
                        "IPV6": "",
                        "IPV6_ADDRESS": "",
                        "IPV6_ADDRESS_OLD": "",
                        "IP_ADDRESS": "",
                        "IP_ADDRESS_OLD": "",
                        "OP_MODE": "",
                        "RESP_TIME": "000000",
                        "USERS": "0000",
                        "WP_QUOTA": 0
                    }
                ]
            },
            "software_components": {
                "ET_ACTIVE_BFUNCS": [],
                "ET_BSET_COMP_MAPPING": [],
                "ET_SFW_COMPS": []
            },
            "swproducts": {
                "ET_INCL_SWFEATURES": [
                    {
                        "DESCRIPT": "Application Server ABAP",
                        "ID": "1",
                        "MASTER_ID": "2",
                        "MASTER_PRD": "73555000100900000781",
                        "NAME": "NW AS ABAP INNOVATION PACKAGE",
                        "PROD_ID": "73555000100900000781",
                        "VENDOR": "sap.com",
                        "VERSION": "7.51"
                    }
                ],
                "ET_SWFEATURES": [
                    {
                        "DESCRIPT": "Application Server ABAP",
                        "ID": "1",
                        "NAME": "NW AS ABAP INNOVATION PACKAGE",
                        "PROD_ID": "73555000100900000781",
                        "VENDOR": "sap.com",
                        "VERSION": "7.51"
                    },
                    {
                        "DESCRIPT": "Basis Apps",
                        "ID": "2",
                        "NAME": "NW AS ABAP INNOVATION PACKAGE",
                        "PROD_ID": "73555000100900000781",
                        "VENDOR": "sap.com",
                        "VERSION": "7.51"
                    }
                ],
                "ET_SWPRODUCTS": [
                    {
                        "DESCRIPT": "NW AS ABAP 7.51 INNOVATION PKG",
                        "ID": "73555000100900000781",
                        "NAME": "NW AS ABAP INNOVATION PACKAGE",
                        "VENDOR": "sap.com",
                        "VERSION": "7.51"
                    }
                ],
                "ET_SWPROD_SPSTACK": [
                    {
                        "ID": "73555000103300002362",
                        "PROD_DESCR": "NW AS ABAP 7.51 INNOVATION PKG",
                        "PROD_ID": "73555000100900000781",
                        "PROD_NAME": "NW AS ABAP INNOVATION PACKAGE",
                        "PROD_VERSION": "7.51",
                        "STACK_CAPTION": "02 (05/2017)",
                        "VENDOR": "sap.com"
                    }
                ],
                "ET_TECH_USAGES": []
            }
        }
"""

from ansible_collections.sap.sap_operations.plugins.module_utils.abap import (  # pyright: ignore[reportMissingImports]
    AnsibleModuleABAP,
)


def main():
    module = AnsibleModuleABAP(argument_spec={}, supports_check_mode=True)

    with module as abap:
        swproducts = abap("OCS_GET_INSTALLED_SWPRODUCTS")
        software_components = abap("OCS_GET_SFW_COMPONENTS")
        # installed_components_ocs = abap("OCS_GET_INSTALLED_COMPS")
        host_data = abap("TH_GET_VIRT_HOST_DATA")
        installed_components = abap("DELIVERY_GET_INSTALLED_COMPS")
        smlg_groups = abap("SMLG_GET_DEFINED_GROUPS")
        smlg_servers = abap("SMLG_GET_DEFINED_SERVERS")
        smlg_setup = abap("SMLG_GET_SETUP")
        computer_info = abap("SLDAG_GET_COMPUTER_INFO")
        # /SDF/CMO_BUSINESS_FUNCTION
        # /SDF/ASR_GET_INFO - Get info for reading ASR data

    module.exit_json(
        changed=False,
        failed=False,
        abap_system_info=dict(
            swproducts=swproducts,
            host_data=host_data,
            installed_components=installed_components,
            smlg_groups=smlg_groups,
            smlg_servers=smlg_servers,
            smlg_setup=smlg_setup,
            computer_info=computer_info,
            software_components=software_components,
        ),
    )


if __name__ == "__main__":
    main()
