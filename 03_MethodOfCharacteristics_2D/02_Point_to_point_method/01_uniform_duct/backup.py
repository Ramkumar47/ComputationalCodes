#!/bin/python3

import numpy as np
import pandas as pd

# disabling setting with a copy warning
pd.options.mode.chained_assignment = None  # default='warn'

# input data-------------------------------------------------------------------
# number of char points in the inlet
N = 4

# number of wall bounces required
n_wall = 3

# inlet Mach number
M_inlet = 1.5

# ratio of specific heats
g = 1.4

# lower wall angle
theta_lower = np.radians(0.0)

# upper wall angle
theta_upper = np.radians(0.0)

# channel height in m
height = 1.0

# initializing dataframe with char points--------------------------------------
# getting total number of char points including inlet ones
N_total = n_wall*(2*N-1)+N

# preparing a list of char points and making a dataframe
fid = pd.DataFrame(np.transpose(np.linspace(1,N_total,N_total,dtype=int)),
        columns = ["N"])
fid["N1"] = 0
fid["N2"] = 0

# preparing list of bottom wall points
pnts_bottom = [1]
pnts_top = [N]
while True:
    val = pnts_bottom[-1] + (2*N-1)
    if val > N_total:
        break
    pnts_bottom.append(val)
    pnts_top.append(val + N-1)

# assigning dependence char points
for i in range(N,N_total):
    # getting current char point
    N_curr = fid["N"].iloc[i]

    # checking if the current point is on a wall
    if N_curr in pnts_bottom:
        fid["N1"].iloc[i] = 0
        fid["N2"].iloc[i] = N_curr - N + 1
    elif N_curr in pnts_top:
        fid["N1"].iloc[i] = N_curr - N
        fid["N2"].iloc[i] = 0
    else:
        fid["N1"].iloc[i] = N_curr - N
        fid["N2"].iloc[i] = N_curr - N + 1

# adding needed columns for further computation
fid["M"] = 0
fid["K1"] = 0
fid["K2"] = 0
fid["theta"] = 0
fid["nu"] = 0
fid["mu"] = 0
fid["X"] = 0
fid["Y"] = 0

# function definitions---------------------------------------------------------
# prandtl-meyer function
def PM_nu(Mach):
    val = (np.sqrt((g+1)/(g-1))*np.arctan(np.sqrt((g-1)/(g+1)*(Mach**2-1)))
            - np.arctan(np.sqrt(Mach**2-1)))
    return val

# inverse prandtl-meyer function
def inv_PM(nu):
    # using bisection method

    # initial values of mach numbers
    Ma = 1
    Mb = 200
    Mc = (Ma+Mb)/2

    # begin loop
    while abs(nu - PM_nu(Mc)) > 1e-6:
        # computing residual
        res = nu - PM_nu(Mc)

        # deciding the offset side
        if res > 0:
            Ma = Mc
        else:
            Mb = Mc

        # updating Mc value
        Mc = (Ma+Mb)/2

    return Mc


# begin computation------------------------------------------------------------
# initializing inlet data in the dataframe
fid["M"].iloc[0:N] = M_inlet #  Mach no
fid["theta"].iloc[0:N] = 0.0 #  flow deflection angle
fid["nu"].iloc[0:N] = PM_nu(M_inlet) # PM function value
fid["mu"].iloc[0:N] = np.arcsin(1/M_inlet) # Mach angle

# computing K1 and K2 for inlet char points
for i in range(N):
    # getting curr char point no.
    N_curr = fid["N"].iloc[i]

    # checking if the current point is on a wall
    if N_curr in pnts_bottom:
        fid["K1"].iloc[i] = 0
        fid["K2"].iloc[i] = fid["theta"].iloc[i] - fid["nu"].iloc[i]
    elif N_curr in pnts_top:
        fid["K1"].iloc[i] = fid["theta"].iloc[i] + fid["nu"].iloc[i]
        fid["K2"].iloc[i] = 0
    else:
        fid["K1"].iloc[i] = fid["theta"].iloc[i] + fid["nu"].iloc[i]
        fid["K2"].iloc[i] = fid["theta"].iloc[i] - fid["nu"].iloc[i]

