import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# defining model parameters
epochs = 100
activation = "tanh"
learningRate = 1e-3
optimizerFunc = tf.keras.optimizers.legacy.Adam(learning_rate = learningRate)
#  init = tf.keras.initializers.RandomNormal(seed=1)
init = tf.keras.initializers.RandomNormal()


# defining model
Inp = tf.keras.Input(shape=(1,), name = "input")

d1 = tf.keras.layers.Dense(units = 5, kernel_initializer = init,
                           bias_initializer = init, activation = activation,
                           name = "dense1")(Inp)

d2 = tf.keras.layers.Dense(units = 5, kernel_initializer = init,
                           bias_initializer = init, activation = activation,
                           name = "dense2")(d1)

d3 = tf.keras.layers.Dense(units = 5, kernel_initializer = init,
                           bias_initializer = init, activation = activation,
                           name = "dense3")(d2)

d4 = tf.keras.layers.Dense(units = 5, kernel_initializer = init,
                           bias_initializer = init, activation = activation,
                           name = "dense4")(d3)

d5 = tf.keras.layers.Dense(units = 5, kernel_initializer = init,
                           bias_initializer = init, activation = activation,
                           name = "dense5")(d4)

d6 = tf.keras.layers.Dense(units = 5, kernel_initializer = init,
                           bias_initializer = init, activation = activation,
                           name = "dense6")(d5)

d7 = tf.keras.layers.Dense(units = 1, kernel_initializer = init,
                           bias_initializer = init, activation = activation,
                           name = "dense7")(d6)

model = tf.keras.Model(inputs = Inp, outputs = d7)

model.compile(optimizer=optimizerFunc, loss = ["mse"])

# reading training data
fid = pd.read_csv("../normalized_data.txt", header = None)

model.load_weights("saved_weights/")

# training model
hist = model.fit(fid[0],fid[1],epochs = epochs, batch_size = None)

model.save_weights("saved_weights/")


y_pred = model.predict(fid[0])



# plotting
plt.rcParams.update({"font.size":15})
plt.figure(figsize=(16,9))
plt.plot(fid[0],fid[1],'-r',label="expected")
plt.plot(fid[0],y_pred,'-b',label="estimated")
plt.grid()
plt.savefig("output.png", dpi = 150)
plt.legend()

plt.show()
