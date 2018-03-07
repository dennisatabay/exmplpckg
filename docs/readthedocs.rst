.. _rdt:

Using ReadtheDocs
==================

Since this is explained well in the `ReadtheDocs documentation`_, I will just refer to it.

Basically you create an account at `readthedocs.org`_ import github repository from there. As soon as you 
update your documentation and push it,
your Readthedocs page will be automatically updated (sometimes this takes a few minutes).


Use ReadtheDocs without python and sphinx
------------------------------------------

You can also use ReadtheDocs without having python and sphinx installed. Simply copy a ``docs`` folder from any
repository that works with readthedocs (this one for example) to your own repository. Now you can change your ``*.rst`` files,
and the ``.conf.py`` file to change the content. Of course you still have to link your repository on at `readthedocs.org`_ .
This will not allow you to build your html files offline, but it should work for your online documentation.

.. _ReadtheDocs documentation: http://docs.readthedocs.io/en/latest/getting_started.html#sign-up-and-connect-an-external-account
.. _readthedocs.org: https://readthedocs.org/