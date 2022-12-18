#!/bin/python3
"""
1D heat conduction with source using spectral methods

plotting and error computation python script file
"""

# importing needed modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# reading the data file written by FORTRAN code
fid = pd.read_csv("data.csv")

# computing error percentage
error = np.max(np.abs(fid["T"]-fid["T_a"])/fid["T_a"])*100.0

# computing number of points to be displayed for analytical solution
N = int(fid.shape[0]*0.15)
Nval = np.linspace(0,fid.shape[0]-1,N, dtype=int)

# plotting graph
plt.figure()
plt.plot(fid["X"],fid["T"],'-b',label="spectral method")
plt.plot(fid["X"].iloc[Nval],fid["T_a"].iloc[Nval],'*r',label="analytical solution")
plt.grid()
plt.legend()
plt.xlabel("X")
plt.ylabel("T")
plt.title("Error = "+str(np.round(error,2))+" %")
plt.savefig("output.png", dpi = 150)

plt.show()
