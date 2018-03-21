.. _autodoc:

Include docstrings from your code
==================================

Sphinx allows you to `include documentation form docstrings`_ you have in your code.



Python
-------

Setting up autodoc
^^^^^^^^^^^^^^^^^^^^

To make autodoc available, you have to make sure that ``sphinx.ext.autodoc`` is included in your extensions
within the ``conf.py`` file. ::

	extensions = ['sphinx.ext.autodoc',
                  more_extensions,
                  ]
		
Now you have to make sure, that your python interpreter can find your source code to include the docstrings.
Therefore you have to add the folder containing our code to the python sys.path variable.
If your conf.py file is in ``\..\myrepo\docs`` and your code in ``\..\myrepo\packagefolder\`` , you add these five line
to your ``conf.py`` file (somehow local sphinx and readthedocs differ here in reading this correctly,
but if I add these three versions, it works for both)::

    import os
    import sys
    sys.path.insert(0, os.path.abspath('.'))
    sys.path.insert(0, os.path.abspath('..'))
    sys.path.insert(0, os.path.abspath('../'))

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

	
This will automatically create ``*.rst`` files for each module. You can find them in your 
``docs`` folder. For our example, this generated  a ``exmplpckg.rst`` and a ``modules.rst`` file.

Now I simply add the ``exmplpckg.rst`` to the toctree in my ``index.rst`` file. 

.. code-block:: RST

	This documentation contains the following pages:

	.. toctree::
	   :maxdepth: 1

	   sphinx_start
	   create_docs
	   autodoc
	   readthedocs
	   rst_syntax
	   exmplpckg
	   todo


You can see how the automated documentation
looks like when selecting ``exmplpckg`` on the left.

Include docstrings for specific modules/classes/methods/functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition (or instead of) creating the ``*.rst`` automatically for each module, you can also
insert the docstrings of a specific module, class, method, attribute or function anywhere in your
documentaion. You can also always link to an specific documented module, class,...


You can for example link to the attribute :attr:`exmplpckg.base.LinearFunction.m` , or in short 
:attr:`~exmplpckg.base.LinearFunction.m` of the 
class :class:`exmplpckg.base.LinearFunction` (or short :class:`~exmplpckg.base.LinearFunction` .

And you can show the docstring of the :class:`~exmplpckg.base.LinearFunction` here:

.. autoclass:: exmplpckg.base.LinearFunction
    :noindex:


Or just the docstring of its method :meth:`~exmplpckg.base.LinearFunction.fit`

.. automethod:: exmplpckg.base.LinearFunction.fit
    :noindex:


For both, you should see the source code, when selecting ``source`` on the right.
   
Have a look at the sphinx `autodoc documentation`_ for more options.


Create a steup.py and requirements.txt file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create both files and add them to your main project folder. 
autodoc on readthedocs will not work without them.
(I am not 100 per cent sure if this is really necessary)


How to document your code
^^^^^^^^^^^^^^^^^^^^^^^^^^

Please have a look at this `Example on Sphinx`_ and this `Guide to NumPy/SciPy Documentation`_


.. java:package:: my_java_package


Java
-----

Using the docstrings from your java code in your documenatation is possible with `javasphinx`_ .

Javasphinx recognizes docstrings written in javadoc syntax. See the `wikipedia article`_ or
thi `How to Write Doc Comments for the Javadoc Tool`_ article for syntax examples.

.. note:: As far as I understand, the java code has to be defined as a package to use javasphinx-apidoc

Create a ``docs`` folder and initial ``*.rst`` file following :ref:start

Install javasphinx, if not already installed

    $ pip install javasphinx

Use ``javasphinx-apidoc`` , which is similar to ``sphinx-apidoc``

$ javasphinx-apidoc -o <outputdir> <sourcedir>
	
For our example, being in our ``exmplpckg/docs`` folder and having the java code in ``exmplpckg/exmpl_java``, we can do this

$ javasphinx-apidoc -o . ../exmpl_java

This will create a file called ``packages.rst`` and a folder ``"package_name"`` for each package defined in the java scripts
within this folder. For our example this is the package ``my_java_package``. The folder again contains some ``*.rst`` files
whith the parsed docstrings from your java code.

We can simply add the ``packages.rst`` to our index toctree. You can see the result when selecting ``Javadoc`` on the left.

.. code-block:: RST

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



.. note:: It seems that it is necessary to run ``javasphinx-apidoc`` every time before commit/push to github. I could't find out yet
  how to make sphinx do this automatically when building. I also don't know how to insert auto generated parts in the rest of your docs
  or how to refer to available functions/methods/classes. 


R
---

I suppose this is also possible for R. Feel free to try.



.. _autodoc documentation: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _javasphinx: https://bronto.github.io/javasphinx/
.. _Example on Sphinx: http://www.sphinx-doc.org/en/stable/ext/example_numpy.html#example-numpy
.. _Guide to NumPy/SciPy Documentation: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#common-rest-concepts
.. _include documentation form docstrings: http://www.sphinx-doc.org/en/master/ext/autodoc.html
.. _wikipedia article: https://en.wikipedia.org/wiki/Javadoc
.. _How to Write Doc Comments for the Javadoc Tool: http://www.oracle.com/technetwork/articles/java/index-137868.html 
