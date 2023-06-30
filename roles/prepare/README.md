# prepare

Prepare RHEL managed host to run content from sap.sap_operations

Role ensures that all collection sap.sap_operations prerequisites are met.

Role works in two modes - normal and assert.

In normal mode it ensures that all prerequisites to run content from collection sap.sap_operations are met.

In assert mode it fails if collection prerequisites are not met on the host.

Role will only collect facts if OS distribution is not RedHat.

## Requirements

Role requires root access in order to install necessary packages and other sap.sap_operations collection prerequisites (normal mode).



<!-- BEGIN: Role Input Parameters -->

## Role Variables

Required parameters:

### prepare_assert

- _Type:_ `bool`
- _Default:_ `False`
- _Required:_ `False`

If set to True role will only assert that all sap.sap_operations collection prerequisites are met.
Is set to False (default) will ensure that all sap.sap_operations collection prerequisites are met (root access required)

<!-- END: Role Input Parameters -->

## Example Playbooks

```ansible
- hosts: all
  roles:
    - role: sap.sap_operations.prepare
```

'unpack_source' can be list of paths to folders and/or files.

Another options is to set 'unpack_source' value to file or folder.

```ansible
- hosts: all
  vars:
    prepare_assert: true
  roles:
    - role: sap.sap_operations.prepare
```

## License

GPL-3.0-only

## Author Information

Kirill Satarin (@kksat)
