#!/bin/python3
"""============================================================================
coeffifient determiner

Ramkumar
Sun Jul 20 11:47:22 AM IST 2025
============================================================================"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#==============================================================================

x1 = -2
x2 = 571
y1 = 1e-15
y2 = 1-1e-15

A = np.array([[x1,1],[x2,1]])
b = np.array([np.log(1-y1)-np.log(y1),np.log(1-y2)-np.log(y2)])

coeff = np.linalg.inv(A)@b

print("a = ",-coeff[0])
print("b = ",coeff[1])

#==============================================================================
