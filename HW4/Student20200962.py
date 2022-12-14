#!/usr/bin/python3
import os
import sys
import numpy as np
import operator
import math

def createDataSet():
	groupArr = []
	labels = []
	for filename in os.listdir(sys.argv[1]):
		with open(os.path.join(sys.argv[1], filename), 'r') as rf:
			data = []
			for line in rf:
				data.append(line.strip())
			data = "".join(data)
			groupArr.append(list(map(int, data)))
			labels.append(filename.split('_')[0])
	group = np.array(groupArr)
	return group, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()

	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]


group, labels = createDataSet()

for k in range(20):
	failNum = 0
	fileCount = 0
	for filename in os.listdir(sys.argv[2]):
		data = []
		with open(os.path.join(sys.argv[2], filename), 'r') as rf:
			for line in rf:
				data.append(line.strip())
			data = "".join(data)
		guessResult = classify0(list(map(int, data)), group, labels, k+1)
		if guessResult != filename.split('_')[0]:
			failNum += 1
		fileCount += 1
#		print(guessResult, filename)
		
	print(math.trunc(failNum / fileCount * 100))
