"""----------------------------------------------------------------------------
Input data definition file
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd

## Network parameters definition-----------------------------------------------

# defining layer sizes
input_size  = 1
layer_sizes = [5,5,5,5,1] #  including output layer

# training epoch count
N_epochs = 100000

# gradient step size
beta = 1.0

# save and load weights
save_weights   = True
load_weights   = True
weights_folder = "saved_weights"

## training data---------------------------------------------------------------

# reading data from file
fid = pd.read_csv("normalized_data.csv", usecols = ["time","V"])
fid = fid.iloc[np.arange(0,fid.shape[0],16)]
X = fid["time"].to_numpy()
Y = fid["V"].to_numpy()
