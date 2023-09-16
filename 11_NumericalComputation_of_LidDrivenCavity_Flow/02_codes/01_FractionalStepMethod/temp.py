import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from copy import copy as cp

nx = 101
ny = 101
L = 2.0

dx = L/float(nx-1)
dy = L/float(ny-1)

fid = pd.read_csv("solution_data/solution_data_1.02E+00.csv", delim_whitespace = True)

p = np.zeros([nx,ny])

S = fid['Source'].to_numpy().reshape([nx,ny])
p_f = fid['P'].to_numpy().reshape([nx,ny])


coeff = 2/dx**2 + 2/dy**2

pp = cp(p)
for itr in range(10000):
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            p[i,j] = 1/coeff*((p[i+1,j] + p[i-1,j])/dx**2 + (p[i,j+1]+p[i,j-1])/dy**2 + S[i,j])

    p[:,0] = p[:,1]*2.0 - p[:,2]
    p[:,ny-1] = p[:,ny-2]*2.0 - p[:,ny-3]
    p[0,:] = p[1,:]*2.0 - p[2,:]
    p[nx-1,:] = p[nx-2,:]*2.0 - p[nx-3,:]

    #  p[:,0] = p[:,1]*1
    #  p[:,ny-1] = p[:,ny-2]*1
    #  p[0,:] = p[1,:]*1
    #  p[nx-1,:] = p[nx-2,:]*1

    err = np.max(np.abs(pp[1:nx-1,1:ny-1]-p[1:nx-1,1:ny-1]))

    pp = cp(p)

    print(itr)

    if err < 1e-6:
        break


plt.figure()
plt.contourf(p,100)
plt.colorbar()
plt.axis('image')

plt.figure()
plt.contourf(p_f,100)
plt.colorbar()
plt.axis('image')

plt.show()
