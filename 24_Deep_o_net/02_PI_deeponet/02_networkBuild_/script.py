#!/bin/python3
"""============================================================================
Deep-o-net model script

Ramkumar
Fri Sep 20 11:13:19 AM IST 2024
============================================================================"""

# hiding system warnings #  needs to be on top for complete suppression
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['KMP_WARNINGS'] = "FALSE"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.keras.backend as K
from customLayer import PI_layer

from copy import copy as cp #  to prevent absolute referencing

tf.keras.backend.set_floatx('float64')

# hiding unnecessary warnings
# tensorflow warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# disabling eager execution
tf.compat.v1.disable_eager_execution()
#  tf.compat.v1.enable_eager_execution() #  needed for custom training loop

tf.compat.v1.experimental.output_all_intermediates(True)

#==============================================================================

# defining model parameters
epochs        = 1000
learning_rate = 1e-3
kern_init     = tf.keras.initializers.RandomNormal(seed = 1)
bias_init     = tf.keras.initializers.RandomNormal(seed = 1)
optimizerFunc = tf.keras.optimizers.legacy.Adam(
                        learning_rate=learning_rate)
m_sensors = 11

#  regularizer = tf.keras.regularizers.l1(0)
regularizer = None

# building model---------------------------------------------------------------

# defining activation function
def scalable_tanh(x):
    return K.constant(5)*K.tanh(x)

# defining branch network layers
Inp_B = tf.keras.Input(shape=(m_sensors,), name="branch_input")

