#!/usr/bin/python
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
    passwd: "SecretPa$$word" # notsecret
    sysnr: '00'
"""

RETURN = r"""
abap_system_info:
  description: ABAP system info
  type: dict
  returned: success
  contains:
    computer_info:
      description: Computer info
      type: dict
      contains:
        IP_ADDRESS:
            description: IP address
            type: str
            sample: 10.0.0.234
        IP_ADDRESSES:
            description: List of IP addresses
            type: list
            elements: dict
            sample:
                - VALUE: 127.0.0.1
                - VALUE: 10.0.0.234
            contains:
                VALUE:
                    description: IP address
                    type: str
        LOCALHOST:
            description: Local hostname
            type: str
            sample: vhcalnplci
        LOCALHOSTFULL:
            description: Local FQDN
            type: str
            sample: vhcalnplci.dummy.nodomain
        OPSYS:
            description: operating system
            type: str
            sample: Linux
        OPSYS_BITS:
            description: Operating system bits
            type: str
            sample: ""
        OPSYS_RELEASE:
            description: Operating system release
            type: str
            sample: 4.12.14-197.102-default
        PHYS_RAM:
            description: Physical RAM in MB
            type: str
            sample: "32161"
    host_data:
        description: Host data
        type: dict
        contains:
            HOSTNAME:
                description: Hostname
                type: str
                sample: vhcalnplci.dummy.nodomain
            PORT:
                description: Port configured for web services
                type: str
                sample: "8000"
    installed_components:
        description: Installed components
        type: dict
        contains:
          TT_COMPTAB:
            description: Installed components
            type: list
            elements: dict
            sample:
              - COMPONENT: SAP_BASIS
                COMP_TYPE: S
                DESC_TEXT: SAP Basis Component
                EXTRELEASE: "0002"
                LANGU: E
                RELEASE: "751"
              - COMPONENT: SAP_BW
                COMP_TYPE: W
                DESC_TEXT: SAP Business Warehouse
                EXTRELEASE: "0002"
                LANGU: E
                RELEASE: "751"
              - COMPONENT: SAP_GWFND
                COMP_TYPE: S
                DESC_TEXT: SAP Gateway Foundation
                EXTRELEASE: "0000000002"
                LANGU: E
                RELEASE: "751"
            contains:
                COMPONENT:
                    description: Component code
                    type: str
                    sample: SAP_ABA
                COMP_TYPE:
                    description: Component type
                    type: str
                    sample: S
                DESC_TEXT:
                    description: Component description
                    type: str
                    sample: Cross-Application Component
                EXTRELEASE:
                    description: Component release SP level
                    type: str
                    sample: "0002"
                LANGU:
                    description: Language
                    type: str
                    sample: E
                RELEASE:
                    description: Component release
                    type: str
                    sample: "751"
    installed_components_ocs:
        description: Installed components
        type: dict
        contains:
            ET_COMPLAYER:
                description: Component layers
                type: list
                elements: dict
                sample:
                  - COMP_TYPE: S
                    LAYER_DESC: NetWeaver Basis Components
                    LAYER_LVL: "01"
                    MODEL_ID: "0000000751"
                  - COMP_TYPE: X
                    LAYER_DESC: NetWeaver PlugIns
                    LAYER_LVL: "02"
                    MODEL_ID: "0000000751"
                  - COMP_TYPE: W
                    LAYER_DESC: NetWeaver Add-Ons
                    LAYER_LVL: "03"
                    MODEL_ID: "0000000751"
                contains:
                    COMP_TYPE:
                        description: Component type
                        type: str
                        sample:
                            - V
                            - R
                            - P
                            - X
                            - W
                    LAYER_DESC:
                        description: Layer description
                        type: str
                        sample: Application Platform Components
                    LAYER_LVL:
                        description: Layer level
                        type: str
                        sample: "04"
                    MODEL_ID:
                        description: Model ID
                        type: str
                        sample: "0000000751"
            ET_COMPONENTS:
                description: Installed components
                type: list
                elements: dict
                sample:
                  - ACTIVE: X
                    COMPONENT: SAP_BASIS
                    COMP_TYPE: S
                    DESC_TEXT: SAP Basis Component
                    INCMPL_STP: ""
                    INCMPL_STPLVL: "0000"
                    MAINT_TYPE: S
                    MASTERCOMP: ""
                    MASTERREL: ""
                    PATCHABLE: X
                    RELEASE: "751"
                    SFW_STATUS: N
                    SP: SAPK-75102INSAPBASIS
                    SPP: ""
                    SPP_LEVEL: "0000"
                    SP_LEVEL: "0002"
                    SUBCOMP_STATUS: ""
                  - ACTIVE: X
                    COMPONENT: SAP_ABA
                    COMP_TYPE: S
                    DESC_TEXT: Cross-Application Component
                    INCMPL_STP: ""
                    INCMPL_STPLVL: "0000"
                    MAINT_TYPE: S
                    MASTERCOMP: ""
                    MASTERREL: ""
                    PATCHABLE: X
                    RELEASE: "751"
                    SFW_STATUS: N
                    SP: SAPK-75102INSAPABA
                    SPP: ""
                    SPP_LEVEL: "0000"
                    SP_LEVEL: "0002"
                    SUBCOMP_STATUS: ""
                contains:
                    ACTIVE:
                        description: Active flag
                        type: str
                        sample: X
                    COMPONENT:
                        description: Component code
                        type: str
                        sample: SAP_GWFND
                    COMP_TYPE:
                        description: Component type
                        type: str
                        sample: S
                    DESC_TEXT:
                        description: Component text description
                        type: str
                        sample: SAP Gateway Foundation
                    INCMPL_STP:
                        description: Service pack text description
                        type: str
                        sample: ""
                    INCMPL_STPLVL:
                        description: Service pack level
                        type: str
                        sample: "0000"
                    MAINT_TYPE:
                        description: Maintenance type
                        type: str
                        sample: P
                    MASTERCOMP:
                        description: Master component
                        type: str
                        sample: ""
                    MASTERREL:
                        description: Master release
                        type: str
                        sample: ""
                    PATCHABLE:
                        description: Patchable
                        type: str
                        sample: X
                    RELEASE:
                        description: Release
                        type: str
                        sample: "751"
                    SFW_STATUS:
                        description: Software status
                        type: str
                        sample: N
                    SP:
                        description: Service pack
                        type: str
                        sample: SAPK-75102INSAPGWFND
                    SPP:
                        description: Software patch
                        type: str
                        sample: ""
                    SPP_LEVEL:
                        description: Software patch
                        type: str
                        sample: "0000"
                    SP_LEVEL:
                        description: Software level
                        type: str
                        sample: "0002"
                    SUBCOMP_STATUS:
                        description: Subcomponent status
                        type: str
                        sample: ""
            ET_CPK:
                description: Components table
                type: list
                elements: dict
                sample: []
            ET_CVERS_SUB:
                description: Versions table
                type: list
                elements: dict
                sample: []
            TT_COMPTAB:
                description: List of components
                type: list
                elements: dict
                sample:
                      - COMPONENT: SAP_BASIS
                        COMP_TYPE: S
                        DESC_TEXT: SAP Basis Component
                        EXTRELEASE: "0002"
                        LANGU: E
                        RELEASE: "751"
                      - COMPONENT: SAP_ABA
                        COMP_TYPE: S
                        DESC_TEXT: Cross-Application Component
                        EXTRELEASE: "0002"
                        LANGU: E
                        RELEASE: "751"
                      - COMPONENT: SAP_GWFND
                        COMP_TYPE: S
                        DESC_TEXT: SAP Gateway Foundation
                        EXTRELEASE: "0002"
                        LANGU: E
                        RELEASE: "751"
                contains:
                    COMPONENT:
                        description: Component
                        type: str
                        sample: SAP_UI
                    COMP_TYPE:
                        description: Component type
                        type: str
                        sample: S
                    DESC_TEXT:
                        description: Description text
                        type: str
                        sample: User Interface Technology
                    EXTRELEASE:
                        description: External release
                        type: str
                        sample: "0002"
                    LANGU:
                        description: Language
                        type: str
                        sample: E
                    RELEASE:
                        description: Release
                        type: str
                        sample: "751"
    smlg_groups:
      description: SMLG groups
      type: dict
      sample:
        GROUPS:
            - GROUPNAME: PUBLIC
    smlg_servers:
        description: SMLG servers
        type: dict
        sample:
            INSTANCES:
                - APPLSERVER: vhcalnplci_NPL_00
    smlg_setup:
        description: SMLG setup
        type: dict
        sample:
            ERFC_SETUP: []
            SETUP:
                  - APPLSERVER: vhcalnplci_NPL_00
                    CLASSNAME: PUBLIC
                    GROUPTYPE: ""
                    IPV6: ""
                    IPV6_ADDRESS: ""
                    IPV6_ADDRESS_OLD: ""
                    IP_ADDRESS: ""
                    IP_ADDRESS_OLD: ""
                    OP_MODE: ""
                    RESP_TIME: "000000"
                    USERS: "0000"
                    WP_QUOTA: 0
    software_components:
        description: Software components
        type: dict
        sample:
            ET_ACTIVE_BFUNCS: []
            ET_BSET_COMP_MAPPING: []
            ET_SFW_COMPS: []
    swproducts:
        description: Software products
        type: dict
        sample:
            ET_INCL_SWFEATURES:
              - DESCRIPT: Application Server ABAP
                ID: "1"
                MASTER_ID: "2"
                MASTER_PRD: "73555000100900000781"
                NAME: NW AS ABAP INNOVATION PACKAGE
                PROD_ID: "73555000100900000781"
                VENDOR: sap.com
                VERSION: "7.51"
            ET_SWFEATURES:
              - DESCRIPT: Application Server ABAP
                ID: "1"
                NAME: NW AS ABAP INNOVATION PACKAGE
                PROD_ID: "73555000100900000781"
                VENDOR: sap.com
                VERSION: "7.51"
              - DESCRIPT: Basis Apps
                ID: "2"
                NAME: NW AS ABAP INNOVATION PACKAGE
                PROD_ID: "73555000100900000781"
                VENDOR: sap.com
                VERSION: "7.51"
            ET_SWPRODUCTS:
              - DESCRIPT: NW AS ABAP 7.51 INNOVATION PKG
                ID: "73555000100900000781"
                NAME: NW AS ABAP INNOVATION PACKAGE
                VENDOR: sap.com
                VERSION: "7.51"
            ET_SWPROD_SPSTACK:
                  - ID: "73555000103300002362"
                    PROD_DESCR: NW AS ABAP 7.51 INNOVATION PKG
                    PROD_ID: "73555000100900000781"
                    PROD_NAME: NW AS ABAP INNOVATION PACKAGE
                    PROD_VERSION: "7.51"
                    STACK_CAPTION: 02 (05/2017)
                    VENDOR: sap.com
            ET_TECH_USAGES: []
"""

from ansible_collections.sap.sap_operations.plugins.module_utils.abap import (
    AnsibleModuleABAP,
)


def main():
    module = AnsibleModuleABAP(argument_spec={}, supports_check_mode=True)

    with module as abap:
        swproducts = abap("OCS_GET_INSTALLED_SWPRODUCTS")
        software_components = abap("OCS_GET_SFW_COMPONENTS")
        host_data = abap("TH_GET_VIRT_HOST_DATA")
        installed_components = abap("DELIVERY_GET_INSTALLED_COMPS")
        smlg_groups = abap("SMLG_GET_DEFINED_GROUPS")
        smlg_servers = abap("SMLG_GET_DEFINED_SERVERS")
        smlg_setup = abap("SMLG_GET_SETUP")
        computer_info = abap("SLDAG_GET_COMPUTER_INFO")

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
