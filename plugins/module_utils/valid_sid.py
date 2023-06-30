# -*- coding: utf-8 -*-

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
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.


from __future__ import absolute_import, division, print_function

__metaclass__ = type


prohibited = [
    "ADD",
    "ADM",
    "ALL",
    "AMD",
    "AND",
    "ANY",
    "ARE",
    "ASC",
    "AUX",
    "AVG",
    "BIN",
    "BIT",
    "CDC",
    "COM",
    "CON",
    "DAA",
    "DBA",
    "DBM",
    "DBO",
    "DTD",
    "ECO",
    "END",
    "EPS",
    "EXE",
    "FOR",
    "GET",
    "GID",
    "IBM",
    "INT",
    "KEY",
    "LIB",
    "LOG",
    "LPT",
    "MAP",
    "MAX",
    "MEM",
    "MIG",
    "MIN",
    "MON",
    "NET",
    "NIX",
    "NOT",
    "NUL",
    "OFF",
    "OLD",
    "OMS",
    "OUT",
    "PAD",
    "PRN",
    "RAW",
    "REF",
    "ROW",
    "SAP",
    "SET",
    "SGA",
    "SHG",
    "SID",
    "SQL",
    "SUM",
    "SYS",
    "TMP",
    "TOP",
    "TRC",
    "UID",
    "USE",
    "USR",
    "VAR",
]


def valid_sid(sid):
    return (
        (len(sid) == 3)
        and (sid.upper() not in prohibited)   # noqa: W503
        and (sid.upper() == sid)   # noqa: W503
        and (sid[0] not in "0123456789")   # noqa: W503
        and (sid.isalnum())   # noqa: W503
    )
