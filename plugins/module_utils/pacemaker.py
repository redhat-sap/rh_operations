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

import xml.etree.ElementTree as ET  # nosec B405

from ansible_collections.sap.sap_operations.plugins.module_utils.compat import dict_union

"""
PACEMAKER_XML_LIST_ELEMENTS is a list of XML tags for which all the tags below will be considered as elements of the list,
not as key - values for the object.
Example is cluster nodes, there are several nodes in the cluster

  <nodes>
    <node name="host1" id="1" online="true" standby="false" standby_onfail="false" maintenance="false" pending="false" unclean="false" shutdown="false" expected_up="true" is_dc="true" resources_running="0" type="member"/>
    <node name="host2" id="2" online="true" standby="false" standby_onfail="false" maintenance="false" pending="false" unclean="false" shutdown="false" expected_up="true" is_dc="false" resources_running="0" type="member"/>
  </nodes>

Adding 'nodes' tag to the list below allows to create list for all the elements in the 'nodes' tag in the xml
"""  # noqa: E501

PACEMAKER_XML_LIST_ELEMENTS = (
    "nodes",
    "constraints",
    "crm_config",
    "cluster_property_set",
    "lrm_resources",
    "lrm_resource",
    "instance_attributes",
    "operations",
    "meta_attributes",
    "transient_attributes",
    "status",
    "fence_history",
    "node_attributes",
    "node_history",
    "resource_history",
    "resources",
    "clone",
    "node",
    "failures",
    "clone",  # TODO handle clones differently - node names, see pacemaker status xml
    "node",  # TODO handle nodes differently - node names, see pacemaker status xml
    "tags",
    "bans",
)


def Element2Dict(root):
    """Converts an Element object to a dictionary.

    Args:
        root (Element): The root element to convert to a dictionary.

    Returns:
        dict: The dictionary representation of the Element object.
    """
    ret = {}
    children = [Element2Dict(child) for child in root]
    attributes = root.attrib
    root_is_list = root.tag in PACEMAKER_XML_LIST_ELEMENTS

    if attributes and children:
        if not root_is_list:
            children_dict = {}
            for child in children:
                children_dict = dict_union(children_dict, child)
            ret[root.tag] = dict_union(root.attrib, children_dict)
        else:
            ret["attrib"] = root.attrib
            ret[root.tag] = children

    elif attributes and not children:
        ret[root.tag] = root.attrib

    elif not attributes and children:
        if not root_is_list:
            children_dict = {}
            for child in children:
                children_dict = dict_union(children_dict, child)
            ret[root.tag] = children_dict
        else:
            ret[root.tag] = children

    elif not attributes and not children:
        return {root.tag: root.text}

    return ret


def get_pacemaker_status_xml(module):
    """This function runs the 'pcs status xml' command and returns the output.

    Args:
        module: The AnsibleModule object.

    Returns:
        The output of the 'pcs status xml' command.

    Raises:
        AnsibleFailJson: If the command fails to execute or returns an error.
    """
    rc, stdout, err = None, None, None
    try:
        rc, stdout, err = module.run_command(args=["pcs", "status", "xml"])
    except Exception as e:
        module.fail_json(msg="Failed with exception", exception=(str(e)))
    if err or rc:
        module.fail_json(msg="Error occurred during execution", error=err, rc=rc)
    return stdout


def get_pacemaker_cib_query_xml(module):
    """This function runs the 'cibadmin --query' command and returns the output.

    Args:
        module: The AnsibleModule object.

    Returns:
        The output of the 'cibadmin --query' command.

    Raises:
        AnsibleFailJson: If the command fails to execute or an error occurs.
    """
    rc, stdout, err = None, None, None
    try:
        rc, stdout, err = module.run_command(args=["cibadmin", "--query"])
    except Exception as e:
        module.fail_json(msg="Failed with exception", exception=(str(e)))
    if err:
        module.fail_json(msg="Error occurred during execution", error=err)
    if not rc:
        return stdout
    return stdout


