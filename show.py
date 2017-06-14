#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:10:45 2017

@author: pingguo
"""

import kNN
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from os import listdir


hwLabels = []
#trainingFileList = listdir('trainingDigits')
m = len(trainingFileList)
trainingMat = np.zeros((m, 1024))
for i in range(m):
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    hwLabels.append(classNumStr)
    trainingMat[i, :] = kNN.img2vector('trainingDigits/%s' % fileNameStr)
#testFileList = listdir('testDigits')
errorCount = 0.0
mTest = len(testFileList)
for i in range(mTest):
    fileNameStr = testFileList[i]
    fileStr = fileNameStr.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    vectorUnderTest = kNN.img2vector('testDigits/%s' % fileNameStr)
    classifierResult = kNN.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
    print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
    if (classifierResult != classNumStr) : errorCount += 1.0
print("\nthe total number of errors is: %d" % errorCount)
print("\nthe total error rate is: %f" % (errorCount/float(mTest)))