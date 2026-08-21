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
linear(x::Float64) = x
# tanh - definition already exists

# dense layer definition
mutable struct Layer

    inputSize::Int64
    outputSize::Int64
    W::Matrix{Float64}
    b::Matrix{Float64}
    activation::Function
    name::String
    aVec::Matrix{Float64}

    function Layer(inputSize::Int64,outputSize::Int64,activation::Function,
                   name::String = "denseLayer")
        W = rand(outputSize,inputSize)
        b = rand(outputSize,1)
        new(inputSize,outputSize,W,b,activation,name)
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
