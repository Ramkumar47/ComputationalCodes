#!/bin/julia
#==============================================================================
Vanilla Neural Networks

Ramkumar
Sun Aug 16 12:59:37 PM IST 2026
==============================================================================#

using Plots

include("declarationsAndDefinitions.jl")

#=============================================================================#

# defining dense layers
l1     = Layer(1,2,tanh,"l1")
l2     = Layer(2,3,tanh,"l2")
l3     = Layer(3,2,tanh,"l3")
l4     = Layer(2,1,linear,"l4")
layers = [l1,l2,l3,l4]

# generating random data
x     = collect(range(0,1,101))
x     = reshape(x,1,x.size[1])
noise = rand(x.size[1]).*0.02.-0.01
y     = x.^2 .+ noise

# performing forward pass
output = Array{Float64}[]
forward(layers[1],x)
for i in range(2,layers.size[1]-1)
    forward(layers[i],layers[i-1].aVec)
end
yHat = forward(layers[end],layers[end-1].aVec)

# computing loss
loss = SSELoss(y,yHat)
# loss = MSELoss(y,yHat)

# # performing back-propagation
#
# dLmdaL = -2.0.*(y-yHat) # last layer
# daLdZL = ones(dLmdaL.size)
# deltaL = dLmdaL.*daLdZL
#
# count = layers.size[1]
# for layer in reverse(layers[1:end])
#     dLmdal = deltaL.*output[count-1]
#     dLmdbl = deltaL
# end

#=============================================================================#
