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

ME_DOWNLOAD_ITEM_SET_SERVICE_URL = (
    "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet"  # noqa: E501
)


def me_download_item_set_url(
    ENR,
    PECGRSC1,
    skip=0,
    top=500,
    _EVENT="LIST",
    EVENT="LIST",
    SWTYPSC="SPP",
    PECCLSC="OS",
    INCL_PECCLSC1="OS",
    V="MAINT",
    TA="ACTUAL",
    PARTNR=None,
    inlinecount="allpages",
    sap_language="en-US",
):
    url = ME_DOWNLOAD_ITEM_SET_SERVICE_URL
    url += "?$skip={}".format(skip)
    url += "&$top={}".format(top)
    url += "&_EVENT={}".format(_EVENT)
    url += "&EVENT={}".format(EVENT)
    url += "&ENR={}".format(ENR)
    url += "&SWTYPSC={}".format(SWTYPSC)
    url += "&PECCLSC={}".format(PECCLSC)
    url += "&INCL_PECCLSC1={}".format(INCL_PECCLSC1)
    url += "&PECGRSC1={}".format(PECGRSC1)
    url += "&V={}".format(V)
    url += "&TA={}".format(TA)
    if PARTNR is not None:
        url += "&PARTNR={}".format(PARTNR)
    url += "&$inlinecount={}".format(inlinecount)
    url += "&sap-language={}".format(sap_language)
    return url


enr_from_alias = {
    "sapcar": "73555000100200018637",
    "sapcar-7.53": "73555000100200018637",
    "sapcar-7.22": "73555000100200014919",
    "saphostagent": "73554900100200011934",
    "saphostagent-7.22": "73554900100200011934",
    # 'hana-platform':    'https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/DownloadItemSet?$skip=0&$top=500&_EVENT=LIST&EVENT=LIST&ENR=73554900100900001301&SWTYPSC=N&PECCLSC=NONE&V=INST&TA=ACTUAL&$inlinecount=allpages&sap-language=en-US',  # noqa: E501
    "hana-server": "73554900100200005327",
    "hana-client": "73554900100200005390",
    "hana-cockpit": "73555000100200005745",
    "swpm-1.0": "67838200100200018544",
    "swpm-2.0": "73555000100200007684",
}

PECGRSC1_from_architecture_and_os_family = {
    "x86_64": {
        "Linux": "LINUX_X64",
        "Darwin": "MACOSX_64",
    },
    "ppc64le": {
        "Linux": "LINPPC64LE",
    },
    "arm64": {
        "Darwin": "MACOSARM64",
        "Linux": "MACOSARM64",
    },
    # 'AIX_64': 'AIX_64',
    # 'HPIA_64': 'HPIA_64',
    # 'LINUXARM64': 'LINUXARM64',
    # 'LINUXPPC64': 'LINUXPPC64',
    # 'LINPPC64LE': 'LINPPC64LE',
    # 'LINUX_X64': 'LINUX_X64',
    # 'S390X_64': 'S390X_64', ## Linux on IBM Z
    # 'MACOSX_64': 'MACOSX_64',
    # 'MACOSARM64': 'MACOSARM64',
    # 'OS400': 'OS400',
    # 'SOLARIS_64': 'SOLARIS_64', # Solaris on SPARC
    # 'SOLARISX64': 'SOLARISX64', ## Solaris on Intel 64-bit
    # 'NT_X64': 'NT_X64', ## Windows on Intel 64-bit
    # 'OS390_64': 'OS390_64', ## z/OS on IBM Z
}
