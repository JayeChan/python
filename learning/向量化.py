import numpy as np
r = np.arange(0.1,0.5,0.01)
# print(r)
# print(r[r>0.3])
# 向量r 的内积
# print(np.dot(r,r.T))
# print(np.dot(r.T,r))
# print(sum(r*r))

#数据集
from pandas import DataFrame
df = DataFrame(
    {
        'data1':np.random.randn(5),
        'data2':np.random.randn(5)
    }
)
a = df.apply(lambda x:min(x))
b = df.apply(lambda x:min(x),axis = 1)
print(a,b)

c = df.apply(lambda x:np.all(x>0),axis=1)
print(c)

