#imporp some block
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import time
import os
import argparse
import sys
from new_mnist_demo import * 
from softmax_train import *
from flask import Flask,request
from scipy import misc
from sklearn.externals import joblib
from put_message_cassandra import *


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    print(f.filename,"......")	
    test_images1,test_labels1=GetImage(f.filename)
    mnist.test = input_data.DataSet(test_images1, test_labels1, dtype=tf.float32)
    #pridect the most similar number
    res=accuracy.eval({x: mnist.test.images, y_: mnist.test.labels})
    now_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    put_message(str(f.filename),int(res[0]),now_time)
    return('identification result:     %s ' % int(res[0]))
    

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>
    <body>
    <form action='/upload' method='post' enctype='multipart/form-data'>
        <input type='file' name='file'>
    <input type='submit' value='begin to recognize'>
    </form>
    '''    
if __name__ == '__main__':
    app.run()
