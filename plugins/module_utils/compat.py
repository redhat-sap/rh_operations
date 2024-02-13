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


def dict_union(dict1, dict2):
    """Returns a new dictionary that is the union of the two input dictionaries.

    This is compatibility function for python 2 and 3.
    The resulting dictionary contains all the key-value pairs from both input
    dictionaries. If a key is present in both input dictionaries, the value from
    the second dictionary (dict2) is used.

    Args:
        dict1 (dict): The first dictionary to include in the union.
        dict2 (dict): The second dictionary to include in the union.

    Returns:
        dict: A new dictionary that is the union of dict1 and dict2.
    """
    return dict(list(dict1.items()) + list(dict2.items()))
