#!/bin/python3
"""============================================================================
Extreme Learning Machines model class definition

Ramkumar
Mon Apr 14 02:37:08 PM IST 2025
============================================================================"""

# importing needed modules
import numpy as np
import pandas as pd

#==============================================================================

class ExtremeLearningMachines:
    def __init__(self,
                 inputData,             # input data 2D array
                 outputData,            # output data 2D array
                 N_h,                   # number of hidden neurons
                 outputBias = False,    # include bias in output
                 name="elm"):           # model name
        self.modelName  = name
        self.Nh         = N_h
        self.randomSeed = None          # seed value for pseudo-randomness
        self.inputData  = inputData
        self.outputData = outputData
        self.outputBias = outputBias
        self.n          = inputData.shape[1]
        self.m          = outputData.shape[1]
        self.N          = outputData.shape[0]  # no. of data points
        self.trainState = False         # training state of the model

        # initializing weight matrices
        self.hiddenWeights = np.zeros([self.Nh,self.n])
        self.hiddenBias    = np.zeros([self.Nh,1])
        self.outputWeights = np.zeros([self.m,self.Nh])

    # hidden activation function
    def h(self,x):
        return np.tanh(x)

    # summary function
    def summary(self):
        print("\n===Model Summary===\n")

        print("Model name           : ", self.modelName)
        print("No of hidden neurons : ", self.Nh)
        print("input size           : ", self.n)
        print("output size          : ", self.m)
        print("Train state          : ", self.trainState)
        print("Included output bias : ", self.trainState)
        print("hidden weights       : \n", self.hiddenWeights)
        print("hidden bias          : \n", self.hiddenBias)
        print("output weights       : \n", self.outputWeights)

    # weights initialization function
    def initializeWeights(self):
        np.random.seed(self.randomSeed)  # setting seed value
        self.hiddenWeights = np.random.rand(self.Nh,self.n)
        self.hiddenBias    = np.random.rand(self.Nh,1)
        self.outputWeights = np.random.rand(self.m,self.Nh)

    # training function
    def fit(self):
        # initializing weights
        self.initializeWeights()

        # computing coefficient matrix
        H = self.h(self.hiddenWeights@self.inputData[0][:,None]+
                   self.hiddenBias)
        for i in range(1,self.N):
            tmp = self.h(self.hiddenWeights@self.inputData[i][:,None]+
                   self.hiddenBias)
            H = np.c_[H,tmp]

        # if to include bias column in weights
        if self.outputBias:
            H = np.transpose(np.c_[H.T,np.ones([self.N,1])])
        self.CoefficientMatrix = H

        # computing output matrix
        Y = self.outputData.T

        # computing output layer weights
        self.outputWeights = Y@np.linalg.pinv(H)

    # predict function
    def predict(self,x_pred):  # x_pred has to be a row vector
        y_pred = []
        if self.outputBias:
            for i in range(x_pred.shape[0]):
                z = self.hiddenWeights@x_pred[i][:,None]+self.hiddenBias
                a = self.h(z)
                a = np.r_[a,np.ones([1,1])]  # appending 1 for bias term
                y_hat = self.outputWeights@a
                y_pred.append(y_hat.flatten())
        else:
            for i in range(x_pred.shape[0]):
                z = self.hiddenWeights@x_pred[i][:,None]+self.hiddenBias
                a = self.h(z)
                y_hat = self.outputWeights@a
                y_pred.append(y_hat.flatten())

        return np.array(y_pred)

#==============================================================================
