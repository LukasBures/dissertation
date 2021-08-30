
import tensorflow as tf

# Create a Tensor.
hello = tf.constant("hello world")
print(hello)



print(hello.numpy())


print(('Your TensorFlow version: {0}').format(tf.__version__))

print(('Is your GPU available for use?\n{0}').format(
    'Yes, your GPU is available: True' if tf.test.is_gpu_available() == True else 'No, your GPU is NOT available: False'
))

print(('\nYour devices that are available:\n{0}').format(
    [device.name for device in tf.config.experimental.list_physical_devices()]
))




import time

cpu_slot = 0
gpu_slot = 0

# Using CPU at slot 0
with tf.device('/CPU:' + str(cpu_slot)):
    # Starting a timer
    start = time.time()

    # Doing operations on CPU
    A = tf.constant([[3, 2], [5, 2]])
    print(tf.eye(2,2))

    # Printing how long it took with CPU
    end = time.time() - start
    print(end)

# Using the GPU at slot 0
with tf.device('/GPU:' + str(gpu_slot)):
    # Starting a timer
    start = time.time()

    # Doing operations on CPU
    A = tf.constant([[3, 2], [5, 2]])
    print(tf.eye(2,2))

    # Printing how long it took with CPU
    end = time.time() - start
    print(end)


import math

def gelu(x):
    return 0.5*x*(1+tf.tanh(tf.sqrt(2/math.pi)*(x+0.044715*tf.pow(x, 3))))

def get_gradient(x, activation_function):
    with tf.GradientTape() as gt:
        y = activation_function(x)

    gradient = gt.gradient(y, x).numpy()

    return gradient

x = tf.Variable(0.5)
gradient = get_gradient(x, gelu)

print('{0} is the gradient of GELU with x={1}'.format(
    gradient, x.numpy()
))



import timeit
conv_layer = tf.keras.layers.Conv2D(100, 3)

@tf.function
def conv_fn(image):
  return conv_layer(image)

image = tf.zeros([1, 200, 200, 100])
# warm up
conv_layer(image); conv_fn(image)

no_tf_fn = timeit.timeit(lambda: conv_layer(image), number=10)
with_tf_fn = timeit.timeit(lambda: conv_fn(image), number=10)
difference = no_tf_fn - with_tf_fn

print("Without tf.function: ", no_tf_fn)
print("With tf.function: ", with_tf_fn)
print("The difference: ", difference)

print("\nJust imagine when we have to do millions/billions of these calculations," \
      " then the difference will be HUGE!")
print("Difference times a billion: ", difference*1000000000)