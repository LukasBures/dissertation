# from tensorflow.python.client import device_lib
import cv2
import tensorflow as tf

with tf.device("/gpu:0"):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name="a")
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name="b")
    c = tf.matmul(a, b)

# with tf.Session() as sess:
# print(sess.run(c)
# print(device_lib.list_local_devices())
print(tf.__version__)
print(tf.test.is_built_with_cuda())
print("--------------")
print(tf.compat.v2.test.is_gpu_available())
print(cv2.__version__)
