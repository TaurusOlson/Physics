#!/opt/local/bin/python

#----------------------------------------------
# interpolin.py -- Linear interpolation
# @Author        : Taurus Olson
# @License       : GPL (see http://www.gnu.org/licenses/gpl.txt)
# @Created       : 2010-02-24.
# @Revision      : 0.0
#----------------------------------------------
# Description    : <+DESCRIPTION+>
# Usage          : <+USAGE+>
#----------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import random


# ----------------------------------------------------------------------------
#       FUNCTIONS
# ----------------------------------------------------------------------------

def interpolin(points, values, grid):
    """Linear interpolation"""

    f =  values[0:-1]   * (points[1:] - grid[0:]) / (points[1:] - points[0:-1]) +\
            values[1:] * (grid[0:] - points[0:-1])   / (points[1:] - points[0:-1]) 
    return f

def interpol_error(points):
    """Error of the interpolation of the function x**2 """

    return ( (points[0:-1] - points[1:])**2 ) / 4.0


# ----------------------------------------------------------------------------
#       INPUT PARAMETERS
# ----------------------------------------------------------------------------

# Number of points
npoints = 30

# Domain
xmax = 10
xmin = -xmax

# Random points
rp = []
for i in range(npoints):
    rp.append(random.randint(xmin,xmax))

# Sort list necessary after the random
rp = np.sort(rp)

# Values we know at given points
points = np.array(rp)
# values = np.array(map(lambda x: x**2, points))
values = np.array(map(lambda x: np.log(x), points))

# Our grid
grid = np.array( map(lambda x, y: (x + y) / 2.0, points[0:-1],  points[1:]) )


# ----------------------------------------------------------------------------
#       PROCESSING
# ----------------------------------------------------------------------------

f = interpolin(points, values, grid)
error = interpol_error(points)


# ----------------------------------------------------------------------------
#       DISPLAY
# ----------------------------------------------------------------------------

print "values: ", values
print "f: ", f

print "diff: ", np.abs(f[0:]-values[0:-1])
print "error: ", error

plt.plot(points, values, 'r*')
plt.errorbar(grid, f, yerr = error, fmt = '+')
plt.show()

