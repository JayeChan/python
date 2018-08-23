# property
# 内置装饰器函数 只在面向对象中使用
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     #把方法伪装成一个属性
#     @property    #把方法伪装成一个属性
#     def perimeter(self):
#         return 2*pi*self.r
#     @property    #把方法伪装成一个属性
#     def area(self):
#         return self.r**2*pi
# c1 = Circle(5)
# # print(c1.area())
# print(c1.area)    #把这里变成了调用属性
# # print(c1.perimeter())
# print(c1.perimeter) #方法伪装成一个属性
#classmethod
#staticmethod

# class Person:
#     def __init__(self,weight,hight):
#         self.weight = weight
#         self.hight = hight
#     @property
#     def BMI(self):
#         return self.weight/pow(self.hight,2)
# a = Person(73,1.70)
# print(a.BMI)

# class Person:
#     def __init__(self,name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name + 'sb'
#     @name.setter     #对对象的一个修改
#     def name(self,new_name):
#         self.__name = new_name
# tiger = Person('泰哥')
# print(tiger.name)
# tiger.name = '全班'
# print(tiger.name)

# class Goods:
#     discount = 0.5
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price * self.discount
# apple = Goods('苹果',5)
# print(apple.price)    #假属性，真方法

#属性 查看 修改 删除
class Person:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):      #直接执行的是我
        print('.name执行的是我')
        return self.__name
    @name.deleter
    def name(self):
        # del self.__name
        print('del执行的是我')
    @name.setter
    def name(self,new_name):
        print('修改名字方法')
        self.__name = new_name
b = Person('二哥')
print(b.name)
del b.name     #del 并没有删除的作用，而是触发b.name（）下的删除属性的行为
print(b.name)