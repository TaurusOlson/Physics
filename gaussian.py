#!/opt/local/bin/python
# --------------------------------------------
# Filename:   gaussian.py
# Description:
# Author: Taurus Olson
#
# Copyright (C) 2009, 
#
#|------------------------------------------------------------------------+
#|Creation and plot of the probability density function (pdf) for normal  |
#|distribution (a bell curve)                                             |
#|------------------------------------------------------------------------+
#|I. Cumulative distribution function                                     |
#|is nothing more than the integration of this pdf from -inf to x         |
#|i.e the probability that a random variable X is                         |
#|<= x (inferior or equal)                                                |
#|------------------------------------------------------------------------+

import numpy as np
import matplotlib.pyplot as plt

phi=0
phi=np.array(phi)

xmin = -5
xmax = 5
x = 0
x = np.arange(xmin, xmax+1, 0.1)

## sigma**2 = 1 & mu = 0##
#------------------------#
# HFWM
sigma = 1.0
# Mean  probability
mu = 0.0
phi = np.array( [np.exp(( -0.5 / sigma**2)*(X - mu)**2)  / ( sigma * np.sqrt( 2*np.pi ) ) for X in x] )
# Display
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(x, phi, 'r-')

# Axes
ax.set_xlabel('x')
ax.set_ylabel('phi(x)')
leg = ax.legend(('label1'), 'upper center', shadow = False)
#------------------------#

## sigma**2 = 0.2 & mu = 0##
#------------------------#

#width = [0.2]*len(x)
#plt.plot(x, width)
#-------------------#

# I. Cumulative distribution function (CDF)
#-------------------#
# vim: set tw=80:
