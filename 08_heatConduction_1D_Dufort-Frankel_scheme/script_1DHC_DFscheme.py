#!/bin/python3
"""----------------------------------------------------------------------------
1D heat conduction equation solution using Dufort-Frankel scheme

reference: https://folk.ntnu.no/leifh/teaching/tkt4140/._main064.html

----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# computation parameters definition--------------------------------------------
Lx = 1.0
Nx = 101
endTime = 1000.0
Nt = 101
alpha = 7.47e-05

T_left = 500.0
T_right = 300.0
T_init = 350.0

# simulation variables definition----------------------------------------------
# simulation timestep and space step
dx = Lx/(Nx-1)
dt = endTime/(Nt-1)

# computing sigma parameter
sigma = 2*alpha*dt/dx**2

# defining computation matrix
T = np.zeros([Nt,Nx], dtype = np.float64) + T_init
T[:,0] = T_left
T[:,Nx-1] = T_right

# grid generation
X = np.linspace(0,Lx,Nx)

# computation begin------------------------------------------------------------
for itr in range(1,Nt-1):
    # starting from the 2rd timestep

    # begining loop through space steps
    for i in range(1,Nx-1):
        T[itr+1,i] = (T[itr-1,i]*(1-sigma) + sigma*(T[itr,i+1]+T[itr,i-1]))/(1+sigma)

    print("timestep = ", itr)

# plotting solution
plt.figure()
for i in range(Nt):
    plt.plot(X,T[i,:],'-b')
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("T")
    plt.title("time : "+str((i+1)*dt)+" s")
    plt.draw()
    plt.savefig("image_"+str(i)+".png", dpi = 150)
    plt.pause(0.1)
    plt.clf()

#  plt.show()
