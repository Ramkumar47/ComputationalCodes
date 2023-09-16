#!/bin/python3
"""----------------------------------------------------------------------------
Numerical solution of Falkner-Skan wedge flow equation using
shooting method
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from copy import copy as cp

# defining computation parameters----------------------------------------------
m_values = [-0.0904]
eta_max = 10.0

tolerance = 1e-6

dn = 0.0001

# computation variables definition---------------------------------------------
f = []
#  z = np.zeros(N_eta)


# function definitions section-------------------------------------------------
# test function definition
def test_func(h_init,m):
    # defining initial conditions
    g0 = 0
    h0 = cp(h_init)
    f0 = 0

    eta = 0
    # computing solution
    while eta <= eta_max:
        # computing derivatives
        dfdn = g0*1 # *1 to prevent absolute referencing
        dgdn = h0*1
        dhdn = -(1 - g0**2)*m - (m+1)/2*f0*h0

        # computing next step values
        f1 = f0 + dfdn*dn
        g1 = g0 + dgdn*dn
        h1 = h0 + dhdn*dn

        # updating values
        f0 = cp(f1)
        g0 = cp(g1)
        h0 = cp(h1)
        eta += dn

    return g1

# solution making function definition
def make_solution(h_init,m):
    # defining lists to store values with initial conditions
    f = [0]
    g = [0]
    h = [h_init]
    eta = [0]

    g0 = g[-1]
    h0 = h[-1]
    f0 = g[-1]

    # computing solution
    while eta[-1] <= eta_max:

        # computing derivatives
        dfdn = g0*1 # *1 to prevent absolute referencing
        dgdn = h0*1
        dhdn = -(1 - g0**2)*m - (m+1)/2*f0*h0

        # computing next step values
        f1 = f0 + dfdn*dn
        g1 = g0 + dgdn*dn
        h1 = h0 + dhdn*dn

        # appending to the list
        f.append(f1)
        g.append(g1)
        h.append(h1)
        eta.append(eta[-1]+dn)

        # updating values
        f0 = cp(f1)
        g0 = cp(g1)
        h0 = cp(h1)

    print("solution done")

    return f,g,h,eta

# computation section----------------------------------------------------------
# making lists to store computed values
f_list = []
g_list = []
h_list = []

# looping through m values
for i in range(len(m_values)):

    print("solving for m = ",m_values[i])

    # running bisection to compute exact value
    h_a = 0
    h_b = 1
    h_c = (h_a + h_b)/2.0

    while abs(test_func(h_c,m_values[i]) - 1.0) > 1e-6:
        res = test_func(h_c,m_values[i]) - 1.0

        if res < 0:
            h_a = cp(h_c)
        else:
            h_b = cp(h_c)

        h_c = (h_a + h_b)/2.0

    # getting solution for the obtained initial condition
    f,g,h,eta = make_solution(h_c, m_values[i])

    # appending the solution to the list
    f_list.append(f)
    g_list.append(g)
    h_list.append(h)



# post-processing section------------------------------------------------------

# preparing dataframe to save the data
fid = pd.DataFrame(np.transpose([f,g,h,eta]), columns = ["f","g","h","eta"])
fid.to_csv("table_data_m=-0.0904.csv", index = None)

# plotting graphs
plt.figure()
for i in range(len(m_values)):
    plt.plot(g_list[i], eta, label = "m = "+str(m_values[i]))
plt.grid()
plt.xlabel(r"$u/u_e$")
plt.ylabel(r"$\eta$")
plt.title(r"$u/u_e$ vs $\eta$")
plt.legend()
plt.savefig("plot_1.png", dpi = 150)


plt.show()
