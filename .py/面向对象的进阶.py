#反射 *******非常非常重要    高级知识
# isinstance 和 issubclass
# __str 和 __repr__
# __del__
# item系列
#   __getitem__
#   __setitem__
#   __delitem__

# isinstance(obj,cls)检查是否obj是类cls的对象
# class A:pass
# a = A()
# print(isinstance(a,A))
# class B(A):pass
# b = B()
# print(isinstance(b,A))    #判断对象与类的关系
# print(issubclass(B,A))    #判断子类父类关系

# 反射：是用字符串类型的名字 去操作 变量
#   eval 是用字符串内容操作python代码
# 用eval会有 极大的安全隐患
# 用反射 并不会有安全隐患

# 反射对象中的属性和方法  #hasattr getattr setattr delattr
# class A:
#     def func(self):
#         print('in func')
# a = A()
# a.name = 'alex'
# 反射对象的属性
# ret = getattr(a,'name')  #通过变量名的字符串形式去到的值
# print(ret)
# 变量名 = input('>>>>')
# print(getattr(a,变量名))
# 反射对象的方法
# if hasattr(A,'price'):
#     getattr(a,'func')()
#模块
# import my
# #反射模块的属性
# # print(my.day)
# print(getattr(my,'day'))
# #反射模块的方法
# getattr(my,'wahaha')()

#内置模块也能用
# def qqxing():
#     print('qqxing')
# year = 2018
# #反射自己模块中的变量
# import sys
# # print(sys.modules)                          #查看所有导入的模块
# print(getattr(sys.modules[__name__],'year'))#反射自己模块中的变量
# 变量名 = input('>>>>')
# getattr(sys.modules[__name__],变量名)()      #反射自己模块中的函数

#setattr
# class A:
#     pass
# a = A()
# setattr(a,'name','nezha')
# setattr(A,'name','alex')
# # print(A.name)
# # print(a.name)
#
# #delattr
# delattr(a,'name')
# print(a.name)
# delattr(A,'name')
# print(a.name)           #删完了

# 类中的内置方法
# 内置的类方法 和 内置的函数之间有千丝万缕的联系
# 双下方法
# __str__
# __repr__
# print(repr('1'))    #原形毕露
# obj.__str__   == str(obj)
# obj.__repr__  == repr(obj)
# class A:
#     pass
# a = A()
# print(str(a))
#object 中有个__str__,一旦发生调用就返回调用跟这个方法的对象的内存地址
# class A:
#     def __str__(self):              #配置__str__方法 使得打印时调用
#         return "A's object"
# a = A()
# print(a)      #打印一个对象时候，都是调用a.__str__
# print('%s,%s'%('A',a))   # 配置了str方法后 不再返回内存地址
#######  %s   str()   直接打印  都是走的__str__方法

# class Teacher:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def __str__(self):
#         return "Teacher's object :%s"%self.name ######此处必须返回一个str类型
#     def __repr__(self):
#         return str(self.__dict__)
#     @property
#     def func(self):
#         return 'hhahaha'
# nezha = Teacher('哪吒',2000)
# print(nezha)
# print('>>>',str(nezha))
# print(repr(nezha))
# print('>>%r'%nezha)             #没有repr方法时，调用的是父类的repr

# a.__str__  ——> object
# l = [1,2,3]  之所以print可以看见是因为列表类内置了str方法
# repr是str的一个备胎
# str不是repr的备胎
# 如果没有__str__方法，会先找本类中的__repr__方法，在没有再找父类中的__str__方法、__repr__方法，最后找obj类中的__str__
# repr(),只会找__repr__，如果没有就找父类的
# 若只能用一个，我会用__repr__方法


# 内置的方法有很多，但不一定全在object中
# class A:pass
#     # def __len__(self):
#     #     return 10
# a = A()
# print(len(a))
# object of type 'A' has no len()     len方法在obj中不存在
# class Classes:
#     def __init__(self,name):
#         self.name = name
#         self.student = []
#     def __str__(self):
#         return print('obj is %s'%self.name)
#     def __len__(self):
#         return len(self.student)
# py_s9 = Classes('python全站')
# py_s9.student.append('alex')
# print(len(py_s9))      #不会调用str 因为只有在%s  %r  str（）或直接打印时候会调用


