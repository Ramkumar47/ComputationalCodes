import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from copy import copy as cp


Nx = 200
Ny = 200


X = np.zeros([Ny,Nx])
Y = np.zeros([Ny,Nx])

Lx = 0.00005
Ly = 0.00005

X,Y = np.meshgrid(np.linspace(0,Lx,Nx),np.linspace(0,Ly,Ny))

Y[0,:] = np.tan(np.radians(10))*X[0,:]
#  Y[:,Nx-1] = np.linspace(Y[0,Nx-1],Y[Ny-1,Nx-1],Ny)
for i in range(Nx):
    Y[:,i] = np.linspace(Y[0,i],Y[Ny-1,i],Ny)
    #  Y[:,i] = np.linspace(0,1,Ny)**1*(Y[Ny-1,i]-Y[0,i]) + Y[0,i]

#  # elliptic grid generation-----------------------------------------------------
#  dE = 1.0
#  dN = 1.0
#
#  Y_old = cp(Y)
#  for itr in range(1000):
#      for i in range(1,Nx-1):
#          for j in range(1,Ny-1):
#              # computing alpha
#              alpha = ((X[j+1,i] - X[j-1,i])/dN/2.0)**2 + ((Y[j+1,i] - Y[j-1,i])/dN/2.0)**2
#
#              # computing beta
#              beta = ((X[j+1,i] - X[j-1,i])/dN/2.0*(X[j,i+1] - X[j,i-1])/dE/2.0) + ((Y[j+1,i] - Y[j-1,i])/dN/2.0*(Y[j,i+1] - Y[j,i-1])/dE/2.0)
#
#              # computing gamma
#              gamma = ((X[j,i+1] - X[j,i-1])/dE/2.0)**2 + ((Y[j,i+1] - Y[j,i-1])/dE/2.0)**2
#
#              # computing equation in parts for X
#              A = 2*alpha/dE**2 + 2*gamma/dN**2
#              B = alpha*(X[j,i+1]+X[j,i-1])/dE**2
#              C = 2*beta*(X[j+1,i+1]+X[j-1,i-1]-X[j+1,i-1]-X[j-1,i+1])/4.0/dE/dN
#              D = gamma*(X[j+1,i]+X[j-1,i])/dN**2
#
#              X[j,i] = 1.0/A*(B-C+D)
#
#              # computing equation in parts for Y
#              A = 2*alpha/dE**2 + 2*gamma/dN**2
#              B = alpha*(Y[j,i+1]+Y[j,i-1])/dE**2
#              C = 2*beta*(Y[j+1,i+1]+Y[j-1,i-1]-Y[j+1,i-1]-Y[j-1,i+1])/4.0/dE/dN
#              D = gamma*(Y[j+1,i]+Y[j-1,i])/dN**2
#
#              Y[j,i] = 1.0/A*(B-C+D)
#
#      print("iteration = ",itr+1)
#
#      if np.max(abs(Y_old - Y)) < 1e-8:
#          print("converged!")
#          break
#      Y_old = cp(Y)



# plotting grid
plt.figure()
#  for i in range(Nx-1):
#      for j in range(Ny-1):
#          plt.plot([X[j,i],X[j,i+1]],[Y[j,i],Y[j,i+1]],'-b')
#          plt.plot([X[j,i],X[j+1,i]],[Y[j,i],Y[j+1,i]],'-b')
#      plt.plot([X[Ny-1,i],X[Ny-1,i+1]],[Y[Ny-1,i],Y[Ny-1,i+1]],'-b')
#  for j in range(Ny-1):
#      plt.plot([X[j,Nx-1],X[j+1,Nx-1]],[Y[j,Nx-1],Y[j+1,Nx-1]],'-b')

segs1 = np.stack((X,Y), axis = 2)
segs2 = segs1.transpose(1,0,2)
plt.gca().add_collection(LineCollection(segs1))
plt.gca().add_collection(LineCollection(segs2))

plt.axis("image")
plt.savefig("grid.png", dpi = 150)

plt.show()




fid = open("input_grid.dat","w")

fid.writelines('%5i%5i\n'%(Nx,Ny))
for i in range(Nx):
    for j in range(Ny):
        fid.writelines('%16.8E%16.8E\n'%(X[j,i],Y[j,i]))

fid.close()
