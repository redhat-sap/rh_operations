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


class ModuleDocFragment(object):
    DOCUMENTATION = """
---
options: {}
notes:
  - |
    Variable binary_path is required, because hdbuserstore command cannot be found in $PATH environment variable.
    If running ansible module using become directive with <hanasid>adm user and flag '-i' \
    (interactive - meaning load all environment for the user) ansible modules fail.
    This is due to the fact that <hanasid>adm user sets environment variables PYTHONHOME and PYTHONPATH \
    (to use HANA python, not platform python) that confuses ansible.
    And also HANA python might not have all the necessary packages installed to run ansible module.
    In that case hdbuserstore command will not be in PATH environment variable for <hanasid>adm user and I(binary_path) has to be provided.
  - |
    There are several workaround around this unpleasant situation. First one is recommended.
  - |
    Workaround 1 (recommended)
  - Run hdbsuserstore module with <hanasid>adm user with '-i' (interactive) flag like so
  - "- name: Set the key mykey"
  - "sap.sap_operations.hdbuserstore:"
  - "   key: mykey"
  - "   env: localhost:30113"
  - "   username: myuser"
  - "   password: mypassword"
  - "become: true"
  - "become_user: <hanasid>adm"
  - "become_flags: -i"
  - "vars:"
  - "    ansible_python_interpreter: '/usr/libexec/platform-python -E'"
  - |
    Option '-E' for python interpreter will ignore all PYTHON environment variables, so ansible will run platform python without any problems.
    Variable I(ansible_python_interpreter) have to be set to value "/usr/libexec/platform-python -E" on all RHEL versions for any ansible module
    execution when using become directive for <hanasid>adm user with become flag '-i'.
  - |
    ansible_python_interpreter: "/usr/libexec/platform-python -E" can be set at task level (as above),\
    at play level, or be set as host variable either in inventory file or as task in playbook:
  - |
    To use other SAP HANA related ansible modules (for instances hana_system_replication_info),\
    this is the only option, because other modules might not have parameters to accommodate for binary tool path.
  - |
    Workaround 2 (only for hdbuserstore module)
  - |
    Do not use interactive flag when becoming <hanasid>adm user.
  - "- name: Set the key mykey"
  - "sap.sap_operations.hdbuserstore:"
  - "   key: mykey"
  - "   env: localhost:30113"
  - "   username: myuser"
  - "   password: mypassword"
  - "   binary_path: /usr/sap/HAN/SYS/exe/hdb"
  - "become: true"
  - "become_user: <hanasid>adm"
  - |
    In that case hdbuserstore command will not be in PATH environment variable for <hanasid>adm user and I(binary_path) has to be provided.
  - |
    Workaround 3 (only for hdbuserstore module)
  - Do not use interactive flag when becoming <hanasid>adm user. But do not want to provide value for variable I(binary_path).
  - In that case value for I(binary_path) can be extracted from HANA parameter DIR_EXECUTABLE that one can get with I(parameter_info) module
  - "- name: Get DIR_EXECUTABLE"
  - "sap.sap_operations.parameter_info:"
  - "   instance_number: 00"
  - "   name: DIR_EXECUTABLE"
  - "become: true"
  - "become_user: <hanasid>adm"
  - "register: __DIR_EXECUTABLE"
  - "- name: Set the key mykey"
  - "sap.sap_operations.hdbuserstore:"
  - "   key: mykey"
  - "   env: localhost:30113"
  - "   username: myuser"
  - "   password: mypassword"
  - "   binary_path: '{{ __DIR_EXECUTABLE.parameter_value[0] }}'"
  - "become: true"
  - "become_user: <hanasid>adm"
"""
