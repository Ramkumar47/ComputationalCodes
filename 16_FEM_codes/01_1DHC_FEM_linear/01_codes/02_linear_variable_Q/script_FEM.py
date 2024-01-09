#!/bin/python3
"""----------------------------------------------------------------------------
Finite Element solution of 1D HC with source

with
 - linear shape function
 - variable source Q(x)

 Main script
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# importing all the input parameters
from inputFile import *

# number of nodes from number of quadratic elements
N_nod = N_ele + 1

# uniformly discretizing the domain: node coordinates
X_n = np.linspace(0,L,N_nod)

# computing element length
h = X_n[1] - X_n[0]

# initializing A, b matices in Ax=b system
A = np.zeros([N_nod, N_nod])
b = np.zeros([N_nod])

# filling up the A and b matrices
for i in range(N_ele):
    A[i,i]     +=  K/h
    A[i,i+1]   += -K/h
    A[i+1,i]   += -K/h
    A[i+1,i+1] +=  K/h
    b[i]   += -K*(2-6*X_n[i])*h/2
    b[i+1] += -K*(2-6*X_n[i+1])*h/2

# dropping first and last equation components bcoz, fixed T bc (T @ bc is known)
A = A[1:-1,1:-1]
b = b[1:-1]

# computing intermediate temperature profile
T = np.matmul(np.linalg.inv(A),b)

# appending the boundary temperatures to the obtained profile
T = np.r_[0,T,0]

# computing analytical solution
T_a = AnalyticalFunction(X_n)

# computing absolute difference
T_err = np.abs(T-T_a)

# writing out solution file
fid = pd.DataFrame(np.transpose([X_n,T,T_a]), columns = ["X","T","Ta"])
fid["T_err"] = T_err
fid.to_csv(out_fileName, index = None)

# plotting
plt.figure()
plt.plot(X_n,T,'-b', label = "FEM")
plt.plot(X_n,T_a,'*r', label = "Analytical")
plt.grid()
plt.xlabel("X")
plt.ylabel("T")
plt.legend()
plt.savefig(out_figName, dpi = 150)

plt.figure()
plt.plot(X_n,T_err,'-b')
plt.grid()
plt.xlabel("X")
plt.ylabel("absolute error")
plt.savefig(out_errFigName,dpi = 150)

plt.show()
