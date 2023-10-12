#!/bin/python3
"""----------------------------------------------------------------------------
Custom model with custom training trial code.
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
epochs = 10000
learning_rate = 1e-4
kern_init = tf.keras.initializers.GlorotUniform(seed = 1)
bias_init = tf.keras.initializers.GlorotUniform(seed = 1)
optimizerFunc = tf.keras.optimizers.legacy.RMSprop(
                        learning_rate=learning_rate, rho = 0.9)

#  regularizer = tf.keras.regularizers.l1(0)
regularizer = None

# model build------------------------------------------------------------------

model = CustomModel(kernel_initializer=kern_init, bias_initializer=bias_init)

# dataset preparation----------------------------------------------------------
# time
time = np.linspace(0,np.pi/4)[:,None]
time_bc = np.array([0, np.pi/4])[:,None]
x_bc = 0.5*np.sin(time_bc)+time_bc**2/2.0
x = 0.5*np.sin(time)+time**2/2.0

# training model---------------------------------------------------------------

# defining loss function
lossFunc = tf.keras.losses.MeanSquaredError()

# training function
@tf.function
def training_function():

    # evaluating model for bc data
    x_pred = model.predict_x(time_bc, training = True)
    mse_x = lossFunc(x_pred, x_bc)

    # evaluating model for internal points
    res_pred = model.predict_f(time, training = True)
    mse_f = lossFunc(res_pred, res_pred*K.constant(0.0))

    # combining physics and bc losses
    loss_value = mse_x + mse_f

    # computing gradients of loss w.r.t. model weights
    grads = K.gradients(loss_value, model.trainable_weights)

    # backpropagation
    optimizerFunc.apply_gradients(zip(grads, model.trainable_weights))

    return mse_x, mse_f

# custom trainning loop
for epoch in range(epochs):

    # training model
    mse_x, mse_f = training_function()

    print("epoch : ",epoch+1,
          "\t mse_x : ", np.round(mse_x.numpy(),8),
          "\t mse_f : ", np.round(mse_f.numpy(),8))

# prediction-------------------------------------------------------------------

# predicting model outpu
x_pred = model.predict_x(time)
x_pred = x_pred.numpy()
res = model.predict_f(time)
res = res.numpy()

# computing error
err = np.abs(x - x_pred)

# plotting prediction
plt.figure()
plt.plot(time, x_pred, '-b', label = "predicted")
plt.plot(time, x, '-r', label = "actual")
plt.grid()
plt.axis("image")
plt.legend()
plt.xlabel("time")
plt.ylabel("x")
plt.title("prediction vs actual")
plt.savefig("output.png", dpi = 150)

# plotting error
plt.figure()
plt.plot(time, err, '-b')
plt.grid()
plt.xlabel("time")
plt.ylabel("error value")
plt.yscale("log")
plt.title("prediction error")
plt.savefig("error.png", dpi = 150)

# plotting residual
plt.figure()
plt.plot(time, np.abs(res), '-b')
plt.grid()
plt.xlabel("time")
plt.ylabel("equation residual")
plt.yscale("log")
plt.title("equation residual")
plt.savefig("residual.png", dpi = 150)

plt.show()

# writing coefficient value to file
fid = open("coefficientValue.txt","w")
fid.writelines("coefficient value, a = "+str(model.a.numpy()))
fid.close()
print("coefficient value writen to file")
