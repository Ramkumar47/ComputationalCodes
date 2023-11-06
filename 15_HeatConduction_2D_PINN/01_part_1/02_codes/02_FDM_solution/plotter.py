#!/bin/python3
"""----------------------------------------------------------------------------
plotter script for 2d HC
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading computed data
fid = pd.read_csv("computed_data.csv")

# removign extra spaces in the column names
fid = fid.rename(columns = lambda x : x.strip())

# getting array of fields
X = fid["X"].to_numpy()
Y = fid["Y"].to_numpy()
T = fid["T"].to_numpy()

# reshaping to get the contours
N = int(np.sqrt(X.shape[0]))
X = X.reshape(N,N)
Y = Y.reshape(N,N)
T = T.reshape(N,N)

# defining analytical function
def analytical_solution(xa,ya,n):
    L = H = 1
    theta_val = 0
    for i  in range(n):
        A = np.sinh((2*i+1)*np.pi*(L-xa)/H)/np.sinh((2*i+1)*np.pi*L/H)
        B = np.sin((2*i+1)*np.pi*ya/H)/(2*i+1)
        theta_val += 4.0/np.pi*A*B
    return theta_val

# computing mid-x and mid-y data for analytical comparision
T_midy = T[:,int(N/2)]
X_midy = X[:,int(N/2)]
Y_midy = Y[:,int(N/2)]
T_midy_a = analytical_solution(X_midy,Y_midy,100)

T_midx = T[int(N/2),:]
X_midx = X[int(N/2),:]
Y_midx = Y[int(N/2),:]
T_midx_a = analytical_solution(X_midx,Y_midx,100)

# plotting contours
plt.rcParams.update({'font.size':15})

plt.figure(figsize=(13,8))
plt.contourf(X,Y,T,100,cmap = 'jet')
plt.axis("image")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.savefig("contour.png", dpi = 150)

plt.figure(figsize=(13,8))
plt.subplot(1,2,1)
plt.plot(X_midy, T_midy,'-b', label = "FDM")
plt.plot(X_midy, T_midy_a, '-r', label = "analytical")
plt.legend()
plt.xlabel("X")
plt.ylabel("T")
plt.grid()
plt.title("mid y slice plot")
plt.subplot(1,2,2)
plt.plot(T_midx,Y_midx,'-b', label = "FDM")
plt.plot(T_midx_a,Y_midx,'-r', label = "analytical")
plt.legend()
plt.xlabel("T")
plt.ylabel("Y")
plt.grid()
plt.title("mid x slice plot")
plt.savefig("plots.png", dpi = 150)

plt.show()
