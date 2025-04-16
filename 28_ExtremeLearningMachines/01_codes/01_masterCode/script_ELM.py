#!/bin/python3
"""============================================================================
Extreme Learning Machines trials

Ramkumar
Mon Apr 14 02:36:22 PM IST 2025
============================================================================"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ELMClass import ExtremeLearningMachines as ELM

#==============================================================================

# # sine function----------------------------------------------------------------
# x = np.linspace(0,2*np.pi,21)[:,None]
# y = np.sin(x)
#
# # defining ELM model
# elm1 = ELM(x,y,N_h=10,outputBias=False,name="sine_model")
#
# # setting random seed
# elm1.randomSeed = 1
#
# # fitting the model
# elm1.fit()
#
# # printing model summary
# elm1.summary()
#
# # predicting the output with more data points than training
# x_test = np.linspace(0,2*np.pi,501)[:,None]
# y_pred = elm1.predict(x_test)
#
# # plotting the output
# plt.rcParams.update({"font.size":15})
# plt.figure(figsize=(16,9))
# plt.plot(x_test,y_pred,'-b',label="estimation")
# plt.plot(x,y,'or',markerfacecolor="none",label="exact")
# plt.grid()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("sine")
# plt.legend(loc=(1.01,0.75))
# plt.savefig("sinePrediction.png",dpi=150,bbox_inches="tight")
#
# # plateau function-------------------------------------------------------------
# x = np.linspace(0,1,51)[:,None]
# y = (6*x-2)**2*np.sin(12*x-4)
#
# # defining ELM model
# elm2 = ELM(x,y,N_h=40,outputBias=False,name="plateau_model")
#
# # setting random seed
# elm2.randomSeed = 1
#
# # fitting the model
# elm2.fit()
#
# # printing model summary
# elm2.summary()
#
# # predicting the output with more data points than training
# x_test = np.linspace(0,1,501)[:,None]
# y_act = (6*x_test-2)**2*np.sin(12*x_test-4)
# y_pred = elm2.predict(x_test)
#
# # plotting the output
# plt.rcParams.update({"font.size":15})
# plt.figure(figsize=(16,9))
# plt.plot(x_test,y_pred,'-b',label="estimation")
# plt.plot(x_test,y_act,'--k',label="exact")
# plt.plot(x,y,'or',markerfacecolor="none",label="train points")
# plt.grid()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("plateau")
# plt.legend(loc=(1.01,0.75))
# plt.savefig("plateauPrediction.png",dpi=150,bbox_inches="tight")
# plt.show()

# sine experiment--------------------------------------------------------------

from IPython.display import HTML

# fixing test points
x_test = np.linspace(0,2*np.pi,501)[:,None]
y_test = np.sin(x_test)

# fixing number of datapoints
N = [5,10,20,40,80,160,320,640]

# performing experiment on loop
L2_error = []
for n in N:
    # generating data
    x = np.linspace(0,2*np.pi,n)[:,None]
    y = np.sin(x)

    # defining ELM model
    elm1 = ELM(x,y,N_h=10,outputBias=False,name="sine_model")

    # setting random seed
    elm1.randomSeed = 1

    # fitting the model
    elm1.fit()

    # predicting the output with more data points than training
    y_pred = elm1.predict(x_test)

    # computing error
    l2 = np.sqrt(np.mean(np.square(y_pred-y_test)))
    L2_error.append(l2)

# preparing dataframe
fid = pd.DataFrame(np.transpose([N,L2_error]),
                   columns=["No. of datapoints",r"$L_2$ error"])
print(HTML(fid.to_html()))

# plotting graph
plt.figure()
plt.plot(N,L2_error,'-ob')
plt.grid()
plt.xlabel("No. of data points")
plt.ylabel(r"$L_2$ error")
plt.yscale("log")
plt.xscale("log")
plt.show()

#==============================================================================
