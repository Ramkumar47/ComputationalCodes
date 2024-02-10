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
X_bc                = [-4.5,4.5]
Y_bc                = [-4.5,4.5]

# want animation frames?
makeAnimationFrames = True

# want individual particle data?
particleData        = True

# objective functions----------------------------------------------------------

# Beale function
def f_obj(x,y):
    val = (1.5-x+x*y)**2 + (2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2
    return val
