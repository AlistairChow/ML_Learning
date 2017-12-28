#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def forward_euler():
    h = 0.1
    g = 9.81

    num_steps = 50

    t = np.zeros(num_steps + 1)
    x = np.zeros(num_steps + 1)
    v = np.zeros(num_steps + 1)

    for step in range(num_steps):
        t[step + 1] = h * (step + 1)
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] - h * g
    return t, x, v


t, x, v = forward_euler()

axes_height = plt.subplot(211)
plt.plot(t, x)
plt.ylabel('Height in m')
axes_velocity = plt.subplot(212)
plt.plot(t, v)
plt.ylabel('Velocity in m/s')
plt.xlabel('Time in s')

plt.show()