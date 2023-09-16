import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Nx = 100
Ny = 100


X = np.zeros([Ny,Nx])
Y = np.zeros([Ny,Nx])

X[0,:] = np.linspace(0,1e-5,Nx)
X[Ny-1,:] = np.linspace(0,1e-5,Nx)
X[:,Nx-1] = 1e-5

Y[:,0] = np.linspace(0,1e-5,Ny)
Y[:,Nx-1] = np.linspace(0,1e-5,Ny)
Y[Ny-1,:] = 1e-5


# elliptic grid generation


X,Y = np.meshgrid(np.linspace(0,1e-4,Nx),np.linspace(0,1e-5,Ny))

fid = open("input_grid.dat","w")

fid.writelines('%5i%5i\n'%(Nx,Ny))
for i in range(Nx):
    for j in range(Ny):
        fid.writelines('%16.8E%16.8E\n'%(X[j,i],Y[j,i]))

fid.close()
