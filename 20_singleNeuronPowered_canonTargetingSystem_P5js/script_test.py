#!/bin/python3
"""----------------------------------------------------------------------------
single neuron autodiff trial for single value approximation
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import matplotlib.pyplot as plt

#  # fixing input and output
#  y_act = 0.25
#  x_inp = 0.5
#
#  # learning rate
#  LR = 0.1
#
#  # initial values for weight and bias
#  w = np.random.uniform(-1,1)
#  b = np.random.uniform(-1,1)
#
#  print("initial values")
#  print("w = ",w)
#  print("b = ",b)
#
#  # begining loop
#  for itr in range(100):
#      # forward pass
#      dw = 1
#      db = 1
#
#      t1 = w*x_inp + b
#      dt1 = dw*x_inp + db
#
#      t2 = np.exp(-t1)
#      dt2 = -np.exp(-t1)*dt1
#
#      t3 = 1+t2
#      dt3 = dt2*1.0
#
#      t4 = 1/t3
#      dt4 = -1/t3**2*dt3
#
#      L = (y_act - t4)**2
#      dL = -2*(y_act - t4)*dt4
#
#      # reverse mode
#      dLdt4 = -2*(y_act-t4)
#      dLdt3 = dLdt4*dt4/dt3
#      dLdt2 = dLdt3*dt3/dt2
#      dLdt1 = dLdt2*dt2/dt1
#
#      dt1dw = x_inp*1.0
#      dt1db = 1.0
#
#      dLdw = dLdt1*dt1dw
#      dLdb = dLdt1*dt1db
#
#      # adjusting weights
#      w -= dLdw*LR
#      b -= dLdb*LR
#
#      print(itr, L, w, b)
#
#
#  print("predicted value")
#  y_hat = 1.0/(1+np.exp(-(w*x_inp+b)))
#  print("y_hat = ",y_hat)

#  # fixing input and output
#  y_act = 0.0
#  x_inp = 1.0
#
#  # learning rate
#  LR = 0.001
#
#  # initial values for weight and bias
#  #  w = np.random.uniform(0,1)
#  #  b = np.random.uniform(0,1)
#  w = 1e-2
#  b = 1e-2
#
#  print("initial values")
#  print("w = ",w)
#  print("b = ",b)
#
#  l = 1.0
#  height = 1.0
#
#  # begining loop
#  for itr in range(1000):
#      # forward pass
#      dw = 1
#      db = 1
#
#      t1 = w*x_inp + b
#      dt1 = dw*x_inp + db
#
#      t2 = np.exp(-t1)
#      dt2 = -np.exp(-t1)*dt1
#
#      t3 = 1 + t2
#      dt3 = dt2*1.0
#
#      t4 = 1/t3
#      dt4 = -1/t3**2*dt3
#
#      t5 = np.pi/2*t4-np.pi/4.0
#      dt5 = np.pi/2.0*dt4
#
#      t6 = np.tan(t5)*l/height
#      dt6 = l/height*1/np.cos(t5)**2*dt5
#
#      t7 = y_act/height-t6
#      dt7 = -dt6
#
#      L = t7**2
#      dL = 2*t7*dt7
#
#      # reverse pass
#      dLdt7 = 2*t7
#      dLdt6 = dLdt7*dt7/dt6
#      dLdt5 = dLdt6*dt6/dt5
#      dLdt4 = dLdt5*dt5/dt4
#      dLdt3 = dLdt4*dt4/dt5
#      dLdt2 = dLdt3*dt3/dt2
#      dLdt1 = dLdt2*dt2/dt1
#
#      dt1dw = x_inp
#      dt1db = 1.0
#
#      dLdw = dLdt1*dt1dw
#      dLdb = dLdt1*dt1db
#      # adjusting weights
#      w -= dLdw*LR
#      b -= dLdb*LR
#
#      print(itr, L, w, b)
#
#
#  print("predicted value")
#  y_hat = l/height*np.tan(1/(1+np.exp(-(w*x_inp+b)))*np.pi/2-np.pi/4)
#  print("y_hat = ",y_hat)
#
#
#  #  W,B = np.meshgrid(np.linspace(-1,1,101),np.linspace(-1,1,101))
#  #
#  #  L = (y_hat/height - l/height*np.tan(1/(1+np.exp(-(W*x_inp+B)))*np.pi/2-np.pi/4))
#
#  W = np.linspace(-1,1)
#
#  #  L = (y_act - l*np.tan(1/(1+np.exp(-W))*np.pi/2-np.pi/4))**2
#  L = (-0.9 - l*np.tan(1/(1+np.exp(-W))*np.pi/2-np.pi/4))**2
#
#  plt.figure()
#  #  plt.contourf(W,B,L,100,cmap='jet')
#  plt.plot(W,L,'-b')
#  #  plt.colorbar()
#  plt.grid()
#  #  plt.axis("image")
#  plt.show()




l     = 1.0
y_act = -0.5

LR = 0.5

# initializing weights
w = np.random.uniform(-1,1)

# looping
for itr in range(50):
    # forward pass
    dw = 1.0

    t1 = np.exp(-w)
    dt1 = -np.exp(-w)*dw

    t2 = 1+t1
    dt2 = dt1*1.0

    t3 = 1/t2
    dt3 = -1/t2**2*dt2

    t4 = np.pi/2.0*t3 - np.pi/4.0
    dt4 = np.pi/2.0*dt3

    t5 = l*np.tan(t4)
    dt5 = l/np.cos(t4)**2*dt4

    t6 = y_act - t5
    dt6 = -dt5

    L = t6**2
    dL = 2*t6*dt6

    # reverse mode
    dLdt6 = 2*t6
    dLdt5 = dLdt6*dt6/dt5
    dLdt4 = dLdt5*dt5/dt4
    dLdt3 = dLdt4*dt4/dt3
    dLdt2 = dLdt3*dt3/dt2
    dLdt1 = dLdt2*dt2/dt1
    dLdw = dLdt1*dt1/dw

    # adjusting the weight
    w -= LR*dLdw

    print(itr, L, w)

# computing y_hat
y_hat = l*np.tan(1/(1+np.exp(-w))*np.pi/2.0-np.pi/4.0)

print("\npredicted value: y_hat = ",y_hat)

