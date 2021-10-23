pyrasite (updated)
==================

This package is a fork of https://github.com/lmacken/pyrasite containing several important fixes to make pyrasite work on modern systems.

Requirements
~~~~~~~~~~~~

 * `gdb <https://www.gnu.org/s/gdb>`_ (version 7.3+ (or RHEL5+))
 
On OS X you will need to have a codesigned gdb - see https://sourceware.org/gdb/wiki/BuildingOnDarwin
if you get errors while running with --verbose which mention codesigning.

On Linux machines, run `echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope` before running pyrasite.

Compatibility
~~~~~~~~~~~~~

Pyrasite works with Python 2.4 and newer. Injection works between versions
as well, so you can run Pyrasite under Python 3 and inject into 2, and
vice versa.

pyrasite-gui
~~~~~~~~~~~~

The graphical interface can be found here: https://github.com/lmacken/pyrasite-gui

Authors
~~~~~~~

Created by `Luke Macken <http://twitter.com/lmacken>`_ with the help of
`David Malcolm <http://dmalcolm.livejournal.com>`_ and many other
`contributors <https://github.com/lmacken/pyrasite/contributors>`_.
Logo by `Adam Saunders <https://fedorahosted.org/design-team/ticket/214>`_.

Licenses
~~~~~~~~

Code
^^^^

.. image:: https://www.gnu.org/graphics/gplv3-127x51.png
   :target: https://www.gnu.org/licenses/gpl.txt

Logo
^^^^

.. image:: https://creativecommons.org/images/deed/nolaw.png
   :target: https://creativecommons.org/publicdomain/zero/1.0/
