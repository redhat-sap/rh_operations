# Ansible Collection - sap.sap_operations

This collection contains modules and plugins to assist in automating SAP day 2 operations with Ansible.

# Installation and Usage

## Installation
To install the role from Ansible automation hub please follow the steps below:

```bash
ansible-galaxy collection install sap.sap_operations
```

## Usage
Below is the example of using the hdbuserstore module to create a record using <hanasid>adm user.

Variable `binary_path` is required if `hdbuserstore` command cannot be found in `PATH` environment variable.
If running ansible module using become directive with <hanasid>adm user and flag `-i` (interactive - meaning load all environment for the user)
ansible modules fail. This is due to the fact that <hanasid>adm user sets environment variables `PYTHONHOME` and `PYTHONPATH` (to use HANA python,
not platform python) that confuse ansible.

In that case `hdbuserstore` command will not be in `PATH` environment variable for <hanasid>adm user and `binary_path` has to be provided.

There are several workaround around this unplesant situation. One is recommended.

```yaml
---
- name: Create record in hdb user store
  hosts: all
  tasks:
    - name: Create hdbuserstore credentials
      sap.sap_operations.hdbuserstore:
        key: "SYSTEM"
        env: "hana1:30013"
        username: "SYSTEM"
        password: "mysecretpassword"
      become: true
      become_user: <hanasid>adm
      become_flags: -i
      vars:
        ansible_python_interpreter: "/usr/libexec/platform-python -E"
```
