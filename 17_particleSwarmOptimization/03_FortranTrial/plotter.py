#!/bin/python3
"""----------------------------------------------------------------------------
plotter script
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading computed data
fid = pd.read_csv("computed_data.csv")

# removing extra spaces in column names
fid.rename(columns=lambda x: x.strip(), inplace=True)


# plotting output
plt.figure()
plt.plot(fid["x_best"],'-b',label="x")
plt.plot(fid["y_best"],'-r',label="y")
plt.plot(fid["f_eval"],'-g',label="f(x,y)")
plt.title("optimum value evolution")
plt.grid()
plt.xlabel("iterations")
plt.ylabel("value")
plt.legend()
plt.savefig("output.png", dpi = 150)

plt.show()
