#!/opt/local/bin/python
# --------------------------------------------
# Filename:   rope.py
# Description: <+ SHORT_DESC +>
# Author: Taurus Olson
#
# Copyright (C) 2009, 
#
# --------------------------------------------
# Modelisation of a stationary wave:
# Tipycally it's the example of a rope vibrating rope
# Let's call a the distance between its 2 extremities
# --------------------------------------------

__author__ = "Taurus Olson"
__version__ = 0.1
__date__ =  ""

import numpy as np
import matplotlib.pyplot as plt

# Constants
#-------------------#
# Distance between extremities
a = 20
# Amplitude
B = np.sqrt(2.0/a)
# Mode of vibration
n = 3
# Nombre de points
N=a*10

# Loop
#-------------------#
psi = np.zeros((N,1))
psi[0,:] = 0

for i in np.arange(0,N-1):
    psi[i+1,:] = B * np.sin(i* n * np.pi/ N)

psi[N-1,:] = 0
x = np.linspace(0,a,N)

# Display
#-------------------#
plt.plot(x,psi,'r-')

#vim :set tw=80 fdm=indent
