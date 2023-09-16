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
import os

# defining computation parameters----------------------------------------------
m_values = [2,1,0.6,0.3,0,-0.05,-0.08]
eta_max = 10.0
N_eta = 201

N_iteration = 101
tolerance = 1e-6

dn = eta_max/(N_eta-1)

# computation variables definition---------------------------------------------
f_list = []; z_list = []

f = np.zeros(N_eta)
#  z = np.zeros(N_eta)

# applying initial and boundary conditions
f[0] = 0
#  z[0] = 0
#  z[N_eta-1] = 1.0
z = np.linspace(0,1.0,N_eta)
eta = np.linspace(0,eta_max,N_eta)

# solution begin---------------------------------------------------------------
for m in m_values:
    # reinitializing conditions
    f = np.zeros(N_eta)
    z = np.linspace(0,1.0,N_eta)
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
        print("m = ",m,"; iteration : ", itr,"; z iteration : ",j,
                "; z convergence = ",convergence)
    f_list.append(f)
    z_list.append(z)

# post processing section------------------------------------------------------
# obtaining computation variables
f_d_list = z_list
f_dd_list = []

# computing f_double dash
f_dd = np.zeros(N_eta)
for i in range(len(f_d_list)):
    z = f_d_list[i]
    f_dd = np.zeros(N_eta)
    for j in range(1,N_eta-1):
        f_dd[j] = (z[j+1] - z[j-1])/dn/2.0
    # linear interpolation on boundaries
    f_dd[0] = 2*f_dd[1] - f_dd[2]
    f_dd[N_eta-1] = 2*f_dd[N_eta-2] - f_dd[N_eta-3]

    print("name=",i,"\n",f_dd)

    # appending to list
    f_dd_list.append(f_dd)

# preparing dataframe to store computed values to csv
# refreshing storage directory
os.system("rm -rf tables_csv && mkdir tables_csv")
# looping through each m_values
for i in range(len(m_values)):
    # preparing data frame
    fid = pd.DataFrame(np.transpose([eta,f_list[i],f_d_list[i],f_dd_list[i]]),
            columns=["eta","f","g","h"])
    # preparing filename
    fname = "tables_csv/data_table_m="+str(m_values[i])+".csv"
    # writing to csv
    fid.to_csv(fname, index = None)


plt.figure()
for i in range(len(m_values)):
    plt.plot(z_list[i],eta,label='m = '+str(m_values[i]))
plt.grid()
plt.legend()
plt.xlabel("$u/u_e$")
plt.ylabel("$\eta$")
plt.title(r"$u/u_e$ vs $\eta$")
plt.savefig("plot_1.png", dpi = 150)

plt.figure()
for i in range(len(m_values)):
    plt.plot(eta/2*z_list[i],eta,label='m = '+str(m_values[i]))
plt.grid()
plt.legend()
plt.xlabel(r"$\left(v \sqrt{Re_x}\right)/u_e$")
plt.ylabel(r"$\eta$")
plt.title(r"$\left(v \sqrt{Re_x}\right)/u_e$ vs $\eta$")
plt.savefig("plot_2.png", dpi = 150)

plt.show()
