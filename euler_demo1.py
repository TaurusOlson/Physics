#!/usr/bin/python

from math import exp, sin
from physicslib import euler, RK4
import numpy as np

# FUNCTIONS
def func1(x, y):
    """Differential equation: y' = x + 2y"""
    return x + 2 * y

def func2(x, y):
    """docstring for func2"""
    return sin(x)**2

def write_file(fname, data, mode):
    """docstring for write_file"""
    f = open(fname, mode)
    f.write(data)

def exact_solution1(x):
    """ y(x) = 0.25 * exp(2*x) - 0.5 * (x + 0.5) """
    return (0.25 * exp(2*x) - 0.5 * (x + 0.5))


# ODE SOLVING
t, y = euler(func2, 0, 0, 0.2, 200)
# t, y = RK4(func2, 0, 0, 0.2, 200)

# EXACT SOLUTION with CAUCHY CONDITIONS (0, 0)
y_ex = np.array(np.zeros(len(t)))
for i in range(0, len(t)):
    y_ex[i] = exact_solution1(t[i])
print y_ex

# WRITING
filename = 'euler_1.dat'
f = open(filename, 'w')

for i in range(0, len(y)):
    output = "%f\t%f\t%f\n" % (t[i], y[i], y_ex[i])
    write_file(filename, output, 'a')


# DISPLAY MESSAGE
print "The data have been written in the file %s" % filename