L1B = tf.keras.layers.Dense(units = 10, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l1b")(Inp_B)

L2B = tf.keras.layers.Dense(units = 10, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l2b")(L1B)

L3B = tf.keras.layers.Dense(units = 10, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l3b")(L2B)

L4B = tf.keras.layers.Dense(units = 10, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l4b")(L3B)

L5B = tf.keras.layers.Dense(units = 10, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l5b")(L4B)

# defining trunk network layers
Inp_T     = tf.keras.Input(shape=(1,), name="trunk_input_t")
Inp_omega = tf.keras.Input(shape=(1,), name="trunk_input_omega")

Conc = tf.keras.layers.Concatenate(axis=-1,name="concat")([Inp_T,Inp_omega])

L1T = tf.keras.layers.Dense(units = 2, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l1t")(Conc)

L2T = tf.keras.layers.Dense(units = 4, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l2t")(L1T)

L3T = tf.keras.layers.Dense(units = 6, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l3t")(L2T)

L4T = tf.keras.layers.Dense(units = 8, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l4t")(L3T)

L5T = tf.keras.layers.Dense(units = 10, activation = scalable_tanh,
                              kernel_initializer = kern_init,
                              bias_initializer = bias_init,
                              kernel_regularizer = regularizer,
                              bias_regularizer = regularizer,
                              name = "l5t")(L4T)

# computing final output through dot product
X = tf.keras.layers.Dot(axes=1, name = "dot")([L5B,L5T])

#  # computing final output through dot product
#  X = tf.keras.layers.Lambda(lambda x: K.sum(x[0][:,0]*x[1][:,0]), name = "dot")([L5B,L5T])

#  X = Dot_layer()([L5B,L5T])

# defining PI layer
Res = PI_layer(name="pi_layer")([X,Inp_T,Inp_omega])
#  Res = PI_layer(name="pi_layer")([L5T,Inp_T,Inp_omega])

# building and compiling model
model = tf.keras.Model(inputs=[Inp_B,Inp_T,Inp_omega], outputs=[X,Res])

model.compile(optimizer=optimizerFunc, loss = [None,"mse"])

# setting up training data-----------------------------------------------------
fid = pd.read_csv("../01_datasetGeneration/computed_data.csv")

# splitting sensor points data and other columns
sensor_colnames = [str(i) for i in range(m_sensors)]

sensor_data     = fid[sensor_colnames].to_numpy()
output_location = fid["output_location"].to_numpy()[:,None]
output_function = fid["output_function"].to_numpy()[:,None]
omega_values    = fid["omega_values"].to_numpy()[:,None]

# training model---------------------------------------------------------------

#  # loading weights
#  model.load_weights("saved_weights/")

hist = model.fit([sensor_data,output_location,omega_values],
                 #  [output_function,output_function*0.0],
                 output_function*0.0,
                 epochs = epochs,)
                 #  batch_size=1)

# saving weights
model.save_weights("saved_weights/")

# testing model----------------------------------------------------------------

# reading test data
fid_1 = pd.read_csv("../01_datasetGeneration/test_data/test_data_1.csv")
fid_2 = pd.read_csv("../01_datasetGeneration/test_data/test_data_2.csv")
fid_3 = pd.read_csv("../01_datasetGeneration/test_data/test_data_3.csv")
fid_4 = pd.read_csv("../01_datasetGeneration/test_data/test_data_4.csv")
fid_5 = pd.read_csv("../01_datasetGeneration/test_data/test_data_5.csv")

# preparing test dataset
sensor_data_1     = fid_1[sensor_colnames].to_numpy()
output_location_1 = fid_1["output_location"].to_numpy()[:,None]
output_function_1 = fid_1["output_function"].to_numpy()[:,None]
output_omega_1    = fid_1["omega_values"].to_numpy()[:,None]
sensor_data_2     = fid_2[sensor_colnames].to_numpy()
output_location_2 = fid_2["output_location"].to_numpy()[:,None]
output_function_2 = fid_2["output_function"].to_numpy()[:,None]
output_omega_2    = fid_2["omega_values"].to_numpy()[:,None]
sensor_data_3     = fid_3[sensor_colnames].to_numpy()
output_location_3 = fid_3["output_location"].to_numpy()[:,None]
output_function_3 = fid_3["output_function"].to_numpy()[:,None]
output_omega_3    = fid_3["omega_values"].to_numpy()[:,None]
sensor_data_4     = fid_4[sensor_colnames].to_numpy()
output_location_4 = fid_4["output_location"].to_numpy()[:,None]
output_function_4 = fid_4["output_function"].to_numpy()[:,None]
output_omega_4    = fid_4["omega_values"].to_numpy()[:,None]
sensor_data_5     = fid_5[sensor_colnames].to_numpy()
output_location_5 = fid_5["output_location"].to_numpy()[:,None]
output_function_5 = fid_5["output_function"].to_numpy()[:,None]
output_omega_5    = fid_5["omega_values"].to_numpy()[:,None]

# predicting output
output_function_1_pred, res_1 = model.predict([sensor_data_1,output_location_1,output_omega_1])
output_function_2_pred, res_2 = model.predict([sensor_data_2,output_location_2,output_omega_2])
output_function_3_pred, res_3 = model.predict([sensor_data_3,output_location_3,output_omega_3])
output_function_4_pred, res_4 = model.predict([sensor_data_4,output_location_4,output_omega_4])
output_function_5_pred, res_5 = model.predict([sensor_data_5,output_location_5,output_omega_5])

# saving predicted outputs
df1 = pd.DataFrame(np.transpose([output_location_1.flatten(),
                                 output_function_1.flatten(),
                                 output_function_1_pred.flatten()]),
                   columns=["t","x","x_pred"])
df2 = pd.DataFrame(np.transpose([output_location_2.flatten(),
                                 output_function_2.flatten(),
                                 output_function_2_pred.flatten()]),
                   columns=["t","x","x_pred"])
df3 = pd.DataFrame(np.transpose([output_location_3.flatten(),
                                 output_function_3.flatten(),
                                 output_function_3_pred.flatten()]),
                   columns=["t","x","x_pred"])
df4 = pd.DataFrame(np.transpose([output_location_4.flatten(),
                                 output_function_4.flatten(),
                                 output_function_4_pred.flatten()]),
                   columns=["t","x","x_pred"])
df5 = pd.DataFrame(np.transpose([output_location_5.flatten(),
                                 output_function_5.flatten(),
                                 output_function_5_pred.flatten()]),
                   columns=["t","x","x_pred"])
df1.to_csv("predicted_data_1.csv", index = None)
df2.to_csv("predicted_data_2.csv", index = None)
df3.to_csv("predicted_data_3.csv", index = None)
df4.to_csv("predicted_data_4.csv", index = None)
df5.to_csv("predicted_data_5.csv", index = None)

# plotting graphs
plt.rcParams.update({"font.size":15})

plt.figure(figsize=(16,9))
plt.plot(output_location_1,output_function_1_pred,'-b',label="estimated")
plt.plot(output_location_1,output_function_1,'-r',label="exact")
plt.grid()
plt.legend(loc=(1.05,0.9))
plt.xlabel("x")
plt.ylabel("y")
l2 = np.round(np.sqrt(np.sum((output_function_1_pred-output_function_1)**2)),5)
title = r"test case 1: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_1.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(output_location_2,output_function_2_pred,'-b',label="estimated")
plt.plot(output_location_2,output_function_2,'-r',label="exact")
plt.grid()
plt.legend(loc=(1.05,0.9))
plt.xlabel("x")
plt.ylabel("y")
l2 = np.round(np.sqrt(np.sum((output_function_2_pred-output_function_2)**2)),5)
title = r"test case 2: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_2.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(output_location_3,output_function_3_pred,'-b',label="estimated")
plt.plot(output_location_3,output_function_3,'-r',label="exact")
plt.grid()
plt.legend(loc=(1.05,0.9))
plt.xlabel("x")
plt.ylabel("y")
l2 = np.round(np.sqrt(np.sum((output_function_3_pred-output_function_3)**2)),5)
title = r"test case 3: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_3.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(output_location_4,output_function_4_pred,'-b',label="estimated")
plt.plot(output_location_4,output_function_4,'-r',label="exact")
plt.grid()
plt.legend(loc=(1.05,0.9))
plt.xlabel("x")
plt.ylabel("y")
l2 = np.round(np.sqrt(np.sum((output_function_4_pred-output_function_4)**2)),5)
title = r"test case 4: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_4.png", dpi = 150, bbox_inches="tight")

plt.figure(figsize=(16,9))
plt.plot(output_location_5,output_function_5_pred,'-b',label="estimated")
plt.plot(output_location_5,output_function_5,'-r',label="exact")
plt.grid()
plt.legend(loc=(1.05,0.9))
plt.xlabel("x")
plt.ylabel("y")
l2 = np.round(np.sqrt(np.sum((output_function_5_pred-output_function_5)**2)),5)
title = r"test case 5: $L_2$ = "+str(l2)
plt.title(title)
plt.savefig("test_case_5.png", dpi = 150, bbox_inches="tight")

plt.show()

#==============================================================================
