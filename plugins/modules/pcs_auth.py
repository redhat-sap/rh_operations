#!/usr/bin/python

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

# Copyright: (c) 2018, Ondrej Famera <ondrej-xa2iel8u@famera.cz>
# GNU General Public License v3.0+ (see LICENSE-GPLv3.txt or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

DOCUMENTATION = """
---
author:
  - Ondrej Famera (@OndrejHome)
  - Kirill Satarin (@kksat)
module: pcs_auth
extends_documentation_fragment:
    - sap.sap_operations.community
short_description: Module for managing cluster node authorization with 'pcs auth' commands
description:
  - Module for managing cluster node authorization with 'pcs auth' commands
options:
  state:
    description:
    - "'present' authenticates the node while 'absent' will remove the node authentication"
    - "node from which this is run is (de)authenticated against the node specified in 'node_name'"
    required: false
    default: present
    choices:
     - present
     - absent
    type: str

  node_name:
    description:
      - hostname of node for authentication
    required: true
    type: str
    aliases:
        - node
        - host
        - hostname

  username:
    description:
      - username of user for cluster authentication
    required: false
    default: hacluster
    type: str

  password:
    description:
      - password for cluster authentication
    required: false
    type: str

  pcsd_conf_filepath:
    description:
      - path to pcsd configuration file
      - only required if pcsd configuration file is in unusual location or for testing
    required: false
    type: path
    default: ""
notes:
  - This module is (de)authenticating nodes only 1-way == authenticating node 1 against
    node 2 doesn't mean that node 2 is authenticated against node 1!
"""

EXAMPLES = """
---
- name: Authorize node 'n1' with default user 'hacluster' and password 'testtest'
  sap.sap_operations.pcs_auth:
    node_name: 'n1'
    password: 'testtest'

- name: authorize all nodes in ansible play to each other
  sap.sap_operations.pcs_auth:
    node_name: "{{ hostvars[item]['ansible_hostname'] }}"
    password: 'testtest'
  with_items: "{{ play_hosts }}"

- name: de-authorize all nodes from each other in ansible play
  sap.sap_operations.pcs_auth:
    node_name: "{{  hostvars[item]['ansible_hostname'] }}"
    state: 'absent'
  with_items: "{{ play_hosts }}"
"""


from ansible_collections.sap.sap_operations.plugins.module_utils.monad import (
    Failure,
    Result,
    Success,
    same,
    changed,
    liftA2,
)
from ansible.module_utils.basic import AnsibleModule
from typing import ChainMap, List, TextIO
from collections.abc import Callable
import json

__metaclass__ = type


def get_pcs_version(
    pcs_run_command: Callable[[List[str]], tuple[int, str, str]],
) -> Result:
    rc, stdout, stderr = pcs_run_command(["--version"])
    if rc == 0:
        pcs_version = stdout.split(".")[0] + "." + stdout.split(".")[1]
        return Success(pcs_version)
    error = dict(
        msg="'pcs --version' exited with non-zero exit code",
        rc=rc,
        stdout=stdout,
        stderr=stderr,
    )
    return Failure(error)


def get_pcsd_conf_filepath(pcsd_conf_filepath: str) -> Callable:
    def f(pcs_version: str) -> Result:
        if pcsd_conf_filepath != "":
            return Success(pcsd_conf_filepath)
        mapping = {
            "0.9": "/var/lib/pcsd/tokens",
            "0.10": "/var/lib/pcsd/known-hosts",
            "0.11": "/var/lib/pcsd/known-hosts",
        }
        filename = mapping.get(pcs_version)
        if filename is not None:
            return Success(filename)
        return Failure(
            dict(
                msg="Failed to determine pcsd configuration file based on pcs version",
                pcs_version=pcs_version,
            )
        )

    return f


def get_file_contents(filepath: str) -> Result:
    try:
        file = open(filepath, "r+")
    except IOError as e:
        return Failure(
            dict(
                msg=f"IOError during reading file {filepath}",
                error=str(e),
            )
        )
    except Exception as e:
        return Failure(
            dict(
                msg=f"Exception during reading file {filepath}",
                error=str(e),
            )
        )
    return Success(file)


def read_file_to_dict(file: TextIO) -> Result:
    try:
        res = json.load(file)
    except Exception as e:
        return Failure(
            dict(
                msg="Failed to load json",
                error=str(e),
            )
        )
    return Success(res)


def get_pcsd_node_status(node_name: str, pcs_run_command: Callable) -> Callable:
    def f(pcs_version: str) -> Result:
        rc, stdout, stderr = pcs_run_command(
            ["cluster", "pcsd-status", node_name])
        if rc != 0:
            return Failure(
                dict(msg="Failed to call 'pcs cluster'",
                     stdout=stdout, stderr=stderr)
            )
        return Success((rc, stdout, stderr))

    return f


def get_pcs_auth_node_command(node_name: str, username: str, password: str) -> Callable:
    def f(pcs_version: str) -> Result:
        mapping = {
            "0.9": [
                "cluster",
                "auth",
                node_name,
                "-u",
                username,
                "-p",
                password,
            ],
            "0.10": [
                "host",
                "auth",
                node_name,
                "-u",
                username,
                "-p",
                password,
            ],
            "0.11": [
                "host",
                "auth",
                node_name,
                "-u",
                username,
                "-p",
                password,
            ],
        }
        args = mapping.get(pcs_version)
        if args is not None:
            return Success(args)
        else:
            return Failure(
                dict(
                    msg="Cannot determine pcs node auth command based on pcs version",
                    pcs_version=pcs_version,
                )
            )

    return f


