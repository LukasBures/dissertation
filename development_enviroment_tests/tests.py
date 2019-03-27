import keras
import torch
import tensorflow as tf
import chainer

# print(chainer.backends.cuda.available)
# print(chainer.backends.cuda.cudnn_enabled)
# python3 -c 'import chainer; print(chainer.backends.cuda.available,print(chainer.backends.cuda.cudnn_enabled)'
# import tensorflow as tf;
# print(tf.reduce_sum(tf.random_normal([1000, 1000])))
# import tensorflow as tf

with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)
    d = 1515
    print(d)

with tf.Session() as sess:
    print(sess.list_devices())
    print(sess.run(c))
    print(tf.__version__)
