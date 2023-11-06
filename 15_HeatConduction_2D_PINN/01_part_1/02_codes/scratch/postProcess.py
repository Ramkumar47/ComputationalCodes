#!/bin/python3
"""----------------------------------------------------------------------------
comparing prediction with analytical solution
----------------------------------------------------------------------------"""

# importing needed libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

# reading predicted data
fid = pd.read_csv("predicted_data.csv")

# defining analytical function
def analytical_solution(xa,ya,n):
    L = H = 1
    theta_val = 0
    for i  in range(n):
        A = np.sinh((2*i+1)*np.pi*(L-xa)/H)/np.sinh((2*i+1)*np.pi*L/H)
        B = np.sin((2*i+1)*np.pi*ya/H)/(2*i+1)
        theta_val += 4.0/np.pi*A*B
    return theta_val

# preparing smaller grid for analytical solution
Na = 101
Xa,Ya = np.meshgrid(np.linspace(0,1,Na),np.linspace(0,1,Na))

# computing analytical solution
theta_act = analytical_solution(Xa,Ya,100)

# reading predited solution
Xp = fid["X"].to_numpy()
Yp = fid["Y"].to_numpy()
theta_p = fid["theta_pred"].to_numpy()

Np = int(np.sqrt(Xp.shape[0]))

Xp = Xp.reshape(Np,Np)
Yp = Yp.reshape(Np,Np)
theta_p = theta_p.reshape(Np,Np)

# plotting contour
plt.rcParams.update({'font.size':15})

plt.figure(figsize=(13,8))

plt.subplot(1,2,1)
plt.contourf(Xp,Yp,theta_p,100,cmap = 'jet')
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('image')
cb = plt.colorbar(orientation = 'horizontal')
tick_locator = ticker.MaxNLocator(nbins = 5)
cb.locator = tick_locator
cb.update_ticks()
plt.title("predicted temperature")

plt.subplot(1,2,2)
plt.contourf(Xa,Ya,theta_act,100,cmap = 'jet')
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('image')
cb = plt.colorbar(orientation = 'horizontal')
tick_locator = ticker.MaxNLocator(nbins = 5)
cb.locator = tick_locator
cb.update_ticks()
plt.title("actual temperature")

plt.savefig("contours_out.png", dpi = 150)

plt.figure(figsize=(13,8))

plt.subplot(1,2,1)
plt.plot(Xp[int(Np/2),:],theta_p[int(Np/2),:],'-b',label = "predicted")
plt.plot(Xa[int(Na/2),:],theta_act[int(Na/2),:],'-r',label = "analytical")
plt.grid()
plt.xlabel("X")
plt.ylabel(r"$\theta$")
plt.title("mid-horizontal slice plot")
plt.legend()

plt.subplot(1,2,2)
plt.plot(theta_p[:,int(Np/2)],Yp[:,int(Np/2)],'-b',label = "predicted")
plt.plot(theta_act[:,int(Na/2)],Ya[:,int(Na/2)],'-r',label = "analytical")
plt.grid()
plt.xlabel(r"$\theta$")
plt.ylabel("Y")
plt.title("mid-vertical slice plot")
plt.legend()
plt.savefig("slice_plots_out.png", dpi = 150)

plt.show()
