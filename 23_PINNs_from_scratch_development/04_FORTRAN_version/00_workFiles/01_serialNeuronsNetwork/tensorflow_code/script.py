import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf


# defining model parameters----------------------------------------------------
epochs = 10000
kern_init = tf.keras.initializers.RandomUniform(seed = 1)
bias_init = tf.keras.initializers.RandomUniform(seed = 1)
activation = "tanh"
optimizerFunc = tf.keras.optimizers.legacy.Adam(learning_rate = 0.001)


# constructing model-----------------------------------------------------------

Inp = tf.keras.Input(shape = (1,), name = "input")

d1 = tf.keras.layers.Dense(units = 1,
                           activation = activation,
                           name = "dense1")(Inp)

d2 = tf.keras.layers.Dense(units = 1,
                           activation = activation,
                           name = "dense2")(d1)

d3 = tf.keras.layers.Dense(units = 1,
                           activation = activation,
                           name = "dense3")(d2)

d4 = tf.keras.layers.Dense(units = 1,
                           activation = activation,
                           name = "dense4")(d3)

d5 = tf.keras.layers.Dense(units = 1,
                           activation = activation,
                           name = "dense5")(d4)

d6 = tf.keras.layers.Dense(units = 1,
                           activation = activation,
                           name = "dense6")(d5)

model = tf.keras.Model(inputs = [Inp], outputs = [d6])

model.compile(optimizer = optimizerFunc, loss = ["mse"])

# preparing dataset

x = np.linspace(0,0.5,101)[:,None]
y = 0.5*np.sin(4*x)[:,None]

model.load_weights("saved_weights/")

hist = model.fit(x,y, epochs = epochs, batch_size = None)

model.save_weights("saved_weights/")

y_pred = model.predict(x)

plt.rcParams.update({'font.size':15})
plt.figure(figsize=(16,9))
plt.plot(x.flatten(),y_pred.flatten(),'-b',label = "estimated")
plt.plot(x.flatten(),y.flatten(),'-r', label = "expected")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("estimation_tf.png", dpi = 150)

plt.show()


fid = pd.DataFrame(np.transpose([x.flatten(),y.flatten(),y_pred.flatten()]),
                   columns = ["x","y","y_pred"])
fid.to_csv("estimation.csv", index = None)
