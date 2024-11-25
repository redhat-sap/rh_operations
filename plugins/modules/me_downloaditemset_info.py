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

DOCUMENTATION = """
module: me_downloaditemset_info

author:
  - Kirill Satarin (@kksat)

short_description: Fetch information from SAP software download center

description:
  - Fetch information from SAP software download center
  - Information is fetched from service https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet

version_added: 1.10.0

options:
  username:
    description:
      - I(username) of SAP support portal. Either universal id or suser.
    type: str
    required: true

  password:
    description:
      - I(password) of the I(username).
      - Will not be logged (no_log = True)
    type: str
    required: true

  enr:
    description:
      - ENR
    type: str

  alias:
    description:
      - Software alias.
    type: str
    choices:
      - sapcar
      - sapcar-7.53
      - sapcar-7.22
      - saphostagent
      - saphostagent-7.22
      - hana-server
      - hana-client
      - hana-cockpit
      - swpm-1.0
      - swpm-2.0
    required: true

  architecture:
    description:
      - Architecture
    type: str
    required: false
    choices:
      - x86_64
      - ppc64le
      - arm64
    default: x86_64

  os_family:
    description:
      - OS family
    type: str
    required: false
    choices:
      - Linux
      - Darwin
    default: Linux

"""  # noqa: E501

EXAMPLES = r"""
- name: Download item set information
  sap.sap_operations.me_downloaditemset_info:
    username: username
    password: pa$$word
    alias: saphostagent
    architecture: x86_64
    os_family: Linux
"""

