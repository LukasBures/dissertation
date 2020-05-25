import os
import numpy as np
import tensorflow as tf
import cv2


a = np.array([1.0, 2.0, 3.0, 4.0])
s = np.sqrt(a)



print(cv2.__version__)
print(cv2.getBuildInformation())




import tensorflow as tf

@tf.function
def mm():
    with tf.device('/device:gpu:0'):
        a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
        b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
        return tf.matmul(a, b)
out = mm()
print(out)









