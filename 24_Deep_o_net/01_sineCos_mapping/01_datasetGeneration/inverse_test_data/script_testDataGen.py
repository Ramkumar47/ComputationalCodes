#!/bin/python3
"""----------------------------------------------------------------------------
Dataset generation for the deep-o-net trial

input function: sin(omega*theta)
output function: omega*cos(omega*theta)

Ramkumar
Thu Sep 19 08:14:43 PM IST 2024
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------

# PARAMETERS DEFINITION
m     = 11            # number of sensor points
theta = [0,np.pi/2.0] # theta range min and max
omega = [1,2]      # angular frequency range
P     = 101           # number of output theta points per input function
N     = 1           # number of input function variations

# GENERATING DATA

# generating random omega and theta values
omega_array = np.random.rand(N)*omega[1]+omega[0]
theta_array = np.sort(np.random.rand(P)*theta[1]+theta[0])

# generating uniform sensor location theta values
theta_sensor = np.linspace(theta[0],theta[1],m)

# creating lists to store each data record
input_function  = []
output_location = []
output_function = []

# looping through numbers to generate data
for i in range(N): # looping through number of input function variations
    for j in range(P): # looping through no. of output function locations

        # computing input function values
        input_func = list(np.cos(omega_array[i]*theta_sensor))

        # computing output function value
        output_func = -omega_array[i]*np.sin(omega_array[i]*theta_array[j])

        # appending computed to the lists
        input_function.append(input_func)
        output_function.append(output_func)
        output_location.append(theta_array[j])

# creating dataframes to store the results
fid                    = pd.DataFrame(input_function)
fid["output_location"] = output_location
fid["output_function"] = output_function

#  # shuffling rows
#  fid = fid.sample(frac=1)
#  fid.reset_index(drop=True, inplace=True)

# writing computed data to csv file
fid.to_csv("test_data.csv", index = None)

#------------------------------------------------------------------------------
