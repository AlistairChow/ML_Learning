#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
import random as rd


def sin_cos():

    num_point = 50

    x = np.zeros(num_point)
    sin_x = np.zeros(num_point)
    cos_x = np.zeros(num_point)

    for i in range(num_point):
        x[i] = 2. * math.pi * i / (num_point - 1.)
        sin_x[i] = math.sin(x[i])
        cos_x[i] = math.cos(x[i])
    return x, sin_x, cos_x


x, sin_x, cos_x = sin_cos()

plt.plot(x, sin_x)
plt.plot(x, cos_x)
plt.show()