#基础版本的装饰器
#装饰器的形成过程
#装饰器的作用
#原则：开放封闭原则
#装饰器的固定模式
import time
#time.sleep(5)#让程序执行时候暂停5s
# def func():
#     print('你好呀')
# # func()
# def start_end(f):   #写出闭包是为了固定住func的内存地址于f中
#     def inner():
#             start = time.time()
#             f()
#             time.sleep(0.01)
#             end = time.time()
#             print(end-start)
#     return inner
# func = start_end(func)       #把inner返回到func地址中
# func()               #执行inner函数  其中f（）就是固定住的func（）

#重写


#添加计算时间的功能（装饰器函数）：
# def timmer(f):
#     def inner():
#         start = time.time()
#         r = f()       #被装饰函数
#         time.sleep(0.01)
#         end = time.time()
#         print(end - start)
#         return r     #加上了返回值
#     return inner
# @timmer#语法糖（让代码变得更简单）
# def func():
#     print('今天下三分，益州疲弊，此为危急存亡之秋也。')
#     return '新年好'
# # func = timmer(func)
# ret = func()      #inner()
# print(ret)


#装饰带参数函数的装饰器（被装饰函数）
# def timmer(f):    #装饰器函数
# #     def inner(*args,**kwargs):  #使得无论如何传参都可以
# #         start = time.time()
# #         r = f(*args,**kwargs)       #被装饰函数
# #         time.sleep(0.01)
# #         end = time.time()
# #         print(end - start)
# #         return r     #加上了返回值
# #     return inner
# # @timmer#语法糖（让代码变得更简单）
# # def func(*args,**kwargs):
# #     print('今天下三分，益州疲弊，此为危急存亡之秋也。',args)
# #     return '新年好'
# # # func = timmer(func)
# # ret = func(1,4,5,6)  #inner()
# # ret = func(1,a=3)
# # print(ret)
#原则：开放封闭原则
#1开放：对拓展是开放的     可以添加新功能（装饰器）
#2封闭：对修改是封闭的     不能轻易修改以前的代码
#封版
# def outer():
#     def inner():
#         return 'inner'
#     inner()
# outer()
# print(outer())



#装饰器格式
# def wrapper(f):      #装饰器函数，f是被装饰的函数
#     def inner(*args,**kwargs):
#         '''在被装饰函数之前要做什么'''
#         ret = f(*args,**kwargs)
#         """在被装饰函数之后要做什么"""
#         return ret
#     return inner
# @wrapper   #语法糖   等价于 func = wrapper(func)
# def func(a,b):     #被装饰的函数
#     time.sleep(0.01)
#     print('我被装饰了诶，我是最美滴')
#     return '我爱你'
# func()       #inner

