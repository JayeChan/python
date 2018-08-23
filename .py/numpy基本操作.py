import numpy as np
# a = [1,2,3,4]
# b = np.array(a)
# print(b.size)
# print(b.shape)
# print(b.ndim)
# print(b.dtype)

# array_1 = np.ones([10,10])
# array_0 = np.zeros([10,10])
# print(array_0,array_1)

#均匀分布
# print(np.random.rand(10,10))
# print(np.random.uniform(0,100))
# print(np.random.randint(0,100))

#正态分布
# print(np.random.normal(1.75,0.1,(2,3)))
# a = np.random.normal(0,1,(5,6))
# print('正态分布随机生成5函6列数组：',a)
# xiaoa = a[2:5,4:6]
# print('切数组中第3到5行、5到6列成矩阵：',xiaoa)
#
# b = xiaoa.reshape([2,3])
# print('重新排列为2×3矩阵：',b)


# Numpy的计算：
    #条件运算
# score = np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
# print(score >80)
# t = np.where(score <85,'不合格','凑合')   #三目运算 当值小于80 则用0 替换，否则用90 替换
# print(t)
    #统计运算
# stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一列的最大值(0表示列)   每个小列表为行向量
# print("每一列的最大值为:")
# result = np.amax(stus_score, axis=0)     ！！#amin最小值  mean均值  std方差
# print(result)
#
# print("每一行的最大值为:")
# result = np.amax(stus_score, axis=1)
# print(result)

#数组与数的运算
# stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# print("加分前:")
# print(stus_score)
# # 为所有平时成绩都加5分
# stus_score[:, 0] = stus_score[:, 0]+5        #0代表第一列，1代表第二列
# print("加分后:")
# print(stus_score)

#向量对应位置相加减
# a = np.array([1, 2, 3, 4])
# b = np.array([10, 20, 30, 40])
# c = a + b
# d = a - b
# e = a * b
# f = a / b
# print("a+b为", c)
# print("a-b为", d)
# print("a*b为", e)
# print("a/b为", f)

#矩阵运算
# stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])   #5行2列矩阵
# # 平时成绩占40% 期末成绩占60%, 计算结果
# q = np.array([[0.4], [0.6]])        #2行1列矩阵
# result = np.dot(stus_score, q)
# print("最终结果为:\n",result)

#矩阵拼接
# print("v1为:")
# v1 = [[0, 1, 2, 3, 4, 5],
#       [6, 7, 8, 9, 10, 11]]
# print(v1)
# print("v2为:")
# v2 = [[12, 13, 14, 15, 16, 17],
#       [18, 19, 20, 21, 22, 23]]
# print(v2)
# # 垂直拼接
# result = np.vstack((v1, v2))   #result = np.hstack((v1, v2))  水平拼接
# print("v1和v2垂直拼接的结果为")
# print(result)

##读取csv数据：
#genformtxt
# result = np.genfromtxt("C:\\Users\\陈曌宇\\Desktop\\生物学数据\\data-40.csv",delimiter=',')
# print(result)
#如果数值据有无法识别的值出现,会以nan显示,nan相当于np.nan,为float类型.