#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os,glob

# reading files
fnames = sorted(glob.glob1(os.getcwd()+"/solution_data/", "*.csv"))
fid = pd.read_csv("solution_data/"+fnames[-1], delim_whitespace=True)

Nx = 101
Ny = 101

# transforming data into matrix
X = fid['X'].to_numpy().reshape([Ny,Nx]).transpose()
Y = fid['Y'].to_numpy().reshape([Ny,Nx]).transpose()
U = fid['U'].to_numpy().reshape([Ny,Nx]).transpose()
V = fid['V'].to_numpy().reshape([Ny,Nx]).transpose()
P = fid['P'].to_numpy().reshape([Ny,Nx]).transpose()

# plotting contours
Umag = np.sqrt(U**2+V**2)

# magnitude contour
plt.figure()
plt.contourf(X,Y,Umag,100,cmap = 'jet')
plt.colorbar()
plt.axis('image')
plt.title("velocity magnitude")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("velocityMagnitude.png", dpi = 150)

# x-velocity contour
plt.figure()
plt.contourf(X,Y,U,100,cmap = 'jet')
plt.colorbar()
plt.axis('image')
plt.title("x-velocity")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("x-velocity.png", dpi = 150)

# y-velocity contour
plt.figure()
plt.contourf(X,Y,V,100,cmap = 'jet')
plt.colorbar()
plt.axis('image')
plt.title("y-velocity")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("y-velocity.png", dpi = 150)

# pressure contour
plt.figure()
plt.contourf(X,Y,P,100,cmap = 'jet')
plt.colorbar()
plt.axis('image')
plt.title("Pressure")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("velocityMagnitude.png", dpi = 150)

plt.show()
