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

DOCUMENTATION = r"""
  name: mount_path
  extends_documentation_fragment: sap.sap_operations.community
  author:
    - Ondra Machacek (@machacekondra)
    - Kirill Satarin (@kksat)
  version_added: 1.10.0
  short_description: Return the mount path of the filepath.
  description:
    - Filter plugin is intended to be used this way ansible_facts['mounts'] | sap.sap_operations.mount_path(filepath='/file/path')
    - From all mounts only one where file is located will be returned.
    - All other mounts will be filtered out.
  options:
    filepath:
      description: From all mounts only mount that contain this filepath will not be filtered out.
      type: path
      required: True
"""  # noqa: E501

EXAMPLES = r"""
- name: Example how to use mount_path filter
  debug:
    msg: "{{ ansible_facts['mounts'] | sap.sap_operations.mount_path(filepath='/') }}"
"""  # noqa: E501

RETURN = r"""
  data:
    type: str
    description:
      - Parameter `mount` from `ansible_mounts` list that was collected by `ansible.builtin.setup` module
      - This is mount point there file with provided `filepath` is located.
      - If provided filepath is not found filter returns None.
      - If list of mounts is empty filter returns None.
"""  # noqa: E501

from ansible.errors import AnsibleFilterError


def mount_path(mounts, filepath=None):
    if filepath is None:
        raise AnsibleFilterError("Please provide filepath")

    try:
        ret = max(
            [m for m in mounts if filepath.startswith(m["mount"])],
            key=lambda m: len(m["mount"]),
        )
    except ValueError:
        return None
    return ret


class FilterModule(object):
    def filters(self):
        return {"mount_path": mount_path}
