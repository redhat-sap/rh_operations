#!/usr/bin/python

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

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""

module: pcs_capabilities_info

extends_documentation_fragment: sap.sap_operations.community

author: Kirill Satarin (@kksat)

short_description: Get pacemaker capabilities

description:
  - Get pacemaker capabilities
  - This module will execute command C(pcs --version --full) and process results to present them nicely in Ansible
  - If pacemaker is not running, or ansible user does not have authorizations to execution C(pcs --version --full) command, module will fail
  - Required user with permissions to execute C(pcs --version --full) command

version_added: 1.4.0-galaxy

seealso:
  - module: sap.sap_operations.pcs_status_info
  - module: sap.sap_operations.pcs_cib_info

options: {}

"""

EXAMPLES = r"""
- name: Get pacemaker capabilities
  sap.sap_operations.pcs_capabilities_info:
"""

RETURN = r"""
pcs_version:
  description: pcs version
  returned: success
  type: str
  sample: "0.10.17"

pcs_version_full_raw:
  description: raw output of pcs --version --full
  returned: always
  type: str
  sample: |-
    0.10.17
    booth booth.enable-authfile.set booth.enable-authfile.unset cluster.config.backup-local cluster.config.restore-cluster cluster.config.restore-local cluster.config.uuid cluster.create cluster.create.enable cluster.create.local cluster.create.no-keys-sync cluster.create.separated-name-and-address cluster.create.start cluster.create.start.wait cluster.create.transport.knet cluster.create.transport.udp-udpu cluster.create.transport.udp-udpu.no-rrp cluster.destroy cluster.destroy.all cluster.report cluster.verify corosync.authkey.update corosync.config.get corosync.config.get.struct corosync.config.reload corosync.config.sync-to-local-cluster corosync.config.update corosync.link.add corosync.link.remove corosync.link.remove.list corosync.link.update corosync.qdevice corosync.qdevice.model.net corosync.quorum corosync.quorum.device corosync.quorum.device.heuristics corosync.quorum.device.model.net corosync.quorum.set-expected-votes-runtime corosync.quorum.status corosync.quorum.unblock corosync.totem.block_unlisted_ips corosync.uidgid node.add node.add.enable node.add.separated-name-and-address node.add.start node.add.start.wait node.attributes node.attributes.set-list-for-node node.confirm-off node.fence node.guest node.kill node.maintenance node.maintenance.all node.maintenance.list node.maintenance.wait node.remote node.remote.onfail-demote node.remove node.remove-from-caches node.remove.list node.standby node.standby.all node.standby.list node.standby.wait node.start-stop-enable-disable node.start-stop-enable-disable.all node.start-stop-enable-disable.list node.start-stop-enable-disable.start-wait node.utilization node.utilization.set-list-for-node pcmk.acl.enable-disable pcmk.acl.group pcmk.acl.role pcmk.acl.role.create-with-permissions pcmk.acl.role.delete-with-users-groups pcmk.acl.user pcmk.alert pcmk.cib.checkpoints pcmk.cib.checkpoints.diff pcmk.cib.edit pcmk.cib.get pcmk.cib.get.scope pcmk.cib.roles.promoted-unpromoted pcmk.cib.set pcmk.constraint.colocation.set pcmk.constraint.colocation.set.options pcmk.constraint.colocation.simple pcmk.constraint.colocation.simple.options pcmk.constraint.hide-expired pcmk.constraint.location.simple pcmk.constraint.location.simple.options pcmk.constraint.location.simple.resource-regexp pcmk.constraint.location.simple.rule pcmk.constraint.location.simple.rule.node-attr-type-number pcmk.constraint.location.simple.rule.options pcmk.constraint.location.simple.rule.rule-add-remove pcmk.constraint.no-autocorrect pcmk.constraint.order.set pcmk.constraint.order.set.options pcmk.constraint.order.simple pcmk.constraint.order.simple.options pcmk.constraint.ticket.set pcmk.constraint.ticket.set.options pcmk.constraint.ticket.simple pcmk.constraint.ticket.simple.constraint-id pcmk.properties.cluster pcmk.properties.cluster.config.output-formats pcmk.properties.cluster.defaults pcmk.properties.cluster.describe pcmk.properties.cluster.describe.output-formats pcmk.properties.operation-defaults pcmk.properties.operation-defaults.multiple pcmk.properties.operation-defaults.rule pcmk.properties.operation-defaults.rule-rsc-op pcmk.properties.operation-defaults.rule.hide-expired pcmk.properties.operation-defaults.rule.node-attr-type-number pcmk.properties.resource-defaults pcmk.properties.resource-defaults.multiple pcmk.properties.resource-defaults.rule pcmk.properties.resource-defaults.rule-rsc-op pcmk.properties.resource-defaults.rule.hide-expired pcmk.properties.resource-defaults.rule.node-attr-type-number pcmk.resource.ban-move-clear pcmk.resource.ban-move-clear.clear-expired pcmk.resource.bundle pcmk.resource.bundle.container-docker pcmk.resource.bundle.container-docker.promoted-max pcmk.resource.bundle.container-podman pcmk.resource.bundle.container-podman.promoted-max pcmk.resource.bundle.container-rkt pcmk.resource.bundle.container-rkt.promoted-max pcmk.resource.bundle.reset pcmk.resource.bundle.wait pcmk.resource.cleanup pcmk.resource.cleanup.one-resource pcmk.resource.cleanup.strict pcmk.resource.clone pcmk.resource.clone.custom-id pcmk.resource.clone.meta-in-create pcmk.resource.clone.wait pcmk.resource.config.output-formats pcmk.resource.create pcmk.resource.create.clone.custom-id pcmk.resource.create.in-existing-bundle pcmk.resource.create.meta pcmk.resource.create.no-master pcmk.resource.create.operations pcmk.resource.create.operations.onfail-demote pcmk.resource.create.promotable pcmk.resource.create.promotable.custom-id pcmk.resource.create.wait pcmk.resource.debug pcmk.resource.delete pcmk.resource.disable.safe pcmk.resource.disable.safe.brief pcmk.resource.disable.safe.tag pcmk.resource.disable.simulate pcmk.resource.disable.simulate.brief pcmk.resource.disable.simulate.tag pcmk.resource.enable-disable pcmk.resource.enable-disable.list pcmk.resource.enable-disable.tag pcmk.resource.enable-disable.wait pcmk.resource.failcount pcmk.resource.group pcmk.resource.group.add-remove-list pcmk.resource.group.wait pcmk.resource.manage-unmanage pcmk.resource.manage-unmanage.list pcmk.resource.manage-unmanage.tag pcmk.resource.manage-unmanage.with-monitor pcmk.resource.move.autoclean pcmk.resource.promotable pcmk.resource.promotable.custom-id pcmk.resource.promotable.meta-in-create pcmk.resource.promotable.wait pcmk.resource.refresh pcmk.resource.refresh.one-resource pcmk.resource.refresh.strict pcmk.resource.relations pcmk.resource.relocate pcmk.resource.restart pcmk.resource.update pcmk.resource.update-meta pcmk.resource.update-meta.list pcmk.resource.update-meta.wait pcmk.resource.update-operations pcmk.resource.update-operations.onfail-demote pcmk.resource.update.meta pcmk.resource.update.operations pcmk.resource.update.operations.onfail-demote pcmk.resource.update.wait pcmk.resource.utilization pcmk.resource.utilization-set-list-for-resource pcmk.stonith.cleanup pcmk.stonith.cleanup.one-resource pcmk.stonith.cleanup.strict pcmk.stonith.create pcmk.stonith.create.in-group pcmk.stonith.create.meta pcmk.stonith.create.operations pcmk.stonith.create.operations.onfail-demote pcmk.stonith.create.wait pcmk.stonith.delete pcmk.stonith.enable-disable pcmk.stonith.enable-disable.list pcmk.stonith.enable-disable.wait pcmk.stonith.history.cleanup pcmk.stonith.history.show pcmk.stonith.history.update pcmk.stonith.levels pcmk.stonith.levels.add-remove-devices-list pcmk.stonith.levels.clear pcmk.stonith.levels.node-attr pcmk.stonith.levels.node-regexp pcmk.stonith.levels.verify pcmk.stonith.refresh pcmk.stonith.refresh.one-resource pcmk.stonith.refresh.strict pcmk.stonith.update pcmk.stonith.update.scsi-devices pcmk.stonith.update.scsi-devices.add-remove pcmk.stonith.update.scsi-devices.mpath pcmk.tag pcmk.tag.resources pcs.auth.client pcs.auth.client.cluster pcs.auth.client.token pcs.auth.deauth-client pcs.auth.deauth-server pcs.auth.no-bidirectional pcs.auth.separated-name-and-address pcs.auth.server.token pcs.cfg-in-file.cib pcs.daemon-ssl-cert.set pcs.daemon-ssl-cert.sync-to-local-cluster pcs.disaster-recovery.essentials pcs.request-timeout resource-agents.describe resource-agents.list resource-agents.list.detailed resource-agents.ocf.version-1-0 resource-agents.ocf.version-1-1 resource-agents.self-validation sbd sbd.option-timeout-action sbd.shared-block-device status.corosync.membership status.pcmk.resources.hide-inactive status.pcmk.resources.id status.pcmk.resources.node status.pcmk.resources.orphaned status.pcmk.xml stonith-agents.describe stonith-agents.list stonith-agents.list.detailed stonith-agents.ocf.version-1-0 stonith-agents.ocf.version-1-1 stonith-agents.self-validation

