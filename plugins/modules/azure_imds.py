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
module: azure_imds

# extends_documentation_fragment: sap.sap_operations.experimental

author: Kirill Satarin (@kksat)

short_description: Get Azure instance metadata

description:
  - Get Azure instance metadata
  - Module uses Azure Instance Metadata Service (IMDS) to get information about the instance
  - See U(https://docs.microsoft.com/en-us/azure/virtual-machines/linux/instance-metadata-service) for more information

version_added: 1.5.0-galaxy

requirements:
  - Requests Python library must be installed on the host

options: {}

"""

EXAMPLES = r"""
- name: Get Azure instance metadata
  sap.sap_operations.azure_imds:
  register: result
"""

RETURN = r"""
metadata:
  description: Azure instance metadata
  returned: success
  type: dict
  elements: dict
  contains:
    instance:
      description: Azure instance metadata
      returned: success
      type: dict
      elements: dict
      sample:
        {
          "additionalCapabilities": {
              "hibernationEnabled": "false"
          },
          "azEnvironment": "AzurePublicCloud",
          "customData": "",
          "evictionPolicy": "",
          "extendedLocation": {
              "name": "",
              "type": ""
          },
          "host": {
              "id": ""
          },
          "hostGroup": {
              "id": ""
          },
          "isHostCompatibilityLayerVm": "false",
          "licenseType": "",
          "location": "northeurope",
          "name": "azure-imds",
          "offer": "RHEL-SAP-HA",
          "osProfile": {
              "adminUsername": "molecule",
              "computerName": "azure-imds",
              "disablePasswordAuthentication": "true"
          },
          "osType": "Linux",
          "placementGroupId": "",
          "plan": {
              "name": "",
              "product": "",
              "publisher": ""
          },
          "platformFaultDomain": "0",
          "platformSubFaultDomain": "",
          "platformUpdateDomain": "0",
          "priority": "",
          "provider": "Microsoft.Compute",
          "publicKeys": [
              {
                  "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDcic+BJ53/8Tu47fPlnd6GfLJEPP8WtuVDSgIdom/YoUFK+7HCEdpVnPXj3mkgrfH9elbKlLWlBd2i+leQKyRSP4LG/Dhw3RU6l7kn4DPOcWzJa0dhuD/EhCRHg58UVXJQ2qtdDkMZL7OfQ8bhslCIbwz4YRCl+Axd/KqwtlrYWxewUjOwIvKxtZ3Sk/YOomfY4Y21zL/p/Q3qH/h8+qnI9Qd/8jdzAi77rusCE/uIZvV+QOMzBSiGYR6rPrUDKKOcEWioc5ZKlSrTW0UZAv2tX/EZfLK1UFxesao5cbCz3VLRg7k3Qt9UBUa9GUyRTCqhJV82JYw7VjDB2veNfHtRhXQQf8ElAJozygfgLr+56Kp2pXcNHL3x5/H2MS3ZD5ShJywDxEoYj2tqSPmF9nABYDY4GNiGzfrxeXEmjLgT1DGG90nCXB8em6FPTuai7GiKF1m7PKsxLamdlYMWIS5sA5QwoQP5fNW6QYEXuZdPc0fdsESMX4ClkKJCdi7axlGQsJwlbrssUaSA21VjgmOSAbBidS7xvhDQDoSZmOUYTTtKsOmrCLVm/w+Rs4HQ6SOvqkI9yCk+GmYUzzUH1s0ima7MnxcvZDdRYGRK3WSmDptjsX6pX9qaMsC/KKW+WbANI+ZyX5c1lCT1WpsV1RKOYBuUbqP2cWSOLkyPvWygcQ==",
                  "path": "/home/molecule/.ssh/authorized_keys"
              }
          ],
          "publisher": "RedHat",
          "resourceGroupName": "molecule",
          "resourceId": "/subscriptions/6a73742d-8c0a-4b2d-9c60-67c592a0df50/resourceGroups/molecule/providers/Microsoft.Compute/virtualMachines/azure-imds",
          "securityProfile": {
              "encryptionAtHost": "false",
              "secureBootEnabled": "false",
              "securityType": "",
              "virtualTpmEnabled": "false"
          },
          "sku": "84sapha-gen2",
          "storageProfile": {
              "dataDisks": [],
              "imageReference": {
                  "id": "",
                  "offer": "RHEL-SAP-HA",
                  "publisher": "RedHat",
                  "sku": "84sapha-gen2",
                  "version": "8.4.2023310514"
              },
              "osDisk": {
                  "caching": "ReadOnly",
                  "createOption": "FromImage",
                  "diffDiskSettings": {
                      "option": ""
                  },
                  "diskSizeGB": "64",
                  "encryptionSettings": {
                      "diskEncryptionKey": {
                          "secretUrl": "",
                          "sourceVault": {
                              "id": ""
                          }
                      },
                      "enabled": "false",
                      "keyEncryptionKey": {
                          "keyUrl": "",
                          "sourceVault": {
                              "id": ""
                          }
                      }
                  },
                  "image": {
                      "uri": ""
                  },
                  "managedDisk": {
                      "id": "/subscriptions/6a73742d-8c0a-4b2d-9c60-67c592a0df50/resourceGroups/molecule/providers/Microsoft.Compute/disks/azure-imds",
                      "storageAccountType": "Premium_LRS"
                  },
                  "name": "azure-imds",
                  "osType": "Linux",
                  "vhd": {
                      "uri": ""
                  },
                  "writeAcceleratorEnabled": "false"
              },
              "resourceDisk": {
                  "size": "65536"
              }
          },
          "subscriptionId": "6a73742d-8c0a-4b2d-9c60-67c592a0df50",
          "tags": "_own_nic_:azure-imds01;_own_nsg_:azure-imds01;_own_pip_:azure-imds01",
          "tagsList": [
              {
                  "name": "_own_nic_",
                  "value": "azure-imds01"
              },
              {
                  "name": "_own_nsg_",
                  "value": "azure-imds01"
              },
              {
                  "name": "_own_pip_",
                  "value": "azure-imds01"
              }
          ],
          "userData": "",
          "version": "8.4.2023310514",
          "virtualMachineScaleSet": {
              "id": ""
          },
          "vmId": "6277b885-20b1-43ba-81a2-ee4e94e7c0af",
          "vmScaleSetName": "",
          "vmSize": "Standard_D8s_v3",
          "zone": ""
        }

    network:
      description: Azure network metadata
      returned: success
      type: dict
      elements: dict
      sample:
        {
          "interface": [
              {
                  "ipv4": {
                      "ipAddress": [
                          {
                              "privateIpAddress": "10.0.0.14",
                              "publicIpAddress": "4.210.73.173"
                          }
                      ],
                      "subnet": [
                          {
                              "address": "10.0.0.0",
                              "prefix": "24"
                          }
                      ]
                  },
                  "ipv6": {
                      "ipAddress": []
                  },
                  "macAddress": "002248A18C6C"
              }
          ]
        }

    identity:
      description: Azure identity metadata
      returned: success
      type: dict
      elements: dict
      sample:
        {
        "error": "Not Found"
        }

    loadbalancer:
      description: Azure loadbalancer metadata
      returned: success
      type: dict
      elements: dict
      sample:
        {
        "error": "No load balancer metadata is found. Please check if your VM is using any non-basic SKU load balancer and retry later."
        }

    scheduledevents:
      description: Azure scheduledevents metadata
      returned: success
      type: dict
      elements: dict
      sample:
        {
        "error": "Not found"
        }

    attest:
      description: Azure scheduledevents metadata
      returned: success
      type: dict
      elements: dict
      sample:
        {
        "encoding": "pkcs7",
        "signature": "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"
        }
"""  # noqa: E501


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.sap.sap_operations.plugins.module_utils.azure import (
    AZURE_METADATA_HEADERS,
    AZURE_METADATA_URL,
    AZURE_METADATA_VERSION,
)

import traceback

from ansible.module_utils.basic import missing_required_lib

try:
    import requests
except ImportError:
    HAS_REQUESTS_LIBRARY = False
    REQUESTS_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_REQUESTS_LIBRARY = True
    REQUESTS_LIBRARY_IMPORT_ERROR = None

azure_imds_timeout = 5


def main():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)

    if not HAS_REQUESTS_LIBRARY:
        module.fail_json(
            msg=missing_required_lib("requests"),
            exception=REQUESTS_LIBRARY_IMPORT_ERROR,
        )

    compute_endpoint = "{0}/instance/compute?api-version={1}".format(
        AZURE_METADATA_URL, AZURE_METADATA_VERSION
    )
    network_endpoint = "{0}/instance/network?api-version={1}".format(
        AZURE_METADATA_URL, AZURE_METADATA_VERSION
    )
    identity_endpoint = "{0}/identity?api-version={1}".format(
        AZURE_METADATA_URL, AZURE_METADATA_VERSION
    )
    loadbalancer_endpoint = "{0}/loadbalancer?api-version={1}".format(
        AZURE_METADATA_URL, AZURE_METADATA_VERSION
    )
    scheduledevents_endpoint = "{0}/scheduledevents?api-version={1}".format(
        AZURE_METADATA_URL, AZURE_METADATA_VERSION
    )
    attest_endpoint = "{0}/attested/document?api-version={1}".format(
        AZURE_METADATA_URL, AZURE_METADATA_VERSION
    )
    headers = AZURE_METADATA_HEADERS

    try:
        response = requests.get(
            compute_endpoint, headers=headers, timeout=azure_imds_timeout
        )
        response.raise_for_status()
        instance = response.json()

        response = requests.get(
            network_endpoint, headers=headers, timeout=azure_imds_timeout
        )
        response.raise_for_status()
        network = response.json()

        # identity, loadbalancer and scheduled events information is optional
        response = requests.get(
            identity_endpoint, headers=headers, timeout=azure_imds_timeout
        )
        identity = response.json()

        response = requests.get(
            loadbalancer_endpoint, headers=headers, timeout=azure_imds_timeout
        )
        loadbalancer = response.json()

        response = requests.get(
            scheduledevents_endpoint, headers=headers, timeout=azure_imds_timeout
        )
        scheduledevents = response.json()

        response = requests.get(
            scheduledevents_endpoint, headers=headers, timeout=azure_imds_timeout
        )
        scheduledevents = response.json()

        response = requests.get(
            attest_endpoint, headers=headers, timeout=azure_imds_timeout
        )
        response.raise_for_status()
        attest = response.json()

        module.exit_json(
            changed=False,
            metadata=dict(
                instance=instance,
                network=network,
                identity=identity,
                loadbalancer=loadbalancer,
                scheduledevents=scheduledevents,
                attest=attest,
            ),
        )
    except requests.exceptions.RequestException as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