RETURN = r"""
me_downloaditemset_info:
  description: Parameter values
  type: list
  elements: dict
  returned: success
  sample:
    - ApplicationLink: ''
      ChangeDate: "/Date(1699401600000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001345642023
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP62
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001345642023
      Fastkey: '0020000001345642023'
      Filename: 002/2023/0000000014/000000134564/001/SAPHOSTAGENT6
      Filesize: 78551
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822062 62
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '62'
      ReleaseDate: "/Date(1699401600000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT62_62-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001345642023')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001345642023')
    - ApplicationLink: ''
      ChangeDate: "/Date(1699401600000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001293762023
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001293762023
      Fastkey: '0020000001293762023'
      Filename: 002/2023/0000000013/000000129376/001/saphostagentr
      Filesize: 50876
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822062 62
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '62'
      ReleaseDate: "/Date(1699401600000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_62-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001293762023')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001293762023')
    - ApplicationLink: ''
      ChangeDate: "/Date(1689724800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000867792023
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP61
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000867792023
      Fastkey: '0020000000867792023'
      Filename: 002/2023/0000000009/000000086779/001/SAPHOSTAGENT6
      Filesize: 78228
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822061 61
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '61'
      ReleaseDate: "/Date(1689724800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT61_61-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000867792023')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000867792023')
    - ApplicationLink: ''
      ChangeDate: "/Date(1689724800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000776892023
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000776892023
      Fastkey: '0020000000776892023'
      Filename: 002/2023/0000000008/000000077689/001/saphostagentr
      Filesize: 50601
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822061 61
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '61'
      ReleaseDate: "/Date(1689724800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_61-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000776892023')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000776892023')
    - ApplicationLink: ''
      ChangeDate: "/Date(1680480000000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000406172023
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP60
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000406172023
      Fastkey: '0020000000406172023'
      Filename: 002/2023/0000000005/000000040617/001/SAPHOSTAGENT6
      Filesize: 78181
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822060 60
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '60'
      ReleaseDate: "/Date(1680480000000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT60_60-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000406172023')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000406172023')
    - ApplicationLink: ''
      ChangeDate: "/Date(1680480000000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000378462023
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000378462023
      Fastkey: '0020000000378462023'
      Filename: 002/2023/0000000004/000000037846/001/saphostagentr
      Filesize: 50570
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822060 60
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '60'
      ReleaseDate: "/Date(1680480000000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_60-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000378462023')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000378462023')
    - ApplicationLink: ''
      ChangeDate: "/Date(1673222400000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000021552023
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP59
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000021552023
      Fastkey: '0020000000021552023'
      Filename: 002/2023/0000000001/000000002155/001/SAPHOSTAGENT5
      Filesize: 78439
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822059 59
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '59'
      ReleaseDate: "/Date(1673222400000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT59_59-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000021552023')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000021552023')
    - ApplicationLink: ''
      ChangeDate: "/Date(1673222400000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001727602022
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001727602022
      Fastkey: '0020000001727602022'
      Filename: 002/2022/0000000018/000000172760/001/saphostagentr
      Filesize: 66383
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822059 59
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '59'
      ReleaseDate: "/Date(1673222400000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_59-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001727602022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001727602022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1665705600000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001370172022
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP58
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001370172022
      Fastkey: '0020000001370172022'
      Filename: 002/2022/0000000014/000000137017/001/SAPHOSTAGENT5
      Filesize: 78257
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822058 58
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '58'
      ReleaseDate: "/Date(1665705600000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT58_58-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001370172022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001370172022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1665705600000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001317142022
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001317142022
      Fastkey: '0020000001317142022'
      Filename: 002/2022/0000000014/000000131714/001/saphostagentr
      Filesize: 66361
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822058 58
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '58'
      ReleaseDate: "/Date(1665705600000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_58-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001317142022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001317142022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1659052800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000983272022
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP57
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000983272022
      Fastkey: '0020000000983272022'
      Filename: 002/2022/0000000010/000000098327/001/SAPHOSTAGENT5
      Filesize: 78025
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822057 57
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '57'
      ReleaseDate: "/Date(1659052800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT57_57-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000983272022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000983272022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1659052800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000974822022
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000974822022
      Fastkey: '0020000000974822022'
      Filename: 002/2022/0000000010/000000097482/001/saphostagentr
      Filesize: 66043
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822057 57
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '57'
      ReleaseDate: "/Date(1659052800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_57-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000974822022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000974822022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1651795200000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000591682022
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP56
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000591682022
      Fastkey: '0020000000591682022'
      Filename: 002/2022/0000000006/000000059168/001/SAPHOSTAGENT5
      Filesize: 77727
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822056 56
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '56'
      ReleaseDate: "/Date(1651795200000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT56_56-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000591682022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000591682022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1651795200000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000578012022
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000578012022
      Fastkey: '0020000000578012022'
      Filename: 002/2022/0000000006/000000057801/001/saphostagentr
      Filesize: 65964
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822056 56
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '56'
      ReleaseDate: "/Date(1651795200000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_56-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000578012022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000578012022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1645660800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000239812022
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP55
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000239812022
      Fastkey: '0020000000239812022'
      Filename: 002/2022/0000000003/000000023981/001/SAPHOSTAGENT5
      Filesize: 77513
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822055 55
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '55'
      ReleaseDate: "/Date(1645660800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT55_55-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000239812022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000239812022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1645660800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000208912022
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000208912022
      Fastkey: '0020000000208912022'
      Filename: 002/2022/0000000003/000000020891/001/saphostagentr
      Filesize: 65676
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822055 55
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '55'
      ReleaseDate: "/Date(1645660800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_55-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000208912022')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000208912022')
    - ApplicationLink: ''
      ChangeDate: "/Date(1635292800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001542872021
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP54
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001542872021
      Fastkey: '0020000001542872021'
      Filename: 002/2021/0000000016/000000154287/001/SAPHOSTAGENT5
      Filesize: 77248
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822054 54
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '54'
      ReleaseDate: "/Date(1635292800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT54_54-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001542872021')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001542872021')
    - ApplicationLink: ''
      ChangeDate: "/Date(1635292800000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001305892021
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001305892021
      Fastkey: '0020000001305892021'
      Filename: 002/2021/0000000014/000000130589/001/saphostagentr
      Filesize: 65368
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822054 54
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '54'
      ReleaseDate: "/Date(1635292800000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_54-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001305892021')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001305892021')
    - ApplicationLink: ''
      ChangeDate: "/Date(1629158400000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001179602021
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP53
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001179602021
      Fastkey: '0020000001179602021'
      Filename: 002/2021/0000000012/000000117960/001/SAPHOSTAGENT5
      Filesize: 77193
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822053 53
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '53'
      ReleaseDate: "/Date(1629158400000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT53_53-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001179602021')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001179602021')
    - ApplicationLink: ''
      ChangeDate: "/Date(1629158400000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000001175162021
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000001175162021
      Fastkey: '0020000001175162021'
      Filename: 002/2021/0000000012/000000117516/001/saphostagentr
      Filesize: 65358
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822053 53
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '53'
      ReleaseDate: "/Date(1629158400000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_53-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001175162021')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000001175162021')
    - ApplicationLink: ''
      ChangeDate: "/Date(1622160000000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000772502021
      DependenciesLink: ''
      Description: SAP HOST AGENT 7.22 SP52
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000772502021
      Fastkey: '0020000000772502021'
      Filename: 002/2021/0000000008/000000077250/001/SAPHOSTAGENT5
      Filesize: 87074
      InfoObjectLink: ''
      Infotype: SAR
      ObjectKey: 80004822052 52
      ObjectType: SP_B
      PackApplicationLink: ''
      PatchLevel: '52'
      ReleaseDate: "/Date(1622160000000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: SAPHOSTAGENT52_52-80004822.SAR
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000772502021')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000772502021')
    - ApplicationLink: ''
      ChangeDate: "/Date(1622160000000)/"
      ContentInfoLink: https://me.sap.com/softwarecenter/object/0020000000668012021
      DependenciesLink: ''
      Description: SAPHostAgent RPM Package
      DownloadDirectLink: https://softwaredownloads.sap.com/file/0020000000668012021
      Fastkey: '0020000000668012021'
      Filename: 002/2021/0000000007/000000066801/001/saphostagentr
      Filesize: 74756
      InfoObjectLink: ''
      Infotype: RPM
      ObjectKey: 80004822052 52
      ObjectType: PT_B
      PackApplicationLink: ''
      PatchLevel: '52'
      ReleaseDate: "/Date(1622160000000)/"
      SideEffectsLink: ''
      SoftwareEntitlementKey: ''
      Title: saphostagentrpm_52-80004822.rpm
      __metadata:
        id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000668012021')
        type: SVT_SWDC_UI_SRV.DownloadItem
        uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet('0020000000668012021')
"""  # noqa: E501


