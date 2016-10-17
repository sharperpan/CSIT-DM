# -*- coding: cp936 -*-

def hashFunction(result):
    if result>0:
        return 1
    else:
        return 0

def nuralFunction(inputData,trainingPara,targetResult):
    resultData = []
    print 'sub calulate value of W'
    for i in range(len(inputData)):
        tempResult = inputData[i][0] * trainingPara[0] + inputData[i][1] *trainingPara[1] + inputData[i][2] * trainingPara[2]
        tempResult = hashFunction(tempResult)
        ## 每次计算后更新参数W
        trainingPara = updataPara(tempResult,targetResult[i],trainingPara,inputData[i])
        print trainingPara
        resultData.append(tempResult)
    return resultData,trainingPara

def updataPara(tempResult,targetResult,trainingPara,inputData):
    for i in range(len(trainingPara)):
        trainingPara[i] = trainingPara[i] + 0.05*inputData[i]*(targetResult-tempResult)
    return trainingPara
        

if __name__ == "__main__":
    inputData = [[-1,0,0],[-1,0,1],[-1,1,0],[-1,1,1]]
    targetResult = [0,0,0,1]
    trainingPara = [-0.1,-0.2,0.2]
    alpha = 0.05
    flag = True;
    resultData = []
    i = 1
    while(flag):
        print str(i) + '.the value of W:  ' + str(trainingPara)
        i = i+1
        temp = nuralFunction(inputData,trainingPara,targetResult)
        tempResult = temp[0]
        trainingPara = temp[1]
        print 'after iteration the result is:' +  str(tempResult)
        print '------------------------------'
        if cmp(tempResult,targetResult) == 0:
            print 'traing finish'
            flag = False
        else:
            continue
    
            
    
