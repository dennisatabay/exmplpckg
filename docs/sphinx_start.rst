.. _start:

Getting Started with Sphinx
============================

This chapter will show you how to get started with sphinx, based on the
description from `getting started at readthedocs`_ and the official `install Sphinx`_ 
instructions.


Install and Quickstart
-----------------------


There is `a screencast`_ that will help you get started if you prefer.

Sphinx is a tool that makes it easy to create beautiful documentation.
Assuming you have Python_ already, `install Sphinx`_::

    $ pip install -U sphinx

Create a directory inside your project to hold your docs::

    $ cd /path/to/exmplpckg
    $ mkdir docs

Run ``sphinx-quickstart`` in there::

    $ cd docs
    $ sphinx-quickstart

This quick start will walk you through creating the basic configuration; in most cases, you
can just accept the [defaults] or choose an project name/version. If you want to include documentation from the docstrings of your code,
choose **y** here! Also select **y** for include math, rendered in the browser by JSMath to properly display math code.

* Root path for the documentation [.]:
* Separate source and build directories (y/N) [n]:
* Name prefix for templates and static dir [_]:
* Project name: 	**project name**
* Author name(s): 	**Your Name**
* Project version: 	(0.0.1)
* Project release [0.0.1]:
* Source file suffix [.rst]:
* Name of your master document (without suffix) [index]: 
* epub: Do you want to use the epub builder (y/n) [n]:
* autodoc: automatically insert docstrings from modules (y/N) [n]: 	**y**
* doctest: automatically test code snippets in doctest blocks (y/N) [n]: 
* intersphinx: link between Sphinx documentation of different projects (y/N) [n]:
* todo: write “todo” entries that can be shown or hidden on build (y/N) [n]:
* coverage: checks for documentation coverage (y/N) [n]:
* pngmath: include math, rendered as PNG images (y/N) [n]: **y**
* jsmath: include math, rendered in the browser by JSMath (y/N) [n]: **y**
* ifconfig: conditional inclusion of content based on config values (y/N) [n]:
* viewcode: include links to the source code of documented Python objects (y/n) [n]: **y**
* Create Makefile? (Y/n) [y]:
* Create Windows command file? (Y/n) [y]:


When it's done, you'll have an ``index.rst``, a
``conf.py`` and some other files. Add these to your git revision control.


Edit your conf.py settings
---------------------------

After running `sphinx-quickstart`, your docs folder should contain a ``conf.py`` file.
This file contains all the settings you just choose during the quickstart. If you want to change them,
just do it within this file. It is well documented and most of the parameters should be 
clear.

html theme
^^^^^^^^^^

You can also specify some additional settings, such as the html theme. Just choose one of
the `available html themes`_ . You should find this line in your ``conf.py`` file::

	html_theme = 'alabasta'

For readthedocs, we would like to use the readthedocs default theme ``sphinx_rtd_theme`` . We could set it here, but
then we have to install it to use it locally (pip install sphinx_rtd_theme). Instead we just outcomment the theme
setting line. Now Sphinx will use its default (alabasta) when building the html locally and readthedocs
will use its default when importing the documentation::

	#html_theme = 'alabasta'

.. _math_label:
	
Extension
^^^^^^^^^^^^

Your config.py document contains one (or more) lines defining the sphinx extensions. After running 
sphinx quickstart, it shoul look like this::

    extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    ]


``sphinx.ext.autodoc`` enables auto documentation (see :ref:`autodoc`)

To ``sphinx.ext.mathjax`` extension is needed to write proper math code. This extension uses the JavaScript 
package MathJax to transform the LaTeX markup to readable math live in the browser.
See also `Math support in sphinx`_ .

``sphinx.ext.viewcode`` makes it possible to link to your source code from the documentation

I usually also add one extension manually, the ``sphinx.ext.napoleon`` extension, which allows you to
write your docstrings in more readable style, that is still recognized by sphinx (http://www.sphinx-doc.org/en/master/ext/napoleon.html)

And if your code is written in java and you want to provide auto documentation here, you need to add ``javasphinx`` .
(make sure it is installed and added to the requirements)

So my config.py extensions look like this::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.mathjax',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon',
        'javasphinx'
    ]


More changes
^^^^^^^^^^^^^^

Usually I don't change more than that within ``conf.py`` . If  you want to change more, see the `sphinx documentation for config.py`_

  

.. _a screencast: https://www.youtube.com/watch?feature=player_embedded&v=oJsUvBQyHBs
.. _getting started at readthedocs: http://docs.readthedocs.io/en/latest/getting_started.html#
.. _install Sphinx: http://sphinx-doc.org/latest/install.html
.. _Python: https://www.python.org/
.. _reStructuredText: http://sphinx-doc.org/rest.html
.. _this template: http://docs.writethedocs.org/guide/writing/beginners-guide-to-docs/#id1
.. _available html themes: http://www.sphinx-doc.org/en/stable/theming.html#builtin-themes
.. _sphinx documentation for config.py: http://www.sphinx-doc.org/en/stable/config.html
.. _Math support in sphinx: http://www.sphinx-doc.org/en/master/ext/math.html
