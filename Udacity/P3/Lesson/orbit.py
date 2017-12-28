#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt

moon_distance = 384e6


def orbit():
    num_steps = 50
    x = np.zeros([num_steps + 1, 2])

    for i in range(num_steps + 1):
        angle = 2. * math.pi * i / num_steps
        x[i, 0] = moon_distance * math.cos(angle)
        x[i, 1] = moon_distance * math.sin(angle)

    return


x = orbit()

plt.axis('equal')
plt.plot(x[:, 0], x[:, 1])
axes = plt.plot.gca()
plt.xlabel('Longitudinal position in m')