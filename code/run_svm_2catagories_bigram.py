#!/usr/bin/env python3
# encoding=utf-8
import sys
import random
sys.path.append("/Users/liucongyou/Downloads/libsvm/python")
from svmutil import *

y, x = svm_read_problem("./bigramsvm.txt")
test_scale = 0.2
ilist = random.sample(range(len(y)), int(len(y) * 0.2))
x_test = []
y_test = []
x_train = []
y_train = []
for i in range(len(y)):
    if i in ilist:
        y_test.append(y[i] // 3)
        x_test.append(x[i])
    else:
        y_train.append(y[i] // 3)
        x_train.append(x[i])

m = svm_train(y_train, x_train, '-t 0 -c 100')
l, a, v = svm_predict(y_test, x_test, m)
correct = 0
total = 0
