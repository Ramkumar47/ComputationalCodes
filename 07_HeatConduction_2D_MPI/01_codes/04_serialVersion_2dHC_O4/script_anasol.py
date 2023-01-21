import pandas as pd
import numpy as np

# reading the output file
fid = pd.read_csv("output_data.csv")

# defining parameters
N = 100
Lx = 0.01
Ly = 0.01
T1 = 373.0
T2 = 293.0

# computing analytical solution
fid["T_a"] = fid["T"]

for i in range(fid.shape[0]):
    summation = 0.0
    for j in range(N):
        summation += (np.sinh((2*j+1)*np.pi*(Lx-fid[' X'].iloc[i])/Ly)*np.sin((2*j+1)*np.pi*fid['Y'].iloc[i]/Ly))/(np.sinh((2*j+1)*np.pi*Lx/Ly)*(2*j+1))
    fid["T_a"].iloc[i] = T2 + (T1 - T2)*4.0/np.pi*summation

    print(i)

fid.to_csv("output_data.csv", index = None)
