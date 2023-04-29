#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os,glob

# preparing directories to store contours
os.system("rm -rf contours")
os.system("mkdir -p contours/pressure")
os.system("mkdir -p contours/x-velocity")
os.system("mkdir -p contours/y-velocity")
os.system("mkdir -p contours/velocity-magnitude")
os.system("mkdir -p contours/vorticity")
os.system("mkdir -p contours/streamlines")

# reading files
fnames = sorted(glob.glob1(os.getcwd()+"/solution_data/", "*.csv"))

Nx = 101
Ny = 101

# transforming data into matrix
X = np.zeros([Ny,Nx])
Y = np.zeros([Ny,Nx])
U = np.zeros([Ny,Nx])
V = np.zeros([Ny,Nx])
P = np.zeros([Ny,Nx])


# looping through the files
for name in fnames:
    # reading data
    fid = pd.read_csv("solution_data/"+name, delim_whitespace=True)

    # getting time
    time = fid['Time'].iloc[0]

    # getting filecount
    filecount = name.split("_")[2].split(".csv")[0]

    count = 0
    for i in range(Nx):
        for j in range(Ny):
            X[j,i] = fid['X'].iloc[count]
            Y[j,i] = fid['Y'].iloc[count]
            U[j,i] = fid['U'].iloc[count]
            V[j,i] = fid['V'].iloc[count]
            P[j,i] = fid['P'].iloc[count]
            count += 1

    # computing vorticity
    dx = X[0,1]-X[0,0] # step size
    dy = Y[1,0]-Y[0,0] # step size
    omega = np.zeros([Ny,Nx])
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            omega[j,i] = (U[j+1,i]-U[j-1,i])/dy/2.0 - (V[j,i+1]-V[j,i-1])/dx/2.0
    for i in range(1,Nx-1):
        j = 0
        omega[0,i] = (U[j+1,i]-U[j,i])/dy - (V[j,i+1]-V[j,i-1])/dx/2.0
        j = Ny-1
        omega[0,i] = (U[j,i]-U[j-1,i])/dy - (V[j,i+1]-V[j,i-1])/dx/2.0
    for j in range(1,Ny-1):
        i = 0
        omega[j,i] = (U[j+1,i]-U[j-1,i])/dy/2.0 - (V[j,i+1]-V[j,i])/dx
        i = Nx-1
        omega[j,i] = (U[j+1,i]-U[j-1,i])/dy/2.0 - (V[j,i]-V[j,i-1])/dx

    i = 0; j = 0
    omega[j,i] = (U[j+1,i]-U[j,i])/dy - (V[j,i+1]-V[j,i])/dx
    i = Nx-1; j = 0
    omega[j,i] = (U[j+1,i]-U[j,i])/dy - (V[j,i]-V[j,i-1])/dx
    i = Nx-1; j = Ny-1
    omega[j,i] = (U[j,i]-U[j-1,i])/dy - (V[j,i]-V[j,i-1])/dx
    i = 0; j = Ny-1
    omega[j,i] = (U[j,i]-U[j-1,i])/dy - (V[j,i+1]-V[j,i])/dx

    # plotting contours
    Umag = np.sqrt(U**2+V**2)

    # magnitude contour
    plt.figure()
    plt.contourf(X,Y,Umag,100,cmap = 'jet')
    plt.colorbar()
    plt.axis('image')
    plt.title("velocity magnitude, t = "+str(np.round(time,5))+" s")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("contours/velocity-magnitude/velocityMagnitude_"+filecount+".png", dpi = 150)

    # x-velocity contour
    plt.figure()
    plt.contourf(X,Y,U,100,cmap = 'jet')
    plt.colorbar()
    plt.axis('image')
    plt.title("x-velocity, t = "+str(np.round(time,5))+" s")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("contours/x-velocity/x-velocity_"+filecount+".png", dpi = 150)

    # y-velocity contour
    plt.figure()
    plt.contourf(X,Y,V,100,cmap = 'jet')
    plt.colorbar()
    plt.axis('image')
    plt.title("y-velocity, t = "+str(np.round(time,5))+" s")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("contours/y-velocity/y-velocity_"+filecount+".png", dpi = 150)

    # pressure contour
    plt.figure()
    plt.contourf(X,Y,P,100,cmap = 'jet')
    plt.colorbar()
    plt.axis('image')
    plt.title("pressure, t = "+str(np.round(time,5))+" s")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("contours/pressure/pressure_"+filecount+".png", dpi = 150)

    # streamlines
    plt.figure()
    plt.streamplot(X,Y,U,V)
    plt.axis('image')
    plt.title("streamlines, t = "+str(np.round(time,5))+" s")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("contours/streamlines/streamlines_"+filecount+".png", dpi = 150)

    # vorticity contour
    cmap = plt.cm.get_cmap('Greys').reversed()
    plt.figure()
    plt.contourf(X,Y,omega,100,cmap = cmap,levels = np.linspace(-6,6,100))
    plt.colorbar()
    plt.axis('image')
    plt.title("vorticity, t = "+str(np.round(time,5))+" s")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("contours/vorticity/vorticity_"+filecount+".png", dpi = 150)

    #  plt.show()
    plt.close("all")

    print("processed ",name)
