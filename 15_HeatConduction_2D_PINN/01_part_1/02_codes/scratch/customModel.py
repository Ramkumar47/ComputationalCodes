#!/bin/python3
"""----------------------------------------------------------------------------
Custom Tensorflow Model build for HCPINN
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

# hiding unnecessary warnings--------------------------------------------------
# tensorflow warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# setting float type
tf.keras.backend.set_floatx('float64')

# disabling eager execution
#  tf.compat.v1.disable_eager_execution()
#  tf.compat.v1.enable_eager_execution()

tf.compat.v1.experimental.output_all_intermediates(True)

# building model---------------------------------------------------------------

class CustomModel(tf.keras.Model): #  with unscaled inputs
    def __init__(self, kernel_initializer, bias_initializer,
            activation = 'selu', regularizer = None):
        super(CustomModel, self).__init__(name = "custom_model")

        # defining layer parameters
        kern_init    = kernel_initializer
        bias_init    = bias_initializer
        activation   = self.tanh
        #  activation   = self.RotatedHyperbola
        #  activation   = tf.keras.activations.sigmoid
        NeuronsCount_Tnet = 15

        # defining layers for T_net

        # defining concat layer
        self.concat = tf.keras.layers.Concatenate(axis = -1, name = 'concat')

        # defining dense layer 1
        self.L1T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l1t")

        # defining dense layer 2
        self.L2T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l2t")

        # defining dense layer 3
        self.L3T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l3t")

        # defining dense layer 4
        self.L4T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l4t")

        # defining dense layer 5
        self.L5T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l5t")

        # defining dense layer 6
        self.L6T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l6t")

        # defining dense layer 7
        self.L7T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l7t")

        # defining dense layer 8
        self.L8T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l8t")

        # defining dense layer 9
        self.L9T = tf.keras.layers.Dense(units = NeuronsCount_Tnet, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "l9t")

        # defining output layer :
        self.T_layer = tf.keras.layers.Dense(units = 1, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "theta")

    def RotatedHyperbola(self,x):
        """
        hyperbola open-upwards equation, rearranged to get y-value
               2          2
        (y - k)    (x - h)
        ──────── - ──────── = 1
            2          2
           b          a

        applying rotation to get a proper curve that goes in both +ve and -ve
        directions, using rotation matrix as below.

        ⎛x       ⎞
        ⎜ rotated⎟   ⎛cos(ϑ) -sin(ϑ)⎞   ⎛x⎞
        ⎜        ⎟ = ⎜              ⎟ ⋅ ⎜ ⎟
        ⎜y       ⎟   ⎝sin(ϑ) cos(ϑ) ⎠   ⎝y⎠
        ⎝ rotated⎠

        taking only y-component as the final activation value

        y        = x ⋅ sin(ϑ) + y ⋅ cos(ϑ)
         rotated
        """

        # defining equation constants
        h = K.constant(0)
        k = K.constant(-1)
        a = K.constant(3)
        b = K.constant(1)
        angle = K.constant(np.pi/4)

        # calculating y value by rearranging hyperbola equation
        y = (k + b*K.sqrt(K.constant(1) + (x-h)**2/a**2))

        # rotating the calculated hyperbola by "angle" about x-axis
        y_rotated = x*K.sin(angle) + y*K.cos(angle)

        return y_rotated

    def tanh(self,x):
        val = tf.keras.activations.tanh(x)

        return val

    # defining neural function for RKNN
    @tf.function
    def NeuralFunction(self,x,y):

        # training T network
        d_out = self.concat([x,y])
        d_out = self.L1T(d_out)
        d_out = self.L2T(d_out)
        d_out = self.L3T(d_out)
        d_out = self.L3T(d_out)
        d_out = self.L3T(d_out)
        d_out = self.L3T(d_out)
        d_out = self.L3T(d_out)
        d_out = self.L3T(d_out)
        #  d_out = self.L4T(d_out)
        #  d_out = self.L5T(d_out)
        #  d_out = self.L6T(d_out)
        #  d_out = self.L7T(d_out)
        #  d_out = self.L8T(d_out)
        #  d_out = self.L9T(d_out)
        T      = self.T_layer(d_out)

        return T

    # defining PINN function
    def PINNFunction(self, x,y):

        # computing NN output
        T = self.NeuralFunction(x,y)

        # computing the derivatives
        dTdx   = K.gradients(T,x)[0]
        dTdy   = K.gradients(T,y)[0]
        d2Tdx2 = K.gradients(dTdx,x)[0]
        d2Tdy2 = K.gradients(dTdy,y)[0]

        # framing equation and computing residuals
        res_T = d2Tdx2 + d2Tdy2

        return res_T

    @tf.function
    def predict_x(self, inputs):

        # inputs
        x = inputs[0]
        y = inputs[1]

        # computing NN output
        T = self.NeuralFunction(x,y)

        # returning output
        return T

    @tf.function
    def predict_f(self, inputs):

        # inputs
        x = inputs[0]
        y = inputs[1]

        # computing NN output
        res = self.PINNFunction(x,y)

        # returning outputs
        return res

    def call(self, inputs, training = True):

        """
            made dummy
        """
        return 0
