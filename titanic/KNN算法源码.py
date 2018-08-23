#进行模型测试
import csv
import random
import math
import operator

def loadDataset(filename,split,trainingSet = [],testSet = []):#导入数据集,进行训练集和测试集的切割
    with open(filename,'r+') as csvfile:  #通过，分隔开的数据
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def euclideanDistance(instance1,instance2,length):# 两向量的欧氏距离，length是维度的表达
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

def getNeighbors(trainingSet,testInstance,k): #选出来一个实例的k个最近的点
    distances = []                            #容器
    length = len(testInstance)-1              #实例的维数
    for x in range(len(trainingSet)):        #算出训练集中每个点到实例的距离信息（包括点是谁
        dist = euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1)) #取得的距离排个序
    neighbors = []
    for x in range(k):                         #找到距离最近的前k个“名字”，加到neighbors里
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):  #投票看邻居属于哪
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),key = operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet,predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] ==predictions[x]:  #预测对了+1
            correct += 1
    return (correct/float(len(testSet)))*100.0    #返回预测的准确度

def main():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset(r'F:\BaiduNetdiskDownload\irisdata.txt',split,trainingSet,testSet)
    print('训练集：',repr(len(trainingSet)))
    print('测试集：',repr(len(testSet)))
    #开始预测
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet,testSet[x],k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted = ',repr(result),',actual = ',repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet,predictions)
    print('Accuracy:',repr(accuracy),"%")
main()