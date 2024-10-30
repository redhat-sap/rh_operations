<!--
SPDX-License-Identifier: GPL-3.0-only
SPDX-FileCopyrightText: 2023-2024 Red Hat, Project Atmosphere

Copyright 2023-2024 Red Hat, Project Atmosphere

This program is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

You should have received a copy of the GNU General Public License along with this program.
If not, see <https://www.gnu.org/licenses/>.
-->

# quality

Role to run SAP quality checks


Role to run SAP quality checks
Quality checks are available in Azure SAP repository https://github.com/Azure/SAP-on-Azure-Scripts-and-Utilities.git
How role works
Ansible facts are collected
Information from sap hostagent is collected - what databases are installed, what instances are installed, what processes are running, etc.
Information from Azure instance metadata service is collected instance type, data disks types, resource group, region (location), etc.
All collected information is available in the quality_context variable for each check.
A lot of checks are skipped and not executed on the host based on following rules
1. only checks that run in local mode executed
2. only os checks are executed (not powershell)
3. only checks without postprocessing command are executed
4. only checks for VMs are executed, checks for HLI are skipped
5. if ha status collected (true or false) is in the list of ha statuses in the check - only when check is executed
6. checks are executed for relevant os family (suse or redhat) and for relevant os versions
7. only checks for FencingAgent as high availability agent are executed
8. checks are executed if one of the following is true
a. check.role contains 'db' and respective database is detected by sap hostagent
b. check.role contains instance types that are detected by sap hostagent.
Instance types (ASCS, ERS) are determined using processes detected by sap hostagent

Limitations
Role tested only on single instance
Role tested only with HANA and ASE databases and works only with these databases (configuration has to be changed)
Role does not run checks with postprocessing commands
Role does not run powershell checks - only OS checks
User executing role should be able to sudo to root
Role does not yet support RHEL 9



## Role Variables

### Required parameters:

 
 
