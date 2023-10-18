=======================================
SAP Operations Collection Release Notes
=======================================

.. contents:: Topics


v1.8.0-galaxy
=============

Release Summary
---------------

Feature release (galaxy only)

Major Changes
-------------

- Add plugins to manage SAP licenses with saplikey program.

New Plugins
-----------

Filter
~~~~~~

- sap.sap_operations.license_content - Get sap license attributes from sap license file

New Modules
-----------

- sap.sap_operations.saplikey - Manage sap license keys for SAP application instance with saplikey program.
- sap.sap_operations.saplikey_get_info - Get host hardware key information and other useful information with saplikey program.
- sap.sap_operations.saplikey_show_info - Get information about SAP license keys with saplikey program.

v1.7.0-galaxy
=============

Release Summary
---------------

Feature release (galaxy only)

Major Changes
-------------

- Add 'all' and 'any' filter and test plugins

v1.6.0-galaxy
=============

Release Summary
---------------

Feature release (galaxy only)

Major Changes
-------------

- Add pcs_cluster_property_mapping filter plugin
- Add pcs_resources filter plugins

v1.5.0-galaxy
=============

Release Summary
---------------

Feature release (galaxy only)

v1.4.0-galaxy
=============

Release Summary
---------------

Feature release (galaxy only)

Major Changes
-------------

- Add ansble modules to get pacemaker status and configuration

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

- Add functionality to release different content to AAP and Ansible galaxy
- Clarify collection license
- Collection license applied is GPL-3.0-only

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
