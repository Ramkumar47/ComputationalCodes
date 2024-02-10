#!/bin/python3
"""----------------------------------------------------------------------------
2D Particle Swarm Optimization Algorithm Visualization
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd
import os

# reading all inputs
from inputFile import *

# initializing Gbest vector
Gbest = [np.random.random()*(X_bc[1]-X_bc[0]),
         np.random.random()*(Y_bc[1]-Y_bc[0])]

# particle object definition---------------------------------------------------
class Particle:
    def __init__(self, x,y,vx,vy):
        # initializing position and velocity
        self.x_curr  = x
        self.y_curr  = y
        self.vx_curr = vx
        self.vy_curr = vy
        self.vx_np1  = vx
        self.vy_np1  = vy
        self.x_np1   = x
        self.y_np1   = y

        # initializing list to store history
        self.x_hist  = [self.x_curr]
        self.y_hist  = [self.y_curr]
        self.vx_hist = [self.vx_curr]
        self.vy_hist = [self.vy_curr]
        self.r1_hist = []
        self.r2_hist = []
        self.f_eval  = []

        # initializing p-best with current coordinates
        self.Pbest_x = self.x_curr
        self.Pbest_y = self.y_curr
        self.Pbest_f = f_obj(self.x_curr,self.y_curr)
        self.f_eval.append(self.Pbest_f)

    def updateVelocity(self):
        """ computing the next iteration velocity """
        # computing random numbers
        r1 = np.random.random()
        r2 = np.random.random()

        # computing velocity
        self.vx_np1 = (w*self.vx_curr + C1*r1*(self.Pbest_x - self.x_curr) +
                            C2*r2*(Gbest[0] - self.x_curr))
        self.vy_np1 = (w*self.vy_curr + C1*r1*(self.Pbest_y - self.y_curr) +
                            C2*r2*(Gbest[1] - self.y_curr))

        # adding to the history
        self.r1_hist.append(r1)
        self.r2_hist.append(r2)
        self.vx_hist.append(self.vx_np1)
        self.vy_hist.append(self.vy_np1)

    def updatePosition(self):
        """ computing the position vector for the next iteration """
        self.x_np1 = self.x_curr + self.vx_np1
        self.y_np1 = self.y_curr + self.vy_np1

        self.x_hist.append(self.x_np1)
        self.y_hist.append(self.y_np1)

    def updatePbest(self):
        """ updating Pbest vector """
        # computing f_obj value for new position
        f_new = f_obj(self.x_np1,self.y_np1)
        self.f_eval.append(f_new)

        # checking if f_new is best
        if f_new < self.Pbest_f:
            self.Pbest_x = self.x_np1
            self.Pbest_y = self.y_np1
            self.Pbest_f = f_new

        self.x_curr  = self.x_np1
        self.y_curr  = self.y_np1
        self.vx_curr = self.vx_np1
        self.vy_curr = self.vy_np1


# optimization-----------------------------------------------------------------

# initializing particles
P = []
for i in range(Np):
    x_init  = np.random.random()*(X_bc[1]-X_bc[0])+X_bc[0]
    y_init  = np.random.random()*(Y_bc[1]-Y_bc[0])+X_bc[0]
    vx_init = 0.1*np.cos(np.random.random()*np.pi)
    vy_init = 0.1*np.cos(np.random.random()*np.pi)

    P.append( Particle(x_init,y_init,vx_init,vy_init) )

# begin optimization
for itr in range(maxIter):
    # looping through particles
    Pbest_list = []
    for particle in P:
        particle.updateVelocity()
        particle.updatePosition()
        particle.updatePbest()
        Pbest_list.append(particle.Pbest_f)

    # updating gbest
    idxOfBest = np.where(Pbest_list == np.min(Pbest_list))[0][0]
    Gbest[0]  = P[idxOfBest].Pbest_x
    Gbest[1]  = P[idxOfBest].Pbest_y

    print("Marching : ",itr+1," of ",maxIter)

# writing finalState computation data
pid = []; X_f = []; Y_f = []; Vx_f = []; Vy_f = []
for i in range(Np):
    pid.append(i)
    X_f.append(P[i].x_curr)
    Y_f.append(P[i].y_curr)
    Vx_f.append(P[i].vx_curr)
    Vy_f.append(P[i].vy_curr)
fid = pd.DataFrame(np.transpose([pid,X_f,Y_f,Vx_f,Vy_f]),
                   columns = ["PID","X","Y","Vx","Vy"])
fid.to_csv("final_data.csv", index = None)

# generating animation frames
if makeAnimationFrames:
    # initializing directories to store animation frames
    os.system("rm -rf AnimationFrames")
    os.system("mkdir AnimationFrames")

    # creating meshgrid
    X,Y = np.meshgrid(np.linspace(X_bc[0],X_bc[1],101),
                      np.linspace(Y_bc[0],Y_bc[1],101))
    f_vals = f_obj(X,Y)

    print("creating animation frames")
    for itr in range(maxIter):
        # creating frame
        plt.figure()
        plt.contourf(X,Y,f_vals,100,cmap='jet',alpha=0.4,locator = ticker.LogLocator())
        #  plt.contourf(X,Y,f_vals,100,cmap='jet',alpha=0.4)
        plt.colorbar()
        plt.axis('image')
        plt.grid()
        for i in range(Np):
            plt.scatter(P[i].x_hist[itr],P[i].y_hist[itr],marker='o',
                        color='black')
            plt.quiver(P[i].x_hist[itr],P[i].y_hist[itr],
                       P[i].vx_hist[itr],P[i].vy_hist[itr],
                       color='black',angles='xy',scale_units='xy',scale=1)
        plt.title("iteration = "+str(itr+1))
        fname = "image.{:04d}.png".format(itr+1)
        plt.savefig("AnimationFrames/"+fname, dpi = 150)
        plt.close()
        print("Frame : ",itr+1," of ",maxIter)

# writing individual particle data
if particleData:
    # creating directory to store particle data
    os.system("rm -rf particleData && mkdir particleData")

    # looping through particles
    for i in range(Np):
        fname = "particle_{:04d}.csv".format(i+1)
        fid = pd.DataFrame(np.transpose([P[i].x_hist,P[i].y_hist,P[i].vx_hist,
                                         P[i].vy_hist,P[i].f_eval]),
                            columns=["X","Y","Vx","Vy","f_eval"])
        fid["itr"] = np.linspace(0,maxIter,maxIter+1, dtype=int)
        fid.to_csv("particleData/"+fname, index = None)
        print("writing "+fname)

print("done")
