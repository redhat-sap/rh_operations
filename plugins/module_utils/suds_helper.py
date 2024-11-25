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

import traceback

HAS_SUDS_LIBRARY = True
SUDS_LIBRARY_IMPORT_ERROR = None
try:
    from suds.sudsobject import items
    from suds.sudsobject import Object as sudsobject
except ImportError:
    try:
        from virtwho.virt.esx.suds.sudsobject import items
        from virtwho.virt.esx.suds.sudsobject import Object as sudsobject
    except ImportError:
        HAS_SUDS_LIBRARY = False
        SUDS_LIBRARY_IMPORT_ERROR = traceback.format_exc()
        items = None
        sudsobject = None


def deep_asdict2(obj):
    """Function to convert sudsobject.reply to dict/list structure.

    This is to return data to Ansible, otherwise Ansible does not know how to work with returned classes
    Due to how sudsobjects are structured, we skip 'item' attribute, and return list of items instead.

    There is a strange thing about suds module, if reply contains only one type, it is not returned as reply object,
    but as an object of that type. So we need to check if obj is not reply, and if it is not reply, add classname to resulting dict.
    This is where decided to return reply or not.
    https://github.com/suds-community/suds/blob/master/suds/bindings/binding.py#L132
    """
    if getattr(obj, "item", None):
        return [deep_asdict2(item) for item in getattr(obj, "item", None)]
    if isinstance(obj, sudsobject):
        return {k: deep_asdict2(v) for k, v in items(obj)}
    if isinstance(obj, list):
        return [deep_asdict2(elem) for elem in obj]
    return (
        obj if (obj is not None) else ""
    )  # return empty string if obj is None, this is because in RFC processing None is returned as empty string


def deep_asdict(obj):
    if (
        obj.__class__.__name__ == "reply"
    ):  # This has to be done once only for highest level object
        return deep_asdict2(obj)
    return {obj.__class__.__name__: deep_asdict2(obj)}
