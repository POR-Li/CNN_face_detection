'''
List all params of face12c_full_conv_quantize_3
'''

import numpy as np
import sys

file_write = open('face12c_full_conv_quantize_3_params.txt', 'w')
sys.stdout = file_write
# ==================  caffe  ======================================
caffe_root = '/home/anson/caffe-master/'  # this file is expected to be in {caffe_root}/examples
sys.path.insert(0, caffe_root + 'python')
import caffe
# =================================================================================

# ==================  load face12c_full_conv  ======================================
MODEL_FILE = '/home/anson/caffe-master/models/face_12c/face12c_full_conv.prototxt'
PRETRAINED = '/home/anson/caffe-master/models/face_12c/face12c_full_conv_quantize_3.caffemodel'
caffe.set_mode_gpu()
net = caffe.Net(MODEL_FILE, PRETRAINED, caffe.TEST)

print "\n============face12c_full_conv_quantize_3================="
for k, v in net.params.items():
    print (k, v[0].data.shape)
    filters_weights = net.params[k][0].data
    filters_bias = net.params[k][1].data

    print ("Shape of " + k + " weight params : " + str(filters_weights.shape))
    for currentNum in np.nditer(filters_weights):
        print currentNum

    print ("Shape of " + k + " bias params: " + str(filters_bias.shape))
    for currentNum in np.nditer(filters_bias):
        print currentNum

# net_quantized.save('/home/anson/caffe-master/models/face_12c/face12c_full_conv_quantize_3.caffemodel')

file_write.close()