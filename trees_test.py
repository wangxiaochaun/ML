#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 19:34:02 2017

@author: pingguo
"""

import trees
import treePlotter

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)

print(lensesTree)

treePlotter.createPlot(lensesTree)