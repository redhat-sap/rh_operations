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
from ansible_collections.sap.sap_operations.plugins.action.cf_service_plans_info import (
    run_action as get_service_plans,
)

from ansible_collections.sap.sap_operations.plugins.action.cf_spaces_info import (
    run_action as get_spaces,
)


def validate_service_plan_name(client: CFClient, name: str, service_plan: str) -> dict:
    result = get_service_plans(client, service_offering_names=[name])
    if result["failed"]:
        return result

    return {
        "failed": service_plan
        not in [sp["name"] for sp in result["cf_service_plans_info"]]
    }


def run_action(  # noqa C901
    # TODO: simplify function
    client: CFClient,
    name: str,
    service: str,
    state: str,
    space_name: str,
    parameters: dict,
    service_plan_name: str,
    metadata: dict,
) -> dict:
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
    service_instance = None

    for si in service_instances["resources"]:
        if name and si["name"] == name:
            service_instance = si

    if state == "absent" and service_instance:
        service_instance_guid = service_instance["guid"]
        rc, stdout, stderr = client.run_method(
            path=f"/v3/service_instances/{service_instance_guid}",
            method="DELETE",
            headers={},
            data={},
        )
        if rc:
            return {
                "failed": True,
                "msg": "Could not delete service_instance",
                "stdout": stdout,
            }
        return dict(failed=False, changed=True)

    if state == "absent" and not service_instance:
        return {"failed": False, "changed": False}

    if state == "present" and service_instance:
        return {"failed": False, "changed": False}

    if state == "present" and not service_instance:
        data = {}
        data["type"] = "managed"
        data["name"] = name
        data["parameters"] = parameters
        data["metadata"] = metadata
        service_plans = get_service_plans(client, service_offering_names=[service])
        service_plan = [
            sp
            for sp in service_plans["cf_service_plans_info"]
            if sp["name"] == service_plan_name
        ][0]

        spaces = get_spaces(client)
        space = [sp for sp in spaces["cf_spaces_info"] if sp["name"] == space_name][0]

        data["relationships"] = {}
        data["relationships"]["service_plan"] = {}
        data["relationships"]["service_plan"]["data"] = {}
        data["relationships"]["service_plan"]["data"]["guid"] = service_plan["guid"]

        data["relationships"]["space"] = {}
        data["relationships"]["space"]["data"] = {}
        data["relationships"]["space"]["data"]["guid"] = space["guid"]

        rc, stdout, stderr = client.run_method(
            path="/v3/service_instances/",
            method="POST",
            # headers={"Content-type": "application/json"},
            data=data,
        )
        if rc or stderr or "errors" in stdout:
            return {
                "failed": True,
                "msg": "Could not create service_instance",
                "stdout": stdout,
                "stderr": stderr,
            }
        # return get_service_instance_info(client, name=name)
        return {"failed": False, "stdout": stdout, "stderr": stderr}


class CFServiceInstanceModule(ActionBase):
    _VALID_ARGS = frozenset(
        [
            "username",
            "password",
            "api_endpoint",
            "name",
            "service",
            "state",
            "space",
            "service_plan",
            "parameters",
            "metadata",
        ]
    )
    argument_spec = dict(
        username=dict(type="str", required=False),
        password=dict(type="str", required=False),
        api_endpoint=dict(type="str", required=False),
        name=dict(type="str", required=True),
        service=dict(type="str", required=True),
        state=dict(
            type="str", required=False, default="present", choices=["present", "absent"]
        ),
        space=dict(type="str", required=True),
        service_plan=dict(type="str", required=False),
        parameters=dict(type="dict", required=False),
        metadata=dict(type="dict", required=False),
    )
    required_together = [
        [
            "username",
            "password",
            "api_endpoint",
        ],
    ]
    mutually_exclusive = []
    required_one_of = [
        [
            "username",
            "password",
            "api_endpoint",
        ],
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
        name = self._task.args.get("name")
        service = self._task.args.get("service")
        state = self._task.args.get("state", "present")
        space_name = self._task.args.get("space")
        parameters = self._task.args.get("parameters", {})
        service_plan = self._task.args.get("service_plan")
        metadata = self._task.args.get("metadata", {})

        with tempfile.TemporaryDirectory() as cf_home:
            client = CFClient(
                api_endpoint=api_endpoint,
                username=username,
                password=password,
                cf_home=cf_home,
            )
            if state == "present":
                validation_results = validate_service_plan_name(
                    client, name=service, service_plan=service_plan
                )
                if validation_results["failed"]:
                    return {
                        "failed": True,
                        "msg": f"Service plan name {service_plan=} is not correct for service name {service=}",
                    }

            return run_action(
                client,
                name=name,
                service=service,
                state=state,
                space_name=space_name,
                parameters=parameters,
                service_plan_name=service_plan,
                metadata=metadata,
            )


class ActionModule(CFServiceInstanceModule):
    pass