#__del__析构函数
# class A:
#     def __del__(self):            #析构函数  在删除对象之前 做一些收尾工作
#         self.f.close()
#         print('执行我了！')
# a = A()
# a.f = open('')   #打开文件 1在操作系统中打开一个文件 拿到了文件操作符存在内存中
# del a           #先关闭了f，a.f 的文件操作符消失了
                  #发现程序结束后会执行del方法
#引用计数


# __call__
# class A:
#     def __init__(self,name):
#         pass
#     def __call__(self):
#         print('执行我啦')
# a = A('alex')()
#一个对象加上（）相当于执行call方法


#item系列
# dic = {'k':'v'}
# class Foo:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __getitem__(self, item):
#         if hasattr(self,item):
#             return self.__dict__[item]
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#     def __delitem__(self, key):
#         del self.__dict__[key]
# f = Foo('egon',38,'男')
# print(f['name'])
# f['habby'] = '男'
# print(f.habby,f['habby'])
# del f['habby']
# print(f.__dict__)

 #  __init__ 是一个初始化方法
 # __new__构造方法:创建一个对象
# class A:
#     def __init__(self):
#         self.x = 1
#         print('in init function')
#     def __new__(cls, *args, **kwargs):
#         print('in new function')
#         return object.__new__(A,*args,**kwargs)
# a = A()
#先进行new方法 ，在进行init方法

# 设计模式
# 23种
# 单例模式： 一个类 始终只有一个实例
# 当你第一次实例化这个类的时候 就创建一个实例化对象
# 当你之后再来实例化时，就使用之前创建的对象
# class A:
#     __instance = False
#     def __init__(self,name,age):
#         self.name  = name
#         self.age = age
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance:
#             return cls.__instance
#         cls.__instance = object.__new__(A)
#         return cls.__instance
# egon = A('egg',38)
# egon.cloth = '大棉袄'
# nezha = A('nezha',25)
# print(nezha)
# print(egon)
# #内存地址一样
# print(nezha.name)
# print(egon.name)
# print(nezha.cloth)
                   # 只有一个对象

######__eq__方法

# class A:
#     def __init__(self,name):
#         self.name = name
#     def __eq__(self, other):
#         if self.name == other.name:
#             return  True
#         else:
#             return  False
# obj1 = A('egg')
# obj2 = A('egg')
# print(obj1 == obj2)   #  ==触发eq方法

#########__hash__方法
# class A:
#     def __init__(self,name):
#         self.name = name
# a = A('egon')
# b = A('egon')
# print(hash(a))
# print(hash(b))
#哈希值不同是因为是根据内存地址来哈希的
# class A:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#     def __hash__(self):   #自己定制的哈希函数
#         return hash(self.name+self.sex)
# a = A('egon','男')
# b = A('egon','男')
# print(hash(a))
# print(hash(b))
#哈希值相等了

# from collections import namedtuple
# Card = namedtuple('Card',['rank','suit'])    #只有属性没有方法的类
# # c1 = Card(2,'红心')
# # print(c1)
# # print(c1.suit)
# import json
# class FranchDeck:
#     ranks = [str(n) for n in range(2,11)]+list('JQKA')  #2-A
#     suits = ['红心','方片','梅花','黑桃']
#
#     def __init__(self):
#         self._cards = [Card(rank,suit) for rank in FranchDeck.ranks
#                                         for suit in FranchDeck.suits]
#     def __len__(self):
#         return len(self._cards)
#     def __getitem__(self, item):
#         return self._cards[item]
#     def __setitem__(self, key, value):
#         self._cards[key] = value
#     def __str__(self):
#         return json.dumps(self._cards,ensure_ascii=False)
# deck = FranchDeck()
# print(deck[10])    #由于getitem可以直接查看
# from random import choice
# print(choice(deck))     #抽牌
#
# from random import  shuffle
# shuffle(deck)                #洗牌
# print(deck[10])         #重抽第十个
# print(deck)
# print(deck[:5])

#内置函数 内置模块 内置基础类型  与   类的内置方法有千丝万缕的联系

#面试题：~~~~~~~》》》》》》》》》》》》》》 100 名字 性别 和 年龄不同的对象要去重
# set 依赖对象的 hash 、eq 方法
class A:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
        return False
    def __hash__(self):
        return hash(self.name+self.sex)
a = A('chan','男',22)
b = A('chan','男',23)
print(set((a,b)))   #内存地址不一样（哈希值不一样）