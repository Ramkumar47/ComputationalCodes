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
C1                  = 0.02
C2                  = 0.02

# maximum iteration
maxIter             = 201

# bounds for 2D domain
X_bc                = [0,5]
Y_bc                = [0,5]

# want animation frames?
makeAnimationFrames = True

# want individual particle data?
particleData        = True

# objective functions----------------------------------------------------------

# deformed egg carton
def f_obj(x,y):
    val = (x-3.14)**2 + (y-2.72)**2 + np.sin(3*x+1.41) +np.sin(4*y-1.73)
    return val

