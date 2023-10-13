#!/usr/bin/python
# -*- coding: utf-8 -*-

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

DOCUMENTATION = r"""
---
module: host_info
extends_documentation_fragment:
  - sap.sap_operations.saphost

author:
  - Kirill Satarin (@kksat)

short_description: Collect information about installed SAP instances on the host

description:
  - Collect information about installed SAP instances on the host

options: {}

version_added: 1.1.0
"""

EXAMPLES = r"""
- name: Collection information about SAP instances installed on the current host
  sap.sap_operations.host_info:

- name: Collection information about SAP instances installed on the remote host
  sap.sap_operations.host_info:
    username: sapadm
    password: "secret123!"
    hostname: "sap.system.example.com"
"""

RETURN = r"""
instances:
    description: SAP Instances installed on a host
    type: list
    returned: success
    sample: |-
        [
            {
                "mSid": "NPL",
                "mHostname": "vhcalnplci",
                "mSystemNumber": "00",
                "mSapVersionInfo": "749, patch 10, changelist 1698137",
                "VersionInfo":
                [
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/sapstartsrv",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/disp+work",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/gwrd",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/msg_server",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/dboraslib.so",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/dbmssslib.so",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/dbdb2slib.so",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/dbdb4slib.so",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/dbdb6slib.so",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/dbsybslib.so",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/enserver",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/enq_server",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/icman",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/sapwebdisp",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/jcontrol",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/jlaunch",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/D00/exe/jstart",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    }
                ],
                "InstanceProperties":
                [
                    {
                        "property": "Process List",
                        "propertytype": "NodeWebmethod",
                        "value": "GetProcessList"
                    },
                    {
                        "property": "Access Points",
                        "propertytype": "NodeWebmethod",
                        "value": "GetAccessPointList"
                    },
                    {
                        "property": "Parameter Documentation",
                        "propertytype": "NodeURL",
                        "value": "http://vhcalnplci:50013/sapparamEN.html"
                    },
                    {
                        "property": "Kernel Update",
                        "propertytype": "NodeURL",
                        "value": "http://service.sap.com/~form/handler?_APP=00200682500000001943&_EVENT=DISPHIER&HEADER=Y&FUNCTIONBAR=N&EVENT=TREE&NE=NAVIGATE&ENR=73554900100200004760&V=MAINT"
                    },
                    {
                        "property": "Current Status",
                        "propertytype": "NodeWebmethod",
                        "value": "GetAlertTree"
                    },
                    {
                        "property": "Open Alerts",
                        "propertytype": "NodeWebmethod",
                        "value": "GetAlertTree"
                    },
                    {
                        "property": "Syslog",
                        "propertytype": "NodeWebmethod",
                        "value": "ABAPReadSyslog"
                    },
                    {
                        "property": "Queue Statistic",
                        "propertytype": "NodeWebmethod",
                        "value": "GetQueueStatistic"
                    },
                    {
                        "property": "ABAP WP Table",
                        "propertytype": "NodeWebmethod",
                        "value": "ABAPGetWPTable"
                    },
                    {
                        "property": "ICM",
                        "propertytype": "NodeURL",
                        "value": "HTTP://vhcalnplci:8000/sap/admin/public/index.html"
                    },
                    {
                        "property": "ICM Threads",
                        "propertytype": "NodeWebmethod",
                        "value": "ICMGetThreadList"
                    },
                    {
                        "property": "ICM Connections",
                        "propertytype": "NodeWebmethod",
                        "value": "ICMGetConnectionList"
                    },
                    {
                        "property": "ICM Cache",
                        "propertytype": "NodeWebmethod",
                        "value": "ICMGetCacheEntries"
                    },
                    {
                        "property": "ICM Proxy Connections",
                        "propertytype": "NodeWebmethod",
                        "value": "ICMGetProxyConnectionList"
                    },
                    {
                        "property": "ABAP DB Connection",
                        "propertytype": "Attribute",
                        "value": "Database=SYBASE,DBHost=wdflbmd16697,DBName=NPL,DBPort=4901"
                    },
                    {
                        "property": "Protected Webmethods",
                        "propertytype": "Attribute",
                        "value": "ABAPAcknowledgeAlerts,ABAPCheckRFCDestinations,ABAPGetComponentList,ABAPGetSystemWPTable,ABAPGetWPTable,ABAPReadRawSyslog,ABAPReadSyslog,AnalyseLogFiles,Bootstrap,CheckParameter,CheckPSE,CheckUpdateSystem,ConfigureLogFileList,CreatePSECredential,CreateSnapshot,DeletePSE,DeleteSnapshots,EnqGetLockTable,EnqGetStatistic,EnqRemoveLocks,EnqRemoveUserLocks,GetAccessPointList,GetAlerts,GetAlertTree,GetCallstack,GetEnvironment,GetLogFileList,GetProcessParameter,GetQueueStatistic,GetStartProfile,GetSystemUpdateList,GetTraceFile,GetVersionInfo,HACheckConfig,HACheckFailoverConfig,HAFailoverToNode,HAGetFailoverConfig,HASetMaintenanceMode,ICMGetCacheEntries,ICMGetConnectionList,ICMGetProxyConnectionList,ICMGetThreadList,InstanceStart,InstanceStop,J2EEControlCluster,J2EEControlComponents,J2EEControlProcess,J2EEDisableDbgSession,J2EEEnableDbgSession,J2EEGetApplicationAliasList,J2EEGetCacheStatistic,J2EEGetCacheStatistic2,J2EEGetClusterMsgList,J2EEGetComponentList,J2EEGetEJBSessionList,J2EEGetProcessList,J2EEGetProcessList2,J2EEGetRemoteObjectList,J2EEGetSessionList,J2EEGetSharedTableInfo,J2EEGetThreadCallStack,J2EEGetThreadList,J2EEGetThreadList2,J2EEGetThreadTaskStack,J2EEGetVMGCHistory,J2EEGetVMGCHistory2,J2EEGetVMHeapInfo,J2EEGetWebSessionList,J2EEGetWebSessionList2,ListDeveloperTraces,ListLogFiles,ListSnapshots,OSExecute,ParameterValue,ReadDeveloperTrace,ReadLogFile,ReadSnapshot,RestartInstance,RestartService,RestartSystem,SendSignal,SetProcessParameter,SetProcessParameter2,ShmDetach,Shutdown,Start,StartBypassHA,StartSystem,Stop,StopBypassHA,StopService,StopSystem,StorePSE,UpdateInstancePSE,UpdateSCSInstance,UpdateSystem,UpdateSystemPKI,WebDispGetServerList,WebDispGetGroupList,WebDispGetVirtHostList,WebDispGetUrlPrefixList,GetAgentConfig,MtChangeStatus,MtCustomizeWrite,MtDbsetToWpsetByTid,MtDestroyMarkNTry,MtReset,PerfCustomizeWrite,ReadDirectory,ReadFile,ReadProfileParameters,Register,SnglmgsCustomizeWrite,SystemObjectSetValue,ToolSet,ToolSetRuntimeStatus,TriggerDataCollection,Unregister,UtilAlChangeStatus"
                    },
                    {
                        "property": "StartPriority",
                        "propertytype": "Attribute",
                        "value": "3"
                    },
                    {
                        "property": "SAPSYSTEM",
                        "propertytype": "Attribute",
                        "value": "00"
                    },
                    {
                        "property": "SAPSYSTEMNAME",
                        "propertytype": "Attribute",
                        "value": "NPL"
                    },
                    {
                        "property": "SAPLOCALHOST",
                        "propertytype": "Attribute",
                        "value": "vhcalnplci"
                    },
                    {
                        "property": "INSTANCE_NAME",
                        "propertytype": "Attribute",
                        "value": "D00"
                    },
                    {
                        "property": "IGS",
                        "propertytype": "NodeURL",
                        "value": "http://vhcalnplci:40080"
                    },
                    {
                        "property": "Webmethods",
                        "propertytype": "Attribute",
                        "value": "Start,InstanceStart,StartBypassHA,Bootstrap,Stop,InstanceStop,StopBypassHA,Shutdown,ParameterValue,GetProcessList,GetStartProfile,GetTraceFile,GetAlertTree,GetAlerts,RestartService,StopService,GetEnvironment,ListDeveloperTraces,ReadDeveloperTrace,RestartInstance,SendSignal,GetVersionInfo,GetQueueStatistic,GetInstanceProperties,OSExecute,ReadLogFile,AnalyseLogFiles,ListLogFiles,GetAccessPointList,GetSystemInstanceList,GetSystemUpdateList,StartSystem,StopSystem,RestartSystem,UpdateSystem,UpdateSCSInstance,CheckUpdateSystem,AccessCheck,GetProcessParameter,SetProcessParameter,SetProcessParameter2,CheckParameter,ShmDetach,GetNetworkId,GetSecNetworkId,RequestLogonFile,CreateSnapshot,ReadSnapshot,ListSnapshots,DeleteSnapshots,GetCallstack,ABAPReadSyslog,ABAPReadRawSyslog,ABAPGetWPTable,ABAPAcknowledgeAlerts,ABAPGetComponentList,ABAPCheckRFCDestinations,ABAPGetSystemWPTable,J2EEGetProcessList,J2EEGetProcessList2,J2EEControlProcess,J2EEGetThreadList,J2EEGetThreadList2,J2EEGetThreadCallStack,J2EEGetThreadTaskStack,J2EEGetSessionList,J2EEGetWebSessionList,J2EEGetWebSessionList2,J2EEGetCacheStatistic,J2EEGetCacheStatistic2,J2EEGetApplicationAliasList,J2EEGetVMGCHistory,J2EEGetVMGCHistory2,J2EEGetVMHeapInfo,J2EEGetEJBSessionList,J2EEGetRemoteObjectList,J2EEGetClusterMsgList,J2EEGetSharedTableInfo,J2EEGetComponentList,J2EEControlComponents,ICMGetThreadList,ICMGetConnectionList,ICMGetCacheEntries,ICMGetProxyConnectionList,WebDispGetServerList,WebDispGetGroupList,WebDispGetVirtHostList,WebDispGetUrlPrefixList,EnqGetLockTable,EnqRemoveLocks,EnqRemoveUserLocks,EnqGetStatistic,UpdateSystemPKI,UpdateInstancePSE,StorePSE,DeletePSE,CheckPSE,HACheckConfig,HACheckFailoverConfig,HAGetFailoverConfig,HAFailoverToNodeHASetMaintenanceMode"
                    }
                ],
                "ProcessList":
                [
                    {
                        "name": "disp+work",
                        "description": "Dispatcher",
                        "dispstatus": "SAPControl-GREEN",
                        "textstatus": "Running",
                        "starttime": "2023 04 14 05:32:59",
                        "elapsedtime": "1:43:26",
                        "pid": 3457
                    },
                    {
                        "name": "igswd_mt",
                        "description": "IGS Watchdog",
                        "dispstatus": "SAPControl-GREEN",
                        "textstatus": "Running",
                        "starttime": "2023 04 14 05:32:59",
                        "elapsedtime": "1:43:26",
                        "pid": 3458
                    },
                    {
                        "name": "gwrd",
                        "description": "Gateway",
                        "dispstatus": "SAPControl-GREEN",
                        "textstatus": "Running",
                        "starttime": "2023 04 14 05:33:01",
                        "elapsedtime": "1:43:24",
                        "pid": 3476
                    },
                    {
                        "name": "icman",
                        "description": "ICM",
                        "dispstatus": "SAPControl-GREEN",
                        "textstatus": "Running",
                        "starttime": "2023 04 14 05:33:01",
                        "elapsedtime": "1:43:24",
                        "pid": 3477
                    }
                ],
                "AccessPointList":
                [
                    {
                        "address": "127.0.0.1",
                        "port": 8000,
                        "protocol": "HTTP",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 8000,
                        "protocol": "HTTP",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 44300,
                        "protocol": "HTTPS",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 44300,
                        "protocol": "HTTPS",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 0,
                        "protocol": "SMTP",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 0,
                        "protocol": "SMTP",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 8101,
                        "protocol": "HTTP",
                        "processname": "icm",
                        "active": "No"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 8101,
                        "protocol": "HTTP",
                        "processname": "icm",
                        "active": "No"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 50000,
                        "protocol": "HTTP",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 50000,
                        "protocol": "HTTP",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 50001,
                        "protocol": "HTTPS",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 50001,
                        "protocol": "HTTPS",
                        "processname": "icm",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 50013,
                        "protocol": "HTTP",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 50013,
                        "protocol": "HTTP",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 50014,
                        "protocol": "HTTPS",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 50014,
                        "protocol": "HTTPS",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 3300,
                        "protocol": "RFC",
                        "processname": "gwrd",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 3300,
                        "protocol": "RFC",
                        "processname": "gwrd",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 4800,
                        "protocol": "RFC SNC",
                        "processname": "gwrd",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 4800,
                        "protocol": "RFC SNC",
                        "processname": "gwrd",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 3200,
                        "protocol": "DPTM",
                        "processname": "disp+work",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 3200,
                        "protocol": "DPTM",
                        "processname": "disp+work",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 40000,
                        "protocol": "IGS",
                        "processname": "igsmux",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 40000,
                        "protocol": "IGS",
                        "processname": "igsmux",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 40080,
                        "protocol": "HTTP",
                        "processname": "igsmux",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 40080,
                        "protocol": "HTTP",
                        "processname": "igsmux",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 40001,
                        "protocol": "IGS",
                        "processname": "igspw",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 40001,
                        "protocol": "IGS",
                        "processname": "igspw",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 40002,
                        "protocol": "IGS",
                        "processname": "igspw",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 40002,
                        "protocol": "IGS",
                        "processname": "igspw",
                        "active": "Yes"
                    }
                ],
                "Environment":
                {
                    "LOGNAME": "npladm",
                    "HOME": "/home/npladm",
                    "SHELL": "/bin/csh",
                    "TERM": "vt100",
                    "PATH": "/home/npladm/bin:/usr/local/bin:/bin:/usr/bin:/usr/lib/mit/bin:/usr/sap/NPL/SYS/exe/uc/linuxx86_64:/usr/sap/NPL/SYS/exe/run:/home/npladm:/sybase/NPL/ASE-16_0/jobscheduler/bin:/sybase/NPL/ASE-16_0/bin:/sybase/NPL/ASE-16_0/install:/sybase/NPL/OCS-16_0/bin:",
                    "HOSTTYPE": "x86_64",
                    "VENDOR": "unknown",
                    "OSTYPE": "linux",
                    "MACHTYPE": "x86_64-suse-linux",
                    "SHLVL": "1",
                    "PWD": "/home/npladm",
                    "USER": "npladm",
                    "GROUP": "sapsys",
                    "HOST": "sid-npl",
                    "CSHEDIT": "emacs",
                    "MAIL": "/var/spool/mail/npladm",
                    "CPU": "x86_64",
                    "HOSTNAME": "sid-npl",
                    "LESS": "-M -I -R",
                    "LESSOPEN": "lessopen.sh %s",
                    "LESSCLOSE": "lessclose.sh %s %s",
                    "LESS_ADVANCED_PREPROCESSOR": "no",
                    "LESSKEY": "/etc/lesskey.bin",
                    "PAGER": "less",
                    "MORE": "-sl",
                    "MINICOM": "-c on",
                    "MANPATH": "/usr/local/man:/usr/share/man",
                    "XKEYSYMDB": "/usr/X11R6/lib/X11/XKeysymDB",
                    "XNLSPATH": "/usr/X11R6/lib/X11/nls",
                    "COLORTERM": "1",
                    "JAVA_BINDIR": "/usr/lib64/jvm/jre-1.8.0-ibm/bin",
                    "JAVA_ROOT": "/usr/lib64/jvm/jre-1.8.0-ibm",
                    "JAVA_HOME": "/usr/lib64/jvm/jre-1.8.0-ibm",
                    "JRE_HOME": "/usr/lib64/jvm/jre-1.8.0-ibm",
                    "JDK_HOME": "/usr/lib64/jvm/java-1_8_0-ibm-1.8.0",
                    "SDK_HOME": "/usr/lib64/jvm/java-1_8_0-ibm-1.8.0",
                    "XCURSOR_THEME": "DMZ",
                    "QT_SYSTEM_DIR": "/usr/share/desktop-data",
                    "LANG": "C.UTF-8",
                    "FROM_HEADER": "",
                    "WINDOWMANAGER": "xterm",
                    "XDG_DATA_DIRS": "/usr/local/share:/usr/share",
                    "XDG_CONFIG_DIRS": "/etc/xdg",
                    "G_BROKEN_FILENAMES": "1",
                    "CSHRCREAD": "true",
                    "LS_COLORS": "no",
                    "LS_OPTIONS": "-N --color",
                    "GPG_TTY": "/dev/pts/1",
                    "SAPSYSTEMNAME": "NPL",
                    "DIR_LIBRARY": "/usr/sap/NPL/SYS/exe/run",
                    "RSEC_SSFS_DATAPATH": "/usr/sap/NPL/SYS/global/security/rsecssfs/data",
                    "RSEC_SSFS_KEYPATH": "/usr/sap/NPL/SYS/global/security/rsecssfs/key",
                    "rsdb_ssfs_connect": "1",
                    "LD_LIBRARY_PATH": "/usr/sap/NPL/D00/exe:/usr/sap/NPL/SYS/exe/run:/usr/sap/NPL/SYS/exe/uc/linuxx86_64:/usr/sap/NPL/SYS/global/syb/linuxx86_64/sybodbc:/sybase/NPL/ASE-16_0/lib:/sybase/NPL/OCS-16_0/lib:/sybase/NPL/OCS-16_0/lib3p64:/sybase/NPL/OCS-16_0/lib3p:",
                    "INCLUDE": "/sybase/NPL/OCS-16_0/include:",
                    "LIB": "/sybase/NPL/OCS-16_0/lib:",
                    "SAP_JRE7_32": "/sybase/NPL/shared/SAPJRE-7_1_043_32BIT",
                    "SAP_JRE7": "/sybase/NPL/shared/SAPJRE-7_1_043_64BIT",
                    "SAP_JRE7_64": "/sybase/NPL/shared/SAPJRE-7_1_043_64BIT",
                    "SYBASE_OCS": "OCS-16_0",
                    "SYBASE": "/sybase/NPL",
                    "SYBASE_ASE": "ASE-16_0",
                    "SYBROOT": "/sybase/NPL",
                    "SYBASE_JRE_RTDS": "/sybase/NPL/shared/SAPJRE-7_1_043_64BIT",
                    "SYBASE_WS": "WS-16_0",
                    "dbms_type": "syb",
                    "dbs_syb_schema": "SAPSR3",
                    "dbs_syb_server": "wdflbmd16697",
                    "dbs_syb_dbname": "NPL",
                    "dbs_syb_port": "4901",
                    "dbs_syb_ssl": "0"
                },
                "StartProfile":
                {
                    "name": "/usr/sap/NPL/SYS/profile/NPL_D00_vhcalnplci",
                    "lines":
                    [
                        "#.******************************************************************************************************************************",
                        "#.*                                                                                                                            *",
                        "#.*       Instance profile NPL_D00_VHCALNPLCI                                                                                  *",
                        "#.*                                                                                                                            *",
                        "#.*       Version                 = 000002                                                                                     *",
                        "#.*       Generated by user = DDIC                                                                                             *",
                        "#.*       Generated on = 12.03.2023 , 19:56:00                                                                                 *",
                        "#.*                                                                                                                            *",
                        "#.******************************************************************************************************************************",
                        "SAPSYSTEMNAME = NPL",
                        "SAPSYSTEM = 00",
                        "INSTANCE_NAME = D00",
                        "DIR_CT_RUN = $(DIR_EXE_ROOT)$(DIR_SEP)$(OS_UNICODE)$(DIR_SEP)linuxx86_64",
                        "DIR_EXECUTABLE = $(DIR_INSTANCE)/exe",
                        "SAPLOCALHOST = vhcalnplci",
                        "DIR_PROFILE = $(DIR_INSTALL)/profile",
                        "_PF = $(DIR_PROFILE)/NPL_D00_vhcalnplci",
                        "SETENV_00 = DIR_LIBRARY=$(DIR_LIBRARY)",
                        "SETENV_01 = LD_LIBRARY_PATH=$(DIR_LIBRARY):%(LD_LIBRARY_PATH)",
                        "SETENV_02 = SHLIB_PATH=$(DIR_LIBRARY):%(SHLIB_PATH)",
                        "SETENV_03 = LIBPATH=$(DIR_LIBRARY):%(LIBPATH)",
                        "SETENV_04 = PATH=$(DIR_EXECUTABLE):%(PATH)",
                        "#-----------------------------------------------------------------------",
                        "# Copy SAP Executables",
                        "#-----------------------------------------------------------------------",
                        "# Change for release 751",
                        "# Change for release 751",
                        "Execute_00 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PF)",
                        "# SYB change for release 751",
                        "Execute_01 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPJDBC)",
                        "# SYB change for release 751",
                        "Execute_02 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPODBC)",
                        "# SYB change for release 751",
                        "Execute_03 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPJDBC)",
                        "# SYB change for release 751",
                        "Execute_04 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPODBC)",
                        "# Change for release 751",
                        "#Execute_01 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PF)",
                        "# SYB change for release 751",
                        "Execute_06 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPJDBC)",
                        "# SYB change for release 751",
                        "Execute_07 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPODBC)",
                        "# SYB change for release 751",
                        "Execute_08 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPJDBC)",
                        "# SYB change for release 751",
                        "Execute_09 = immediate $(DIR_CT_RUN)$(DIR_SEP)sapcpe$(FT_EXE) pf=$(_PFL) $(_CPE) $(_CPODBC)",
                        "# Change for release 751",
                        "#Execute_01 = immediate $(DIR_CT_RUN)/sapcpe$(FT_EXE) pf=$(_PF)",
                        "_CPARG0 = list:$(DIR_GLOBAL)/syb/linuxx86_64/cpe_sybjdbc.lst",
                        "_CPARG1 = source:$(DIR_GLOBAL)/syb/linuxx86_64",
                        "Execute_11 = immediate $(DIR_CT_RUN)/sapcpe$(FT_EXE) pf=$(_PF) $(_CPARG0) $(_CPARG1)",
                        "# Change for release 751",
                        "#Execute_03 = immediate $(DIR_CT_RUN)/sapcpe$(FT_EXE) pf=$(_PF)",
                        "_CPARG2 = list:$(DIR_GLOBAL)/syb/linuxx86_64/cpe_sybodbc.lst",
                        "_CPARG3 = source:$(DIR_GLOBAL)/syb/linuxx86_64/sybodbc",
                        "Execute_13 = immediate $(DIR_CT_RUN)/sapcpe$(FT_EXE) pf=$(_PF) $(_CPARG2) $(_CPARG3)",
                        "_CPARG4 = list:$(DIR_CT_RUN)/sapcrypto.lst",
                        "Execute_14 = immediate $(DIR_CT_RUN)/sapcpe$(FT_EXE) pf=$(_PF) $(_CPARG4)",
                        "#-----------------------------------------------------------------------",
                        "# Start ABAP database",
                        "#-----------------------------------------------------------------------",
                        "Execute_15 = immediate $(DIR_CT_RUN)/startdb",
                        "exe/saposcol = $(DIR_CT_RUN)/saposcol",
                        "rdisp/wp_no_dia = 6",
                        "rdisp/wp_no_btc = 4",
                        "rdisp/wp_no_vb = 1",
                        "rdisp/wp_no_vb2 = 1",
                        "rdisp/wp_no_spo = 1",
                        "exe/icmbnd = $(DIR_CT_RUN)/icmbnd",
                        "#-----------------------------------------------------------------------",
                        "# Start SCSA administration",
                        "#-----------------------------------------------------------------------",
                        "Execute_16 = local $(DIR_EXECUTABLE)/sapmscsa pf=$(_PF) -n",
                        "#-----------------------------------------------------------------------",
                        "# Start application server",
                        "#-----------------------------------------------------------------------",
                        "_DW = dw.sap$(SAPSYSTEMNAME)_$(INSTANCE_NAME)",
                        "Execute_17 = local rm -f $(_DW)",
                        "Execute_18 = local ln -s -f $(DIR_EXECUTABLE)/disp+work$(FT_EXE) $(_DW)",
                        "Start_Program_00 = local $(_DW) pf=$(_PF)",
                        "#-----------------------------------------------------------------------",
                        "# Start internet graphics server",
                        "#-----------------------------------------------------------------------",
                        "_IG = ig.sap$(SAPSYSTEMNAME)_$(INSTANCE_NAME)",
                        "# Start IGS",
                        "#Execute_14 = local rm -f $(_IG)",
                        "# Start IGS",
                        "#Execute_15 = local ln -s -f $(DIR_EXECUTABLE)/igswd_mt $(_IG)",
                        "# Start IGS",
                        "# Start IGS",
                        "#Execute_21 = local rm -f $(_IG)",
                        "# Start IGS",
                        "# Start IGS",
                        "#Execute_22 = local ln -s -f $(DIR_EXECUTABLE)/igswd_mt $(_IG)",
                        "# Start IGS",
                        "Execute_23 = local rm -f $(_IG)",
                        "# Start IGS",
                        "Execute_24 = local ln -s -f $(DIR_EXECUTABLE)/igswd_mt $(_IG)",
                        "# Start IGS",
                        "#Start_Program_01 = local $(_IG) -mode=profile pf=$(_PF)",
                        "# Start IGS",
                        "# Start IGS",
                        "#Start_Program_02 = local $(_IG) -mode=profile pf=$(_PF)",
                        "# Start IGS",
                        "Start_Program_03 = local $(_IG) -mode=profile pf=$(_PF)",
                        "SETENV_05 = SECUDIR=$(DIR_INSTANCE)/sec",
                        "ipc/shm_psize_10 = 124000000",
                        "ipc/shm_psize_40 = 1722000000",
                        "# SYB change for release 751",
                        "_CPE = copy_links target:$(DIR_EXECUTABLE)",
                        "_SYBLST = $(DIR_GLOBAL)$(DIR_SEP)syb$(DIR_SEP)linuxx86_64",
                        "_DIRODBC = $(DIR_GLOBAL)$(DIR_SEP)syb$(DIR_SEP)linuxx86_64$(DIR_SEP)sybodbc",
                        "_CPJDBC = list:$(_SYBLST)$(DIR_SEP)cpe_sybjdbc.lst source:$(_SYBLST)",
                        "_CPODBC = list:$(_SYBLST)$(DIR_SEP)cpe_sybodbc.lst source:$(_DIRODBC)",
                        "_PFL = $(DIR_PROFILE)$(DIR_SEP)NPL_D00_vhcalnplci",
                        "SAPFQDN = dummy.nodomain",
                        "#SAPLOCALHOSTFULL = $(SAPLOCALHOST).$(SAPFQDN)",
                        "SAPLOCALHOSTFULL = $(SAPLOCALHOST).$(SAPFQDN)",
                        "icm/server_port_4 = PROT=HTTP, PORT=50000, PROCTIMEOUT=300, TIMEOUT=300",
                        "icm/server_port_5 = PROT=HTTPS, PORT=50001, PROCTIMEOUT=300, TIMEOUT=300",
                        "icm/server_port_2 = PROT=SMTP, PORT=0, PROCTIMEOUT=300, TIMEOUT=300",
                        "icm/server_port_3 = PROT=HTTP, PORT=8101, PROCTIMEOUT=300, TIMEOUT=300",
                        "abap/shared_objects_size_MB = 1024",
                        "PHYS_MEMSIZE = 30%",
                        "em/initial_size_MB = ($(PHYS_MEMSIZE)*0.7)",
                        "#abap/buffersize = (ceil($(em/initial_size_MB)*1024*0.15/4096)*4096)",
                        "gw/alternative_hostnames = abapci,abapci.dummy.nodomain",
                        "login/create_sso2_ticket = 2",
                        "login/accept_sso2_ticket = 1",
                        "icm/server_port_0 = PROT=HTTP,PORT=80$$,PROCTIMEOUT=600,TIMEOUT=600",
                        "icm/server_port_1 = PROT=HTTPS,PORT=443$$,PROCTIMEOUT=600,TIMEOUT=600"
                    ]
                },
                "HAFailoverConfig":
                {
                    "HAActive": false,
                    "HAProductVersion": null,
                    "HASAPInterfaceVersion": null,
                    "HADocumentation": null,
                    "HAActiveNode": null,
                    "HANodes": ""
                }
            },
            {
                "mSid": "NPL",
                "mHostname": "vhcalnplcs",
                "mSystemNumber": "01",
                "mSapVersionInfo": "749, patch 10, changelist 1698137",
                "VersionInfo":
                [
                    {
                        "Filename": "/usr/sap/NPL/ASCS01/exe/sapstartsrv",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/ASCS01/exe/gwrd",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/ASCS01/exe/msg_server",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/ASCS01/exe/enserver",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/ASCS01/exe/enq_server",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    },
                    {
                        "Filename": "/usr/sap/NPL/ASCS01/exe/sapwebdisp",
                        "VersionInfo": "749, patch 10, changelist 1698137, RKS compatibility level 0, optU (Aug 23 2016, 17:53:49), linuxx86_64",
                        "Time": "2022 08 19 08:37:20"
                    }
                ],
                "InstanceProperties":
                [
                    {
                        "property": "Process List",
                        "propertytype": "NodeWebmethod",
                        "value": "GetProcessList"
                    },
                    {
                        "property": "Access Points",
                        "propertytype": "NodeWebmethod",
                        "value": "GetAccessPointList"
                    },
                    {
                        "property": "Parameter Documentation",
                        "propertytype": "NodeURL",
                        "value": "http://vhcalnplcs:50113/sapparamEN.html"
                    },
                    {
                        "property": "Kernel Update",
                        "propertytype": "NodeURL",
                        "value": "http://service.sap.com/~form/handler?_APP=00200682500000001943&_EVENT=DISPHIER&HEADER=Y&FUNCTIONBAR=N&EVENT=TREE&NE=NAVIGATE&ENR=73554900100200004760&V=MAINT"
                    },
                    {
                        "property": "Syslog",
                        "propertytype": "NodeWebmethod",
                        "value": "ABAPReadSyslog"
                    },
                    {
                        "property": "Enque Locks",
                        "propertytype": "NodeWebmethod",
                        "value": "EnqGetLockTable"
                    },
                    {
                        "property": "Enque Statistic",
                        "propertytype": "NodeWebmethod",
                        "value": "EnqGetStatistic"
                    },
                    {
                        "property": "Protected Webmethods",
                        "propertytype": "Attribute",
                        "value": "ABAPAcknowledgeAlerts,ABAPCheckRFCDestinations,ABAPGetComponentList,ABAPGetSystemWPTable,ABAPGetWPTable,ABAPReadRawSyslog,ABAPReadSyslog,AnalyseLogFiles,Bootstrap,CheckParameter,CheckPSE,CheckUpdateSystem,ConfigureLogFileList,CreatePSECredential,CreateSnapshot,DeletePSE,DeleteSnapshots,EnqGetLockTable,EnqGetStatistic,EnqRemoveLocks,EnqRemoveUserLocks,GetAccessPointList,GetAlerts,GetAlertTree,GetCallstack,GetEnvironment,GetLogFileList,GetProcessParameter,GetQueueStatistic,GetStartProfile,GetSystemUpdateList,GetTraceFile,GetVersionInfo,HACheckConfig,HACheckFailoverConfig,HAFailoverToNode,HAGetFailoverConfig,HASetMaintenanceMode,ICMGetCacheEntries,ICMGetConnectionList,ICMGetProxyConnectionList,ICMGetThreadList,InstanceStart,InstanceStop,J2EEControlCluster,J2EEControlComponents,J2EEControlProcess,J2EEDisableDbgSession,J2EEEnableDbgSession,J2EEGetApplicationAliasList,J2EEGetCacheStatistic,J2EEGetCacheStatistic2,J2EEGetClusterMsgList,J2EEGetComponentList,J2EEGetEJBSessionList,J2EEGetProcessList,J2EEGetProcessList2,J2EEGetRemoteObjectList,J2EEGetSessionList,J2EEGetSharedTableInfo,J2EEGetThreadCallStack,J2EEGetThreadList,J2EEGetThreadList2,J2EEGetThreadTaskStack,J2EEGetVMGCHistory,J2EEGetVMGCHistory2,J2EEGetVMHeapInfo,J2EEGetWebSessionList,J2EEGetWebSessionList2,ListDeveloperTraces,ListLogFiles,ListSnapshots,OSExecute,ParameterValue,ReadDeveloperTrace,ReadLogFile,ReadSnapshot,RestartInstance,RestartService,RestartSystem,SendSignal,SetProcessParameter,SetProcessParameter2,ShmDetach,Shutdown,Start,StartBypassHA,StartSystem,Stop,StopBypassHA,StopService,StopSystem,StorePSE,UpdateInstancePSE,UpdateSCSInstance,UpdateSystem,UpdateSystemPKI,WebDispGetServerList,WebDispGetGroupList,WebDispGetVirtHostList,WebDispGetUrlPrefixList,GetAgentConfig,MtChangeStatus,MtCustomizeWrite,MtDbsetToWpsetByTid,MtDestroyMarkNTry,MtReset,PerfCustomizeWrite,ReadDirectory,ReadFile,ReadProfileParameters,Register,SnglmgsCustomizeWrite,SystemObjectSetValue,ToolSet,ToolSetRuntimeStatus,TriggerDataCollection,Unregister,UtilAlChangeStatus"
                    },
                    {
                        "property": "CentralServices",
                        "propertytype": "Attribute",
                        "value": "YES"
                    },
                    {
                        "property": "StartPriority",
                        "propertytype": "Attribute",
                        "value": "1"
                    },
                    {
                        "property": "SAPSYSTEM",
                        "propertytype": "Attribute",
                        "value": "01"
                    },
                    {
                        "property": "SAPSYSTEMNAME",
                        "propertytype": "Attribute",
                        "value": "NPL"
                    },
                    {
                        "property": "SAPLOCALHOST",
                        "propertytype": "Attribute",
                        "value": "vhcalnplcs"
                    },
                    {
                        "property": "INSTANCE_NAME",
                        "propertytype": "Attribute",
                        "value": "ASCS01"
                    },
                    {
                        "property": "SupportsUpdateSCSInstance",
                        "propertytype": "Attribute",
                        "value": "YES"
                    },
                    {
                        "property": "Webmethods",
                        "propertytype": "Attribute",
                        "value": "Start,InstanceStart,StartBypassHA,Bootstrap,Stop,InstanceStop,StopBypassHA,Shutdown,ParameterValue,GetProcessList,GetStartProfile,GetTraceFile,GetAlertTree,GetAlerts,RestartService,StopService,GetEnvironment,ListDeveloperTraces,ReadDeveloperTrace,RestartInstance,SendSignal,GetVersionInfo,GetQueueStatistic,GetInstanceProperties,OSExecute,ReadLogFile,AnalyseLogFiles,ListLogFiles,GetAccessPointList,GetSystemInstanceList,GetSystemUpdateList,StartSystem,StopSystem,RestartSystem,UpdateSystem,UpdateSCSInstance,CheckUpdateSystem,AccessCheck,GetProcessParameter,SetProcessParameter,SetProcessParameter2,CheckParameter,ShmDetach,GetNetworkId,GetSecNetworkId,RequestLogonFile,CreateSnapshot,ReadSnapshot,ListSnapshots,DeleteSnapshots,GetCallstack,ABAPReadSyslog,ABAPReadRawSyslog,ABAPGetWPTable,ABAPAcknowledgeAlerts,ABAPGetComponentList,ABAPCheckRFCDestinations,ABAPGetSystemWPTable,J2EEGetProcessList,J2EEGetProcessList2,J2EEControlProcess,J2EEGetThreadList,J2EEGetThreadList2,J2EEGetThreadCallStack,J2EEGetThreadTaskStack,J2EEGetSessionList,J2EEGetWebSessionList,J2EEGetWebSessionList2,J2EEGetCacheStatistic,J2EEGetCacheStatistic2,J2EEGetApplicationAliasList,J2EEGetVMGCHistory,J2EEGetVMGCHistory2,J2EEGetVMHeapInfo,J2EEGetEJBSessionList,J2EEGetRemoteObjectList,J2EEGetClusterMsgList,J2EEGetSharedTableInfo,J2EEGetComponentList,J2EEControlComponents,ICMGetThreadList,ICMGetConnectionList,ICMGetCacheEntries,ICMGetProxyConnectionList,WebDispGetServerList,WebDispGetGroupList,WebDispGetVirtHostList,WebDispGetUrlPrefixList,EnqGetLockTable,EnqRemoveLocks,EnqRemoveUserLocks,EnqGetStatistic,UpdateSystemPKI,UpdateInstancePSE,StorePSE,DeletePSE,CheckPSE,HACheckConfig,HACheckFailoverConfig,HAGetFailoverConfig,HAFailoverToNodeHASetMaintenanceMode"
                    }
                ],
                "ProcessList":
                [
                    {
                        "name": "msg_server",
                        "description": "MessageServer",
                        "dispstatus": "SAPControl-GREEN",
                        "textstatus": "Running",
                        "starttime": "2023 04 14 05:31:52",
                        "elapsedtime": "1:44:33",
                        "pid": 2864
                    },
                    {
                        "name": "enserver",
                        "description": "EnqueueServer",
                        "dispstatus": "SAPControl-GREEN",
                        "textstatus": "Running",
                        "starttime": "2023 04 14 05:31:52",
                        "elapsedtime": "1:44:33",
                        "pid": 2865
                    }
                ],
                "AccessPointList":
                [
                    {
                        "address": "127.0.0.1",
                        "port": 50113,
                        "protocol": "HTTP",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 50113,
                        "protocol": "HTTP",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 50114,
                        "protocol": "HTTPS",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 50114,
                        "protocol": "HTTPS",
                        "processname": "sapstartsrv",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 3201,
                        "protocol": "ENQ",
                        "processname": "enserver",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 3201,
                        "protocol": "ENQ",
                        "processname": "enserver",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 3901,
                        "protocol": "MS",
                        "processname": "msg_server",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 3901,
                        "protocol": "MS",
                        "processname": "msg_server",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 3601,
                        "protocol": "MS",
                        "processname": "msg_server",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 3601,
                        "protocol": "MS",
                        "processname": "msg_server",
                        "active": "Yes"
                    },
                    {
                        "address": "127.0.0.1",
                        "port": 8101,
                        "protocol": "HTTP",
                        "processname": "msg_server",
                        "active": "Yes"
                    },
                    {
                        "address": "10.0.0.234",
                        "port": 8101,
                        "protocol": "HTTP",
                        "processname": "msg_server",
                        "active": "Yes"
                    }
                ],
                "Environment":
                {
                    "LOGNAME": "npladm",
                    "HOME": "/home/npladm",
                    "SHELL": "/bin/csh",
                    "TERM": "vt100",
                    "PATH": "/home/npladm/bin:/usr/local/bin:/bin:/usr/bin:/usr/lib/mit/bin:/usr/sap/NPL/SYS/exe/uc/linuxx86_64:/usr/sap/NPL/SYS/exe/run:/home/npladm:/sybase/NPL/ASE-16_0/jobscheduler/bin:/sybase/NPL/ASE-16_0/bin:/sybase/NPL/ASE-16_0/install:/sybase/NPL/OCS-16_0/bin:",
                    "HOSTTYPE": "x86_64",
                    "VENDOR": "unknown",
                    "OSTYPE": "linux",
                    "MACHTYPE": "x86_64-suse-linux",
                    "SHLVL": "1",
                    "PWD": "/home/npladm",
                    "USER": "npladm",
                    "GROUP": "sapsys",
                    "HOST": "sid-npl",
                    "CSHEDIT": "emacs",
                    "MAIL": "/var/spool/mail/npladm",
                    "CPU": "x86_64",
                    "HOSTNAME": "sid-npl",
                    "LESS": "-M -I -R",
                    "LESSOPEN": "lessopen.sh %s",
                    "LESSCLOSE": "lessclose.sh %s %s",
                    "LESS_ADVANCED_PREPROCESSOR": "no",
                    "LESSKEY": "/etc/lesskey.bin",
                    "PAGER": "less",
                    "MORE": "-sl",
                    "MINICOM": "-c on",
                    "MANPATH": "/usr/local/man:/usr/share/man",
                    "XKEYSYMDB": "/usr/X11R6/lib/X11/XKeysymDB",
                    "XNLSPATH": "/usr/X11R6/lib/X11/nls",
                    "COLORTERM": "1",
                    "JAVA_BINDIR": "/usr/lib64/jvm/jre-1.8.0-ibm/bin",
                    "JAVA_ROOT": "/usr/lib64/jvm/jre-1.8.0-ibm",
                    "JAVA_HOME": "/usr/lib64/jvm/jre-1.8.0-ibm",
                    "JRE_HOME": "/usr/lib64/jvm/jre-1.8.0-ibm",
                    "JDK_HOME": "/usr/lib64/jvm/java-1_8_0-ibm-1.8.0",
                    "SDK_HOME": "/usr/lib64/jvm/java-1_8_0-ibm-1.8.0",
                    "XCURSOR_THEME": "DMZ",
                    "QT_SYSTEM_DIR": "/usr/share/desktop-data",
                    "LANG": "C.UTF-8",
                    "FROM_HEADER": "",
                    "WINDOWMANAGER": "xterm",
                    "XDG_DATA_DIRS": "/usr/local/share:/usr/share",
                    "XDG_CONFIG_DIRS": "/etc/xdg",
                    "G_BROKEN_FILENAMES": "1",
                    "CSHRCREAD": "true",
                    "LS_COLORS": "no",
                    "LS_OPTIONS": "-N --color",
                    "GPG_TTY": "/dev/pts/1",
                    "SAPSYSTEMNAME": "NPL",
                    "DIR_LIBRARY": "/usr/sap/NPL/SYS/exe/run",
                    "RSEC_SSFS_DATAPATH": "/usr/sap/NPL/SYS/global/security/rsecssfs/data",
                    "RSEC_SSFS_KEYPATH": "/usr/sap/NPL/SYS/global/security/rsecssfs/key",
                    "rsdb_ssfs_connect": "1",
                    "LD_LIBRARY_PATH": "/usr/sap/NPL/ASCS01/exe:/usr/sap/NPL/SYS/exe/run:/usr/sap/NPL/SYS/exe/uc/linuxx86_64:/usr/sap/NPL/SYS/global/syb/linuxx86_64/sybodbc:/sybase/NPL/ASE-16_0/lib:/sybase/NPL/OCS-16_0/lib:/sybase/NPL/OCS-16_0/lib3p64:/sybase/NPL/OCS-16_0/lib3p:",
                    "INCLUDE": "/sybase/NPL/OCS-16_0/include:",
                    "LIB": "/sybase/NPL/OCS-16_0/lib:",
                    "SAP_JRE7_32": "/sybase/NPL/shared/SAPJRE-7_1_043_32BIT",
                    "SAP_JRE7": "/sybase/NPL/shared/SAPJRE-7_1_043_64BIT",
                    "SAP_JRE7_64": "/sybase/NPL/shared/SAPJRE-7_1_043_64BIT",
                    "SYBASE_OCS": "OCS-16_0",
                    "SYBASE": "/sybase/NPL",
                    "SYBASE_ASE": "ASE-16_0",
                    "SYBROOT": "/sybase/NPL",
                    "SYBASE_JRE_RTDS": "/sybase/NPL/shared/SAPJRE-7_1_043_64BIT",
                    "SYBASE_WS": "WS-16_0",
                    "dbms_type": "syb",
                    "dbs_syb_schema": "SAPSR3",
                    "dbs_syb_server": "wdflbmd16697",
                    "dbs_syb_dbname": "NPL",
                    "dbs_syb_port": "4901",
                    "dbs_syb_ssl": "0"
                },
                "StartProfile":
                {
                    "name": "/usr/sap/NPL/SYS/profile/NPL_ASCS01_vhcalnplcs",
                    "lines":
                    [
                        "#.******************************************************************************************************************************",
                        "#.*                                                                                                                            *",
                        "#.*       Instanzprofil NPL_ASCS01_VHCALNPLCS                                                                                  *",
                        "#.*                                                                                                                            *",
                        "#.*       Version                 = 000001                                                                                     *",
                        "#.*       Generiert von Benutzer  = DDIC                                                                                       *",
                        "#.*       Datum der Generierung   = 25.09.2017 , 07:43:55                                                                      *",
                        "#.*                                                                                                                            *",
                        "#.******************************************************************************************************************************",
                        "SAPSYSTEMNAME = NPL",
                        "SAPSYSTEM = 01",
                        "INSTANCE_NAME = ASCS01",
                        "DIR_CT_RUN = $(DIR_EXE_ROOT)$(DIR_SEP)$(OS_UNICODE)$(DIR_SEP)linuxx86_64",
                        "DIR_EXECUTABLE = $(DIR_INSTANCE)/exe",
                        "SAPLOCALHOST = vhcalnplcs",
                        "DIR_PROFILE = $(DIR_INSTALL)/profile",
                        "_PF = $(DIR_PROFILE)/NPL_ASCS01_vhcalnplcs",
                        "SETENV_00 = DIR_LIBRARY=$(DIR_LIBRARY)",
                        "SETENV_01 = LD_LIBRARY_PATH=$(DIR_LIBRARY):%(LD_LIBRARY_PATH)",
                        "SETENV_02 = SHLIB_PATH=$(DIR_LIBRARY):%(SHLIB_PATH)",
                        "SETENV_03 = LIBPATH=$(DIR_LIBRARY):%(LIBPATH)",
                        "SETENV_04 = PATH=$(DIR_EXECUTABLE):%(PATH)",
                        "#-----------------------------------------------------------------------",
                        "# Copy SAP Executables",
                        "#-----------------------------------------------------------------------",
                        "_CPARG0 = list:$(DIR_CT_RUN)/scs.lst",
                        "Execute_00 = immediate $(DIR_CT_RUN)/sapcpe$(FT_EXE) pf=$(_PF) $(_CPARG0)",
                        "_CPARG1 = list:$(DIR_CT_RUN)/sapcrypto.lst",
                        "Execute_01 = immediate $(DIR_CT_RUN)/sapcpe$(FT_EXE) pf=$(_PF) $(_CPARG1)",
                        "#-----------------------------------------------------------------------",
                        "# Start SAP message server",
                        "#-----------------------------------------------------------------------",
                        "_MS = ms.sap$(SAPSYSTEMNAME)_$(INSTANCE_NAME)",
                        "Execute_02 = local rm -f $(_MS)",
                        "Execute_03 = local ln -s -f $(DIR_EXECUTABLE)/msg_server$(FT_EXE) $(_MS)",
                        "Restart_Program_00 = local $(_MS) pf=$(_PF)",
                        "#-----------------------------------------------------------------------",
                        "# Start SAP enqueue server",
                        "#-----------------------------------------------------------------------",
                        "_EN = en.sap$(SAPSYSTEMNAME)_$(INSTANCE_NAME)",
                        "Execute_04 = local rm -f $(_EN)",
                        "Execute_05 = local ln -s -f $(DIR_EXECUTABLE)/enserver$(FT_EXE) $(_EN)",
                        "Restart_Program_01 = local $(_EN) pf=$(_PF)",
                        "#-----------------------------------------------------------------------",
                        "# SAP Message Server parameters are set in the DEFAULT.PFL",
                        "#-----------------------------------------------------------------------",
                        "ms/standalone = 1",
                        "ms/server_port_0 = PROT=HTTP,PORT=81$$",
                        "#-----------------------------------------------------------------------",
                        "# SAP Enqueue Server",
                        "#-----------------------------------------------------------------------",
                        "enque/table_size = 64000",
                        "enque/snapshot_pck_ids = 1600",
                        "enque/server/max_query_requests = 5000",
                        "enque/server/max_requests = 5000",
                        "enque/server/threadcount = 4",
                        "rdisp/enqname = $(rdisp/myname)",
                        "SETENV_05 = SECUDIR=$(DIR_INSTANCE)/sec",
                        "SAPFQDN = dummy.nodomain",
                        "SAPLOCALHOSTFULL = $(SAPLOCALHOST).$(SAPFQDN)"
                    ]
                },
                "HAFailoverConfig":
                {
                    "HAActive": false,
                    "HAProductVersion": null,
                    "HASAPInterfaceVersion": null,
                    "HADocumentation": null,
                    "HAActiveNode": null,
                    "HANodes": ""
                }
            }
        ]

databases:
    description: SAP databases installed on a host
    type: list
    returned: success
    sample: |-
        [
            {
                "mStatus": "SAPHostControl-DB-RUNNING",
                "mDatabase":
                {
                    "Database/InstanceName": "NPL",
                    "Database/Host": "sid-npl",
                    "Database/Vendor": "SYB",
                    "Database/Type": "syb",
                    "Database/Release": "16.0.02.05",
                    "Database/Name": "NPL",
                    "Database/Status": "Running"
                },
                "mComponents":
                [
                    {
                        "mProperties":
                        {
                            "Database/ComponentName": "Client",
                            "Database/ComponentDescription": "SYBASE Server Client Software",
                            "Database/ComponentStatusDescription": "SAP ASE Server client software is configured properly."
                        },
                        "mStatus": "SAPHostControl-DB-RUNNING"
                    },
                    {
                        "mProperties":
                        {
                            "Database/ComponentName": "Server",
                            "Database/ComponentDescription": "SYBASE Server Software",
                            "Database/ComponentStatusDescription": "The database server is running and configured properly."
                        },
                        "mStatus": "SAPHostControl-DB-RUNNING"
                    },
                    {
                        "mProperties":
                        {
                            "Database/ComponentName": "Database",
                            "Database/ComponentDescription": "SYBASE Server Database",
                            "Database/ComponentStatusDescription": "The database is running and configured properly."
                        },
                        "mStatus": "SAPHostControl-DB-RUNNING"
                    },
                    {
                        "mProperties":
                        {
                            "Database/ComponentName": "Backup Server",
                            "Database/ComponentDescription": "SYBASE Backup Server Software",
                            "Database/ComponentStatusDescription": "Backup Server is running."
                        },
                        "mStatus": "SAPHostControl-DB-RUNNING"
                    },
                    {
                        "mProperties":
                        {
                            "Database/ComponentName": "Job Scheduler",
                            "Database/ComponentDescription": "SYBASE Job Scheduler",
                            "Database/ComponentStatusDescription": "Job Scheduler is running."
                        },
                        "mStatus": "SAPHostControl-DB-RUNNING"
                    },
                    {
                        "mProperties":
                        {
                            "Database/ComponentName": "RepAgent thread",
                            "Database/ComponentDescription": "SYBASE Replication Agent Thread",
                            "Database/ComponentStatusDescription": "Running Rep Agents:  / Stopped Rep Agents:"
                        },
                        "mStatus": "SAPHostControl-DB-RUNNING"
                    }
                ],
                "DatabaseProperties":
                {
                    "Database/IsRelocationTarget": "true",
                    "Database/IsRelocatable": "true",
                    "Database/IsSharedInstance": "true",
                    "Database/IsSharedNetService": "true",
                    "Database/Capability/CopyMethods": "Offline, Online",
                    "Database/MaxPhysMemSize": "7812",
                    "Database/CPUCount": "4",
                    "Database/ConfigurationDirectory/Default": "/sybase/NPL/sapdbctrl-config",
                    "Database/DBRelease": "16.0.02.05",
                    "Database/DBSysBits": "64",
                    "Database/Distribution": "local",
                    "Database/ConnectAddress": "Protocol=tcp;Host=wdflbmd16697;Port=4901",
                    "Database/ManagementHosts": "wdflbmd16697"
                },
                "DatabaseStatus":
                {
                    "result":
                    [
                        {
                            "mProperties":
                            {
                                "Database/ComponentName": "Client",
                                "Database/ComponentDescription": "SYBASE Server Client Software",
                                "Database/ComponentStatusDescription": "SAP ASE Server client software is configured properly."
                            },
                            "mStatus": "SAPHostControl-DB-RUNNING"
                        },
                        {
                            "mProperties":
                            {
                                "Database/ComponentName": "Server",
                                "Database/ComponentDescription": "SYBASE Server Software",
                                "Database/ComponentStatusDescription": "The database server is running and configured properly."
                            },
                            "mStatus": "SAPHostControl-DB-RUNNING"
                        },
                        {
                            "mProperties":
                            {
                                "Database/ComponentName": "Database",
                                "Database/ComponentDescription": "SYBASE Server Database",
                                "Database/ComponentStatusDescription": "The database is running and configured properly."
                            },
                            "mStatus": "SAPHostControl-DB-RUNNING"
                        },
                        {
                            "mProperties":
                            {
                                "Database/ComponentName": "Backup Server",
                                "Database/ComponentDescription": "SYBASE Backup Server Software",
                                "Database/ComponentStatusDescription": "Backup Server is running."
                            },
                            "mStatus": "SAPHostControl-DB-RUNNING"
                        },
                        {
                            "mProperties":
                            {
                                "Database/ComponentName": "Job Scheduler",
                                "Database/ComponentDescription": "SYBASE Job Scheduler",
                                "Database/ComponentStatusDescription": "Job Scheduler is running."
                            },
                            "mStatus": "SAPHostControl-DB-RUNNING"
                        },
                        {
                            "mProperties":
                            {
                                "Database/ComponentName": "RepAgent thread",
                                "Database/ComponentDescription": "SYBASE Replication Agent Thread",
                                "Database/ComponentStatusDescription": "Running Rep Agents:  / Stopped Rep Agents:"
                            },
                            "mStatus": "SAPHostControl-DB-RUNNING"
                        }
                    ],
                    "status": "SAPHostControl-DB-RUNNING"
                }
            }
        ]
"""  # noqa: E501

from ansible_collections.sap.sap_operations.plugins.module_utils.saphost import (
    AnsibleModuleSAPHostAgent,
    saphostctrl,
    sapcontrol,
    convert2ansible,
)


def main():
    module = AnsibleModuleSAPHostAgent(argument_spec={}, supports_check_mode=True)

    m = saphostctrl(
        hostname=module.params.get("hostname"),
        username=module.params.get("username"),
        password=module.params.get("password"),
        ca_file=module.params.get("ca_file"),
        security=module.params.get("security"),
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
            EnvironmentRaw = convert2ansible(instance_sapcontrol.client.service.GetEnvironment())
            instance["EnvironmentRaw"] = EnvironmentRaw
            instance["Environment"] = {
                line.split("=")[0]: line.split("=")[1]
                for line in EnvironmentRaw if "=" in line
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
                m.client.service.GetDatabaseProperties(aArguments=ArrayOfProperty)
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
