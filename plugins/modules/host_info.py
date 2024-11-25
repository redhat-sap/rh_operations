#!/usr/bin/python
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

from ansible_collections.sap.sap_operations.plugins.module_utils.saphost import (
    AnsibleModuleSAPHostAgent,
    saphostctrl,
    sapcontrol,
    convert2ansible,
)


def main():
    module = AnsibleModuleSAPHostAgent(
        argument_spec={}, supports_check_mode=True)
    try:
        m = saphostctrl(
            hostname=module.params.get("hostname"),
            username=module.params.get("username"),
            password=module.params.get("password"),
            ca_file=module.params.get("ca_file"),
            security=module.params.get("security"),
        )
    except FileNotFoundError:
        module.exit_json(
            msg="No saphost agent installed",
            instances=[],
            databases=[],
        )

    try:
        instances = convert2ansible(m.client.service.ListInstances())
        for instance in instances:
            instance_sapcontrol = sapcontrol(
                instance=instance["mSystemNumber"],
                hostname=module.params.get("hostname"),
                username=module.params.get("username"),
                password=module.params.get("password"),
                ca_file=module.params.get("ca_file"),
                security=module.params.get("security"),
            )

            instance["VersionInfo"] = convert2ansible(
                instance_sapcontrol.client.service.GetVersionInfo()
            )
            instance["InstanceProperties"] = convert2ansible(
                instance_sapcontrol.client.service.GetInstanceProperties()
            )
            instance["ProcessList"] = convert2ansible(
                instance_sapcontrol.client.service.GetProcessList()
            )
            instance["AccessPointList"] = convert2ansible(
                instance_sapcontrol.client.service.GetAccessPointList()
            )
            EnvironmentRaw = convert2ansible(
                instance_sapcontrol.client.service.GetEnvironment()
            )
            instance["EnvironmentRaw"] = EnvironmentRaw
            instance["Environment"] = {
                line.split("=")[0]: line.split("=")[1]
                for line in EnvironmentRaw
                if "=" in line
            }
            instance["StartProfile"] = convert2ansible(
                instance_sapcontrol.client.service.GetStartProfile()
            )
            # instance['Snapshots'] = convert2ansible(instance_sapcontrol.client.service.ListSnapshots())
            # instance['GetProcessParameter'] = convert2ansible(instance_sapcontrol.client.service.GetProcessParameter())
            instance["HAFailoverConfig"] = convert2ansible(
                instance_sapcontrol.client.service.HAGetFailoverConfig()
            )

        databases = convert2ansible(m.client.service.ListDatabases())
        for database in databases:
            ArrayOfProperty = m.client.factory.create("ArrayOfProperty")
            for property_key, property_value in database["mDatabase"].items():
                Property = m.client.factory.create("Property")
                Property.mKey = property_key
                Property.mValue = property_value
                ArrayOfProperty.item.append(Property)
            database["DatabaseProperties"] = convert2ansible(
                m.client.service.GetDatabaseProperties(
                    aArguments=ArrayOfProperty)
            )
            database["DatabaseStatus"] = convert2ansible(
                m.client.service.GetDatabaseStatus(aArguments=ArrayOfProperty)
            )

        # computer_system = convert2ansible(m.client.service.GetComputerSystem())
        # database_systems = convert2ansible(m.client.service.ListDatabaseSystems())

        module.exit_json(
            instances=instances,
            databases=databases,
        )
    except Exception as e:
        module.fail_json(
            msg="Issue during calling SOAP host agent methods",
            exception=str(e),
        )


if __name__ == "__main__":
    main()
