#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:45:50 2017

@author: pingguo
"""

import numpy as np
import operator

a = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
label = ['a', 'a', 'b', 'b']
b = a.shape
inX = [0, 0]
c = np.tile(inX, (b[0], 1))

diffMat = c - a
sqDiffMat = diffMat**2
sqDistance = sqDiffMat.sum(axis = 1)
distances = sqDistance**0.5
sortedDistIndices = distances.argsort()


classCount = {}
#k = 3
for i in range(3):
    voteIlabel = label[sortedDistIndices[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)

print(sortedClassCount[0][0])