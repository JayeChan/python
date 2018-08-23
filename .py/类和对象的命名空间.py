#在类里可以定义两种属性
#静态、动态属性
# class Course:
#     #静态属性
#     language = 'Chinese'
#     def __init__(self,teacher,name,period,price):
#         self.teacher = teacher
#         self.name = name
#         self.period = period
#         self.price = price
#     def func(self):
#         pass
# python = Course('egon','python','6 months',20000)
# Course.language = "English"   #修改类的静态属性
# print(Course.language)
# python.language = 'Japanese'
# print(python.language)
#静态属性修改之后，再也用不了原来类中的静态类型了
#除非
# del python.language
# print(python.language)
# 对于不可变数据类型来说，类对象最好使用类名来操作
# 对于可变数据类型来说，对象名的修改是共享的，重新赋值是独立的

# 模拟人生
# class Person:
#     money = 0
#     def work(self):
#         Person.money += 1000
# mother = Person()
# mother.work()
# print(mother.money)

# class Foo():
#     count = 0
#     def __init__(self):
#         Foo.count += 1
# f1 = Foo()
# f2 = Foo()
# print(f1.count,f2.count)
# f3 = Foo()
# print(f1.count)
#静态变量的特性  所有对对象共享静态变量

 # 认识绑定方法

class Foo():
     def func(self):
         print('func')
f1 = Foo()
print(f1.func)   #<bound method Foo.func of <__main__.Foo object at 0x000001EA58568390>>
print(Foo.func)
print(f1)
#当对象调用方法时候，会把对象中的值带入方法中，叫做绑定方法
# import package   ——类的实例化的过程
# time.time()就是使用类中方法
