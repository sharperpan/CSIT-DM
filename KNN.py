# -*- coding: cp936 -*-
import csv

def ReadDataSet(csvFileName):
    with open(csvFileName,'rb') as csvfile:
        spamReader = csv.reader(csvfile,delimiter=' ')
        dataList = []
        resultList = []
        dataList = list(spamReader)
        for str in dataList:
            intData = str[0].split(',')
            resultList.append(intData)
        return resultList

def CaculateDistance(trainList,sampleList):
    distance  = 0
    for i in range(len(trainList)):
        if trainList[i] != sampleList[i]:
            distance = distance + 1
    return distance

def k1Index(distanceList):
    return distanceList.index(min(distanceList))
        
    


def KNN1(trainingLabel,dateLabel,distanceList):
    labelResult = []
    result = []
    for data in distanceList:
        lableIndex = k1Index(data)
        labelResult.append(lableIndex)
    for i in range(10):       
        if trainingLabel[labelResult[i]] != dateLabel[i]:
            result.append(1)
    return float(sum(result))/10
        
#return min three index
def minThree(distanceList):
    temp = []
    for i in range(3):
        temp.append(distanceList.index(min(distanceList)))
        distanceList[temp[i]] = 1000000000
    return temp
        
        

def KNN3(trainingLabel,dateLabel,distanceList):
    labelResult = []  #index
    result = []
    temp = []
    for i in range(10):
        temp = minThree(distanceList[i])
        print temp
        indexSum = 0
        for j in temp:
            indexSum = trainingLabel[j] + indexSum
        if indexSum > 1:
            labelResult.append(1)
        else:
            labelResult.append(0)
    for i in range(10):       
        if labelResult[i] != dateLabel[i]:
            result.append(1)                
        
    return float(sum(result))/10

if __name__ == "__main__":
    trainingLabel =[0,1,1,1,0,0,0,1,0,1]
    dateLabel = [1,0,1,1,0,0,0,1,1,0]
    trainingData = ReadDataSet('training.csv')
    dataSet = ReadDataSet('data.csv')
    distanceList = [[] for i in range(10)]
    for i in range(10):
        for j in range(10):
            tempDistance = CaculateDistance(dataSet[i],trainingData[j])
            distanceList[i].append(tempDistance)
    for i in distanceList:
        print i\

    print "The right rate of K=1： " + str(KNN1(trainingLabel,dateLabel,distanceList))
    print "The right rate of K=3： " + str(KNN3(trainingLabel,dateLabel,distanceList))

     

    
