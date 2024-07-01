import numpy as np
import matplotlib.pyplot as plt
from inputData import *
from customLayers import Dense

## loading network weights

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

# performing forward evaluation------------------------------------------------
X = np.linspace(0,0.5,101)
Y_pred = X.copy()
dYdX_pred = X.copy()
Y = V0*np.exp(-k*X) # velocity decay profile

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
        dSigmadx *= tmp

    # assiging exact name to the derivative
    dYdX_pred[i_dat] = dSigmadx*1.0 # to prevent absolute referencing


# computing dYdX analytical
dYdX = -k*Y

# error percentage
Ep = abs(Y_pred - Y)/Y*100

plt.figure()
plt.plot(X,Y_pred,'-b',label="estimated")
plt.plot(X,Y,'-r',label="exact")
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("estimated vs exact results")
plt.legend()
plt.savefig("estimated_output.png", dpi = 150)

plt.figure()
plt.plot(X,dYdX_pred,'-b',label="estimated")
plt.plot(X,dYdX,'-r',label="exact")
plt.grid()
plt.xlabel("X")
plt.ylabel("dYdX")
plt.title("gradient computation")
plt.legend()
plt.savefig("gradient_computation.png", dpi = 150)

plt.figure()
plt.plot(X,Ep,'-b')
plt.grid()
plt.xlabel("X")
plt.ylabel("Ep")
plt.title("Estimation error percentage")
plt.legend()
plt.savefig("error_percentage.png", dpi = 150)

plt.show()
