#   封装非常重要
# 广义上面向对象的封装：代码的保护，面向对象的思想本身就是一种封装
# 只让自己的对象能调用自己类中的方法

# 狭义上的封装 ——面向对象的三大特性之一
# 把属性和方法都藏起来  不让你看见
# class Person:
#     __key = 123     #私有静态属性
#     def __init__(self,name,password):
#         self.name = name
#         self.__password = password     #私有属性（只在内部发生）
#     def __get_pw(self):     #私有方法
#         return self.__password      #只要在类的内部使用会自动转换
#     def login(self):
#         self.__get_pw()
# alex = Person('alex','alex3714')
# print(alex._Person__password)       #_类名__属性名

# 所有的私有 都是在变量的左边加上双下划线
#   对象的私有属性
#   对象的私有方法
#   类中的静态私有属性
# 所有的私有的 都不能在类的外部使用
#
# class Room:
#     def __init__(self,name,length,width):
#         self.name = name
#         self.__length = length
#         self.__width = width
#     def get_width(self):   #对私有属性进行操作（常见于java）
#         print(self.__width)
#     def area(self):
#         return self.__length * self.__width
# jin = Room('金老板',2,1)
# print(jin.area())

#父类的私有属性不能被子类调用
# class Foo:
#     __key = '123'
# class Son(Foo):
#     print(Foo.__key)

#会用到私有的概念的场景
#1、隐藏起一个属性  不想让类的外部调用
#2、我想保护这个属性，不想让属性随意被改变
#3、我想保护这个属性，不然子类继承