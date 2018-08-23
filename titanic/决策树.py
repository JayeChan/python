#decision tree
#机器学习中分类和预测算法的评估：
#准确率
#速度
#鲁棒性
#可规模性
#可解释性
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

allElectronicsData = open(r'F:\BaiduNetdiskDownload\第04阶段-机器学习深度学习篇-1-基础进阶强化-9G\第一阶段-深度学习基础\代码与素材(1)\01DTree\AllElectronics.csv','r+',encoding='utf-8')
reader = csv.reader(allElectronicsData)
headers = next(reader)

print(headers)

featureList = []
lableList = []

for row in reader:  #遍历每一行
    lableList.append(row[len(row)-1])  #取每行最后一个值
    rowDict = {}
    for i in range(1,len(row)-1):
        rowDict[headers[i]] = row[i]   #每行（每个人）标题对应的值加入字典中（{年纪：年轻,信用：良好,...}）
    featureList.append(rowDict)        #所有的字典（每个人的信息）放入列表中
print(featureList)

#向量化列字典中的特征Vetorize feature
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print('dummyX:',str(dummyX))
print(vec.get_feature_names())
print('labelList:',str(lableList))

#向量化类标签：vectorize labels  切记是用   preprocessing.LabelBinarizer
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(lableList)
print('dummy:',str(dummyY))

#创建决策树  criterion不做任何规定则用CART方法
clf = tree.DecisionTreeClassifier(criterion = 'entropy')    #用entropy是采用ID3方法
clf = clf.fit(dummyX,dummyY)
print('clf:',str(clf))

#可视化决策树
with open('allElectronicsInformationGainDri.dot','w') as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f) #画决策树时候，我们得把特征名返回为原来的英文名


#开始预测
oneRowX = dummyX[0,:]
print('oneRowX',str(oneRowX))

newRowX = oneRowX              #创建个新的向量
newRowX[0] = 1
newRowX[2] = 0
print('newRowX:',str(newRowX))

predictedY = clf.predict([newRowX])     #注意维数
print('predictedY :',predictedY)