def get_pcs_deauth_node_command(node_name: str) -> Callable:
    def f(pcs_version: str) -> Result:
        mapping = {
            "0.10": [
                "host",
                "deauth",
                node_name,
                "-u",
            ],
            "0.11": [
                "host",
                "deauth",
                node_name,
            ],
        }
        args = mapping.get(pcs_version)
        if args is not None:
            return Success(args)
        return Failure(
            dict(
                msg="Cannot determine pcs node deauth command based on pcs version",
                pcs_version=pcs_version,
            )
        )

    return f


def pcs_execute_command(pcs_run_command: Callable) -> Callable:
    def f(args: List[str]) -> Result:
        if args == []:
            return Success(dict(msg="pcs command not executed"))
        rc, stdout, stderr = pcs_run_command(args)
        if rc != 0:
            return Failure(
                dict(
                    msg="Failed to run pcs command",
                    rc=rc,
                    stdout=stdout,
                    stderr=stderr,
                )
            )
        return Success(
            dict(
                rc=rc,
                stdout=stdout,
                stderr=stderr,
            )
        )

    return f


def change_required(node_name, state):
    def f(pcsd_configuration_data):
        known_hosts = pcsd_configuration_data.get("known_hosts")
        if known_hosts is not None:
            node_present = node_name in known_hosts
            node_should_present = state == "present"
            return Success(node_should_present != node_present)
        return Failure(
            dict(
                msg="Error getting key 'known_hosts' from pcs configuration",
                pcsd_configuration_data=pcsd_configuration_data,
            )
        )

    return f


def run_module_check_mode(pcs_run_command: Callable, params: dict):
    state = params["state"]
    node_name = params["node_name"]
    pcsd_conf_filepath = params.get("pcsd_conf_filepath", "")

    pcs_version = get_pcs_version(pcs_run_command=pcs_run_command)
    pcsd_conf_filename = pcs_version.bind(
        get_pcsd_conf_filepath(pcsd_conf_filepath))
    pcsd_conf_file_contents = pcsd_conf_filename.bind(get_file_contents)
    pcsd_configuration_data = pcsd_conf_file_contents.bind(read_file_to_dict)
    changed = pcsd_configuration_data.bind(
        change_required(node_name=node_name, state=state)
    )

    return liftA2(
        ChainMap,
        changed.bind(same("changed")),
        pcsd_configuration_data.bind(same("pcs_auth")),
    )


def get_command_to_execute(
    state: str, node_name: str, username: str, password: str
) -> Callable:
    def f(change_required):
        if change_required and state == "present":
            return Success(
                [
                    "host",
                    "auth",
                    node_name,
                    "-u",
                    username,
                    "-p",
                    password,
                ],
            )
        if change_required and state == "absent":
            return Success(
                [
                    "host",
                    "deauth",
                    node_name,
                ],
            )
        return Success([])

    return f


def has_changed(attribute: str):
    def f(change_required):
        if change_required:
            return changed(attribute)
        return same(attribute)

    return f


def run_module(pcs_run_command: Callable, params: dict):
    state = params["state"]
    node_name = params["node_name"]
    username = params["username"]
    password = params["password"]
    pcs_version = get_pcs_version(pcs_run_command=pcs_run_command)
    pcsd_conf_filepath = params.get("pcsd_conf_filepath", "")

    pcs_version = get_pcs_version(pcs_run_command)

    pcsd_configuration_data = (
        get_pcs_version(pcs_run_command)
        .bind(get_pcsd_conf_filepath(pcsd_conf_filepath))
        .bind(get_file_contents)
        .bind(read_file_to_dict)
    )
    change_required_var = pcsd_configuration_data.bind(
        change_required(node_name=node_name, state=state)
    )
    pcs_command_to_execute = change_required_var.bind(
        get_command_to_execute(state, node_name, username, password)
    )
    pcs_command_to_execute = change_required_var.bind(
        get_command_to_execute(state, node_name, username, password)
    )

    pcs_command_result = pcs_command_to_execute.bind(
        pcs_execute_command(pcs_run_command)
    )
    pcsd_conf_filename = pcs_version.bind(
        get_pcsd_conf_filepath(pcsd_conf_filepath))
    pcsd_conf_file_contents = pcsd_conf_filename.bind(get_file_contents)
    pcsd_configuration_data = pcsd_conf_file_contents.bind(read_file_to_dict)

    f_return_pcs_auth = change_required_var.map(has_changed("pcs_auth"))
    f_return_pcs = change_required_var.map(has_changed("pcs"))
    pcs_auth = pcsd_configuration_data.apply(f_return_pcs_auth)
    pcs = pcs_command_result.apply(f_return_pcs)

    return liftA2(ChainMap, pcs_auth, pcs)


def get_pcs_run_command(module: AnsibleModule) -> Callable:
    def pcs_run_command(args: List[str]) -> tuple[int, str, str]:
        rc, stdout, stderr = module.run_command(["pcs"] + args)
        return rc, stdout, stderr

    return pcs_run_command


def main():
    argument_spec = dict(
        state=dict(default="present", choices=["present", "absent"]),
        node_name=dict(required=True, aliases=["node", "host", "hostname"]),
        username=dict(required=False, default="hacluster"),
        password=dict(required=False, no_log=True),
        pcsd_conf_filepath={
            'required': False,
            'type': 'path',
            'default': "",
        },
    )
    required_if = [
        ("state", "present", ("password",)),
    ]

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    pcs_run_command = get_pcs_run_command(module)

    if module.check_mode:
        result = run_module_check_mode(
            pcs_run_command=pcs_run_command, params=module.params
        )
    else:
        result = run_module(
            pcs_run_command=pcs_run_command,
            params=module.params,
        )
    if result.is_failure():
        module.fail_json(**result.result)
    module.exit_json(
        **result.result,
    )


if __name__ == "__main__":
    main()
