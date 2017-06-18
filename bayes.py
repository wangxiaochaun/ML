#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 19:50:10 2017

@author: pingguo
"""
from numpy import *


def loadDataset():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec

def createVocablist(dataset):
    vocabSet = set([]) #创建一个空集
    for document in dataset:
        vocabSet = vocabSet | set(document) #两个集合的并集,无重复单词
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList) #创建一个所有元素为0，长度为词汇表的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word : %s is not in my Vacabulart!" % word)
    return returnVec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    #print(numTrainDocs)
    numWords = len(trainMatrix[0])
    #print(numWords)
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    #print(pAbusive)
    #p0Num = np.zeros(numWords); p1Num = np.zeros(numWords)
    p0Num = ones(numWords); p1Num = ones(numWords) #防止有一项为零导致乘积为零
    #p0Denom = 0.0; p1Denom = 0.0
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            #print(p1Num)
            p1Denom += sum(trainMatrix[i])
            #print(p1Denom)
        else:
            p0Num += trainMatrix[i]
            #print(p0Num)
            p0Denom += sum(trainMatrix[i])
    #p1Vect = p1Num / p1Denom
    p1Vect = log(p1Num / p1Denom) #取对数防止极小值在计算后舍入成0
    #print(p1Vect)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def classfyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
    
def testingNB():
    listOfPost, listClasses = loadDataset()
    myVocabList = createVocablist(listOfPost)
    trainMat = []
    for postinDoc in listOfPost:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0v, p1v, pA = trainNB0(trainMat, listClasses)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classfyNB(thisDoc, p0v, p1v, pA))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classfyNB(thisDoc, p0v, p1v, pA))
    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

#过滤垃圾邮件  
def textParse(bigString):      #正则表达式进行文本解析  
    import re  
    listOfTokens = re.split(r'\W*',bigString)  
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]  
  
def spamTest(): 
    import codecs
    docList = []; classList = []; fullText = []  
    for i in range(1,26):                          #导入并解析文本文件  
        wordList = textParse(codecs.open('email/spam/%d.txt' % i, 'r', 'ISO-8859-1').read())  
        docList.append(wordList)  
        fullText.extend(wordList)  
        classList.append(1)  
        wordList = textParse(codecs.open('email/ham/%d.txt' % i, 'r', 'ISO-8859-1').read())  
        docList.append(wordList)  
        fullText.extend(wordList)  
        classList.append(0)  
    vocabList = createVocablist(docList)  
    trainingSet = list(range(50));testSet = []  
    for i in range(10):                         #随机构建训练集  
        randIndex = int(random.uniform(0,len(trainingSet)))  
        testSet.append(trainingSet[randIndex])  
        del(trainingSet[randIndex])  
    trainMat = []; trainClasses = []  
    for docIndex in trainingSet:  
        randIndex = int(random.uniform(0,len(trainingSet)))  
        testSet.append(trainingSet[randIndex])  
        del(trainingSet[randIndex])  
    trainMat = []; trainClasses = []  
    for docIndex in trainingSet:  
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))  
        trainClasses.append(classList[docIndex])  
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))  
    errorCount = 0  
    for docIndex in testSet:              #对测试集进行分类  
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])  
        if classfyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:  
            errorCount += 1  
    print('the error rate is: ', float(errorCount)/len(testSet))  