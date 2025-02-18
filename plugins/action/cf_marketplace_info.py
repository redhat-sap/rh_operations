# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2023 Red Hat, Project Atmosphere
#
# Copyright 2023 Red Hat, Project Atmosphere
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
import subprocess  # nosec B404
from ansible.plugins.action import ActionBase


class CFClient:
    def __init__(
        self,
        api_endpoint: str = "",
        username: str = "",
        password: str = "",  # nosec B107
        cf_home: str = "",
    ):
        """Initializes the CFClient object with optional keyword arguments."""
        self.api_endpoint = api_endpoint
        self.username = username
        self.password = password
        self.cf_home = cf_home
        self.env = {"CF_HOME": cf_home}

    def authenticate(self):
        rc = subprocess.run(
            [
                f'cf login -a "{self.api_endpoint}" -u "{self.username}" -p "{self.password}"',
            ],
            shell=True,  # nosec B602
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            env=self.env,
        )
        if rc.returncode:
            return {
                "failed": True,
                "msg": "Error while authorizing cf cli",
                "stderr": rc.stderr.decode("utf-8"),
                "stdout": rc.stdout.decode("utf-8"),
            }
        else:
            return {"failed": False}

    def run_method(
        self,
        path: str,
        data: dict,
        method: str = "GET",
        headers: dict[str, str] = None,
    ):
        rc = self.authenticate()
        if rc.get("failed"):
            return rc

        if headers is None:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # headers_command = [f'-H "{k}:{v}"' for k, v in headers]
        data_string = json.dumps(data)
        command_run = subprocess.run(
            [
                f"""cf curl "{path}" -X {method} -d '{data_string}'""",
            ],
            # + headers_command,
            shell=True,  # nosec B602
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            env=self.env,
        )

        return (
            command_run.returncode,
            command_run.stdout.decode("utf-8"),
            command_run.stderr.decode("utf-8"),
        )


def run_action(client: CFClient) -> dict:
    rc = client.authenticate()
    if rc.get("failed"):
        return rc

    rc, stdout, stderr = client.run_method(
        path="/v3/service_offerings",
        method="GET",
        headers={},
        data={},
    )

    if rc or stderr:
        return {"failed": True, "msg": stdout}

    result = json.loads(stdout)

    if "errors" in result:
        return {
            "failed": True,
            "msg": "Error retrieving service offerings",
            "errors": result["errors"],
        }

    return dict(failed=False, changed=False, cf_marketplace_info=result["resources"])


class CFMarketplaceInfoActionModule(ActionBase):
    _VALID_ARGS = frozenset(["username", "password", "api_endpoint"])
    argument_spec = dict(
        username=dict(type="str", required=False),
        password=dict(type="str", required=False),
        api_endpoint=dict(type="str", required=False),
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
        ]
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

        with tempfile.TemporaryDirectory() as cf_home:
            client = CFClient(
                api_endpoint=api_endpoint,
                username=username,
                password=password,
                cf_home=cf_home,
            )
            return run_action(client)


class ActionModule(CFMarketplaceInfoActionModule):
    pass
