# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:18:52 2022
@author: zorik
"""

"Exc. 1 - Potenial Simulation"
#%%

import numpy as np # math functions
import scipy # scientific functions
import scipy.stats # contains linregress (for linear regression)
import matplotlib.pyplot as plt # for plotting figures and setting their properties
import pandas as pd # handling data structures (loaded from files)
from scipy.optimize import curve_fit as cfit # non-linear curve fitting

"Potential, x and y"
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

"Potential, x"
x = np.linspace(-a, a , 21)

V_x = potential(x, 0, a, C)

plt.plot(x, V_x, '.')

#%%

"Exc. 2 - Capacitor"

"Theoretical C and Tau"
eps0 = 8.854e-12 
d = 0.5e-3
D = 18e-2
area = np.pi * D**2 / 4

C_theoretical = eps0 * area / d

Rtot = 38.4e3
R    = 977

tau_theoretical = Rtot * C_theoretical

#%%

"Loading Data"

C_data = pd.read_csv('capacitor.csv')
C_data = C_data.rename(columns = {"time (sec)":"t", "ch2":"V_R"})

C_data["V_C"] = C_data["ch1"] - C_data["V_R"]

#%%

"Plottng V_C over time"

plt.plot(C_data["t"], C_data["V_C"], '.')

#%%

"Fitting a function to data"

def V_decay(t,a,b):
    return a*np.exp(-t*b)

fit2 = cfit(V_decay,C_data['t'], C_data["V_C"])
plt.plot(C_data['t'], V_decay(C_data['t'],fit2[0][0],fit2[0][1]))

#%%

"Logarithm of data plot"
inds = (C_data['t'] > 0) & (C_data['t'] < 3e-5)
plt.plot(C_data['t'][inds], np.log(np.array(C_data["V_C"][inds])),'.')
plt.grid()

#%%

"Linear Regression on log values and calculating V_R integral"
reg2 = scipy.stats.linregress(C_data['t'][inds], np.log(C_data["V_C"][inds]))
print('slope:', reg2.slope)
print('intercept:', reg2.intercept)

V_0_reg = np.exp(reg2.intercept)
tau_reg = -1/reg2.slope

C_data["int_V_R"] = scipy.integrate.cumtrapz(C_data["V_R"], x = C_data["t"], initial = 0)

#%%

"Plotting capacitor voltage over integral of V_R and linear regression for C_meas"
plt.plot(C_data["int_V_R"], C_data["V_C"], '.')

reg3 = scipy.stats.linregress(C_data['int_V_R'], C_data["V_C"])
print('slope:', reg3.slope)
print('intercept:', reg3.intercept)

C_meas = 1/(R * reg3.slope)

"plotting regresion"
plt.plot(C_data["int_V_R"],C_data["int_V_R"]*reg3.slope + reg3.intercept)
plt.xlabel("integral of V_R")
plt.ylabel("V_C")
plt.legend(["data","regression"])
plt.grid("both")

#%%

"Exc. 3 - Ohm's Law"

"Functions and getting the data"

def I_R(V2, R1):
    return V2/R1

def V_R(V1, V2):
    return V1-V2

def R_t(V_R, I_R):
    return V_R / I_R

def P_t(V_R, I_R):
    return V_R * I_R 

def Energy(P_t, t):
    return scipy.integrate.cumtrapz(P_t, x = t, initial = 0)

R_data = pd.read_csv("ohm.csv", header = 1)
R_data = R_data.rename(columns = {"Time (s)":"t", "1 (VOLT)":"V1", "2 (VOLT)":"V2"})

"Calculating resistance"

I_R = I_R(R_data["V2"], 5.48)
V_R = V_R(R_data["V1"], R_data["V2"])
P_t = P_t(V_R, I_R)

R_t = R_t(V_R, I_R)
energy = Energy(P_t, R_data["t"])


#%%

"Plotting R_t over the energy"
inds = (energy > 0.2) & (energy < 0.9)
plt.plot(energy[inds], R_t[inds], '.')

#%%

"Linear regression"

reg4 = scipy.stats.linregress(energy, R_t)
R0 = reg4.intercept
slope_constants = reg4.intercept / R0

#%%


"Exc. 4 - Inductance"

L = np.array([30, 24, 18, 14, 8])
Ind_data = []
phiRef = []
phiSignal = []
maxTimeRef = []
maxTimeSignal = []
t_coil = []


def calcPhi(t, V):
    return scipy.integrate.cumtrapz(V, x = t, initial = 0)

def findMaxTime(V):
    return np.argmax(V)

def calcLoverTErr(L, t_coil, Lerr, Terr):
    t_coil = np.array(t_coil)
    L = np.array(L)
    LoverT = L / t_coil
    LoverTErr = LoverT * np.sqrt((Terr / t_coil)**2 + (Lerr / L)**2)
    return LoverTErr

for n in range(0,5,1):
    df = pd.read_csv('Trace %d.csv'%(n,),header = 1)
    df = df.rename(columns = {"Time (s)":"t", "1 (VOLT)":"ref", "2 (VOLT)":"signal"})
    phiRef.append(np.abs(calcPhi(df["t"], -df["ref"])))
    phiSignal.append(np.abs(calcPhi(df["t"], -df["signal"])))
    Ind_data.append(df)
    
    CurrentMaxTimeRef = df["t"][findMaxTime(df["ref"])]
    CurrentMaxTimeSignal = df["t"][findMaxTime(df["signal"])]
    
    t_coil.append(CurrentMaxTimeSignal - CurrentMaxTimeRef)
    maxTimeRef.append(CurrentMaxTimeRef)  
    maxTimeSignal.append(CurrentMaxTimeSignal)

LoverT = L / t_coil

# plt.plot(t_coil, LoverT, '.')

LoverTErr = calcLoverTErr(L, t_coil, 0.2, 10**-2)
plt.errorbar(t_coil, LoverT, LoverTErr, 10**-2)
