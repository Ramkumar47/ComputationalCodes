"""----------------------------------------------------------------------------
Input data definition file
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np


# defining layer sizes
input_size  = 1
layer_sizes = [1,1,1] #  including output layer

# training epoch count
N_epochs = 10000

# gradient step size
beta = 1.0

# save and load weights
save_weights   = True
load_weights   = True
weights_folder = "saved_weights"

# training data
X = np.linspace(0.0,0.5,101)
Y = X**2
