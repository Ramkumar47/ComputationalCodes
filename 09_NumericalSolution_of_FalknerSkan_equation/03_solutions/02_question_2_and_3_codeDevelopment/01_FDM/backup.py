#!/bin/python3
"""----------------------------------------------------------------------------
Numerical solution of Falkner-Skan wedge flow equation using
finite difference method
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from copy import copy as cp

# defining computation parameters----------------------------------------------
m = 2
eta_max = 10.0
N_eta = 101

N_iteration = 101
tolerance = 1e-6

dn = eta_max/(N_eta-1)

# computation variables definition---------------------------------------------
f = np.zeros(N_eta)
#  z = np.zeros(N_eta)

# applying initial and boundary conditions
f[0] = 0
#  z[0] = 0
#  z[N_eta-1] = 1.0
z = np.linspace(0,1.0,N_eta)
eta = np.linspace(0,eta_max,N_eta)

# solution begin---------------------------------------------------------------
for itr in range(N_iteration):
    # marching the f equation from lower boundary
    for i in range(N_eta-1):
        f[i+1] = f[i] + 0.5*(z[i]+z[i+1])*dn

    # solving iteratively the z equation
    z_prev = cp(z)

    for j in range(1000):
        for i in range(1,N_eta-1):
            # computing coefficients
            ai = 2/dn**2 + m*z[i]
            bi = 1/dn**2 + (m+1)/4/dn*f[i]
            ci = 1/dn**2 - (m+1)/4/dn*f[i]
            di = cp(m)

            # solving equation
            z[i] = 1/ai*(bi*z[i+1] + ci*z[i-1]+di)
        # convergence check
        convergence = np.max(np.abs(z_prev - z))
        z_prev = cp(z)
        if convergence < tolerance:
            break

    # status update
    print("iteration : ", itr,"; z iteration : ",j,"; z convergence = ",convergence)
