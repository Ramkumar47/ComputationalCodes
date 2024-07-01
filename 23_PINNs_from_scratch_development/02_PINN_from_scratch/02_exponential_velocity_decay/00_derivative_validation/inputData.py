"""----------------------------------------------------------------------------
Input data definition file
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np


# defining layer sizes
input_size  = 1
layer_sizes = [3,2,1] #  including output layer

# training epoch count
N_epochs = 100000

# gradient step size/ learning rate function
def beta_func(epoch):
    decay = 0.01
    beta = 1/(1+decay*epoch)
    #  return beta
    return 0.5

# save and load weights
save_weights   = True
load_weights   = True
weights_folder = "saved_weights"

# training data
k = 5.0 # constant representing viscosity of fluid
V0 = 0.5 # initial velocity value
X = np.linspace(0,0.5,41) # simulation time
Y = V0*np.exp(-k*X) # velocity decay profile
