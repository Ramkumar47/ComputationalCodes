"""----------------------------------------------------------------------------
Input Definition File
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np

# input parameters-------------------------------------------------------------

# number of particles
Np                  = 11

# PSO constants
w                   = 0.8
C1                  = 0.05
C2                  = 0.05

# maximum iteration
maxIter             = 101

# bounds for 2D domain
X_bc                = [-512,512]
Y_bc                = [-512,512]

# want animation frames?
makeAnimationFrames = True

# want individual particle data?
particleData        = True

# objective functions----------------------------------------------------------

# eggholder function
def f_obj(x,y):
    val = -(y+47)*np.sin(np.sqrt(np.abs(x/2+(y+47))))+x*np.sin(np.abs(x-(y+47)))
    return val
