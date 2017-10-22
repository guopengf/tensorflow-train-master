#imporp some block
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

import os
import argparse
import sys
from new_mnist_demo import * 
from softmax_train import *


#get image and pridect it
dir_name="test_num"
files = os.listdir(dir_name)
cnt=len(files)
for i in range(cnt):
   # read file dir
  files[i]=files[i]
  print(files[i])
  #return value and lable
  test_images1,test_labels1=GetImage(files[i])
  mnist.test = input_data.DataSet(test_images1, test_labels1, dtype=tf.float32)
  #pridect the most similar number
  res=accuracy.eval({x: mnist.test.images, y_: mnist.test.labels})
  print("output:",int(res[0]))
  print("\n")


