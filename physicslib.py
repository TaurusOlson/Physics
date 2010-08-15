#!/usr/bin/python

import numpy as np

def euler(fp, t0, y0, h, N):
    """
    Euler method.
    
    Arguments:
    - fp: derivative of the function we want to approximate 
    - t0: absciss (Initial condition)
    - y0: value of the function in t0 (Initial condition)
    - h: step of the calculus
    - N: number of points

    """

    # Initialization
    y = np.array(np.zeros(N))
    t = np.array(np.zeros(N))
    t[0] = t0
    y[0] = y0

    # Euler algorithm
    for i in range(N-1):
        y[i+1] = y[i] + h * fp(t[i], y[i])
        t[i+1] = t[i] + h
    return t, y


def RK4(fp, t0, y0, h, N):
    """
    Runge-Kutta 4 method.
    
    Arguments:
    - fp: derivative of the function we want to approximate 
    - t0: absciss (Initial condition)
    - y0: value of the function in t0 (Initial condition)
    - h: step of the calculus
    - N: number of points

    """

    # Initialization
    y = np.array(np.zeros(N))
    t = np.array(np.zeros(N))
    t[0] = t0
    y[0] = y0

    # RK algorithm
    for i in range(N-1):
        k1 = h * fp(t[i], y[i]) 
        k2 = h * fp(t[i] +  0.5 * h, y[i] + 0.5 * k1)
        k3 = h * fp(t[i] +  0.5 * h, y[i] + 0.5 * k2)
        k4 = h * fp(t[i] + h, y[i] + k3) 
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        t[i+1] = t[i] + h

    return t, y

