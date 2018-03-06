# -*- coding: utf-8 -*-
"""Example Package in python to show how to use documentation with `sphinx`_ 
and `readthedocs`_ .

The purpose of this module is to demonstrate documentation as specified by the 
`NumPy Documentation HOWTO`_. Docstrings may extend over multiple lines.
Sections are created with a section header followed by an underline of equal 
length.

Sphinx allows to `include documentation from docstrings`_ . To make the 
docstrings look nice within your html page, use any reStructuredText 
formatting.

This simple package calculates the slope m and the offset t of a linear 
function for two given points P1 = [x,y] and P2 = [x,y]

.. math::
	
	y = m * x + t

Example
-------
Here you can provide an Example in `doctest`_ format

    
>>> import exmplpckg as ep
>>> P1 = [3,4]    
>>> P2 = [6,8]	
>>> linf = ep.LinearFunction(P1,P2)
>>> linf.calc_y(3)
4
	

Notes
-----
* Here you can specify more stuff
* e.g. in a list

.. _sphinx:
   http://www.sphinx-doc.org/en/master/
.. _readthedocs:  
   https://readthedocs.org/	
.. _include documentation from docstrings:
   http://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _NumPy Documentation HOWTO:
   https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _doctest:
   https://docs.python.org/3/library/doctest.html
"""


class LinearFunction(object):
    """Linear function object

    Some more description of your class

    Attributes
    ----------
    m : float
        slope of the linear function
    t : float
        offset of the linear function.

    """

    def __init__(self, P1, P2):
        """Example of docstring on the __init__ method.

        initializes m and t and then calls he "fit" method

        """
        self.m = 1
        self.t = 0
        self.fit(P1, P2)

    def fit(self, P1, P2):
        """Calculate slope m and offset t.

        Parameters
        ----------
        P1 : list
            List with x and y value of point 1: P1 = [x,y]
        P2 : list
            List with x and y value of point 2: P2 = [x,y]
        """

        self.m = (P2[1] - P1[1]) / (P2[0] - P1[0])
        self.t = P1[1] - P1[0] * self.m

    def calc_y(self, x):
        """Calculate function output for given x

        Parameters
        ----------
        x : float
            any float number
			
        Returns
        -------
        float
            function output y = m*x + t

        """
		
        y = self.m * x + self.t
		
        return y