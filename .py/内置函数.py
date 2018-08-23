# 下次问题：递归函数
#能直接写完加（）的都是内置函数

# 内置函数
#     #作用域相关的
#     print(locals())     #返回本地作用域中的所有名字
#     print(globals())    #返回全局作用域中的所有名字
#     #与迭代器生成器相关
#     next('迭代器')
#     range(10)  #是可迭代的，但不是迭代器
#     #dir 查看一个变量所拥有的方法
#     #help  打印所有的方法
#     #callable
#     print(callable(print)) #查看函数是否能被调用
#某个方法属于某个数据类型的变量，则用  .调用
#若某个方法不依赖与任何数据类型，则可直接调用
# t = __import__('time')
# print(t.time())
    #open()
    #id
    #hash    对于相同可哈希数据的哈希值再一次程序的执行过程中总是不变的
# print(hash((1,2)))#可哈希
# print(hash([1,2]))#不可哈希
#哈希函数与字典的存储规则有关系（字典中的键转化为哈希值然后作为内存地址存储数据）

    # input()
    # print()   \n是回车
# print('我','们的祖国是花园',sep = '| ',end = '')

# import time
# for i in range(0,101,2):
#     time.sleep(0.1)
#     char_num = i//2
#     per_str = '\r%s%%:%s\n' % (i,'*'*char_num) \
#         if i == 100 else '\r%s%%:%s'%(i,'*'*char_num)
#     print(per_str,end = '',flush=True)
# #progress Bar  #进度条模块

#exec与eval
# exec('print(123)')
# eval('print(123)')
# print(exec('1+2+3'))
# print(eval('1+2+3'))
#exec和eval都可以执行字符串类型的代码
# eval 有返回值 ——有结果的简单计算
# exec 没有返回值——简单流程控制
#eval只能用在你明确知道要执行的代码是什么

# code = '''for i in range(10):
#     print(i*'*')'''
# exec(code)

    #compile()
# code = 'for i in range(10):print(i)'
# compile1 = compile(code,'','exec')
# exec(compile1)

# code = '1+8+9+999'
# compile1 = compile(code,'','eval')
# print(eval(compile1))

# code = 'name = input("please input your name:")'
# compile1 = compile(code,'','single')
# exec(compile1)
# print(name)    #ptcharm不是万能的 傻逼编译器

    #进制转换
# print(bin(10))   #0b代表二进制
# print(oct(10))    #0o代表8进制
# print(hex(10))     #0x代表16进制

    #数学运算
# print(abs(-7))
# print(divmod(7,3))   #除余运算
# print(divmod(6,3))
# print(round(3.1415926535897,3))
# print(pow(3,3))  #求幂
# print(pow(3,3,5))  #求完幂求余

    #reversed()
# l = [1,2,3,4,5]
# l.reverse()
# l2 = reversed(l)
# print(l,l2)
#reversed()是个迭代器
#保留原列表，返回一个反向迭代器

    #slice
# l = (1,2,23,213,5612,342,43)
# sli = slice(1,5,2)
# print(l[sli])
# print(l[1:5:2])

    #format
# print(format('text','>20'))
# print(format('text','<40'))

    #bytes
#我拿到gbk编码时，我想转换成utf-8
# print(bytes('你好',encoding="gbk"))
# print(bytes('你好',encoding='utf-8'))    #unicode 转化为utf-8

#网络编程 只能传二进制
#照片和视频也只能以二进制储存
#HTML网页爬取的也是编码
# b_array = bytearray('你好',encoding='utf-8')
# print(b_array)
# print(b_array[0])
# '''\xe4\xbd\xa0\xe5\xa5\xbd'''

# l = 'alfjdksahkfdsnakfdsklajfklds'
# l[:10]   #每次切片都在内存中存一次
#memoryview  字节类型的切片  不占内存

# print(ord('a'))   #转化为Unicode编码
# print(ord('我'))
# print(ascii('啊'))   #转化为ASCII码

# name = 'jaye'
# print('你好%s'%name)
# print('你好%r'%name)
# print(str('1'))
# print(repr('1'))

#集合set 、frozenset(不变集合)

###############################################################################
########################################################################################
#############################################################################################
#################################################################################################
#重要方法：
# print(all(['a',123]))
# print(all(['a','',123]))
# print(all([0,123]))
#
# print(any([1,0,'a']))
# print(any([0,0,'']))
# print(any(['',1]))

#zip拉进元组
# l = [1,2,3]
# l2 = ['a','b','c','d']
# print(zip(l,l2))
# for i in zip(l,l2):
#     print(i)
# l3 = ('*','**',[1,4])
# for i in zip(l,l2,l3):
#     print(i)
# d = {'k1':1,'k2':2}
# for i in zip(l,l2,l3,d):
#     print(i)

#filter    过滤函数  对后边可迭代数据进行判断
# def is_odd(x):
#     return x%2 ==1
# ret = filter(is_odd,[1,4,6,7,9,12,17])   #只能传进去一个函数名字
# print(ret)     #迭代器
# for i in ret:
#     print(i)
# #等价于
# a = (i for i in [1,4,6,7,9,12,17] if i%2==1)
# for i in a:
#     print(i)

#过滤字符串：
# def no_str(x):
#         return type(x) == str
# a = filter(no_str,[1,'5','fhsdka',9,80])
# for i in a:
#     print(i)

##可以用filter函数删除none或者空字符串
# def delete_blank(s):
#     return s and str(s).strip()
# r = filter(delete_blank,[1,'kdjklfjaios','   ',None,'','ok'])
# for i in r:
#     print(i)

#过滤从1到1000中平方根是整数的数
# def sp(x):
#     for i in range(1000):
#         if x == i**2:
#             return x
#         else:pass
# r = filter(sp,[i for i in range(1000)])
# for i in r:
#     print(i)

#  map   筛选后值变了
# r = map(abs,[1,-4,-8,9])
# for i in r:
#     print(i)

##########################比较：
#filter  执行了filter之后的结果的集合<=执行之前的个数
    #filter只管筛选，不改变原来的值
#map   执行前后元素个数不变
    #值可能会发生改变

#sorted 生成了一个新列表 占用了新的内存空间
# l = [1,-4,6,5,8]
# l.sort()       #在原列表的基础上进行排序
# print(l)
# l.sort(key = abs)  #根据绝对值对原列表排序
# print(l)

# print(sorted(l,key = abs,teverse = True))
# print(l)

#按照元素的长度排序
# l = ['   ',[1,2],'hello world']
# new_1 = sorted(l,key = len)
# print(new_1)

