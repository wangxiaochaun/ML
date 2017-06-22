# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:23:02 2017

@author: ThinkStation
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)
gama = 2; miu = 1

#y = 1 / (2 * gama) * np.exp(-np.abs(x - miu) / gama)
y = np.log(1 + np.exp(x))

fig = plt.subplot(111)

ax = plt.plot(x, y)

plt.show()