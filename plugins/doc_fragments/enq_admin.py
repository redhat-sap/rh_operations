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


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
---
requirements:
  - only for ENSA2 instances with enq_admin tool installed

author:
  - Kirill Satarin (@kksat)

options:
  profile_filepath:
    description:
      - A path to the profile file
      - Either I(profile_filepath) or I(sid), I(hostname) and I(port) required
      - I(sid), I(hostname) and I(port) are required together
    required: false
    type: path
    aliases:
      - pf
      - profile
  sid:
    description: SAP system id
    required: false
    type: str
  hostname:
    description: hostname where enque process is running
    required: false
    type: str
    aliases:
      - host
  port:
    description: Port where enque process is running
    required: false
    type: int

seealso:
  - name: Architecture of the Standalone Enqueue Server 2
    description: Architecture of the Standalone Enqueue Server 2
    link: https://help.sap.com/docs/latest/e458064e3077486994caaf9a85c4aa23/902412f09e134f5bb875adb6db585c92.html
  - name: Parameter Reference of Standalone Enqueue Server 2
    description: Parameter Reference of Standalone Enqueue Server 2
    link: https://help.sap.com/docs/latest/e458064e3077486994caaf9a85c4aa23/1ca2eab4fca04d2696b7185f470b51aa.html
"""
