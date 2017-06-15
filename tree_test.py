# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 16:03:00 2017

@author: ThinkStation
"""

import trees

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

myDat, labels = createDataSet()
test = trees.calcShannonEnt(myDat)