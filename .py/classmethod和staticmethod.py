# staticmathod 静态的方法
# classmathod 类方法    非常重要
# 类里面的操作行为
# class Goods:
#     discount = 0.5
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price * Goods.discount
#     @classmethod     #把一个方法 变成一个类中的方法，这个方法就直接可以被类类类类调用
#     def change_discount(cls,new_discount):
#         cls.discount = new_discount
# apple = Goods('苹果',5)
# print(apple.price)    #假属性，真方法
# Goods.change_discount(0.5)   #类可以直接调用方法 不依赖于对象！！！！
# print(apple.price)
#这个方法的操作只涉及静态属性的时候，就应该用类方法

# 学java的 所有代码都要写入对象中
#java
# class Login:
#     def __init__(self,name,password):
#         self.name = name
#         self.password = password
#     def login(self):pass
# def get_user_pwd():  #面向过程 不支持面向对象
#     username = input('用户名')
#     pwd = input('密码：')
#     Login(username,pwd)

class Login:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):pass
    @staticmethod
    def get_user_pwd():  #静态方法
        usr = input('用户名：')
        pwd = input('密码：')
        return Login(usr,pwd)

a = Login.get_user_pwd()
print(a.name)
# 在完全面向对象的程序中，若一个函数集合对象没有关系，也和类没有关系
# 那么可以伪装成一个静态方法
#    类方法和静态方法 都是类调用的
#    对象可以调用静态方法 推荐用类名调用
#    类方法 中有个默认参数cls 代表此类
#    静态方法中无参数（或者有自己的参数）（无类、无对象）

# 接口就是类中的方法