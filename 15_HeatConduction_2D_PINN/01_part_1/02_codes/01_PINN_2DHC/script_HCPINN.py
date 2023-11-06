#!/bin/python3
"""----------------------------------------------------------------------------
2D HC equation solution using PINNs : typical
----------------------------------------------------------------------------"""

# hiding system warnings #  needs to be on top for complete suppression
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['KMP_WARNINGS'] = "FALSE"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.keras.backend as K
from matplotlib import ticker

#  from functions import build_dense_layer
from customModel import CustomModel

from copy import copy as cp #  to prevent absolute referencing

tf.keras.backend.set_floatx('float64')

# hiding unnecessary warnings--------------------------------------------------
# tensorflow warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# disabling eager execution
#  tf.compat.v1.disable_eager_execution()
tf.compat.v1.enable_eager_execution() #  needed for custom training loop

tf.compat.v1.experimental.output_all_intermediates(True)

# ML parameters definition-----------------------------------------------------
epochs = 40000
learning_rate = 1e-3
kern_init = tf.keras.initializers.GlorotUniform(seed = 1)
bias_init = tf.keras.initializers.GlorotUniform(seed = 1)
optimizerFunc = tf.keras.optimizers.legacy.Adam(
                        learning_rate=learning_rate)

#  regularizer = tf.keras.regularizers.l1(0)
regularizer = None

# model build------------------------------------------------------------------

model = CustomModel(kernel_initializer=kern_init, bias_initializer=bias_init)

# dataset preparation----------------------------------------------------------

# defining analytical function
def analytical_solution(xa,ya,n):
    L = H = 1
    theta_val = 0
    for i  in range(n):
        A = np.sinh((2*i+1)*np.pi*(L-xa)/H)/np.sinh((2*i+1)*np.pi*L/H)
        B = np.sin((2*i+1)*np.pi*ya/H)/(2*i+1)
        theta_val += 4.0/np.pi*A*B
    return theta_val

# defining dataset function
def generate_dataset(N_bc,N_int):

    # generating bounary data points
    x_AB     = np.linspace(0,1,N_bc)
    y_AB     = x_AB*0.0
    theta_AB = x_AB*0.0

    y_BC     = np.linspace(0,1,N_bc)
    x_BC     = y_BC*0.0 + 1.0
    theta_BC = x_BC*0.0

    x_CD     = np.linspace(0,1,N_bc)
    y_CD     = x_CD*0.0 + 1.0
    theta_CD = x_CD*0.0

    y_DA     = np.linspace(0,1,N_bc)
    x_DA     = y_DA*0.0
    theta_DA = x_DA*0.0 + 1.0

    x_bc     = np.r_[x_AB,x_BC,x_CD,x_DA]
    y_bc     = np.r_[y_AB,y_BC,y_CD,y_DA]
    theta_bc = np.r_[theta_AB,theta_BC,theta_CD,theta_DA]

    # getting permutation to shuffle the bc data points
    p        = np.random.permutation(4*N_bc)
    x_bc     = x_bc[p]
    y_bc     = y_bc[p]
    theta_bc = theta_bc[p]

    # generating internal data points
    x_int,y_int = np.meshgrid(np.linspace(0.1,0.9,N_int),np.linspace(0.1,0.9,N_int))
    x_int = x_int.flatten()
    y_int = y_int.flatten()

    # reshaping arrays
    x_bc = x_bc[:,None]; x_int = x_int[:,None]; theta_bc = theta_bc[:,None]
    y_bc = y_bc[:,None]; y_int = y_int[:,None]

    return x_bc,y_bc,theta_bc,x_int,y_int

# getting initial data
N_bc = 10
N_int = 10
x_bc,y_bc,theta_bc,x_int,y_int = generate_dataset(N_bc,N_int)

# training model---------------------------------------------------------------

# defining loss function
lossFunc = tf.keras.losses.MeanSquaredError()

# loss weightage definition
beta = 0.5

