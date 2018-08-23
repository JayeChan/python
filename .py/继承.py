#复习
# class A:
#     def __init__(self):
#         self.name = 'egon'
#
# class B:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
# b = B(18,1,17)
# a = A()
# a.birth = b   # B 的一个对象作为了 A 的一个属性
# a.birth.year

# class A:pass
# class A_son(A):pass
# class B:pass
# class AB_son(A,B):pass
#一个类可以被多个类继承
#一个类可以继承多个父类（python中的特性）

# print(A_son.__bases__)
# print(AB_son.__bases__)
# print(A.__bases__)
#在py3中所有的类都有父类，没有父类默认继承object  （新式类）

# class Animal:
#     def __init__(self):
#         print('执行Animal.__init__')
#         self.func()
#     def eat(self):
#         print('%s eating'%self.name)
#     def drink(self):
#         print('%s drinking'%self.name)
#     def func(self):
#         print('Animal.func')
# class Dog(Animal):
#     def guard(self):
#         print('guarding')
#     def func(self):
#         print('Dog.func')
# dog = Dog()
# print(dog.guard())

# class Animal:
#     def __init__(self,name,aggr,hp):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#     def eat(self):          #派生方法
#         print('%s吃药回血'%self.name)
#         self.hp+=99
# class Dog(Animal):
#     def __init__(self,name,aggr,hp,kind):
#         Animal.__init__(self,name,aggr,hp)
#         self.kind = kind
#     def eat(self):
#         Animal.eat(self)
#         self.teeth = 2
#     def bite(self,person):      #派生方法
#         person.hp -= self.aggr
#         print('%s掉了%s的血量'%(person.name,self.aggr))
# class Person(Animal):
#     def __init__(self,name,aggr,hp,gender):
#         Animal.__init__(self,name,aggr,hp)
#         self.gender = gender
#     def eat(self):    #在父类中以实现的功能如果需要增加，需要在子类里进行调用并增加
#         Animal.eat(self)
#         self.hair = 5
#     def attack(self,dog):
#         dog.hp -= self.aggr
#         print('%s掉了%s的血量'%(dog.name,self.aggr))
# jin = Dog('金老板',100,500,'吉娃娃')
# alex = Person('alex',5,101,'male')
# print(jin.bite(alex))
# print(alex.eat())
# print(alex.hp)
# print(jin.eat())
# print(jin.teeth)

#父类中没有的属性、方法，在子类中出现，叫做派生属性、方法
#只要是子类的对象调用，子类中有的名字，一定用子类的，没有才找父类的，父类若没有则报错
#如果父类子类都有，用子类的
    #如果还想用父类的，单独调用父类的，需要自己传self参数
    #父类名.方法    需要传self
    #super().方法   不需要自己传self
#正常的代码中  单继承 ====  减少了代码的重复
#继承表达式是一种  子类是父类的关系


# class Animal:
#     def __init__(self,name,aggr,hp):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#     def eat(self):
#         print('animal eating')
#
# class Dog(Animal):
#     def __init__(self,name,aggr,hp,kind):
#         super().__init__(name,aggr,hp)       #用super不用传self (只在新式类中有)  python 3 所有类都是新式类
#         self.kind = kind                    #派生属性
#     def eat(self):
#         # Animal.eat(self)
#         print('dog eating')
# jin = Dog('金老板',200,500,'teddy')
# print(jin.name)
# super(Dog,jin).eat()     #用super来调用父类的方法或属性
# print(jin.eat())      #调用自己的类


#多继承
# class A:
#     def func(self):
#         print('A')
# class B(A):
#     pass
#     # def func(self):
#     #     print('B')
# class E:
#     def func(self):print('E')
# class C(E):
#     pass
#     # def func(self):
#     #     print("C")
# class D(B,C):     #顺序为亲疏程度
#     pass
#     # def func(self):print('D')

# d = D()
# d.func()    #若自己没有，则调用最近的父类的

#钻石继承问题
#按层次来继承，父类先继承完，如果父类都只能找爷爷类，那么就找爷爷类
#广度优先 算法
#继承的父类有相同的爷爷，那么按亲疏顺序执行，若执行不完则进入爷爷类。若不同的爷爷，直接按亲属顺序找

# 继承执行之顺序
    #           6F
    # 3A                   5E
    # 2B                   4C
    #           1D
# class F:
#     def func(self):print('F')
# class A(F):
#     pass
#     # def func(self):print('A')
# class E(F):
#     def func(self):print('E')
# class B(A):
#     pass
#     # def func(self):print('B')
# class C(E):
#     def func(self):print('C')
# class D(B,C):
#     pass
#     # def func(self):print('D')
# d = D()
# # d.func()
# print(D.mro())    #继承顺序显示

#在新式类中实行的是广度优先，而经典类中是深度优先
#多继承中，子类的对象调用一个方法，默认是就近原则
#python2.7中 新式类和经典类共存

class F:
    def func(self):print('F')
class A(F):
    pass
    # def func(self):print('A')
class E(F):
    def func(self):print('E')
class B(A):
    pass
    # def func(self):print('B')
class C(E):
    def func(self):print('C')
class D(B,C):
    pass

 # super只在py3中存在
 # super不是找父类的意思，而是根据广度优先原则找下一个类（根据mro方法的值找）
