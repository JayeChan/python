# K nearst neighbor  KNN算法  k邻近规则分类算法
# import math
# def ComputeEuclideanDistance(x1,y1,x2,y2):
#     d = math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
#     return d
# d_ag = ComputeEuclideanDistance(3,104,18,90)
# d_bg = ComputeEuclideanDistance(2,100,18,90)
# d_cg = ComputeEuclideanDistance(1,81,18,90)
# d_dg = ComputeEuclideanDistance(101,10,18,90)
# d_eg = ComputeEuclideanDistance(99,5,18,90)
# d_fg = ComputeEuclideanDistance(98,2,18,90)
# print("d_ag:",d_ag)
# print("d_bg:",d_bg)
# print("d_cg:",d_cg)
# print("d_dg:",d_dg)
# print("d_eg:",d_eg)
# print("d_fg:",d_fg)

#算法优缺点
#简单、容易实现、对K的选择可具备丢噪音数据的鲁棒性（降噪性）
#需要大量空间储存已知实例
#当样本分布不均匀时，例如其中一类样本密度大，新的位置实例易被归类为密度大的主导样本中

#改进：考虑距离，根据距离加上权重

###应用：  官方方法，也可自行改用
from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

print(iris)
knn.fit(iris.data,iris.target)    #传入参数，iris.data是150×4矩阵，iris.target是1维数组

predictedLabel = knn.predict([[2,2.6,2,4]])    #输入需要预测的数据
print(predictedLabel)                        #输出为第二类花versicolor