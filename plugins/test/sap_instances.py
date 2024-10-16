# -*- coding: utf-8 -*-

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

__metaclass__ = type


def sap_instance(name: str, description: str):
    def f(instance):
        try:
            return any(
                instance_process["name"] == name
                and instance_process["description"] == description
                for instance_process in instance["ProcessList"]
            )
        except KeyError:
            return False

    return f


def ascs_instance(instance):
    return sap_instance(name="enserver", description="EnqueueServer")(
        instance
    ) and sap_instance(name="msg_server", description="MessageServer")(instance)


class TestModule(object):
    def tests(self):
        return {
            "hana_instance": sap_instance(name="hdbdaemon", description="HDB Daemon"),
            "app_instance": sap_instance(name="disp+work", description="Dispatcher"),
            "ascs_instance": ascs_instance,
        }
