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


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
---
requirements:
  - "python >= 3.6"
  - cf CLI should be installed and available in PATH
author:
  - Kirill Satarin (@kksat)
options:
  username:
    description:
      - The username for authentication with the Cloud Foundry API.
      - This is SAP BTP user email address
    type: str
    required: false
  password:
    description:
      - The password for authentication with the Cloud Foundry API.
    type: str
    required: false
  api_endpoint:
    description:
      - The endpoint URL of the Cloud Foundry API.
    type: str
    required: false
"""
