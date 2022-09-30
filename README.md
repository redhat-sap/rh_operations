![black](https://github.com/redhat-sap/operations/actions/workflows/black.yml/badge.svg)
![unit](https://github.com/redhat-sap/operations/actions/workflows/units.yml/badge.svg)
![integration](https://github.com/redhat-sap/operations/actions/workflows/main.yml/badge.svg)
![lint](https://github.com/redhat-sap/operations/actions/workflows/lint.yml/badge.svg)
![sanity](https://github.com/redhat-sap/operations/actions/workflows/sanity.yml/badge.svg)

# Ansible Collection - redhat.sap_operations

This collection contains modules and plugins to assist in automating SAP day 2 operations with Ansible.

# Installation and Usage

# Testing and Development
## Unit tests

```bash
make units
```

## Integration tests
Integration tests are leveraging SAP SOAP API. You need to define env varibles defining the password and hostname of the system you want to test as follows:

```bash
export SAP_PASSWORD='123'
export SAP_HOSTNAME='sap.domain.com'
```

Then you can execute the e2e test script, which executes ansible tests integration targets:

```bash
make e2e
```

# Building & pushing the Galaxy content
The SAP operations collection has tooling to build and publish the content into Ansible Galaxy.
To build the collection run the command:

```bash
make build
```

This will create the tar.gz file with the collection content. You may also build the content for your own namespace as follows:

```bash
make build NAMESPACE=machacekondra
```

When the tar.gz file of collection is created you may upload the content to galaxy as follows:


```bash
make publish TOKEN=abc
```

Where TOKEN variable can be obtained from your Ansible Galaxy account.

# Building the execution environment
The SAP operations collection support the Ansible execution environment.

To build the EE container run:
```bash
ansible-builder build -t quay.io/redhat/sap_operations -f meta/execution-environment.yml
```
