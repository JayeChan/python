# # 面向对象
# def Person(name,blood,aggr,gender):
#     person={
#         'name': name,
#         'blood': blood,
#         'aggr': aggr,
#         'gender': gender
#     }
#     def attack(dog):
#         dog['blood'] -= person['aggr']
#         print('%s被打了，掉了%s的血' % (dog['name'], person['aggr']))
#     person['attack'] = attack
#     return person
# alex = Person('狗剩',100,1,'不详')
# def Dog(name,blood,aggr,gender):
#     dog = {
#         'name': name,
#         'blood': blood,
#         'aggr': aggr,
#         'gender': gender
#     }
#     def bite(person):
#         person['blood'] -= dog['aggr']
#         print('%s被咬了，掉了%s的血' % (person['name'], dog['aggr']))
#     dog['bite'] = bite
#     return dog
#
# # dog1 = Dog('可凡',1000,100,'female')
# # print(alex,dog1)
#
# #Person与Dog函数定义了一类事物（类）
# #调用函数之后，赋值之后才有实际事物
#
# #攻击技能：人 打    狗 咬
# # def attack(person,dog):
# #     dog['blood'] -= person['aggr']
# #     print('%s被打了，掉了%s的血'%(dog['name'],person['aggr']))
# # def bite(dog,person):
# #     person['blood'] -= dog['aggr']
# #     print('%s被咬了，掉了%s的血' % (person['name'],dog['name']))
# jin = Dog('金老板',1000,100,'teddybare')
# alex = Person('alex',105,2,'male')
# # attack(alex,jin)
# # bite(alex,jin)
# # bite(jin,alex)
# jin['bite'](alex)
# alex['attack'](jin)
#
#
# #面向对象编程
# #类 抽象 知道有什么属性 但不知道属性的具体值
# #对象是某个类下的有具体属性的东西
# #面向对象的编程适用于复杂程序
#
# #{ 'k' : 'v' }
# class Person:
#     def __init__(self,*args):   #外部调用类名就会调用__init__方法
#         print(args)
#         self.name = args[0]
#         self.hp = args[1]
#         self.aggr = args[2]
#         self.gender = args[3]
# alex = Person('狗剩',100,1,'none')
# print(alex,'\n',alex.name,'\n',alex.gender,'\n')

#对象 =  类名（）
#过程：
    #类名首先会创造出一个对象，创建了一个self变量
    #调用init方法，类名括号里的参数会被这里接收
    #执行init方法
    #返回self
    #self是一个可以存储很多属性的大字典
#对象能干得事：
    #查看属性
    #调用方法
    #__dict__对于对象的增删改查操作都可以通过字典的语法进行
#类名能干的事：
    #实例化
    #调用方法：只不过要自己传递self参数
    #调用类中的属性，可就是调用静态属性
    #__dict__对于类中的名字只能看，无法操作

# class Dog:
#     animal = 'dog'   #固定属性，静态属性
#     def __init__(self,*args):   #初始化方法，self是对象，是一个必须传的参数，同时是个大字典
#         self.name = args[0]      #给self里边添加属性的方法
#         self.gender = args[1]
#     def walk(self,n):   #类内的方法必须含有self参数，且放在第一个，后面可放其他参数
#         print('%s走走走,走了%s步'%(self.name,n))
#
# print(Dog.animal)             #类名可以查看类中属性
# kefan = Dog('可凡','male')   #类的实例化，变成具体对象
# Dog.walk(kefan,6)            #类名可以调用内部方法
# #等价于
# kefan.walk(3)                 #对象可以调用类的方法
# laowang = Dog('老王','female')
# laowang.walk(6)



 ############################################
#1 练习
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def shangshan(self):
#         print('%s,%s岁,%s,上山去砍柴。'%(self.name,self.age,self.gender))
#     def qudongbei(self):
#         print('%s,%s岁,%s,开车去东北。'%(self.name,self.age,self.gender))
#     def dabaojian(self):
#         print('%s,%s岁,%s,最爱大保健。'%(self.name,self.age,self.gender))
# xiaoming = Person('小明',10,'男')
# xiaoming.qudongbei()

# 练习2
from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def circumference(self):
        return 2*pi*self.radius
    def area(self):
        return pi*pow(self.radius,2)
a = Circle(1)
print('面积为：',a.area())
print('周长为：',a.circumference())