pcs_capabilities:
  description: list of pcs capabilities
  returned: success
  type: list
  elements: str
  sample:
    - booth
    - booth.enable-authfile.set
    - booth.enable-authfile.unset
    - cluster.config.backup-local
    - cluster.config.restore-cluster
    - cluster.config.restore-local
    - cluster.config.uuid
    - cluster.create
    - cluster.create.enable
    - cluster.create.local
    - cluster.create.no-keys-sync
    - cluster.create.separated-name-and-address
    - cluster.create.start
    - cluster.create.start.wait
    - cluster.create.transport.knet
    - cluster.create.transport.udp-udpu
    - cluster.create.transport.udp-udpu.no-rrp
    - cluster.destroy
    - cluster.destroy.all
    - cluster.report
    - cluster.verify
    - corosync.authkey.update
    - corosync.config.get
    - corosync.config.get.struct
    - corosync.config.reload
    - corosync.config.sync-to-local-cluster
    - corosync.config.update
    - corosync.link.add
    - corosync.link.remove
    - corosync.link.remove.list
    - corosync.link.update
    - corosync.qdevice
    - corosync.qdevice.model.net
    - corosync.quorum
    - corosync.quorum.device
    - corosync.quorum.device.heuristics
    - corosync.quorum.device.model.net
    - corosync.quorum.set-expected-votes-runtime
    - corosync.quorum.status
    - corosync.quorum.unblock
    - corosync.totem.block_unlisted_ips
    - corosync.uidgid
    - node.add
    - node.add.enable
    - node.add.separated-name-and-address
    - node.add.start
    - node.add.start.wait
    - node.attributes
    - node.attributes.set-list-for-node
    - node.confirm-off
    - node.fence
    - node.guest
    - node.kill
    - node.maintenance
    - node.maintenance.all
    - node.maintenance.lis
    - node.maintenance.wait
    - node.remote
    - node.remote.onfail-demote
    - node.remove
    - node.remove-from-caches
    - node.remove.list
    - node.standby
    - node.standby.al
    - node.standby.lis
    - node.standby.wai
    - node.start-stop-enable-disabl
    - node.start-stop-enable-disable.al
    - node.start-stop-enable-disable.lis
    - node.start-stop-enable-disable.start-wai
    - node.utilizatio
    - node.utilization.set-list-for-nod
    - pcmk.acl.enable-disabl
    - pcmk.acl.grou
    - pcmk.acl.rol
    - pcmk.acl.role.create-with-permission
    - pcmk.acl.role.delete-with-users-group
    - pcmk.acl.use
    - pcmk.alert
    - pcmk.cib.checkpoints
    - pcmk.cib.checkpoints.diff
    - pcmk.cib.edit
    - pcmk.cib.get
    - pcmk.cib.get.scope
    - pcmk.cib.roles.promoted-unpromoted
    - pcmk.cib.set
    - pcmk.constraint.colocation.set
    - pcmk.constraint.colocation.set.options
    - pcmk.constraint.colocation.simple
    - pcmk.constraint.colocation.simple.options
    - pcmk.constraint.hide-expired
    - pcmk.constraint.location.simple
    - pcmk.constraint.location.simple.options
    - pcmk.constraint.location.simple.resource-regexp
    - pcmk.constraint.location.simple.rule
    - pcmk.constraint.location.simple.rule.node-attr-type-number
    - pcmk.constraint.location.simple.rule.options
    - pcmk.constraint.location.simple.rule.rule-add-remove
    - pcmk.constraint.no-autocorrect
    - pcmk.constraint.order.set
    - pcmk.constraint.order.set.options
    - pcmk.constraint.order.simple
    - pcmk.constraint.order.simple.options
    - pcmk.constraint.ticket.set
    - pcmk.constraint.ticket.set.options
    - pcmk.constraint.ticket.simple
    - pcmk.constraint.ticket.simple.constraint-id
    - pcmk.properties.cluster
    - pcmk.properties.cluster.config.output-formats
    - pcmk.properties.cluster.defaults
    - pcmk.properties.cluster.describe
    - pcmk.properties.cluster.describe.output-formats
    - pcmk.properties.operation-defaults
    - pcmk.properties.operation-defaults.multiple
    - pcmk.properties.operation-defaults.rule
    - pcmk.properties.operation-defaults.rule-rsc-op
    - pcmk.properties.operation-defaults.rule.hide-expired
    - pcmk.properties.operation-defaults.rule.node-attr-type-number
    - pcmk.properties.resource-defaults
    - pcmk.properties.resource-defaults.multiple
    - pcmk.properties.resource-defaults.rule
    - pcmk.properties.resource-defaults.rule-rsc-op
    - pcmk.properties.resource-defaults.rule.hide-expired
    - pcmk.properties.resource-defaults.rule.node-attr-type-number
    - pcmk.resource.ban-move-clear
    - pcmk.resource.ban-move-clear.clear-expired
    - pcmk.resource.bundle
    - pcmk.resource.bundle.container-docker
    - pcmk.resource.bundle.container-docker.promoted-max
    - pcmk.resource.bundle.container-podman
    - pcmk.resource.bundle.container-podman.promoted-max
    - pcmk.resource.bundle.container-rkt
    - pcmk.resource.bundle.container-rkt.promoted-max
    - pcmk.resource.bundle.reset
    - pcmk.resource.bundle.wait
    - pcmk.resource.cleanup
    - pcmk.resource.cleanup.one-resource
    - pcmk.resource.cleanup.strict
    - pcmk.resource.clone
    - pcmk.resource.clone.custom-id
    - pcmk.resource.clone.meta-in-create
    - pcmk.resource.clone.wait
    - pcmk.resource.config.output-formats
    - pcmk.resource.create
    - pcmk.resource.create.clone.custom-id
    - pcmk.resource.create.in-existing-bundle
    - pcmk.resource.create.meta
    - pcmk.resource.create.no-master
    - pcmk.resource.create.operations
    - pcmk.resource.create.operations.onfail-demote
    - pcmk.resource.create.promotable
    - pcmk.resource.create.promotable.custom-id
    - pcmk.resource.create.wait
    - pcmk.resource.debug
    - pcmk.resource.delete
    - pcmk.resource.disable.safe
    - pcmk.resource.disable.safe.brief
    - pcmk.resource.disable.safe.tag
    - pcmk.resource.disable.simulate
    - pcmk.resource.disable.simulate.brief
    - pcmk.resource.disable.simulate.tag
    - pcmk.resource.enable-disable
    - pcmk.resource.enable-disable.list
    - pcmk.resource.enable-disable.tag
    - pcmk.resource.enable-disable.wait
    - pcmk.resource.failcount
    - pcmk.resource.group
    - pcmk.resource.group.add-remove-list
    - pcmk.resource.group.wait
    - pcmk.resource.manage-unmanage
    - pcmk.resource.manage-unmanage.list
    - pcmk.resource.manage-unmanage.tag
    - pcmk.resource.manage-unmanage.with-monitor
    - pcmk.resource.move.autoclean
    - pcmk.resource.promotable
    - pcmk.resource.promotable.custom-id
    - pcmk.resource.promotable.meta-in-create
    - pcmk.resource.promotable.wait
    - pcmk.resource.refresh
    - pcmk.resource.refresh.one-resource
    - pcmk.resource.refresh.strict
    - pcmk.resource.relations
    - pcmk.resource.relocate
    - pcmk.resource.restart
    - pcmk.resource.update
    - pcmk.resource.update-meta
    - pcmk.resource.update-meta.list
    - pcmk.resource.update-meta.wait
    - pcmk.resource.update-operations
    - pcmk.resource.update-operations.onfail-demote
    - pcmk.resource.update.meta
    - pcmk.resource.update.operations
    - pcmk.resource.update.operations.onfail-demote
    - pcmk.resource.update.wait
    - pcmk.resource.utilization
    - pcmk.resource.utilization-set-list-for-resource
    - pcmk.stonith.cleanup
    - pcmk.stonith.cleanup.one-resource
    - pcmk.stonith.cleanup.strict
    - pcmk.stonith.create
    - pcmk.stonith.create.in-group
    - pcmk.stonith.create.meta
    - pcmk.stonith.create.operations
    - pcmk.stonith.create.operations.onfail-demote
    - pcmk.stonith.create.wait
    - pcmk.stonith.delete
    - pcmk.stonith.enable-disable
    - pcmk.stonith.enable-disable.list
    - pcmk.stonith.enable-disable.wait
    - pcmk.stonith.history.cleanup
    - pcmk.stonith.history.show
    - pcmk.stonith.history.update
    - pcmk.stonith.levels
    - pcmk.stonith.levels.add-remove-devices-list
    - pcmk.stonith.levels.clear
    - pcmk.stonith.levels.node-attr
    - pcmk.stonith.levels.node-regexp
    - pcmk.stonith.levels.verify
    - pcmk.stonith.refresh
    - pcmk.stonith.refresh.one-resource
    - pcmk.stonith.refresh.strict
    - pcmk.stonith.update
    - pcmk.stonith.update.scsi-devices
    - pcmk.stonith.update.scsi-devices.add-remove
    - pcmk.stonith.update.scsi-devices.mpath
    - pcmk.tag
    - pcmk.tag.resources
    - pcs.auth.client
    - pcs.auth.client.cluster
    - pcs.auth.client.token
    - pcs.auth.deauth-client
    - pcs.auth.deauth-server
    - pcs.auth.no-bidirectional
    - pcs.auth.separated-name-and-address
    - pcs.auth.server.token
    - pcs.cfg-in-file.cib
    - pcs.daemon-ssl-cert.set
    - pcs.daemon-ssl-cert.sync-to-local-cluster
    - pcs.disaster-recovery.essentials
    - pcs.request-timeout
    - resource-agents.describe
    - resource-agents.list
    - resource-agents.list.detailed
    - resource-agents.ocf.version-1-0
    - resource-agents.ocf.version-1-1
    - resource-agents.self-validation
    - sbd
    - sbd.option-timeout-action
    - sbd.shared-block-device
    - status.corosync.membership
    - status.pcmk.resources.hide-inactive
    - status.pcmk.resources.id
    - status.pcmk.resources.node
    - status.pcmk.resources.orphaned
    - status.pcmk.xml
    - stonith-agents.describe
    - stonith-agents.list
    - stonith-agents.list.detailed
    - stonith-agents.ocf.version-1-0
    - stonith-agents.ocf.version-1-1
    - stonith-agents.self-validation

"""  # noqa: E501


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.sap.sap_operations.plugins.module_utils.pacemaker import run_pcs_command


def main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    pcs_version_full = run_pcs_command(module, ["--version", "--full"])
    if len(pcs_version_full.splitlines()) < 2:
        module.fail_json(
            msg="Unexpected output from pcs --version --full",
            pcs_version_full_raw=pcs_version_full,
        )
    pcs_version = pcs_version_full.splitlines()[0]
    pcs_capabilities = pcs_version_full.splitlines()[1].split(" ")
    module.exit_json(
        changed=False,
        pcs_version=pcs_version,
        pcs_capabilities=pcs_capabilities,
        pcs_version_full_raw=pcs_version_full,
    )


if __name__ == "__main__":
    main()
