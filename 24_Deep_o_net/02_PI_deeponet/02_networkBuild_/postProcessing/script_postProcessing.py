#!/bin/python3
"""============================================================================
postprocessing of PI-Deep-o-net

Ramkumar
Sun Sep 22 06:22:33 PM IST 2024
============================================================================"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#==============================================================================

# reading predicted data
fid_1 = pd.read_csv("../predicted_data_1.csv")
fid_2 = pd.read_csv("../predicted_data_2.csv")
fid_3 = pd.read_csv("../predicted_data_3.csv")
fid_4 = pd.read_csv("../predicted_data_4.csv")
fid_5 = pd.read_csv("../predicted_data_5.csv")

# computing and plotting offset graphs
off_1 = fid_1["x"]-fid_1["x_pred"]
off_2 = fid_2["x"]-fid_2["x_pred"]
off_3 = fid_3["x"]-fid_3["x_pred"]
off_4 = fid_4["x"]-fid_4["x_pred"]
off_5 = fid_5["x"]-fid_5["x_pred"]

# plotting offset graphs
plt.rcParams.update({"font.size":15})

plt.figure(figsize=(16,9))
plt.plot(fid_1["t"],abs(off_1),'-b',label="testcase 1")
plt.plot(fid_2["t"],abs(off_2),'-r',label="testcase 2")
plt.plot(fid_3["t"],abs(off_3),'-g',label="testcase 3")
plt.plot(fid_4["t"],abs(off_4),'-k',label="testcase 4")
plt.plot(fid_5["t"],abs(off_5),'-c',label="testcase 5")
plt.grid()
plt.xlabel(r"$t$")
plt.ylabel(r"offset")
plt.legend(loc=(1.01,0.5))
plt.title("offsets in the estimated vs expected results")
#  plt.yscale("log")
plt.savefig("offsets.png",dpi=150,bbox_inches="tight")

# adjusting offset and plotting the estimated vs expected graphs---------------

# taking mean offsets
mean_off_1 = np.mean(off_1)
mean_off_2 = np.mean(off_2)
mean_off_3 = np.mean(off_3)
mean_off_4 = np.mean(off_4)
mean_off_5 = np.mean(off_5)

# adding offsets to the estimated data
fid_1["x_pred_corrected"] = fid_1["x_pred"]+mean_off_1
fid_2["x_pred_corrected"] = fid_2["x_pred"]+mean_off_2
fid_3["x_pred_corrected"] = fid_3["x_pred"]+mean_off_3
fid_4["x_pred_corrected"] = fid_4["x_pred"]+mean_off_4
fid_5["x_pred_corrected"] = fid_5["x_pred"]+mean_off_5

# plotting estimated vs expected corrected graphs

plt.figure(figsize=(16,9))
plt.plot(fid_1["t"],fid_1["x_pred_corrected"],'-b',label="estimated")
plt.plot(fid_1["t"],fid_1["x"],'-r',label="expected")
plt.grid()
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc=(1.01,0.5))
l2 = np.round(np.sqrt(np.sum((fid_1["x_pred_corrected"]-fid_1["x"])**2)),5)
title = r"test case 1: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_1_corrected.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(fid_2["t"],fid_2["x_pred_corrected"],'-b',label="estimated")
plt.plot(fid_2["t"],fid_2["x"],'-r',label="expected")
plt.grid()
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc=(1.01,0.5))
l2 = np.round(np.sqrt(np.sum((fid_2["x_pred_corrected"]-fid_2["x"])**2)),5)
title = r"test case 2: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_2_corrected.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(fid_3["t"],fid_3["x_pred_corrected"],'-b',label="estimated")
plt.plot(fid_3["t"],fid_3["x"],'-r',label="expected")
plt.grid()
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc=(1.01,0.5))
l2 = np.round(np.sqrt(np.sum((fid_3["x_pred_corrected"]-fid_3["x"])**2)),5)
title = r"test case 3: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_3_corrected.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(fid_4["t"],fid_4["x_pred_corrected"],'-b',label="estimated")
plt.plot(fid_4["t"],fid_4["x"],'-r',label="expected")
plt.grid()
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc=(1.01,0.5))
l2 = np.round(np.sqrt(np.sum((fid_4["x_pred_corrected"]-fid_4["x"])**2)),5)
title = r"test case 4: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_4_corrected.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(fid_5["t"],fid_5["x_pred_corrected"],'-b',label="estimated")
plt.plot(fid_5["t"],fid_5["x"],'-r',label="expected")
plt.grid()
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc=(1.01,0.5))
l2 = np.round(np.sqrt(np.sum((fid_5["x_pred_corrected"]-fid_5["x"])**2)),5)
title = r"test case 5: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_5_corrected.png", dpi = 150, bbox_inches="tight")

plt.show()

#==============================================================================
