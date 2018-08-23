#装饰器进阶
    #functools.wraps
    #带参数的装饰器
    #多个装饰器装饰的同个函数
#装饰器
#原则：开放封闭原则
#作用:在不改变原函数的调用方式的情况下，在函数的前后添加功能
#装饰器的本质：闭包函数

#装饰器的基本格式：           #列出实现步骤
import time
# def wrapper(f):                   #第一步 开辟wrapper函数的内存
#     def inner(*args,**kwargs):    #第三步 局部命名空间中开辟inner函数
#         print('装饰之前')         #第六步
#         '''装饰之前干活'''
#         ret = f(*args,**kwargs)   #第七步 去下边找fucker函数
#         '''装饰之后干活'''
#         print('装饰之后')         #第八步
#         return ret                #第九步  返回ret值给a
#     return inner                 #第四步 返回inner的内存地址
# @wrapper        #fucker=wrapper（fucker）“fucker被wrapper装饰了” 第二步，fucker带进wrapper中
# def fucker(a):                   #第七步 inner中执行原fucker函数
#     print('fucking了%s天'%a)
# a = fucker(1)                   #第五步 fucker调用inner，变成inner（1）
# print(a)                        #第十步 打印a
# print(fucker.__name__)    #实际上fucker函数已经调用inner去了



#参数问题
# def outer(*args,**kwargs):
#     print(args)
#     print(*args)
#     def inner(*args):
#         print('inner:',args)
#     inner(*args)
# #等价
# outer(1,2,3,4)
# outer(*[1,2,3,4])
# outer(*(1,2,3,4))


# def wahaha():
#     '''
#     一个打印娃哈哈的文档
#     :return:
#     '''
#     print('娃哈哈')
# print(wahaha.__name__)#查看字符串格式的函数名
# print(wahaha.__doc__) #查看函数的注释

# 运用——登录检测：
# user,pw='alex','123456'
# login_status = False
# def login():
#     if login_status == False:
#         if auth_type =="jingdong"
#             username = input()
#             password = input()
#             if user == username and pw == password:
#                 print('welcome to ...')
#                 home()
#                 login_status = True
#         elif auth_type =="weixin"
#             ...
#     else:
#         pass
# @login(auth_type = 'jingodng')
# def home():
#     print('welcome to home page')
# @login(auth_type = 'weixin')
# def finance():
#     print('welcome to home page')
# @login(auth_type = 'jingodng')
# def book():
#     print('welcome to home page')

#装饰器函数加参数：
# def time_logger(flag = 0):
#     def show_time(f):
#         def wrapper(*args,**kwargs):
#             start = time.time()
#             f(*args,**kwargs)
#             end = time.time()
#             print('执行时间=',end-start)
#
#             if flag:
#                 print('将这个操作时间记录到日志中')
#         return wrapper
#     return show_time
# @time_logger(3)
# def add(*args,**kwargs):
#     time.sleep(1)
#     sum = 0
#     for i in args:
#         sum+=1
#     print(sum)
# add(2,7,8)

#生成器：#是一个可迭代对象
    #列表生成式：
    # def f(n):
    #     return n**3
    # a = [f(x) for x in range(10)]
    # print(a)
# s = (x*2 for x in range(3))
# print(s)   #生成器(没有值，只拿到了对象(类比于厨师))
# print(s.__next__())  #等价于
# print(next(s))
# print(next(s))
   #迭代结束
#生成器只能一个一个输出

# for i in s:   #for 循环默认调用next函数
#     print(i)

#生成器一共两种创建方式：
#1：（x*2 for x in range(10)）
#2：yield
#yield 生成器对象
# def foo():
#     print('ok')
#     yield 1
#     print('ok2')
#     yield 2
# print(foo())
# g = foo()
# print(next(g))         #next(g)的返回值是1  看做（yield是返回的意思）！！！
# next(g)
# #迭代结束
#
# for i in foo():
#     print(i)



#什么是可迭代对象(对象有__iter__方法的）
# l = [1,2,3]
# l.__iter__()
# t = (1,2,3)
# t.__iter__()
# d = {'name':'123'}
# d.__iter__()

#斐波那契数列  0 1 1 2 3 5 8 13 21
# def fib(max):
#     i = 1
#     n,before,after = 0,0,1
#     while i<max:
#         print(after)
#         n = before
#         before = after
#         after = n + before
#         i += 1
# fib(10)
#生成器生成菲波那切数列
# def fib(max):
#     n,before,after = 0,0,1
#     while n<max:
#         # print(before)
#         yield before
#         before,after = after,before+after
#         n = n+1
# g = fib(8)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


#yield 的断续重连功能是最重要的一个功能
# def bar():
#     print('ok1')
#     count = yield 1
#     print(count)
#     yield 2
# b = bar()
# s = b.send(None)   # = next(b)  第一次send如果前边没有next 就只能传一个send（none）
#
# c = b.send('eee')  #给yield 1 传值
# print(c)

###迭代器
        #list,tuple,dict,string:Iterable
    #生成器都是迭代器，迭代器不都是生成器
# l = [1,2,3,5]
# d = iter(l)    #l.__lter__()
# print(d)
#迭代器满足两个条件：1 有iter方法  2 有next方法
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
#可把可迭代对象变成迭代器

#for循环内部三件事：
#1 调用可迭代对象的iter方法返回一个迭代器对象
#2 调用迭代器的next方法
#3 处理StopIteration异常
# for i in [1,2,34]:
#     iter([1,2,34])

# from collections import  Iterator,Iterable
#
# print(isinstance(2,list))
# l = [1,2,3,5]
# d = iter(l)    #l.__lter__()
# print(d)
# print(isinstance(l,Iterable))
# print(isinstance(l,Iterator))
# print(isinstance(d,Iterator))




## 练 习 1   使用文件读取，找出文件最长的行
# max(len(x.strip()) for x in open('/.py/log','r'))


#
# def add(a,x):
#     return a+x
#
# def gen():
#     for i in range(4):
#         yield i
#
# base = gen()
# for n in [1,10]:
#     base = (add(i,n) for i in base)
#
# print(list(base))