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
module: me_file_info

author:
  - Ondra Machacek (@machacekondra)
  - Kirill Satarin (@kksat)

short_description: File information

description:
  - Fetch the info about file from SAP download center
  - Information is fetched from service https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet.
    See for example https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')

version_added: 1.10.0

options:
  username:
    description:
      - I(username) of SAP support portal. Either universal id or suser.
    type: str
    required: True
  password:
    description:
      - I(password) of the I(username).
    type: str
    required: True
  file_id:
    description:
      - File id to fetch the info.
    type: str
    required: True

"""  # noqa: E501


EXAMPLES = r"""
- name: Fetch info about the file
  me_file_info:
    username: "S0000000000"
    password: "secret"
    file_id: "0030000000103162022"
"""

RETURN = r"""
file_info:
    description: File values
    type: dict
    returned: always
    sample: {
        'ChangedBy': '',
        'ChangedByName': '',
        'ChangedOn': '/Date(1644323565000)/',
        'Checksum': '035167426426e53cadc2112761134fdde66be1033f9f0117966b0b9ad5ea0a97',
        'ComponentRelease': '',
        'CreatedBy': '',
        'CreatedByName': '',
        'CreatedOn': '/Date(1643310038000)/',
        'EpsFileName': '',
        'FileName': '51055299.ZIP',
        'FileSize': '14975391 ',
        'FileType': 'ZIP',
        'FileVersion': '003',
        'InfoMimeType': '',
        'InfoText': '',
        'InfoXml': '',
        'IsAbapObject': False,
        'IsContentInfoAvailable': False,
        'IsFcmsViewAvailable': False,
        'IsSupportPackage': False,
        'MinimalBasisRelease': '',
        'ObjectAttributes': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectAttributes"}},
        'ObjectConditions': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectConditions"}},
        'ObjectKey': '0030000000103162022',
        'ObjectList': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectList"}},
        'ObjectProperties': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectProperties"}},
        'ObjectSAPNotes': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectSAPNotes"}},
        'ObjectSAPNotesCategoryFilter': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectSAPNotesCategoryFilter"}},
        'ObjectSAPNotesComponentFilter': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectSAPNotesComponentFilter"}},
        'ObjectSAPNotesCountryFilter': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectSAPNotesCountryFilter"}},
        'ObjectSAPNotesPriorityFilter': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectSAPNotesPriorityFilter"}},
        'ObjectSideEffects': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectSideEffects"}},
        'ObjectSourcePackages': {'__deferred': {'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')/ObjectSourcePackages"}},
        'PackageLevel': '',
        'PatchType': '',
        'RequiredSpamVersion': '',
        'Responsible': '',
        'ResponsibleName': '',
        'Status': 'AVAILABLE',
        'StatusDescr': 'The File is available to download',
        'Title': 'SAP HANA Platform Edt. 2.0 SPS05 rev57 Linux x86_64',
        '__metadata': {'id': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')",
                      'type': 'SVT_SWDC_UI_SRV.Object',
                      'uri': "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('0030000000103162022')"}
    }
"""  # noqa: E501


from ansible_collections.sap.sap_operations.plugins.module_utils.me_auth import (
    me_AnsibleModule,
)  # noqa: E501


def main():
    argument_spec = dict(
        file_id=dict(type="str", required=True),
    )

    module = me_AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    file_id = module.params.get("file_id")

    url = "https://launchpad.support.sap.com/services/odata/svt/swdcuisrv/ObjectSet('{0}')".format(
        file_id
    )  # noqa: E501

    response = module(url=url)

    if response.get("d") is None:
        module.fail_json(
            msg="Failed to fetch information from SAP software download center",  # noqa: E501
            response=response,
        )

    module.exit_json(
        changed=False,
        me_file_info=response["d"],
    )


if __name__ == "__main__":
    main()