# initializing x and y coordinates for inlet char points
dy = height/(N-1)
for i in range(N-1):
    fid["Y"].iloc[i+1] = fid["Y"].iloc[i] + dy
    fid["X"].iloc[i+1] = 0

# begining loop over all internal char points
for i in range(N,N_total):
    # getting current char point id
    N_curr = fid["N"].iloc[i]

    # checking if it is on bottom wall
    if N_curr in pnts_bottom:
        # it has only K1 characteristics and theta as theta_lower
        theta = theta_lower

        # getting index of dependence node
        n1 = fid["N1"].iloc[i] - 1

        # getting K1 value
        K1 = fid["K1"].iloc[n1]

        # computing nu from K1 characteristics: nu + theta = K1
        nu = K1 - theta

        # computing Mach number for the given nu value
        M = inv_PM(nu)

        # computing Mach angle
        mu = np.arcsin(1/M)

        # computing slope S1 for K1 characteristics
        S1 = (np.tan(theta + mu) +
                np.tan(fid["theta"].iloc[n1]+fid["nu"].iloc[n1]))/2

        # computing the x position of current char pnt
        x = (fid["X"].iloc[n1] - fid["Y"].iloc[n1])/(S1-np.sin(theta_lower))

        # computing the y position of current char pnt
        y = x*np.sin(theta_lower)

    # checking if it is on top wall
    elif N_curr in pnts_top:
        # it has only K2 characteristics and theta as theta_upper
        theta = theta_upper

        # getting index of dependence node
        n2 = fid["N2"].iloc[i] - 1

        # getting K1 value
        K2 = fid["K2"].iloc[n2]

        # computing nu from K2 characteristics: nu - theta = K2
        nu = K2 + theta

        # computing Mach number for the given nu value
        M = inv_PM(nu)

        # computing Mach angle
        mu = np.arcsin(1/M)

        # computing slope S2 for K2 characteristics
        S2 = (np.tan(theta - mu) +
                np.tan(fid["theta"].iloc[n2]-fid["nu"].iloc[n2]))/2

        # computing the x position of current char pnt
        x = (height + fid["X"].iloc[n2] - fid["Y"].iloc[n2])/(S2-np.sin(theta_upper))

        # computing the y position of current char pnt
        y = x*np.sin(theta_upper) + height

    # working on internal char points
    else:
        # it has both K1 and K2 characteristics

        # getting index of dependence nodes
        n1 = fid["N1"].iloc[i] - 1
        n2 = fid["N2"].iloc[i] - 1

        # getting K1 and K2 value
        K1 = fid["K1"].iloc[n1]
        K2 = fid["K2"].iloc[n2]

        # computing nu and theta
        #  nu = (K1+K2)/2
        nu = abs(K1+K2)/2
        theta = (K1-K2)/2

        # computing Mach number for the given nu value
        M = inv_PM(nu)

        # computing Mach angle
        mu = np.arcsin(1/M)

        # computing slope S1 for K1 characteristics
        S1 = (np.tan(theta + mu) +
                np.tan(fid["theta"].iloc[n1]-fid["nu"].iloc[n1]))/2

        # computing slope S2 for K2 characteristics
        S2 = (np.tan(theta - mu) +
                np.tan(fid["theta"].iloc[n2]-fid["nu"].iloc[n2]))/2

        # computing the x position of current char pnt
        x = ((S2*fid["X"].iloc[n2] - S1*fid["X"].iloc[n1]) +
                  (fid["Y"].iloc[n1]-fid["Y"].iloc[n2]))/(S2-S1)

        # computing the y position of current char pnt
        y = fid["Y"].iloc[n1] + (x - fid["X"].iloc[n1])*S1

    # updating the data frame
    fid["nu"].iloc[i] = nu
    fid["M"].iloc[i] = M
    fid["mu"].iloc[i] = mu
    fid["theta"].iloc[i] = theta
    fid["X"].iloc[i] = x
    fid["Y"].iloc[i] = y


print(fid)
