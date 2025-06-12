# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2025 Kirill Satarin (@kksat)
#
# Copyright 2025 Kirill Satarin (@kksat)
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
from ansible.utils.display import Display

__metaclass__ = type


def valid_hostname(
    value, le: int = 13, ge: int = 1, all_lowercase: bool = True
) -> bool:
    """Check if the provided value is a valid SAP hostname as per SAP note 611361.

    :param value: The hostname to validate.
    :return: True if valid, False otherwise.
    """
    if not isinstance(value, str):
        Display().display(
            f"sap.sap_operations.valid_hostname value={value} is not a string"
        )
        return False

    # Check length
    if len(value) < ge or len(value) > le:
        Display().display(
            f"sap.sap_operations.valid_hostname value={value} is longer than {le} or shorter than {ge} characters"
        )
        return False

    # Only allowed non alphanumeric character is '-'
    if not value.replace("-", "").isalnum():
        Display().display(f"sap.sap_operations.valid_hostname value={value} not only contains alphanumeric characters and '-'")
        return False

    # First character must be a character
    if not value[0].isalpha():
        Display().display(f"sap.sap_operations.valid_hostname value={value} first character is not a letter")
        return False

    # Last character must be alphanumeric
    if not value[-1].isalnum():
        Display().display(f"sap.sap_operations.valid_hostname value={value} last character is not alphanumeric")
        return False

    # Hostname should be in lowercase by default
    if all_lowercase and not value.islower():
        Display().display(f"sap.sap_operations.valid_hostname value={value} is not all lowercase")
        return False

    return True


def valid_fqdn(value, le: int = 63) -> bool:
    return (len(value) < 254) and all(
        valid_hostname(hostname, le=le) for hostname in value.split(".")
    )
