# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:18:52 2022

@author: zorik
"""

#%%

import numpy as np # math functions
import scipy # scientific functions
import scipy.stats # contains linregress (for linear regression)
import matplotlib.pyplot as plt # for plotting figures and setting their properties
import pandas as pd # handling data structures (loaded from files)
from scipy.optimize import curve_fit as cfit # non-linear curve fitting

"Potential"
C = 1
a = 1
L = 3
N = 100
coord = np.linspace(-L, L , N)
coord_x, coord_y = np.meshgrid(coord, coord)


def potential(x, y, a, C):
    potential = C * np.log(np.sqrt(np.power(x-a, 2) + np.power(y, 2))) - C * np.log(np.sqrt(np.power(x+a, 2) + np.power(y, 2)))
    return potential




V_xy = potential(coord_x, coord_y, a, C)

plt.figure()
plt.pcolormesh(coord_x, coord_y, V_xy)
plt.contour(coord_x, coord_y, V_xy, np.sort([-2 , -1, 0 , 1, 2]), cmap='hot')
#%%