#!/bin/python3
"""----------------------------------------------------------------------------
preprocessing python script for the flame data
----------------------------------------------------------------------------"""

# importing needed modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading data
fid = pd.read_csv("Flame_spectrum_1343.txt", header = None,
                  names = ["wavenumber","absorbance"])

# fixing needed min and max normalized values
V_min = -0.5
V_max = 0.5

# taking a copy of dataframe for normalized data
fid_norm = fid.copy()

# begining loop over columns on the dataframe
for col in fid.columns:
    # computing actual min and max values of current column
    x_min = fid[col].min()
    x_max = fid[col].max()

    # computing modified min and max values
    M_min = (V_max*x_min - V_min*x_max)/(V_max-V_min)
    M_max = (x_min - M_min)/V_min + M_min

    # normalizing current column
    fid_norm[col] = (fid[col] - M_min)/(M_max - M_min)

# writing normalized data to csv file
fid_norm.to_csv("normalized_data.txt", index = None, header=None)

#  x = np.linspace(-0.5,0.5,101)
#  #  y = 0.5*np.sin(10*x)
#  y = np.tanh(x)
#  df = pd.DataFrame(np.transpose([x,y]))
#  df.to_csv("normalized_data.txt", index = None,header=None)
