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


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
description:
  - This is ansible action plugin, this means it will run on ansible controller, not on managed node.
  - This plugin does not support running with python 2. It requires python 3.6 or higher.
  - This action plugin is using SAP BTP API, see <api.sap.com> for more details.

author:
  - Kirill Satarin (@kksat)

requirements:
  - python >= 3.6
  - requests
  - oauth2_client

seealso:
  - name: SAP BTP API Accounts service API
    description: SAP BTP API Accounts service API
    link: https://api.sap.com/api/APIAccountsService/overview

  - name: Administration and operations section for SAP BTP on help.sap.com
    description: Administration and operations section for SAP BTP on help.sap.com
    link: https://help.sap.com/docs/btp/sap-business-technology-platform/btp-administration-and-operations

options:
  login:
    description: Login to use for authentication. This is usually an email address.
    type: str
    required: true

  password:
    description: Password to use for authentication.
    type: str
    required: true

  api_endpoint:
    description: API endpoint to use. For example C(https://api.cf.eu10.hana.ondemand.com)
    type: str
    required: true

  client_id:
    description: Client ID to use for authentication.
    type: str
    required: true

  client_secret:
    description: Client secret to use for authentication.
    type: str
    required: true

  authorize_service_url:
    description: URL of the authorization service.
    type: str
    required: true

  token_service_url:
    description: URL of the token service.
    type: str
    required: true

"""
