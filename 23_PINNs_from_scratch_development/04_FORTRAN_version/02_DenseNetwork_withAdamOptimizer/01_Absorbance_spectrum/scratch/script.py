import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fid = pd.read_csv("test.csv", header = None, delim_whitespace=True,
                  names = ["z0","rn1","rn2"])


z0 = np.sqrt(-2.0*np.log(fid["rn1"]))*np.cos(2.0*np.pi*fid["rn2"])


plt.figure()
plt.plot(fid["z0"],fid["z0"],'ob',label="fortran")
plt.plot(z0,z0,'*r',label="python")
plt.legend()
plt.grid()
plt.show()
