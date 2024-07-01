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

# constructing network---------------------------------------------------------
# initializing first layer
layers_list = [Dense(layer_sizes[0],input_size)]

N_layers = len(layer_sizes)

# initializing other layers
for i in range(N_layers-1):
    layers_list.append(
            Dense(layer_sizes[i+1],layer_sizes[i])
            )

# training the network---------------------------------------------------------
Y_pred = Y.copy()
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

        ## performing backpropagation
        layers_error = layers_list.copy() #  dLdz
        dL_dW = layers_list.copy() #  dLdW
        dL_db = layers_list.copy() #  dLdb

        # computing error of last layer and updating weights and biases
        dSigmadz,_ = layers_list[-1].compute_derivatives()
        layers_error[-1] = 2.0/Y_pred.shape[0]*np.sum(Y_pred[i_dat]-Y[i_dat])*dSigmadz
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

    ## computing loss value
    L = np.mean(np.square(Y_pred - Y))

    # # computing error of last layer and updating weights and biases
    # dSigmadz,_ = layers_list[-1].compute_derivatives()
    # layers_error[-1] = 2.0/Y_pred.shape[0]*np.sum(Y_pred-Y)*dSigmadz
    # dL_dW[-1] = np.matmul(layers_error[-1],layers_list[-1].layer_input.T)
    # dL_db[-1] = layers_error[-1]
    # layers_list[-1].weight = layers_list[-1].weight - beta*dL_dW[-1]
    # layers_list[-1].bias   = layers_list[-1].bias - beta*dL_db[-1]
    # # computing errors for other layers from back
    # for l_idx in range(N_layers-1):
    #     l = N_layers - l_idx - 1 #  current layer
    #     l_1 = l - 1 #  second layer in from current
    #
    #     W_T = layers_list[l].weight.T
    #     dSigmadz,_ = layers_list[l_1].compute_derivatives()
    #     layers_error[l_1] = np.matmul(W_T,layers_error[l])*dSigmadz
    #     dL_dW[l_1] = np.matmul(layers_error[l_1],layers_list[l_1].layer_input.T)
    #     dL_db[l_1] = layers_error[l_1]*1.0
    #
    #     layers_list[l_1].weight = layers_list[l_1].weight - beta*dL_dW[l_1]
    #     layers_list[l_1].bias   = layers_list[l_1].bias - beta*dL_db[l_1]

    print("epoch = ",epoch+1,"\t Loss = ",L)

# evaluating network-----------------------------------------------------------

plt.figure()
plt.plot(X,Y_pred,'-b',label="estimated")
plt.plot(X,Y,'-r',label="exact")
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("estimation.png", dpi = 150)

plt.show()

print(layers_error)
print(layers_list[1].printInfo())
