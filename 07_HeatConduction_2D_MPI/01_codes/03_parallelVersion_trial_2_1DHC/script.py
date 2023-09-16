import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fid = pd.read_csv("solution_files_csv/data.csv")

plt.figure()
plt.plot(fid["X"],fid["T"],'-b')
plt.grid()
plt.xlabel("X")
plt.ylabel("T")
plt.title("temperature variation")

plt.savefig("output.png", dpi = 150)

plt.show()
