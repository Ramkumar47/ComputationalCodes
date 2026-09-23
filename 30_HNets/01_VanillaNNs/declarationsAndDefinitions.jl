#!/bin/julia
#==============================================================================
declarations and definitions script

Ramkumar
Sun Aug 16 01:06:18 PM IST 2026
==============================================================================#

using Random
using Statistics

Random.seed!(1) # fixing seed value

#=============================================================================#

# activation functions
sigmoid(x::Float64) = 1.0/(1.0+exp(-x))
sigmoidDerivative(x::Float64) = sigmoid(x)*(1-sigmoid(x))
linear(x::Float64) = x
linearDerivative(x::Float64) = 1.0
# tanh - definition already exists
tanhDerivative(x::Float64) = 1.0 - tanh(x)^2

# dense layer definition
mutable struct Layer

    inputSize::Int64
    outputSize::Int64
    W::Matrix{Float64}
    b::Matrix{Float64}
    activation::Function
    activationDerivative::Function
    name::String
    aVec::Matrix{Float64}

    function Layer(inputSize::Int64,outputSize::Int64,activation::Function,
                   activationDerivative::Function,
                   name::String = "denseLayer")
        W = rand(outputSize,inputSize)
        b = rand(outputSize,1)
        #=
"new" constructor initializes in the declaration sequence only
and not by the order given below. So, the order has to be
same between above list of declarations and below within ()
=#
        new(inputSize,outputSize,W,b,activation,activationDerivative,name)
    end

    function describe()
        print("layer name : ",name)
    end

end

# forward function definition
function forward(l::Layer, x::Matrix)
    out = l.W*x .+ l.b
    l.aVec = l.activation.(out)
    return l.activation.(out)
end

# defining loss functions
function SSELoss(x::Matrix, xHat::Matrix)
    lossVal = sum((xHat.-x).^2)
        return lossVal
end
function MSELoss(x::Matrix, xHat::Matrix)
    lossVal = mean((xHat.-x).^2)
    return lossVal
end

#=============================================================================#
