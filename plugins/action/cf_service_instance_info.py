# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2024 Red Hat, Project Atmosphere
#
# Copyright 2024 Red Hat, Project Atmosphere
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
import tempfile
from ansible.errors import AnsibleActionFail

__metaclass__ = type
import json
from ansible.plugins.action import ActionBase

from ansible_collections.sap.sap_operations.plugins.action.cf_marketplace_info import (
    CFClient,
)


def run_action(client: CFClient, name: str = "", guid: str = "") -> dict:

    rc = client.authenticate()
    if rc.get("failed"):
        return rc

    rc, stdout, stderr = client.run_method(
        path="/v3/service_instances",
        method="GET",
        headers={},
        data={},
    )

    if rc or stderr:
        return {"failed": True, "msg": stdout}

    service_instances = json.loads(stdout)

    if "errors" in service_instances:
        return {
            "failed": True,
            "msg": "Error retrieving service instances",
            "errors": service_instances["errors"],
        }
    for service_instance in service_instances["resources"]:
        if name and service_instance["name"] == name:
            return dict(
                failed=False,
                changed=False,
                cf_service_instance_info=service_instance,
            )
        if guid and service_instance["guid"] == guid:
            return dict(
                failed=False,
                changed=False,
                cf_service_instance_info=service_instance,
            )

    return dict(
        failed=True,
        msg="Service instance not found",
    )


class CFServiceInstanceInfoModule(ActionBase):
    _VALID_ARGS = frozenset(["username", "password", "api_endpoint", "name", "guid"])
    argument_spec = dict(
        username=dict(type="str", required=False),
        password=dict(type="str", required=False),
        api_endpoint=dict(type="str", required=False),
        name=dict(type="str", required=False),
        guid=dict(type="str", required=False),
    )
    required_together = [
        [
            "username",
            "password",
            "api_endpoint",
        ],
    ]
    mutually_exclusive = [["name", "guid"]]
    required_one_of = [
        [
            "username",
            "password",
            "api_endpoint",
        ],
        ["name", "guid"],
    ]

    def __init__(
        self, task, connection, play_context, loader, templar, shared_loader_obj
    ):
        """Initialize action module."""
        super().__init__(
            task, connection, play_context, loader, templar, shared_loader_obj
        )

    def run(self, tmp=None, task_vars=None):
        validation_results, _ignore = self.validate_argument_spec(
            argument_spec=self.argument_spec,
            required_together=self.required_together,
            mutually_exclusive=self.mutually_exclusive,
            required_one_of=self.required_one_of,
        )

        if validation_results.error_messages:
            raise AnsibleActionFail(
                message="Validation failed: {0}".format(
                    ", ".join(validation_results.error_messages)
                ),
            )
        api_endpoint = self._task.args.get("api_endpoint")
        username = self._task.args.get("username")
        password = self._task.args.get("password")
        name = self._task.args.get("name", "")
        guid = self._task.args.get("guid", "")

        with tempfile.TemporaryDirectory() as cf_home:
            client = CFClient(
                api_endpoint=api_endpoint,
                username=username,
                password=password,
                cf_home=cf_home,
            )
            return run_action(client, name=name, guid=guid)


class ActionModule(CFServiceInstanceInfoModule):
    pass
