=======================================
SAP Operations Collection Release Notes
=======================================

.. contents:: Topics


v1.1.0
======

Release Summary
---------------

Feature Release

New Modules
-----------

- sap.sap_operations.hana_backup - Create SAP HANA database file backup
- sap.sap_operations.host_info - Collect information about installed SAP instances on the host

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
