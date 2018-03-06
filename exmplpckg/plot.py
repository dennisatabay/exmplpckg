# -*- coding: utf-8 -*-
"""
In this file we define all (here one) methods for plotting. We do this in 
a seperate file because plotting functions usually need many lines of code.
(And to have two different files in this example).
Of courese we could simply add this in the base file (also as a method), 
which even might be the better solution...
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_linf(linf,xrange = [0,10]):
    """Plot the linear function


    Parameters
    ----------
    linf :
        LinearFunction object containing  slope m and offset t
			
    Returns
    -------
    figure
        matplotlib figure object

    """
		
    fig = plt.figure(figsize = [11, 7])
    ax = fig.add_subplot(111)
    y1 = linf.calc_y(xrange[0])
    y2 = linf.calc_y(xrange[1])
    ax.plot(xrange,[y1,y2],lw=3)
    ax.set_xlabel('x',fontsize=18)
    ax.set_ylabel('y',fontsize=18)
    ax.tick_params(labelsize=16)
    ax.set_title('y = ' + str(linf.m)+'*x + '+str(linf.t))
    fig.tight_layout()
    plt.show()
		
    return fig   