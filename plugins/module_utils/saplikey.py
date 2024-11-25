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


import os
from ansible.module_utils.basic import AnsibleModule


from ansible_collections.sap.sap_operations.plugins.module_utils.compat import (  # noqa: E501
    dict_union,
)


__metaclass__ = type
SAPLIKEY_GET_MAPPING = {
    "system_id": "System ID",
    "hardware_key": "Hardware Key",
    "installation_number": "Installation No",
    "system_number": "System No",
    "release": "Release",
    "software_products": "Software products",
}

SAPLIKEY_SHOW_MAPPING = {
    "system_id": ["System", "SAPSYSTEM"],
    "hardware_key": ["Hardware Key", "HARDWARE-KEY"],
    "software_product": ["Software Product", "SWPRODUCTNAME"],
    "validity": ["Validity"],
    "installation_number": ["Installation Number", "INSTNO"],
    "system_number": ["System Number", "SYSTEM-NR"],
    "begin_of_validity": ["Begin of Validity", "BEGIN"],
    "end_of_validity": ["End of Validity", "End   of Validity", "EXPIRATION"],
    "last_successful_check": ["Last successful check"],
    "type_of_license_key": ["Type of License Key"],
    "software_product_limit": ["Software Product Limit", "SWPRODUCTLIMIT"],
    "license_key": ["LKEY"],
}


class AnsibleModule_saplikey(AnsibleModule):
    def __init__(
        self,
        argument_spec,
        bypass_checks=False,
        no_log=False,
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        add_file_common_args=False,
        supports_check_mode=False,
        required_if=None,
        required_by=None,
    ):
        """Extends AnsibleModule with saplikey specific functionality."""
        argument_spec_saplikey = dict(
            profile=dict(type="path", required=False, default="DEFAULT.PFL"),
        )

        AnsibleModule(
            argument_spec=dict_union(argument_spec, argument_spec_saplikey),
            bypass_checks=bypass_checks,
            no_log=no_log,
            mutually_exclusive=mutually_exclusive,
            required_together=required_together,
            required_one_of=required_one_of,
            add_file_common_args=add_file_common_args,
            supports_check_mode=supports_check_mode,
            required_if=required_if,
            required_by=required_by,
        )

    def run_saplikey_command(
        self,
        args,
        check_rc=True,
    ):
        """Runs the saplikey command."""
        self.fail_if_environment_not_set()
        SAPSYSTEMNAME = os.getenv("SAPSYSTEMNAME")

        return self.run_command(
            ["saplikey", "pf={}".format(self.params.get("profile"))] + args,
            check_rc=check_rc,
            cwd="/sapmnt/{0}/profile".format(SAPSYSTEMNAME),
        )

    def fail_if_environment_not_set(self):
        SAPSYSTEMNAME = os.getenv("SAPSYSTEMNAME")
        if not SAPSYSTEMNAME:
            self.fail_json(
                msg="""SAPSYSTEMNAME environment variable is not set.
                Please make sure you are running this module on a host, \
                Where SAP instance is installed and \
                SAP environment variables are set.
                Module should be run as:
                become: true
                become_user: <SID>adm
                become_flags: '-i'"""
            )
        profile = self.params.get("profile")
        if not os.path.isfile("/sapmnt/{0}/profile/{1}".format(SAPSYSTEMNAME, profile)):  # noqa: E501
            self.fail_json(
                msg="Profile does not exist.",
                profile=profile,
            )


def get_saplikey_get_info_from_stdout(stdout):
    """Parses the stdout of the 'saplikey -get' command.

    Parses the stdout of the 'saplikey -get' command
    and returns a dictionary containing the license information.

    Args:
        stdout (str): The stdout of the 'saplikey -get' command.

    Returns:
        dict: A dictionary containing the license information parsed from the stdout.
    """  # noqa: E501
    saplikey_get_info = dict()
    for line in stdout.splitlines():
        for key, value in SAPLIKEY_GET_MAPPING.items():
            if value in line:
                saplikey_get_info[key] = line.split(":")[1].strip()
                if key == "hardware_key":
                    saplikey_get_info[key] = saplikey_get_info[key].split(" ")[0]  # noqa: E501
    return saplikey_get_info


def get_license_keys_from_stdout(stdout):
    # Split the text into individual license key sections
    for section_separator in ["----- Begin SAP License -----", "License Key:"]:
        if section_separator in stdout:
            license_section_separator = section_separator
    # Initialize an empty list to store the parsed license keys
    license_key_sections = stdout.split(license_section_separator)
    license_value_separator = {
        "----- Begin SAP License -----": "=",
        "License Key:": ":",
    }[license_section_separator]
    license_keys = []
    # Loop through each license key section
    for section in license_key_sections:
        # Split the section into individual lines
        lines = section.strip().split("\n")
        # Initialize an empty dictionary to store the parsed license key
        license_key = {}
        # Loop through each line in the section
        for line in lines:
            for key, value in SAPLIKEY_SHOW_MAPPING.items():
                if line.split(license_value_separator)[0].strip() in value:
                    license_key[key] = line.split(license_value_separator)[-1].strip()  # noqa: E501
        # Add the parsed license key to the list of license keys
        if license_key:
            license_keys.append(license_key)
    return license_keys
