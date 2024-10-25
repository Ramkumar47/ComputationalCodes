#!/bin/python3
"""============================================================================
Single hidden layer network code with back-propagation algorithm

with sigmoid activation function for both hidden and output layers

Ramkumar
Thu Oct 24 05:18:17 PM IST 2024
============================================================================"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#==============================================================================

# defining model parameters
N_input      = 1
N_hidden     = 20
N_output     = 1
N_epochs     = 500000
learningRate = 0.1
loadWeights  = False

# reading and framing training data
fid      = pd.read_csv("../../01_trainingDataFiles/XY_data.csv")
N_data   = fid.shape[0]
X_input  = fid["X"].to_numpy()
Y_output = fid["Y"].to_numpy()

# initializing weights and bias vectors
W_IH = np.random.rand(N_hidden, N_input)
b_IH = np.random.rand(N_hidden,1)
W_HO = np.random.rand(N_output, N_hidden)
b_HO = np.random.rand(N_output,1)

# loading saved weights
if loadWeights:
    W_IH = np.loadtxt("saved_weights/W_IH.txt").reshape(N_hidden,N_input)
    b_IH = np.loadtxt("saved_weights/b_IH.txt").reshape(N_hidden,1)
    W_HO = np.loadtxt("saved_weights/W_HO.txt").reshape(N_output,N_hidden)
    b_HO = np.loadtxt("saved_weights/b_HO.txt").reshape(N_output,1)

# defining activation function
def sigma(x):
    return 1.0/(1.0 + np.exp(-x))

# beginning training loop
loss_history = []
for epoch in range(N_epochs):
    # initializing cumulative loss per epoch variable
    loss = 0.0

    # looping through dataset
    for i in range(N_data):
        # preparing input and output with appropriate shapes
        X = X_input[i].reshape(N_input,1)
        Y = Y_output[i].reshape(N_output,1)

        # performing forward pass
        z1    = np.matmul(W_IH,X)+b_IH
        h1    = sigma(z1)
        z2    = np.matmul(W_HO,h1)+b_HO
        y_hat = sigma(z2)

        # computing loss value
        loss += 0.5*(y_hat - Y)**2

        # updating weights
        delta_2 = (y_hat - Y)*y_hat*(1.0-y_hat)
        dLdW_HO = np.matmul(delta_2,h1.T)
        dLdb_HO = delta_2*1.0
        delta_1 = np.matmul(W_HO.T,delta_2)*h1*(1.0-h1)
        dLdW_IH = np.matmul(delta_1,X.T)
        dLdb_IH = delta_1*1.0
        W_IH = W_IH - learningRate*dLdW_IH
        b_IH = b_IH - learningRate*dLdb_IH
        W_HO = W_HO - learningRate*dLdW_HO
        b_HO = b_HO - learningRate*dLdb_HO

    # printing status
    print("Epoch : ",epoch+1,"; loss : ",loss.flatten()[0])
    loss_history.append(loss.flatten()[0])

# saving weights
os.system("rm -rf saved_weights && mkdir saved_weights")
np.savetxt("saved_weights/W_IH.txt",W_IH)
np.savetxt("saved_weights/b_IH.txt",b_IH)
np.savetxt("saved_weights/W_HO.txt",W_HO)
np.savetxt("saved_weights/b_HO.txt",b_HO)
print("weights saved!")

# predicting output
Y_pred = []
for i in range(N_data):
    # preparing input and output with appropriate shapes
    X = X_input[i].reshape(N_input,1)

    # performing forward pass
    z1    = np.matmul(W_IH,X)+b_IH
    h1    = sigma(z1)
    z2    = np.matmul(W_HO,h1)+b_HO
    y_hat = sigma(z2)
    Y_pred.extend(y_hat)
Y_pred = np.array(Y_pred)
df = fid.copy()
for i in range(Y_pred.shape[1]): #  looping through columns of Y_pred
    YcolName = "Y_pred_"+str(i)
    df[YcolName] = Y_pred[:,0]
df.to_csv("predicted_data.csv", index = None)
print(df)

# computing L2 error
L2 = np.sqrt(np.sum(df["Y"].to_numpy()-df["Y_pred_0"].to_numpy())**2)

# plotting loss graph
plt.rcParams.update({"font.size":15})
plt.figure(figsize=(16,9))
plt.plot(np.arange(len(loss_history)),loss_history, '-b')
plt.grid()
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training loss")
plt.yscale("log")
plt.savefig("loss.png",dpi=150,bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(df["X"],df["Y_pred_0"], '-b',label="estimated")
plt.plot(df["X"],df["Y"], '-r',label="expected")
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
titleStr = r"Estimation vs exact profile. $L_2$ = "+str(np.round(L2,4))
plt.title(titleStr)
plt.savefig("prediction.png",dpi=150,bbox_inches="tight")

plt.show()


#==============================================================================
