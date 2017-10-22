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

mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

sess = tf.InteractiveSession()

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# Train
tf.global_variables_initializer().run()
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  train_step.run({x: batch_xs, y_: batch_ys})

# Test trained model
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy=tf.cast(tf.argmax(y, 1),tf.float32)


#get image and pridect it
dir_name="test_num"
files = os.listdir(dir_name)
cnt=len(files)
for i in range(cnt):
  files[i]=dir_name+"/"+files[i]
  test_images1,test_labels1=GetImage([files[i]])
  mnist.test = input_data.DataSet(test_images1, test_labels1, dtype=tf.float32)
  res=accuracy.eval({x: mnist.test.images, y_: mnist.test.labels})

  print("output:",int(res[0]))
  print("\n")


