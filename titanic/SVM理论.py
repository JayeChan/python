#机器学习的一般框架
#训练集-->提取特征向量-->用一定的算法进行学习-->得到结果
#寻找超平面使得边际最大化
#线性可区分
#例子（小数据集进行预测）
# from sklearn import svm
#
# X = [[2,0],[1,1],[2,3]]   #三个点
# y = [0,0,1]     #点的分类
# clf = svm.SVC(kernel = 'linear')   #线性核函数
# clf.fit(X,y)
#
# print(clf)   #打印分类器
#
# print(clf.support_vectors_)#支持向量是谁
#
# print(clf.support_)      #拿下标 (后两个点)
#
# print(clf.n_support_)    #每个类分别找到几个支持向量（0下边一个，1上边一个）
#
# #新点预测：
# print(clf.predict([[2,1]]))     #属于零那边


#例子（大数据集）
import numpy as np
import pylab as pl
from  sklearn import svm

np.random.seed(0)   #随机抓点且抓出固定住
X = np.r_[np.random.randn(20,2) - [2,2],np.random.randn(20,2) + [2,2]] #产生20个点，每个点是2维的，且点都属于正态分布
Y = [0]*20+[1]*20

#构建SVM模型
clf = svm.SVC(kernel='linear')
clf.fit(X,Y)

#找出超平面 (二维直接用公式写出)
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5,5)
yy = a*xx-(clf.intercept_[0])/w[1]

b = clf.support_vectors_[0]
yy_down = a*xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

print('w=',w)
print('a=',a)
print('support_vectors :',clf.support_vectors_)
print('clf.coef_ :',clf.coef_)

pl.plot(xx,yy,'k--')
pl.plot(xx,yy_down,'k--')
pl.plot(xx,yy_up,'k--')

pl.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],s = 80,facecolors = 'none')
pl.scatter(X[:,0],X[:,1],c = Y,cmap = pl.cm.Paired)

pl.axis('tight')
pl.show()
