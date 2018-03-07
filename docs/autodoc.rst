.. _autodoc:

Include docstrings from your code
==================================

Sphinx allows you to `include documentation form docstrings`_ you have in your code.



Python
-------

Setting up autodoc
^^^^^^^^^^^^^^^^^^^^

To make autodoc available, you have to make sure that ``sphinx.ext.autodoc`` is included in your extensions
within the ``conf.py`` file. If you selected this option during quickstart, you should find the following line 
in your ``conf.py`` file.::

	extensions = ['sphinx.ext.autodoc']
	
If we also want to use mathjax for displaying proper math code, it should look like this::

	extensions = ['sphinx.ext.autodoc', 'sphinx.ext.mathjax']
	
Now you have to make sure, that your python interpreter can find your source code to include the docstrings.
Therefore you have to add the folder containing our code to the python sys.path variable.
If your conf.py file is in ``\..\myrepo\docs`` and your code in ``\..\myrepo\packagefolder\`` , you add these three line
to your ``conf.py`` file::

	import os
	import sys
	sys.path.insert(0, os.path.abspath(r'..'))

Make sure your ``packagefolder`` folder contains a ``__init__.py`` so it is defined as a package.


Running sphinx-apidoc
^^^^^^^^^^^^^^^^^^^^^^^^

Now we can use ``spinx-apidoc`` to automatically 
build a nice module index 
with links to documentation generated from the docstrings of your modules and classes 
which is both pretty and a nice excuse to document your code properly too.

Simply run

    $ sphinx-apidoc -o <outputdir> <sourcedir>
	
For our example, being in our ``docs`` folder, we can do this

	$ sphinx-apidoc -o . ..
	
This will automatically create *.rst files for each module. You can find them in your 
docs folder. For our example, this generated  a ``exmplpckg.rst`` file.
We can now include it into our documentation and `change it`_ manually, if we want to.
We treat it like any other .srt file that is part of our documentation.
apidoc alo created a ``modules.rst`` file, which I deleted because I won't use it.

:ref:`exmplpckg_apidoc` This is how it looks like for our example.


How to document your code
^^^^^^^^^^^^^^^^^^^^^^^^^^

Please have a look at this `Example on Sphinx`_ and this `Guide to NumPy/SciPy Documentation`_


Java
-----

This should also be possible using `javasphinx`_ . Maybe someone knowing Java can provide
an example...

R
---

I suppose this is also possible for R. Feel free to try.



.. _change it: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _javasphinx: https://bronto.github.io/javasphinx/
.. Example on Sphinx: http://www.sphinx-doc.org/en/stable/ext/example_numpy.html#example-numpy
.. _Guide to NumPy/SciPy Documentation: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#common-rest-concepts
.. _include documentation form docstrings: http://www.sphinx-doc.org/en/master/ext/autodoc.html