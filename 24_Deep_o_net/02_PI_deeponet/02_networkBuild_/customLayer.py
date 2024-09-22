#!/bin/python3
"""----------------------------------------------------------------------------
Custom layer for the PI-Deeponet model
----------------------------------------------------------------------------"""

# importing needed modules
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['KMP_WARNINGS'] = "FALSE"
import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K

# hiding unnecessary warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# disabling eager execution for PINN feasability
tf.compat.v1.disable_eager_execution()

# defining custom layer
class  PI_layer(tf.keras.layers.Layer):
    # defining initializer function
    def __init__(self, name = "pi_layer"):
        # calling initialization functions of both derived and base classes
        super(PI_layer, self).__init__(name = name)

    # defining call function, this handles layer calculations
    def call(self, inputs):
        """
        "inputs" argument is the input that is given to this layer,
        like previous layer output for example
        """

        # getting inputs in the same order provided
        x     = inputs[0]
        t     = inputs[1]
        omega = inputs[2]

        # computing gradients
        dxdt = K.gradients(x,t)[0]
        #  dxdt = x

        # framing equation to compute residual
        res = dxdt - K.cos(omega*t)
        #  res = K.cos(omega*t)
        #  res = x
        #  res = dxdt*1.0

        # returning residual
        return res

