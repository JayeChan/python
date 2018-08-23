#要点：找到超平面使得边界最大
#算法复杂度是由支持向量的个数决定的，不容易产生过拟合
#SVM完全依赖支持向量，即使非支持向量全都去掉，仍然可以得到相同的结果
#如果训练出的支持向量个数较少，SVM训练出的模型更容易泛化

#线性不可分：
#数据集在空间中对应的向量不可被一个超平面区分开
#将二维升为三维来找新的线性超平面来区分
#核方法：
# h 度多项式核函数
# 高斯径向基核函数
# S 型核函数
#通过核方法可以大量的降低算法复杂度


# SVM 拓展可以解决多个类别分类的问题
# 可以采用多加二类分类器的方式，增加我们的分类能力

#利用M进行人脸识别的实例：
from __future__ import print_function
from time import time
import logging
import matplotlib.pylab as plt

from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn import grid_search
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC

print(__doc__)

logging.basicConfig(level=logging.INFO,format = '%(asctime)s%(message)s')

#人脸数据：
lfw_people = fetch_lfw_people(min_faces_per_person = 70,resize=0.4) #下载人脸数据集

n_samples,h,w = lfw_people.images.shape

X = lfw_people.data
n_feature = X.shape[1]        #返回特征点的列数

y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print('数据的大小：')
print('n_samples:%d'% n_samples)
print('n_features:%d'% n_feature)
print('n_classes:%d'% n_classes)

#进行数据集的划分
# X_train,X_test,y_train,y_test = train_test_split(
#     X,y,test_size=0.25
# )
#
# n_components = 150
#
# print('Extracting the top %d eigenfaces from %d faces'
#       %(n_components,X_train.shape[0]))
# t0 = time()
# pca = RandomizedPCA(n_components = n_components,whiten=True).fit(X_train)
# print('Done in %0.3fs'%(time()-t0))
#
# eigenfaces = pca.components_.reshape((n_components,))