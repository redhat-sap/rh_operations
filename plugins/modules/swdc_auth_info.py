#!/usr/bin/python
# -*- coding: utf-8 -*-

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

DOCUMENTATION = r"""
---
extends_documentation_fragment:
    - sap.sap_operations.community

module: swdc_auth_info

author:
  - Kirill Satarin (@kksat)

short_description: Fetch http requests headers to communicate with SAP software download center (SWDC)

description:
  - Fetch http requests headers to communicate with SAP software download center (SWDC)
  - Information is fetched from https://softwaredownloads.sap.com

version_added: 1.30.0

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
  url:
    description: URL to fetch headers for
    type: str
    required: true
"""

EXAMPLES = r"""
---
- name: Run swdc_auth_info
  sap.sap_operations.swdc_auth_info:
    username: "{{ lookup('ansible.builtin.env', 'LP_EMAIL') }}"
    password: "{{ lookup('ansible.builtin.env', 'LP_PASSWORD') }}"
    url: https://softwaredownloads.sap.com/file/0020000000098712022
"""

RETURN = r"""
---
swdc_auth_info:
  type: dict
  description:
    - List of dictionaries with information about download basket items
  returned: success
  sample:
    Accept: "*/*"
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Cookie: IDP_SESSION_MARKER_accounts=; IDP_USER=; JSESSIONID=; SESSIONID=; __HOST-IDP_J_COOKIE=; __HOST-XSRF_COOKIE=; __HOST-authIdentifierData=
    User-Agent: My User Agent 1.0
  contains:
    Accept:
      description: Accept header
      type: str
      sample: "*/*"
    Accept-Encoding:
      description: Accept-Encoding header
      type: str
      sample: gzip, deflate
    Connection:
      description: Connection header
      type: str
      sample: keep-alive
    Cookie:
      description: Cookie header
      type: str
      sample: IDP_SESSION_MARKER_accounts=; IDP_USER=; JSESSIONID=; SESSIONID=; __HOST-IDP_J_COOKIE=; __HOST-XSRF_COOKIE=; __HOST-authIdentifierData=
"""


from ansible_collections.sap.sap_operations.plugins.module_utils.me_auth import (
    me_AnsibleModule,
)

from ansible_collections.sap.sap_operations.plugins.module_utils.me_auth import (
    get_swdc_headers,
)


def run_module(module):

    url = module.params.get("url")
    password = module.params.get("password")
    username = module.params.get("username")
    swdc_auth_info = get_swdc_headers(url=url, username=username, password=password)
    return dict(
        changed=False,
        swdc_auth_info=swdc_auth_info,
    )


if __name__ == "__main__":
    module = me_AnsibleModule(
        argument_spec=dict(
            url=dict(type="str", required=True),
        ),
        supports_check_mode=True,
    )
    result = run_module(module)
    module.exit_json(**result)