from ansible_collections.sap.sap_operations.plugins.module_utils.me_auth import (
    me_AnsibleModule,
)  # noqa: E501
from ansible_collections.sap.sap_operations.plugins.module_utils.me_helpers import (  # noqa: E501
    me_download_item_set_url,
    PECGRSC1_from_architecture_and_os_family,
    enr_from_alias,
)


def main():
    argument_spec = dict(
        enr=dict(type="str"),
        alias=dict(type="str", required=True, choices=list(enr_from_alias.keys())),
        architecture=dict(
            type="str", default="x86_64", choices=["x86_64", "ppc64le", "arm64"]
        ),
        os_family=dict(type="str", default="Linux", choices=["Linux", "Darwin"]),
    )
    required_one_of = [
        ("enr", "alias"),
    ]

    module = me_AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=required_one_of,
        supports_check_mode=True,
    )
    enr = module.params["enr"]
    alias = module.params["alias"]
    architecture = module.params["architecture"]
    os_family = module.params["os_family"]

    if not enr:
        enr = enr_from_alias.get(alias)
        if not enr:
            module.fail_json(
                msg="Alias {0} is not supported".format(alias),
            )

    url = me_download_item_set_url(
        ENR=enr,
        PECGRSC1=PECGRSC1_from_architecture_and_os_family[architecture][os_family],
    )

    response = module(url=url)

    if response.get("d") is None or response.get("d").get("results") is None:
        module.fail_json(
            msg="Failed to fetch information from SAP software download center",
            response=response,
        )

    me_downloaditemset_info = response["d"]["results"]
    for itemset in me_downloaditemset_info:
        if ("FileSize" not in itemset) and ("Filesize" in itemset):
            itemset["FileSize"] = itemset["Filesize"]

    module.exit_json(
        changed=False,
        me_downloaditemset_info=me_downloaditemset_info,
    )


if __name__ == "__main__":
    main()
