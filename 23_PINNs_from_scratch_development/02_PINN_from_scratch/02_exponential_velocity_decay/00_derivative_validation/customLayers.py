"""----------------------------------------------------------------------------
Custom neural network layers definition file
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np

# Dense layer definition-------------------------------------------------------
class Dense:
    def __init__(self, N_neurons, input_size, layer_name = "denseLayer"):
        self.layer_name = layer_name
        self.N_neurons  = N_neurons
        self.input_size = input_size
        self.layer_output = np.zeros(self.N_neurons)
        self.layer_z = np.zeros(self.N_neurons)
        self.layer_input = np.zeros(input_size)

        # initializing weights and biases
        self.weight = np.random.normal(size=[N_neurons,input_size])
        self.bias = np.random.normal(size=[N_neurons,1])

    # hardcoding activation function
    def activation(self,x):
        return np.tanh(x)
        # return 1.0/(1.0+np.exp(-x))

    # hardcoding activation function derivative
    def activation_derivative(self,x):
        return 1 - np.tanh(x)**2
        # return self.activation(x)*(1.0-self.activation(x))

    # forward pass evaluation function
    def evaluate(self, input_vector):
        self.layer_input = input_vector*1.0  # to prevent absolute referencing
        # evaluating forward way
        self.layer_z = np.matmul(self.weight,input_vector) + self.bias
        self.layer_output = self.activation(self.layer_z)

        return self.layer_output

    def compute_derivatives(self):
        # computing error derivative
        dSigma_dz = self.activation_derivative(self.layer_z)

        # computing derivative w.r.t. input
        dSigma_dx = np.matmul(self.weight.T,np.diag(dSigma_dz.flatten()))

        return dSigma_dz, dSigma_dx

    def printInfo(self):

        print("Layer name        = ", self.layer_name)
        print("Number of neurons = ", self.N_neurons)
        print("input size        = ", self.input_size)
        print("layer weights ")
        print(self.weight)
        print("layer bias ")
        print(self.bias)

    # saving and loading weights
    def save_weights(self, folderName):
        # preparing filename
        wname = folderName+"/"+self.layer_name+"_weights.npy"
        bname = folderName+"/"+self.layer_name+"_bias.npy"

        # saving weights
        np.save(wname,self.weight)
        np.save(bname,self.bias)

    def load_weights(self, folderName):
        # preparing filename
        wname = folderName+"/"+self.layer_name+"_weights.npy"
        bname = folderName+"/"+self.layer_name+"_bias.npy"

        # loading weights
        self.weight = np.load(wname)
        self.bias   = np.load(bname)
