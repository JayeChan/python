#定义类
#init方法
    #python 帮我们创建了一个对象self
    #每当我们调用类的时候就会触发这个方法
    #在init方法里面可以对self进行赋值
# self是什么 self拥有属性都属于对象
    #在类的内部，self就是一个对象
    #alex.walk() == Person.walk(alex)
# 类中可以定义静态属性
#实例化：
    #对象 = 类（参数是init方法的参数）
    #实例 == 对象
#对象：
    #对象查看方法，对象.属性
    #对象.方法名（参数）

#练习，正方形
class Square:
    def __init__(self,b):
        self.b = b
    def permiter(self):
        return 4*self.b
    def area(self):
        return pow(self.b, 2)
a = Square(2)
print('面积为：',a.area())
print('周长为：',a.permiter())



#面向对象入门
#当你见到一个需求，你能恩熙出这个问题适不适合用面向对象来解决
# java 就是完全是面向对象来进行编程

