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
X_bc                = [-5,5]
Y_bc                = [-5,5]

# want animation frames?
makeAnimationFrames = True

# want individual particle data?
particleData        = True

# objective functions----------------------------------------------------------

# three-hump camel function
def f_obj(x,y):
    val = 2*x**2 - 1.05*x**4 + x**6/6.0 + x*y + y**2
    return val
