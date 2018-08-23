# def demo():
#     for i in range(4):
#         yield i
# g = demo()
#
# g1 = (i for i in g)
# g2 = (i for i in g1)
#
# print(list(g))          #取完了所有值
# print(list(g1))
# print(list(g2))



#生成器之难题
# def add(n,i):
#     return n+i
# def test():     #生成器函数
#     for i in range(4):
#         yield i
# g = test()      #生成器对象
# for n in [1,10]:
#     g = (add(n,i) for i in g)      #生成器表达式，不取则不干活
# #开始执行
# # n = 1
# # g = (add(n,i) for i in g)
# # n = 10
# # g = (add(n,i) for i in (add(n,i) for i in test()))
# #故只执行上一行代码
# print(list(g))

def add(n,i):
    return n+i
def test():
    for i in range(4):
        yield i
g = test()
for n in [1,10,5]:
    g = (add(n,i) for i in g)
print(list(g))
