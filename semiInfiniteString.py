#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:26:17 2019

@author: Benjamin Keene

Animation of semi-infinite string with zero initial displacement and
piecewise defined initial velocity.

U_tt = c^2 * U_xx     t,x > 0
U(x,0) = 0              x > 0
U_t(x, 0) = g(x)        x > 0
U(0, t) = 0             t > 0

g(x) = {0,    0 < x < 1
        2,    1 < x < 2
        0,    2 < x    }

This program defines a function G(x, c) which represents the integral of the
ODD extension of our initial velocity equation for the wave equation.  Then
sample graphs are printed out that model our equation at given times t.
"""

import numpy as np
import matplotlib.pyplot as plt
# %%


def G(x, c):  # Integral of g_odd(x) (which is now an even function)
    if 0 <= x < 1:
        return -1 * (1 / (2 * c))
    elif 1 <= x < 2:
        return (2 * (x - 3 / 2)) * (1 / (2 * c))
    elif 2 <= x:
        return 1 * (1 / (2 * c))
# %%


def U(x, c, t):  # Construct U(x, t) for a given c
    if x <= (c * t):  # Reflect characterstic across y-axis
        return (G(x + (c * t), c) - G((c * t) - x, c))
    elif x > (c * t):  # Plot characteristics as they are
        return (G(x + (c * t), c) - G(x - (c * t), c))
# %%


def Gleft(x, c, t):
    if x > (c * t):
        return (-1) * G(x - (c * t), c)
    else:
        return (-1) * G((c * t) - x, c)


def Gright(x, c, t):
    if x > (c * t):
        return G(x + (c * t), c)
    else:
        return G((x + (c * t)), c)


def Xaxis():
    return 0


wfun = np.vectorize(U)
lfun = np.vectorize(Gleft)
rfun = np.vectorize(Gright)

x = np.linspace(0, 6, 1000)  # Plot for positive x values only (semi-infinite)
# %%

#  count = 1
for t in np.linspace(0, 1.5, 151):
    y = wfun(x, 2, t)
    left = lfun(x, 2, t)
    right = rfun(x, 2, t)
#    fig = plt.figure()
    plt.plot(x, y)
    plt.plot(x, left, color='green', linestyle='dashed')
    plt.plot(x, right, color='red', linestyle='dashed')

    plt.legend(loc='lower center')
    plt.ylabel('u (x,' + str(round(t, 2)) + ")")
    plt.xlabel('x')
    plt.axis([0, 6, -.5, .75])
    plt.show()
#    print(str(count))
#    fig.savefig('./semiImages/image' + str(count).zfill(3) + ".png")
#    count = count + 1
