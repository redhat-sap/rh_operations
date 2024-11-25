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
    include_auto_managed_plans: bool = True,
    entitled_services_only: bool = True,
) -> dict:
    btp_global_account_assignments_info, err = client.get_global_account_assignments(
        token=token,
        include_auto_managed_plans=include_auto_managed_plans,
        entitled_services_only=entitled_services_only,
    )
    if err is not None:
        return plugin_failed(
            err, msg="Could not get global account assignments information"
        )

    return {
        "failed": False,
        "changed": False,
        "btp_global_account_assignments_info": dict(
            btp_global_account_assignments_info
        ),
    }


class ActionModule(BTPActionModule):
    _VALID_ARGS = BTPActionModule._VALID_ARGS.union(
        [
            "include_auto_managed_plans",
            "entitled_services_only",
        ]
    )

    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)

        action_argument_spec = dict(
            include_auto_managed_plans=dict(type="bool", required=False, default=True),
            entitled_services_only=dict(type="bool", required=False, default=True),
        )
        argument_spec = dict(**btp_argument_spec, **action_argument_spec)
        self.validate_argument_spec(
            argument_spec=argument_spec, required_together=btp_required_together
        )
        include_auto_managed_plans = self._task.args.get("include_auto_managed_plans")
        entitled_services_only = self._task.args.get("entitled_services_only")

        return run_plugin(
            client=self.client,
            token=self.oauth_client.token,
            include_auto_managed_plans=include_auto_managed_plans,
            entitled_services_only=entitled_services_only,
        )
