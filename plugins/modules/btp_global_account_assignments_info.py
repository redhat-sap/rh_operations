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
module: btp_global_account_assignments_info

extends_documentation_fragment:
  - sap.sap_operations.sap_btp_action_plugin
  - sap.sap_operations.community
  - sap.sap_operations.action_plugin

author:
  - Kirill Satarin (@kksat)

short_description: Fetches global account assignments information from SAP BTP.
version_added: 1.27.0
description:
  - This module fetches global account assignments information from SAP Business Technology Platform (BTP).
  - It can filter the results based on whether to include auto-managed plans and/or only entitled services.

options:
  include_auto_managed_plans:
    description:
      - Whether to include auto-managed plans in the fetched information.
    type: bool
    required: False
    default: True
  entitled_services_only:
    description:
      - Whether to fetch information for only those services that the account is entitled to.
    type: bool
    required: False
    default: True
"""

EXAMPLES = r"""
---
- name: Fetch global account assignments information including auto-managed plans and entitled services only
  sap.sap_operations.btp_global_account_info:
    include_auto_managed_plans: true
    entitled_services_only: true

- name: Fetch global account assignments information excluding auto-managed plans
  sap.sap_operations.btp_global_account_info:
    include_auto_managed_plans: false
    entitled_services_only: true

- name: Fetch global account assignments information for all services, including those not entitled
  sap.sap_operations.btp_global_account_info:
    include_auto_managed_plans: true
    entitled_services_only: false
"""
