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

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r"""

author:
  - Kirill Satarin (@kksat)

description:
  - Uses saplikey program to get information about SAP license keys and manage them.
  - saplikey program is a part of SAP kernel

requirements:
  - saplikey program should be installed on the target host
  - Module should be executed on the host where SAP system is installed
  - Module should be executed with <sid>adm user
  - |
    Module should be executed with interactive shell, for that additional parameters should be used:
    become: true
    become_user: <sid>adm
    become_flags: '-i'
    Flag '-i' is very important, module execution will fail without it.
    This is because saplikey program heavily relies on environment variables provided by SAP profile.

options:
  profile:
    description: Profile filename as mentioned in SAP documentation for saplikey program.
    type: path
    required: false
    default: DEFAULT.PFL

seealso:
  - module: sap.sap_operations.saplikey
  - module: sap.sap_operations.saplikey_show_info
  - module: sap.sap_operations.saplikey_get_info

  - name: License Administration at Operating System Level with Program saplikey
    description: License Administration at Operating System Level with Program saplikey
    link: https://help.sap.com/docs/SAP_NETWEAVER_750/0643d547dfad4ce497bd7da1264fce77/c3e84ae90d9d427e92b0ceb69292ef4f.html?version=7.5.6

"""  # noqa: E501
