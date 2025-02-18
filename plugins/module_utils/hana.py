# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2024 Kirill Satarin (@kksat)
#
# Copyright 2024 Kirill Satarin (@kksat)
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

from ansible_collections.sap.sap_operations.plugins.module_utils.common import (  # noqa: E501
    convert_string2bool,
)
from ansible.module_utils.basic import AnsibleModule
from typing import List
from collections.abc import Callable

HANA_SYSTEM_REPLICATION_INFO_MAPPING = {
    "online": "online",
    "mode": "mode",
    "operation_mode": "operation mode",
    "site_id": "site id",
    "site_name": "site name",
    "is_source_system": "is source system",
    "is_secondary_consumer_system": "is secondary/consumer system",
    "has_secondaries_consumers_attached": "has secondaries/consumers attached",
    "is_takeover_active": "is a takeover active",
    "is_primary_suspended": "is primary suspended",
}


def get_hdbnsutil_run_command(module: AnsibleModule) -> Callable:
    def hdbnsutil_run_command(args: List[str]) -> tuple[int, str, str]:
        rc, stdout, stderr = module.run_command(["hdbnsutil"] + args)
        return rc, stdout, stderr

    return hdbnsutil_run_command


def get_hana_system_replication_info_from_stdout(stdout: str) -> dict:
    """Parses the stdout of the 'hdbnsutil -sr_state' command and returns a dictionary containing the license information.

    Args:
        stdout (str): The stdout

    Returns:
        dict: A dictionary containing the hana system replication configuration information
    """
    hana_system_replication_info = dict()
    for line in stdout.splitlines():
        for key, value in HANA_SYSTEM_REPLICATION_INFO_MAPPING.items():
            if value in line:
                hana_system_replication_info[key] = convert_string2bool(
                    line.split(":")[1].strip()
                )
    return hana_system_replication_info
