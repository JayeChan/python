# def qqxing(l = []):
#     l.append(1)
#     print(l)
# qqxing()
# qqxing([])
# qqxing()

#函数的进阶
#
# a = 1
# def func():
#     print(a)
# func()

#命名空间和作用域
#全局命名空间：  ——自己写的代码
    #在程序从上到下被执行时才被加载进内存的
    #放置了我们设置的所有变量名和函数
#局部命名空间：   ——函数
    #函数内部定义的名字
    #当调用时候才会产生这个空间，并且随着函数执行结束而消失
#内置命名空间：  ——python解释器
    #python解释器内置的函数就存储在内置命名空间
    #内置的名字在启动解释器的时候被加载进内存


#在局部：可以使用全局、内置命名空间的名称
#在全局：可以使用内置命名空间中的名称
#在内置：不可以使用全局和局部命名空间

# def max():
#     print('in a a a ')
# max()

#正常情况下，直接用内置命名空间中的变量
#但我们在全局定义了和内置命名空间中相同的变量时，会只用全局的变量

#函数名去掉括号指向函数名被储存的内存地址
#函数内存地址+（）使得函数被执行
#局部命名空间中的函数互不共享


#作用域
#全局作用域 ——作用在全局——内置和全局命名空间中的变量都属于全局命名空间
#局部作用域 ——作用在局部——函数

#对于不可变数据类型，在局部可查看全局作用域中的变量，若需要修改，需要把全局变量带入
#做在一个局部声明了global变量，那么这个变量在局部的操作对于全局有影响
# a = 1
# def func():
#     global a
#     a +=1
#     print(a)
# func()
# a = 1
# b = 2
# def func():
#     x ='aaa'
#     y ='bbb'
#     print(locals())    #查询到局部作用域中的变量
# # func()
# print(globals())         #还可以看到内置中的变量名
# print(locals())          #在全局中放则展示全局的变量，局部展示局部

#globals 永远使用全局的名字
#locals  只展示locals所在的变量名字

#应该尽量避免使用globals（因为很危险)，可以通过传参和接受返回值等方法替代用globals


#函数的嵌套调用

#函数的嵌套定义
# a = 1
# def outer():
#     a = 1
#     def inner():
#         b = 2
#         print('outer中的局部变量a=',a)
#         print('inner')
#         def inner2():
#             global a    #声明一个全局变量
#             a += 1     #不可变数据类型的修改
#             print('inner2里的全局变量a和inner中的局部变量b等于：',a,b)
#         inner2()
#     inner()
#     print('outer中的局部变量a=',a)    #outer里边的局部变量，没有变成2
# outer()
# print('全局变量a=',a)

##nonlocal  声明一个上层的局部变量，找上层中离此函数最近一层的局部变量
# a = 1
# def outer():
#     a = 1
#     def inner():
#         b = 2
#         print('outer中的局部变量a=',a)
#         print('inner')
#         def inner2():
#             nonlocal a    #声明上层的一个局部变量
#             a += 1     #不可变数据类型的修改
#             print('inner2里的全局变量a和inner中的局部变量b等于：',a,b)
#         inner2()
#     inner()
#     print('outer中的局部变量a=',a)    #outer里边的局部变量，没有变成2
# outer()
# print('全局变量a=',a)

# def func():
#     print(123)
# # func()    #函数名就是内存地址
# # func2 = func   #内存地址可以传递
# # func2()
# #函数名可以作为容器类型的变量
#
# def 娃哈哈(f):  #f 代表某一函数的内存地址
#     f()
#     return f    #函数名可以作为返回值
# 娃哈哈(func)   #函数名（函数的内存地址）可以作为函数的参数
# qqxing =print( 娃哈哈(func))   #传出的内存地址


#第一类对象：（函数名是一个第一类对象）
#1、可以在运行期创建     2、可以做函数参数或返回值   3、可以存入变量的实体

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#闭包:嵌套函数，内部函数调用外部函数的变量
# def outer():
#     a = 1
#     def inner():
#         print(a)
#     print(inner.__closure__)
# outer()   #返回中若有cell。。。 就说明此函数是个闭包

# def outer():
#     a = 1
#     def inner():
#         print(a)
#     return  inner
# inn = outer()
# inn()   #在外部使用inner（）函数,且使用了inn后outer中的局部变量不会消失

from urllib.request import urlopen    #模块
# ret = urlopen('http://www.tom97.com/').read()
# print(ret)

# def get_url(web):
#     ret = urlopen(web).read()
#     print(ret)
# get_url('http://www.tom97.com/')
def get_url():
    url = input('请输入您要查看的网址：')
    def get():
        ret = urlopen(url).read()
        print(ret)
    return get()
get_func = get_url()
get_url()
##闭包的好处：每次调用内部函数的时候不需要生成外部变量