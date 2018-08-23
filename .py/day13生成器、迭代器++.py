#迭代器
    #可迭代协议：含有iter方法
    #迭代器协议：含有next和iter方法
    #特点：
        #节省内存空间
        #方便逐个取值，一个迭代器只能取一次
#生成器
    #生成器函数
        #含有yield关键字的都是生成器函数
        #生成器函数的特点
            #调用之后不执行，返回生成器
            #每次从生成器中取出一个值就执行一段代码，遇见yield停止
            #如何从生成器中取值：
                #for：若果没有break会一直取
                #next：每次只娶一个
                #send：用在第一个只能传none，去一下个值是给上个位置传一个新值
                #数据类型强制转换：会一次性把所有值都读进内存
        #生成器表达式：
            #（条件成立后想放在生成器中的值 for i in 生成器 判断）

# def generator():
#     print(123)
#     k = yield 1
#     print(k)
#     print(456)
#     yield 2
#     print(789)
#
# r = generator()
# b = r.__next__()
# print('***',b)
# b = r.send('hello')
# print('***',b)


#列表推到式
# egg_list = ['鸡蛋%s'%i for i in range(10)]
# print(egg_list)

# e = [i**3 for i in range(10)]
# print(e)

# g = (i for i in range(10))
# print(g)     #g 是个生成器
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# 老母鸡 = (蛋 for 蛋 in range(10))
# print(next(老母鸡))
# print(next(老母鸡))
# print(next(老母鸡))
# print(next(老母鸡))

#各种推导式
#1 列表推导式           可以直接变成生成器表达式
        #[每个元素或者和元素相关的操作 for 元素 in 可迭代数据类型]   #遍历后挨个处理
        #[满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]   #筛选功能
# a = [x for x in range(30) if x%3 == 0]
# print(a)
#
# b = [x**2 for x in range(30) if x%3 == 0]
# print(b)
#嵌套列表的循环
# name = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],
#      ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
# c = [name for list in name for name in list if name.count('e') == 2]
# #那些名字，name中的list中的name，满足name中的e有俩个
# print(c)

#2 字典推到式
#① 将字典的键与值对调
# mcase = {'a':10,'b':34}
# mcase_frequency = {mcase[k]:k for k in mcase}
# print(mcase_frequency)
#②合并大小写(大写化小写，有值加起来)
# mcase = {'a':10,'b':34,'A':7,'Z':3}
# mcase_frequency = {k.lower():mcase.get(k.lower(),0)+mcase.get(k.upper(),0) for k in mcase}
# print(mcase_frequency)

#3 集合推导式    与列表推导式相同，自带去重功能
# a = {x**2 for x in range(30) if x%3 == 0}
# print(a)


#各种推导式    生成器 列表 字典 集合
    #遍历操作
    #筛选操作


#生成器与迭代器都是进行惰性运算
#生成器中的数据只能取一次

#处理文件，用户指定要查找的文件和内容，将文件中包括要查找内容的每一行都输出到屏幕
def check_file(filename,aim):
    with open(filename,'r',encoding='utf-8') as f:     #句柄:handler
        for i in f:
            if aim in i:
                yield i
g = check_file('log','大')
for i in g:
    print(i.strip())