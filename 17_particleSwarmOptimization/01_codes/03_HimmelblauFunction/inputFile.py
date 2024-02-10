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

# Himmelblau function
def f_obj(x,y):
    val = (x**2+y-11)**2 + (x+y**2-7)**2
    return val
