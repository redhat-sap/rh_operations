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
extends_documentation_fragment: sap.sap_operations.community

module: me_downloadbasket_info

author:
  - Kirill Satarin (@kksat)

short_description: Fetch information from SAP software center download basket

description:
  - Fetch the information from SAP software center download basket
  - Information is fetched from service https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadBasketItemSet?sap-language=en

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
    type: str
    required: true

"""  # noqa: E501

EXAMPLES = r"""
- name: Get information about SAP support portal download basket
  sap.sap_operations.me_downloadbasket_info:
    username: "S0000000000"
    password: "secret"
"""

RETURN = r"""
  me_downloadbasket_info:
    type: list
    elements: dict
    description:
      - List of dictionaries with information about download basket items
    returned: success
    sample:
      me_downloadbasket_info:
        - DirectDownloadUrl: https://softwaredownloads.sap.com/file/0030000001159172022
          EccnApproval: ''
          EccnExportLicense: ''
          ObjectBasket: DOWNLOAD
          ObjectChangedBy: S0023963562
          ObjectChangedOn: "/Date(1666506204000)/"
          ObjectDescription: SAP HANA Platform Edt. 2.0 SPS06 rev63 Linux x86_64
          ObjectErrorCode: 0
          ObjectExpirationDate:
          ObjectExportBlockFlag: false
          ObjectKey: '0030000001159172022'
          ObjectLocked: false
          ObjectName: 51055761.ZIP
          ObjectReferenceNumber: ''
          ObjectRegisteredOn: "/Date(1666506203000)/"
          ObjectSize: 14884077
          ObjectSizeUnit: KB
          ObjectStatus: 1
          ObjectStatusDescription: Available to download
          ObjectType: CD
          SoftwareEntitlementKey: ''
          __metadata:
            id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadBasketItemSet(ObjectKey='0030000001159172022',ObjectBasket='DOWNLOAD')
            type: SVT_SWDC_UI_SRV.DownloadBasketItem
            uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadBasketItemSet(ObjectKey='0030000001159172022',ObjectBasket='DOWNLOAD')
        - DirectDownloadUrl: https://softwaredownloads.sap.com/file/0010000000046522013
          EccnApproval: ''
          EccnExportLicense: ''
          ObjectBasket: DOWNLOAD
          ObjectChangedBy: S0023963562
          ObjectChangedOn: "/Date(1666506187000)/"
          ObjectDescription: Attribute Change Package 03 for RTCISM 100
          ObjectErrorCode: 0
          ObjectExpirationDate:
          ObjectExportBlockFlag: false
          ObjectKey: '0010000000046522013'
          ObjectLocked: false
          ObjectName: RTCISM100.SAR
          ObjectReferenceNumber: ''
          ObjectRegisteredOn: "/Date(1666506131000)/"
          ObjectSize: 4
          ObjectSizeUnit: KB
          ObjectStatus: 1
          ObjectStatusDescription: Available to download
          ObjectType: SPAT
          SoftwareEntitlementKey: ''
          __metadata:
            id: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadBasketItemSet(ObjectKey='0010000000046522013',ObjectBasket='DOWNLOAD')
            type: SVT_SWDC_UI_SRV.DownloadBasketItem
            uri: https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadBasketItemSet(ObjectKey='0010000000046522013',ObjectBasket='DOWNLOAD')


"""  # noqa: E501


from ansible_collections.sap.sap_operations.plugins.module_utils.me_auth import me_AnsibleModule  # noqa: E501
from ansible_collections.sap.sap_operations.plugins.module_utils.me_constants import DOWNLOAD_BASKET_SERVICE_URL  # noqa: E501


def main():

    module = me_AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    me_downloadbasket_info = module(url=DOWNLOAD_BASKET_SERVICE_URL)
    if me_downloadbasket_info.get("d") is None:
        module.fail_json(
            msg="Failed to fetch information from SAP software center download basket",  # noqa: E501
            response=me_downloadbasket_info,
        )
        if me_downloadbasket_info.get("d").get("results") is None:
            module.fail_json(
                msg="Failed to fetch information from SAP software center download basket",  # noqa: E501
                response=me_downloadbasket_info,
            )

    module.exit_json(
        changed=False,
        me_downloadbasket_info=me_downloadbasket_info["d"]["results"],
    )


if __name__ == "__main__":
    main()
