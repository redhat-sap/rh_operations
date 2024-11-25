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


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
---
description:
  - SAP start framework is used to collect information and perform actions from host level

author:
  - Kirill Satarin (@kksat)
  - Ondra Machacek (@machacekondra)

requirements:
  - python >= 3.6
  - pyrfc >= 2.7.0

options:
  username:
    description:
      - "I(username) of the OS user that will connect to SAP host agent web services (sapadm, or <sid>adm, or any other user with necessary permissions)"
      - Parameters I(username) I(password) and I(hostname) should be provided together.
    type: str
  password:
    description:
      - "I(password) of the OS user that will connect to SAP host agent web services (sapadm, or <sid>adm, or any other user with necessary permissions"
      - Parameters I(username) I(password) and I(hostname) should be provided together.
    type: str
  hostname:
    description:
      - "I(hostname) of the SAP system, will be used to connect to SAP host agent web services"
      - Parameters I(username) I(password) and I(hostname) should be provided together.
    type: str
  ca_file:
    description:
      - "I(ca_file) - path to file with CA certificate to secure the communication. if not provided system CA store is used."
      - "Required if I(security) is set to C(custom)"
    type: path
  security:
    description:
      - Parameter I(security) specifies how secure communication should be enforced.
      - By default system CA (certification authority) store is used (parameter value is C(system)).
      - If custom CA (certification authority) has to be used, parameter I(ca_file) should be set to path to CA public certificate.
      - If set to C(none) https communication is possible, but server certificate will not be checked for trust.
    choices: ['system', 'custom', 'none']
    default: system
    type: str
  """
