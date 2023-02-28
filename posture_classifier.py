import tensorflow as tf
import numpy as np

good_x_train = np.load("good.npy")
bad_x_train = np.load("bad.npy")

good_y_train = np.ones(len(good_x_train))
bad_y_train = np.zeros(len(bad_x_train))

x_train = np.append(good_x_train, bad_x_train, axis=0)
y_train = np.append(good_y_train, bad_y_train, axis=0)


model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Dense(32, activation="relu", input_dim=8),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid"),  # Output layer
    ]
)

loss_fn = tf.keras.losses.BinaryCrossentropy()

model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

model.fit(x_train, y_train, epochs=10)

good_x_test = np.load("good_test.npy")
bad_x_test = np.load("bad_test.npy")

good_y_test = np.ones(len(good_x_test))
bad_y_test = np.zeros(len(bad_x_test))

x_test = np.append(good_x_test, bad_x_test, axis=0)
y_test = np.append(good_y_test, bad_y_test, axis=0)

print("Model performance:")
model.evaluate(x_test, y_test)

model.save("models/posture-model.h5", overwrite=True, include_optimizer=True)