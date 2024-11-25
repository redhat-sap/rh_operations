# -*- coding: utf-8 -*-
#
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


from ansible_collections.sap.sap_operations.plugins.action.btp_global_account_info import (
    BTPAccountsServiceClient,
    BTPActionModule,
    plugin_failed,
    btp_required_together,
    btp_argument_spec,
)


def run_plugin(
    client: BTPAccountsServiceClient,
    token: str,
    **kwargs,
) -> dict:
    description = kwargs.get("description")
    beta_enabled = kwargs.get("beta_enabled")
    display_name = kwargs.get("display_name")
    region = kwargs.get("region")
    subaccount_admins = kwargs.get("subaccount_admins")
    subdomain = kwargs.get("subdomain")

    btp_subaccounts_info, err = client.get_subaccounts(
        token=token,
    )
    if err is not None:
        return plugin_failed(err, msg="Could not get subaccounts")

    subaccount = None
    for subacc in btp_subaccounts_info:
        if subdomain == subacc.get("subdomain"):
            subaccount = subacc

    if subaccount is not None:
        return {"failed": False, "changed": False, "btp_subaccount": subaccount}

    btp_subaccount, err = client.create_subaccount(
        token=token,
        description=description,
        beta_enabled=beta_enabled,
        display_name=display_name,
        region=region,
        subaccount_admins=subaccount_admins,
        subdomain=subdomain,
    )
    if err is not None:
        return plugin_failed(err, msg="Could not get subaccounts")

    return {
        "failed": False,
        "changed": True,
        "btp_subaccount": dict(btp_subaccount),
    }


class ActionModule(BTPActionModule):
    _VALID_ARGS = BTPActionModule._VALID_ARGS.union(
        [
            "description",
            "beta_enabled",
            "display_name",
            "region",
            "subaccount_admins",
            "subdomain",
        ]
    )

    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)

        action_argument_spec = dict(
            description=dict(type="str", required=True),
            beta_enabled=dict(type="bool", default=True, required=False),
            display_name=dict(type="str", required=True),
            region=dict(type="str", required=True),
            subaccount_admins=dict(type="list", elements="str", required=True),
            subdomain=dict(type="str", required=True),
        )
        argument_spec = dict(**btp_argument_spec, **action_argument_spec)
        self.validate_argument_spec(
            argument_spec=argument_spec, required_together=btp_required_together
        )
        description = self._task.args.get("description")
        beta_enabled = self._task.args.get("beta_enabled")
        display_name = self._task.args.get("display_name")
        region = self._task.args.get("region")
        subaccount_admins = self._task.args.get("subaccount_admins")
        subdomain = self._task.args.get("subdomain")

        return run_plugin(
            client=self.client,
            token=self.oauth_client.token,
            description=description,
            beta_enabled=beta_enabled,
            display_name=display_name,
            region=region,
            subaccount_admins=subaccount_admins,
            subdomain=subdomain,
        )