def run_pcs_command(
    module, args="", check_rc=True, check_stderr=True
):
    """Runs a pcs command with the given arguments and returns the output.

    Args:
        module (AnsibleModule): The AnsibleModule object.
        args (list): The list of arguments to pass to the pcs command.
        check_rc (bool): If True, check the return code of the command for errors. Default is True.
        check_stderr (bool): If True, check the stderr output of the command for errors. Default is True.

    Returns:
        str: The output of the pcs command.

    Raises:
        AnsibleFailJson: If an error occurs while executing the pcs command.

    This function takes an AnsibleModule object and a list of arguments to pass to the pcs command. It then runs the pcs command with the given arguments and returns the output. If an error occurs while executing the pcs command, an AnsibleFailJson exception is raised.
    """  # noqa: E501
    args = [
        "pcs",
    ] + list(args)
    rc, stdout, stderr = None, None, None
    try:
        rc, stdout, stderr = module.run_command(args=args)
    except Exception as e:
        module.fail_json(
            msg="Failed with exception while executing pcs command",
            exception=(str(e)),
            args=args,
        )
    if (check_stderr and stderr) or (check_rc and rc):
        module.fail_json(
            msg="Error occurred during execution while executing pcs command",
            stderr=stderr,
            rc=rc,
            args=args,
        )
    return stdout


def pcs_validate_resource(
    pcs_config_tree,
    resource_id,
):
    """Function to validate if resource is present in the cluster cib.

    Function to validate if resource is present in the cluster cib
    returns True if resource is present in pcs cib, False otherwise
    Only accepts pcs_config_tree as ElementTree object, not pcs_status_tree

    :param pcs_config_tree: ElementTree object representing the pcs configuration
    :type pcs_config_tree: xml.etree.ElementTree.ElementTree

    :param resource_id: ID of the resource to validate
    :type resource_id: str

    :return: True if resource is present in pcs cib, False otherwise
    :rtype: bool
    """  # noqa: E501
    return bool(
        pcs_config_tree.findall(".//resources/primitive[@id='{0}']".format(resource_id)) + pcs_config_tree.findall(".//resources/clone/primitive/[@id='{0}']".format(resource_id))  # noqa: E501
    )


def pcs_validate_node(pcs_config_tree, node):
    """Validates if a given node exists in the pcs_config_tree.

    Args:
        pcs_config_tree (ET): The parsed XML tree of the pcs configuration.
        node (str): The name of the node to validate.

    Returns:
        bool: True if the node exists in the pcs_config_tree, False otherwise.
    """
    return bool(pcs_config_tree.findall(".//nodes/node[@uname='{0}']".format(node)))


def pcs_resource_info(
    pcs_status_query_xml_string, resource,
):
    root = ET.fromstring(pcs_status_query_xml_string)  # nosec B314
    return root.findall("./resources/resource[@id='{0}']".format(resource)) + root.findall(
        "./resources/clone/resource/[@id='{0}']".format(resource)
    )


def pcs_resources_by_id(
    pcs_status_tree,
    resource_id="",
):
    # TODO: use only pcs_config_tree? - yes, message says, there is no resource in CIB
    return (
        pcs_status_tree.findall(".//resources/resource[@id='{}']".format(resource_id)) + pcs_status_tree.findall(".//resources/clone/resource/[@id='{0}']".format(resource_id))  # noqa: E501
    )


def pcs_resources_by_id_from_status(pcs_status_tree, resource_id=None):
    """Returns a list of XML elements representing resources with the given ID.

    Args:
        pcs_status_tree (ElementTree): The parsed XML tree of the PCS status output.
        resource_id (str): The ID of the resource to search for. If not provided, all resources will be returned.

    Returns:
        List[Element]: A list of XML elements representing resources with the given ID.
    """
    if resource_id is None:
        return (
            pcs_status_tree.findall(".//resources/resource") +
            pcs_status_tree.findall(".//resources/clone/resource") +
            pcs_status_tree.findall(".//resources/group/resource") +
            pcs_status_tree.findall(".//resources/clone/group/resource") +
            pcs_status_tree.findall(".//resources/group") +
            pcs_status_tree.findall(".//resources/clone/group")

        )
    return (
        pcs_status_tree.findall(".//resources/resource[@id='{0}']".format(resource_id)) +
        pcs_status_tree.findall(".//resources/clone/resource[@id='{0}']".format(resource_id)) +
        pcs_status_tree.findall(".//resources/group/resource[@id='{0}']".format(resource_id)) +
        pcs_status_tree.findall(".//resources/clone/group/resource[@id='{0}']".format(resource_id)) +
        pcs_status_tree.findall(".//resources/group[@id='{0}']".format(resource_id)) +
        pcs_status_tree.findall(".//resources/clone/group[@id='{0}']".format(resource_id))
    )


