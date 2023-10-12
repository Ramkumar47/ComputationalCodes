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

"""
key points about custom model
    -   model.summary() will not work until the model is fit, or defined an
        input shape.
    -   after fit, model.summary() will work but still it will not show the
        layer shapes, if the input shape is not defined on the first layer
    -   plot.model will plot only a single box, instead of full model graph.
"""

# building model---------------------------------------------------------------

class CustomModel(tf.keras.Model): #  with unscaled inputs
    def __init__(self, kernel_initializer, bias_initializer,
            activation = 'selu', regularizer = None):
        super(CustomModel, self).__init__(name = "custom_model")

        # defining layer parameters
        kern_init = kernel_initializer
        bias_init = bias_initializer
        #  activation = self.ScalableAdaptiveTanH
        activation = self.tanh

        # defining custom variables as trainable parameters
        self.alpha = K.variable(1.0)
        self.beta = K.variable(1.0)
        self.a = K.variable(1.0)

        # defining dense layer 1
        self.D1 = tf.keras.layers.Dense(units = 10, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "d1")

        # defining dense layer 2
        self.D2 = tf.keras.layers.Dense(units = 10, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "d2")

        # defining dense layer 3
        self.D3 = tf.keras.layers.Dense(units = 10, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "d3")

        # defining output
        self.X = tf.keras.layers.Dense(units = 1, activation = activation,
                                      kernel_initializer = kern_init,
                                      bias_initializer = bias_init,
                                      kernel_regularizer = regularizer,
                                      bias_regularizer = regularizer,
                                      name = "x")

    def ScalableAdaptiveTanH(self,x):
        # adaptive tanH activation function
        """
                              ⎛ (α ⋅ x)    (-α ⋅ x)⎞
                              ⎜e        - e        ⎟
        β ⋅ tanh(α ⋅ x) = β ⋅ ⎜────────────────────⎟
                              ⎜ (α ⋅ x)    (-α ⋅ x)⎟
                              ⎝e        + e        ⎠

        """
        val = self.beta*(K.exp(self.alpha*x) - K.exp(-self.alpha*x))/(K.exp(self.alpha*x)+K.exp(-self.alpha*x))

        return val

    def tanh(self,x):
        val = tf.keras.activations.tanh(x)

        return val

    # defining neural function for RKNN
    def NeuralFunction(self,time):

        # passing input through dense layers
        d_out = self.D1(time)
        d_out = self.D2(d_out)
        d_out = self.D3(d_out)
        out = self.X(d_out)

        return out

    # defining PINN function
    def PINNFunction(self,time):

        x = self.NeuralFunction(time)
        dxdt = K.gradients(x, time)[0]

        # framing equation to compute residual
        res = dxdt - self.a*K.cos(time) - time

        return res

    @tf.function
    def predict_x(self, inputs, training = True):

        # inputs
        time = inputs

        # computing NN output
        x = self.NeuralFunction(time)

        # returning outputs
        return x

    @tf.function
    def predict_f(self, inputs, training = True):

        # inputs
        time = inputs

        # computing NN output
        res = self.PINNFunction(time)

        # returning outputs
        return res

    def call(self, inputs, training = True):

        """
            made dummy
        """
        return 0
