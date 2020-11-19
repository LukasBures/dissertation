from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

tf.debugging.set_log_device_placement(True)

try:
    gpus = tf.config.experimental.list_physical_devices('GPU')

    print(gpus)
    # Specify an invalid GPU device
    with tf.device('/device:GPU:0'):
        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        # validation_split = 0-1 procenta, example 0.1 = rozdeli nahodne na trenovaci a validacni sety
        # shuffle, T/F zamicha
        model.fit(x_train, y_train, epochs=5)

        model.save("./muj_model.h5")
        muj_model = tf.keras.models.load_model("muj_model.h5")
        muj_model.evaluate(x_test, y_test, verbose=3)
except RuntimeError as e:
    print(e)