def pcs_resources_by_id_from_cib(pcs_cib_tree, resource_id=None):
    """Returns a list of Element objects representing the resources with the given ID in the given PCS CIB tree.

    Args:
        pcs_cib_tree (ElementTree): The PCS CIB tree to search for resources.
        resource_id (str): The ID of the resource(s) to find. If not specified, all resources will be returned.

    Returns:
        List[Element]: A list of Element objects representing the resources with the given ID.
    """
    if resource_id is None:
        return (
            pcs_cib_tree.findall(".//resources/primitive") +
            pcs_cib_tree.findall(".//resources/clone/primitive") +
            pcs_cib_tree.findall(".//resources/group/primitive") +
            pcs_cib_tree.findall(".//resources/clone/group/primitive") +
            pcs_cib_tree.findall(".//resources/group") +
            pcs_cib_tree.findall(".//resources/clone/group")
        )
    return (
        pcs_cib_tree.findall(".//resources/primitive[@id='{0}']".format(resource_id)) +
        pcs_cib_tree.findall(".//resources/clone/primitive[@id='{0}']".format(resource_id)) +
        pcs_cib_tree.findall(".//resources/group/primitive[@id='{0}']".format(resource_id)) +
        pcs_cib_tree.findall(".//resources/clone/group/primitive[@id='{0}']".format(resource_id)) +
        pcs_cib_tree.findall(".//resources/group[@id='{0}']".format(resource_id)) +
        pcs_cib_tree.findall(".//resources/clone/group[@id='{0}']".format(resource_id))
    )


def pcs_resource_attrib(resource, attrib_name):
    """Returns the value of the specified attribute for the given Pacemaker resource.

    Args:
        resource (Element): The Pacemaker resource element.
        attrib_name (str): The name of the attribute to retrieve.

    Returns:
        str: The value of the specified attribute.
        None: if resource is empty or the attribute does not exist.
    """
    return resource.get(attrib_name)


def pcs_cluster_property_set_from_cib(pcs_cib_tree, cluster_property_set_id=None):
    """Returns a list of Element objects representing the cluster property set with the given ID in the given PCS CIB tree.

    Args:
        pcs_cib_tree (ElementTree): The PCS CIB tree to search for cluster property sets.
        cluster_property_set_id (str): The ID of the cluster property set(s) to find. If not specified, all cluster property sets will be returned.

    Returns:
        List[Element]: A list of Element objects representing the cluster property set with the given ID.
    """
    if cluster_property_set_id is None:
        return pcs_cib_tree.findall(".//cluster_property_set/nvpair")
    return pcs_cib_tree.findall(
        ".//cluster_property_set[@id='{0}']/nvpair".format(
            cluster_property_set_id
        ))


def get_pcs_resource_agent_provider_from_status(pcs_resource):
    if pcs_resource.get('resource_agent'):
        return pcs_resource.get('resource_agent').split(':')[2]
    else:
        return None


def get_pcs_resource_agent_type_from_status(pcs_resource):
    if pcs_resource.get('resource_agent'):
        return pcs_resource.get('resource_agent').split(':')[3]
    else:
        return None


def get_pcs_resource_agent_class_from_status(pcs_resource):
    if pcs_resource.get('resource_agent'):
        return pcs_resource.get('resource_agent').split(':')[0]
    else:
        return None


def get_pcs_resource_agent_class_from_cib(pcs_resource):
    return pcs_resource.get('class')


def get_pcs_resource_agent_provider_from_cib(pcs_resource):
    return pcs_resource.get('provider')


def get_pcs_resource_agent_type_from_cib(pcs_resource):
    return pcs_resource.get("type")


def get_pcs_nodes_from_status(pcs_status_tree):
    """Returns a list of XML elements representing nodes.

    Args:
        pcs_status_tree (ElementTree): The parsed XML tree of the PCS status output.

    Returns:
        List[Element]: A list of XML elements representing nodes.
    """
    return pcs_status_tree.findall(".//nodes/node")
