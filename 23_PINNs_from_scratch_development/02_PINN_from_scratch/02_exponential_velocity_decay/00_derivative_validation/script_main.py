#!/bin/python3
"""----------------------------------------------------------------------------
Dense neural network from scratch development program
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from inputData import *
from customLayers import Dense
import os

# constructing network---------------------------------------------------------
# initializing first layer
layers_list = [Dense(layer_sizes[0],input_size,"dense_1")]

N_layers = len(layer_sizes)

# initializing other layers
for i in range(N_layers-1):
    layername = "dense_"+str(i+2)
    layers_list.append(
            Dense(layer_sizes[i+1],layer_sizes[i],layername)
            )

# loading weights if insisted
if load_weights:
    print("loading saved weights")
    for i in range(N_layers):
        layers_list[i].load_weights(weights_folder)

# training the network---------------------------------------------------------
Y_pred = Y.copy()
res = Y.copy()
dYdX = Y.copy()
for epoch in range(N_epochs):
    ## looping through each data record
    for i_dat in range(X.shape[0]):
        ## evaluating forward pass
        # evaluating first dense layer
        d_out = layers_list[0].evaluate(X[i_dat].reshape(input_size,1))
        # evaluating remaining dense layers
        for i_layer in range(N_layers-1):
            d_out = layers_list[i_layer+1].evaluate(d_out)

        # saving final output to Y_pred
        Y_pred[i_dat] = d_out

        # computing derivative through automatic differentiation
        _,dSigmadx = layers_list[0].compute_derivatives()
        for i in range(N_layers-1):
            _,tmp = layers_list[i+1].compute_derivatives()
            dSigmadx = np.matmul(dSigmadx,tmp)

        # assiging exact name to the derivative
        dYdX[i_dat] = dSigmadx*1.0 # to prevent absolute referencing

        #  # computing equation residual for the loss
        #  res[i_dat] = dYdX[i_dat] + k*Y_pred[i_dat]

        #  # adding initial condition loss
        #  if i_dat == 0:
        #      res_IC = Y_pred[i_dat] - Y[i_dat]
        #      res[i_dat] += res_IC*10

        res_IC = Y_pred[i_dat] - Y[i_dat]
        res[i_dat] = res_IC*1

        ## performing backpropagation
        layers_error = layers_list.copy() #  dLdz
        dL_dW = layers_list.copy() #  dLdW
        dL_db = layers_list.copy() #  dLdb

        # computing learning rate size
        beta = beta_func(epoch)

        # computing error of last layer with res and updating weights and biases
        dSigmadz,_ = layers_list[-1].compute_derivatives()
        layers_error[-1] = 2.0/Y_pred.shape[0]*np.sum(res[i_dat])*dSigmadz
        dL_dW[-1] = np.matmul(layers_error[-1],layers_list[-1].layer_input.T)
        dL_db[-1] = layers_error[-1]
        layers_list[-1].weight = layers_list[-1].weight - beta*dL_dW[-1]
        layers_list[-1].bias   = layers_list[-1].bias - beta*dL_db[-1]

        # computing errors for other layers from back
        for l_idx in range(N_layers-1):
            l = N_layers - l_idx - 1 #  current layer
            l_1 = l - 1 #  second layer in from current

            W_T = layers_list[l].weight.T
            dSigmadz,_ = layers_list[l_1].compute_derivatives()
            layers_error[l_1] = np.matmul(W_T,layers_error[l])*dSigmadz
            dL_dW[l_1] = np.matmul(layers_error[l_1],layers_list[l_1].layer_input.T)
            dL_db[l_1] = layers_error[l_1]*1.0

            layers_list[l_1].weight = layers_list[l_1].weight - beta*dL_dW[l_1]
            layers_list[l_1].bias   = layers_list[l_1].bias - beta*dL_db[l_1]

    ## computing loss value using equation residual vector
    L = np.mean(np.square(res))

    print("epoch = ",epoch+1,"\t Loss = ",L)

# saving weights if insisted
if save_weights:
    os.system("mkdir -p "+weights_folder)
    print("saving weights...")
    for i in range(N_layers):
        layers_list[i].save_weights(weights_folder)

# evaluating network-----------------------------------------------------------

# saving estimation to file
df = pd.DataFrame(np.transpose([X,Y_pred,Y]), columns = ["X","Y","Y_pred"])
df.to_csv("estimated_output.csv", index = None)

plt.figure()
plt.plot(X,Y_pred,'-b',label="estimated")
plt.plot(X,Y,'-r',label="exact")
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("estimation.png", dpi = 150)

plt.figure()
plt.plot(X,dYdX,'-b',label="estimated")
plt.plot(X,-k*Y,'-r',label="exact")
plt.grid()
plt.xlabel("X")
plt.ylabel("dYdX")
plt.legend()
plt.savefig("derivative.png", dpi = 150)

plt.show()

print("\n",layers_error)
