#匿名函数  lambda
# def calc(n):
#     return n**n
# print(calc(10))

# add = lambda x,y:x+y
# print(add(9,19))

# dic = {'k1':10,'k2':100,'k3':30}
# print(max(dic,key=lambda k:dic[k]))

###max min filter map sorted  都可以用lambda简化之



##练习：
#匿名函数  找与key有关的
# ret = zip((('a'),('b')),(('c'),('d')))
# # def func(tup):
# #     return {tup[0]:tup[1]}
# # res = map(func,ret)
# res = map(lambda tup:{tup[0]:tup[1]},ret)
# print(list(res))
# #一句话：
# print(list(map(lambda tup:{tup[0]:tup[1]},zip((('a'),('b')),(('c'),('d'))))))

#以下代码的输出：
def multipliers():
    return [lambda x:i*x for i in range(4)]
print([m(2) for m in multipliers()])

def multipliers():
    return (lambda x:i*x for i in range(4))
print([m(2) for m in multipliers()])
