.. exmplpckg

.. _index:



Documetation with sphinx and readthedocs
=========================================

:Maintainer: Dennis Atabay, <dat@wattsight.com>
:Organization: `Wattsight`_
:Version: |version|
:Date: |today|
:Copyright:
  This documentation is licensed under a `Creative Commons Attribution 4.0 
  International`__ license.

.. __: http://creativecommons.org/licenses/by/4.0/


Contents
=========

This documentation contains the following pages:

.. toctree::
   :maxdepth: 1

   sphinx_start
   create_docs
   autodoc
   readthedocs
   rst_syntax
   exmplpckg
   packages
   todo


Features
--------
* simple linear function fitting


Get Started
-----------

1. Clone this repository to a directory of your choice.
2. If you actually want to use the package, copy the main folder to a directory which is already in python's search path or add the it to python's search path (sys.path) (`how to`_)
3. Use it or just have a look at the documentation


Dependencies
------------

* `numpy`_ for mathematical operations 
* `matplotlib`_ for making plots



.. _Wattsight: https://www.wattsight.com/
.. _how to: http://stackoverflow.com/questions/17806673/where-shall-i-put-my-self-written-python-packages/17811151#17811151) 
.. _numpy: http://www.numpy.org/
.. _matplotlib: https://matplotlib.org/