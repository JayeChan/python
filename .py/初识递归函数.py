#递归函数：
    #了解什么是递归
    #能看懂递归
    #能知道应用场景
# def story():
#     print('从前有座山')
#     story()
#     print('111')    #永远到不了这一步
# story()
#从函数中调用自己，就是递归
#RecursionError递归错误，maximum recursion depth exceeded 超过了最大递归深度
# n = 0
# def func():
#     global n
#     n += 1
#     print(n)
#     func()
# func()
##递归的最大深度为998   从内存角度出发作出的限制

# import sys
# sys.setrecursionlimit(1000000)  #更改最大深度限制
# n = 0
# def func():
#     global n
#     n += 1
#     print(n)
#     func()
# func()

#如果需要递归次数太多，就不适合用递归来解决问题
#递归缺点：占内存
#递归优点：让代码变简单

#与数学递归函数类似
#递归从结果出发，倒叙找到原因
#迭代的思想
#例：age(n) = age(n+1) + 2 , age(4)=40
# def age(n):
#     if n == 4:
#         return 40
#     elif   n>0 and n<4:
#         return age(n+1)+2
# print(age(1))
#谁调用返回给谁



#算法
#查找：找数据
#排序：
#最短路径问题：

#二分查找算法
#如何查找66的位置
# def find(l,aim,start = 0,end = None):
#     end = len(l) if end is None else end
#     if start>end:
#         print('找不到所求值')
#     else:
#         mid_index = (end-start)//2 + start
#         if l[mid_index] < aim:
#             return find(l,aim,start = mid_index+1,end = end)
#         elif l[mid_index] > aim:
#             return find(l, aim, start=start, end=mid_index - 1)
#         else:
#             return mid_index
# l = [2,6,3,8,34,25,68,345,654,23,78,454,3,9,90,99,67,44,33,25,68,9,0]
# l.sort()
# a = find(l,67)
# print(a)
#层层返回的问题


###三级菜单的代码看一遍
#斐波那契数列问题     第n个菲薄那些数列是多少
#阶乘
# def find(l,dim,start = 0,end = None):
#     end = len(l) if end is None else end
#     if start > end:
#         print('找不到该值')
#     else:
#         mid_index = (end - start)//2 + start
#         if l[mid_index] < dim:
#             return find(l,dim,start = mid_index+1 ,end = end)
#         elif l[mid_index] > dim:
#             return find(l,dim,start = start,end = mid_index-1 )
#         else:
#             return mid_index
# l = [2,6,3,8,34,25,68,345,654,23,78,454,3,9,90,99,67,44,33,25,68,9,0]
# l.sort()
# a = find(l,345)
# print(a)


#斐波那契数列：
#a1=1 a2=1 a3=2 a4=3 a5=5 a6=8 an =  a(n-1)+a(n-2)
#要输出an = ？
# def f(n):
#     if n == 1:
#         return 1
#     elif n==2:
#         return 1
#     elif n>=3:
#         return f(n-1)+f(n-2)
# a = f(30)
# print(a)

#阶乘：
# def j(n):
#     if n == 1:
#         return 1
#     elif n>=1:
#         return j(n-1)*n
# a = j(4)
# print(a)

#注：
#递归函数1、必须要有结束条件
# 2、不要只看return就结束，要看返回操作是在递归的第几层结束的
# 3、如果不是返回给最外层函数，调用者接受不到
# 4、几乎所有的递归都可以用循环解决

