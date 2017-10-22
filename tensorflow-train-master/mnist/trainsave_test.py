#imporp some block
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

import os
import argparse
import sys
from mnist_demo import * 

# Import data
import input_data

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('data_dir', 'data/', 'Directory for storing data')

# Import data
mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
saver = tf.train.Saver() # produce saver
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # initial
    # Train
    for _ in range(1000):
      batch_xs, batch_ys = mnist.train.next_batch(100)
      sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy=tf.cast(tf.argmax(y, 1),tf.float32)
    print("\n")
    print("model's accuracy: ")
    print(sess.run(tf.reduce_mean(tf.cast(correct_prediction, tf.float32)), 
		feed_dict={x: mnist.train.images,y_: mnist.train.labels}))

    print("Train Successful ! \n")
    saver.save(sess, "model.ckpt") #save to model.ckpt
    print("Successul save train model to model.ckpt !")




