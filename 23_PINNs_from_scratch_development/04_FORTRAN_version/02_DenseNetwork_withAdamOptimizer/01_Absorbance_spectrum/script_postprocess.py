#!/bin/python3
"""----------------------------------------------------------------------------
single composed neurons
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading estimated data
fid = pd.read_csv("estimation.csv", delim_whitespace = True)

# reading loss values
fid_loss = pd.read_csv("loss.csv", header = None)

# plotting graph
plt.rcParams.update({'font.size':15})
plt.figure(figsize=(16,9))
plt.plot(fid["x"],fid["y"],'-r',label="expected")
plt.plot(fid["x"],fid["y_pred"],'-b',label="estimated")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("network estimation graph")
plt.savefig("estimation.png", dpi = 150)

# plotting loss value
plt.figure(figsize=(16,9))
plt.plot(fid_loss[0],'-b')
plt.yscale("log")
plt.grid()
plt.xlabel("epochs")
plt.ylabel("loss value")
plt.title("training loss")
plt.savefig("loss.png", dpi = 150)

plt.show()

# mean absolute error
mae = np.mean(np.abs(fid["y_pred"]-fid["y"]))/0.5

print("mean absolute error = ", mae)
