#面向对象的三大特性： 继承   多台   封装
#组合
#人狗大战
# class Dog:
#     def __init__(self,name,aggr,hp,kind):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#         self.kind = kind
#     def bite(self,person):
#         person.blood -= self.aggr
# class Person:
#     def __init__(self,name,aggr,hp,gender):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#         self.gender = gender
#         self.money = 0
#     def attack(self,dog):
#         dog.blood -= self.aggr
#     def get_weapon(self,weapon):
#         if self.money >= weapon.price:
#             self.money -= weapon.price
#             self.weapon = weapon
#             self.aggr += weapon.aggr
#         else:
#             print('没钱买啥装备啊，滚吧凑屌丝')
#
# class Weapon:
#     # 加伤害、加血量
#     def __init__(self,name,aggr,njd,price):
#         self.name = name
#         self.aggr = aggr
#         self.njd = njd
#         self.price = price
#     def hand18(self,person):   #
#         if self.njd >=0:
#             person.hp -= self.aggr*2
#             self.njd -=1
# alex = Person('alex',0.5,100,'不详')
# jin = Dog('金老板',100,500,'不详')
# w = Weapon('打狗棒',100,3,998)
# alex.money += 1000
# alex.get_weapon(w)
# print(alex.weapon.njd)
# print(alex.aggr)
# print('原来金老板的血量：',jin.hp)
#
# alex.weapon.hand18(jin)
# print('目前金老板的血量：',jin.hp)



#组合：一个对象的属性值是另一个类的对象
#  alex.weapon   是 Weapon的一个对象
# 会出现两元点


####圆环类
# from math import pi
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def perimeter(self):
#         return 2*pi*self.radius
#     def area(self):
#         return pi*pow(self.radius,2)
# # a = Circle(1)
# # print('面积为：',a.area())
# # print('周长为：',a.perimeter())
#
# class Ring:
#     def __init__(self,outside,inside):
#         self.outside = Circle(outside)          #上边类的对象作为此类的属性
#         self.inside = Circle(inside)            #这种被称之为组合
#     def area(self):
#         return self.outside.area()-self.inside.area()
#     def perimeter(self):
#         return self.outside.perimeter()+self.inside.perimeter()
# ring = Ring(20,10)
# print(ring.area())
# print(ring.perimeter())

#创建一个老师类
#老师有生日
#生日也可以是一个类
#组合
class Birthday:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def jinian(self):
        print('今天是出生的第%s年'%(2018-self.year))

class Course:
    language = 'Chinese'
    def __init__(self,teacher,name,period,price):
        self.teacher = teacher
        self.name = name
        self.period = period
        self.price = price

class Teacher:
    def __init__(self,name,age,gender,birthday):
        self.name = name
        self.age = age
        self.gender = gender
        self.birthday = birthday
        self.course = Course(self,'python','6 month',20000)

b = Birthday(2018,1,16)
egg = Teacher('egon',0,'female',b)
print(egg.name)
print(egg.birthday.year)
print(egg.course.price)