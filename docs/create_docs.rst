
.. _create_docs:

Create your documentation
============================

This chapter will show you how to create your own documentation by editing the existing
``*.rst`` files and adding new ones.


Build html files
--------------------

In your docs folder, there should be a make.bat file. You can simply build html files of 
your documentation by running::

    $ make html

Make sure you are in the right folder. With the default settings using sphinx-quickstart 
now your docs folder should now have a `_build\html\` folder containing at some html files
(at least a `index.html` file). You can open these file using any web browser. 
This is how your documentation looks at the moment. Now you can start editing them and adding
new files to your documentation.

.. note:: You can build a new version of your html files using `make html` at any time to see
  how your documentation currently looks.

Edit your index.rst
--------------------

Now, edit your ``index.rst`` and add some information about your project.
Include as much detail as you like.

The ``index.html`` is the starting page when you go to your documentation.
Therefore it usually contains some general information about your repository and a link to all
chapters of your documentation. But you can design it the way you like.

For documentations on readthedocs, that are linked to a public github repo (like this one), you can usually see the code
by selecting `edit on github` and then `raw`  there.
Here you can get some inspiration from other documentations.
Refer to the reStructuredText_ syntax if you need help.

Adding a new .rst file
------------------------

I usually keep my chapters in different files. Before I add a new file, I add the following two lines at the beginning of my
`index.rst` file (actually there first one is already there and I delete the additional  sphinx generated comments). The second one defines a reference the following
section header, so I can link to it.

.. code-block:: RST

	.. exmplpckg 
	.. _index:

Then I create a new .rst file in my docs folder. For this example it will be `sphinx_start.rst` . The first thing I do in this
file is creating a reference and the first section header. This defines `_start:` as a reference to the following section header.
	
.. code-block:: RST

	.. _start:

	Getting Started with Sphinx
	============================	

Now I update the contents in the `index.rst` file. Therefor I use the filename, not the reference label.

.. code-block:: RST

	.. toctree::
	   :maxdepth: 1

	   sphinx_start

		
Now you can edit your new file(s) and describe your project. :ref:`rst` gives some example on how to use 
restructured text.

Here you can find a `list of documentations`_ you can get some inspiration from.



.. list of documentations: https://github.com/PharkMillups/beautiful-docs
.. _reStructuredText: http://sphinx-doc.org/rest.html
