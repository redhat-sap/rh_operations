=======================================
SAP Operations Collection Release Notes
=======================================

.. contents:: Topics


v1.9.0
======

Release Summary
---------------

Lifecycle release

Major Changes
-------------

- Clarify ansible-core versions supported by the collection

v1.3.2
======

Release Summary
---------------

Bugfix release

Minor Changes
-------------

- Resolve sanity errors for python 2.7 and lower versions of python 3

v1.3.1
======

Release Summary
---------------

Bugfix release

Minor Changes
-------------

- Resolve syntax issues with hana_update role

v1.3.0
======

Release Summary
---------------

Feature release

Minor Changes
-------------

- Clarify collection license
- Collection license applied is GPL-3.0-only

v1.2.3
======

Release Summary
---------------

Feature release

Minor Changes
-------------

- Add functionality to release different content to AAP and Ansible galaxy

v1.2.2
======

Release Summary
---------------

Feature release

Minor Changes
-------------

- Small changes to role argument_specs - fixes documentation linting errors

v1.2.1
======

Release Summary
---------------

Feature release

Minor Changes
-------------

- Collection automatically uploaded to Ansible Galaxy and AAP

v1.2.0
======

Release Summary
---------------

Feature release

Major Changes
-------------

- Introduction of NW RFC modules to connect to manage SAP ABAP system with Ansible

v1.1.2
======

Release Summary
---------------

Bug Fix Release

Minor Changes
-------------

- Fix issue with role prepare

v1.1.1
======

Release Summary
---------------

Bug Fix Release

Minor Changes
-------------

- Fix issue with module host_info - module failed if SAP HANA databases installed (incorrect indexing)
- Licensing clarification in the README.md file
- add bindep.txt to collection
- role prepare will not fail for non RedHat distributions (role will do nothing)

v1.1.0
======

Release Summary
---------------

Feature Release

v1.0.5
======

Release Summary
---------------

Bug fix release

Minor Changes
-------------

- Documentation added for roles `hana_update` and `prepare`

v1.0.4
======

Release Summary
---------------

Two roles are added `hana_update` and `prepare`


Major Changes
-------------

- Role hana_update - update SAP HANA system
- Role prepare - prepare RHEL hosts to run collection content

Minor Changes
-------------

- GitHub action to publish collection

v1.0.3
======

Release Summary
---------------

Using changelog fragments to build collection changelog.


Minor Changes
-------------

- Improvements in the collection build and publish process.
- Now using automatic generation of collection changelogs with fragments.

v1.0.2
======

Release Summary
---------------

First release of SAP Operations collection.


Major Changes
-------------

- parameter_info - module to fetch parameter information.
- sap_kernel_update - SAP kernel update role.
- service - module to manage SAP HANA services.
- system  - module to manage SAP system.
- system_info - module to fetch SAP system information.

v1.0.0
======

Release Summary
---------------

First release of SAP Operations collection.


Major Changes
-------------

- parameter_info - module to fetch parameter information.
- sap_kernel_update - SAP kernel update role.
- service - module to manage SAP HANA services.
- system  - module to manage SAP system.
- system_info - module to fetch SAP system information.