# training function
@tf.function
def training_function():

    # evaluating model for bc data output
    theta_bc_pred = model.predict_x([x_bc,y_bc])
    mse_data      = lossFunc(theta_bc_pred, theta_bc)

    # evaluating model for PINN residual output
    res_T   = model.predict_f([x_int,y_int])
    mse_phy = lossFunc(res_T,res_T*K.constant(0.0))

    # combining physics and data losses
    loss_value = beta*mse_phy + (1-beta)*mse_data

    # computing gradients of loss w.r.t. model weights
    grads = K.gradients(loss_value, model.trainable_weights)

    # backpropagation
    optimizerFunc.apply_gradients(zip(grads, model.trainable_weights))

    return mse_data, mse_phy

#  # loading previously trained weights
#  model.load_weights("./model_weights/weights")

# custom trainning loop
for epoch in range(epochs):

    # training model
    mse_data, mse_phy = training_function()

    print("epoch : ",epoch+1,
          "\t mse_data : ", np.round(mse_data.numpy(),8),
          " mse_phy : ", np.round(mse_phy.numpy(),8))

# saving weights
model.save_weights(os.getcwd()+"/model_weights/weights")

# prediction-------------------------------------------------------------------
N = 1001

x,y        = np.meshgrid(np.linspace(0,1,N),np.linspace(0,1,N))
x          = x.flatten()[:,None]
y          = y.flatten()[:,None]
theta_pred = model.predict_x([x,y])
theta_res  = model.predict_f([x,y])
theta_res  = abs(theta_res)

# getting actual solution
theta_act = analytical_solution(x,y,100)

# writing predicted data to file
x = x.flatten(); y = y.flatten()
theta_pred = theta_pred.numpy().flatten(); theta_act = theta_act.flatten()
fid = pd.DataFrame(np.transpose([x,y,theta_pred,theta_act]),
                   columns=["X","Y","theta_pred","theta_act"])
fid.to_csv("predicted_data.csv", index = None)

# reshaping for contour plots
x = x.reshape(N,N)
y = y.reshape(N,N)
theta_pred = theta_pred.reshape(N,N)
theta_act  = theta_act.reshape(N,N)

# plotting contours
plt.rcParams.update({'font.size':15})

plt.figure(figsize=(13,8))

plt.subplot(1,2,1)
plt.contourf(x,y,theta_pred,100,cmap = 'jet')
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('image')
cb = plt.colorbar(orientation = 'horizontal')
tick_locator = ticker.MaxNLocator(nbins = 5)
cb.locator = tick_locator
cb.update_ticks()
plt.title("predicted temperature")

plt.subplot(1,2,2)
plt.contourf(x,y,theta_act,100,cmap = 'jet')
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('image')
cb = plt.colorbar(orientation = 'horizontal')
tick_locator = ticker.MaxNLocator(nbins = 5)
cb.locator = tick_locator
cb.update_ticks()
plt.title("actual temperature")

plt.savefig("contours.png", dpi = 150)

plt.figure(figsize=(13,8))

plt.subplot(1,2,1)
plt.plot(x[int(N/2),:],theta_pred[int(N/2),:],'-b',label = "predicted")
plt.plot(x[int(N/2),:],theta_act[int(N/2),:],'-r',label = "analytical")
plt.grid()
plt.xlabel("X")
plt.ylabel(r"$\theta$")
plt.title("mid-horizontal slice plot")
plt.legend()

plt.subplot(1,2,2)
plt.plot(theta_pred[:,int(N/2)],y[:,int(N/2)],'-b',label = "predicted")
plt.plot(theta_act[:,int(N/2)],y[:,int(N/2)],'-r',label = "analytical")
plt.grid()
plt.xlabel(r"$\theta$")
plt.ylabel("Y")
plt.title("mid-vertical slice plot")
plt.legend()
plt.savefig("slice_plots.png", dpi = 150)

plt.show()
#  plt.close()

print("\n done")
