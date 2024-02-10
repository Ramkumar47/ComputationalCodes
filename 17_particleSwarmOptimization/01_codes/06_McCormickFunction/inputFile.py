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
X_bc                = [-1.5,4]
Y_bc                = [-3,4]

# want animation frames?
makeAnimationFrames = True

# want individual particle data?
particleData        = True

# objective functions----------------------------------------------------------

# mccormick function
def f_obj(x,y):
    val = np.sin(x+y)+(x-y)**2-1.5*x+2.5*y+1
    return val
