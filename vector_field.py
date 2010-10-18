#!/usr/bin/python

# Simple snippet showing how to plot vector fields with pylab

from pylab import *

X,Y = meshgrid( arange(-2*pi,2*pi,.5),arange(-2*pi,2*pi,.5) )
# U = cos(X)
# V = sin(Y)

#1
figure()
Q = quiver(-Y, X)
# qk = quiverkey(Q, 0.5, 0.92, 2, r'$2 \frac{m}{s}$', labelpos='W',
#                fontproperties={'weight': 'bold'})

# l, r, b, t = axis()
# dx, dy = r - l, t - b
# axis([l - 0.05 * dx,
#       r + 0.05 * dx, 
#       b - 0.05 * dy,
#       t + 0.05 * dy,
#       ])

title('{-Y, X}')
show()
