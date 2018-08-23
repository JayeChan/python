# f = open('课程周期',mode='w+',encoding='utf-8')
# f.write('课程周期：''\n'
#         'python基础   2个月''\n'
#         '数据库：增删改查   1-2周''\n'
#         '前端     2周''\n'
#         '框架：django      2个月')
# f.seek(0)
# print(f.read())
# f.close()

# f = open('python基础',mode='w+',encoding='utf-8')
# f.write('课程周期：''\n'
#         '函数   2周''\n'
#         '面向对象和模块   2周''\n'
#         '网络编程     1周''\n'
#         '并发编程      1周')
# f.seek(0)
# print(f.read())
# f.close()

#修改文件信息（删除+替换）
# with open('小护士班主任',encoding='utf-8') as f,open('小护士班主任.bak','w',encoding = 'utf-8') as f2:
#     for line in f:
#         if '信儿' in line:
#             line = line.replace('信儿','结衣')   #用结衣代替信儿
#         f2.write(line)      #写入f2中
#
# import os
# os.remove('小护士班主任')     #删除文件
# os.rename('小护士班主任.bak','小护士班主任')  #修改文件名字

#函数
# s = '金老板小护士'
# def my_len():   #声明函数
#     i = 0
#     for k in s:
#         i += 1
#     return i     #返回值
#
# a = my_len()   #调用
# print(a)

# def func():
#     l = ['金老板','二哥']
#     for i in l:
#         print(i)
#     return  None        #(return\return none\不写，都一样是返回空值)   只写是结束本函数
#     print('我爸是李刚')   #return后边不执行
# ret = func()
# print(ret)

#返回值定下之后不能更改
# def func():
#     return {'k':'v'}
# k = '我爱你'
# v = '猪猪'              #做不了任何更改
# print(func())

#多个返回值用多个变量接收
# def func2():
#     return 1,2
# r1,r2 = func2()
# print(r1,r2)
#
# def func3():
#     return 1,2,3
# r = func3()
# print(r)

#含参变量
# def my_len(s):
#     i = 0
#     for k in s:
#         i += 1
#     return i
# a = my_len('我爱你中国，亲爱的母亲')
# print(a)

#互不影响
# def f1(l1):
#     for i in l1:
#         print(i)
# def f2(l1)
#     for i in l1:
#         print(i)

#参数
    #无参数
        #定义函数和调用函数时括号里都不写
    #有一个参数
        #传什么就是什么
    #有多个参数

# def my_sum(a,b):
#     res = a+b
#     return res
# a = my_sum(1,7)
# print(a)

# def classmate(name,sex = '男'):    #默认参数sex为男
#     print("%s:%s"%(name,sex))
# classmate('二哥')
# classmate('小孟')
# classmate('大孟')
# classmate('懒个','女')

# def classmate(name,sex):
#     print("%s:%s" % (name, sex))
# classmate('二哥','男')
# classmate(sex = '男',name ='傻逼')

#定义时，
# 位置参数：直接定义参数
#默认参数，关键字参数：参数名 = ‘默认值’
#动态参数:可以接受任意多个参数，前边加*
#顺序：必须先定义位置参数，接下来*args，后定义默认参数

# def sum(a,b,c=0):
#     pass
# sum(1,2)
# sum(1,2,3)

#动态参数：  (一般情况下动态参数就用args
# def sum(*args):
#     n = 0
#     for i in args:
#         n += 1
#     return n
# print(sum(1,2,3,4,5,8)

# def func(*args,l=[]):
#     print(args,l)
# func(1,2,'str',['list',1])
# func(1,2,'str',l =['list',1])

