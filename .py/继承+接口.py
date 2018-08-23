# 继承
# 单继承
    # 先抽象再继承
    # 子类可以使用父类的方法和属性（前提是子类自己没有）
    # 子类有的方法和属性优先使用自己的，可以在类内调用父类的方法和属性
# 多继承
    # 新式类和经典类
        # 多继承寻找名字的顺序：新式类广度优先，经典类深度优先
        # 新式类中有一个 类名.mro方法 查看广度优先的执行顺序
        # python 3 中有个super方法，根据广度优先的继承顺序调用上一个类

# 接口类
# java ：面向对象中的设计模式
# 设计模式  ——接口类
# 接口类 ：python原生不支持
# 抽象类： python原生支持
from abc import abstractmethod,ABCMeta
class Payment(metaclass=ABCMeta):  #元类  默认元类是 type
    @abstractmethod
    def pay(self,money):
        pass
#规范：接口类或者抽象类都可以
#接口类 默认多继承，接口类中的所有的方法 都必须不能实现——java
#抽象类 不支持多继承，抽象类中的方法可以由一些代码的实现——java

class Wechat(Payment):
    def pay(self,money):
        print('您已经用微信支付了%s元'%money)
class Alipay(Payment):
    def pay(self,money):
        print('您已经用支付宝支付了%s元'%money)
class Applepay(Payment):
    def fuqian(self,money):
        print('您已经用ApplePay支付了%s元'%money)

def pay(pay_obj,money):   # 统一支付入口
    pay_obj.pay(money)
# wechat = Wechat()
# wechat.pay(100)
# ali = Alipay()
# ali.pay(1000)
app = Applepay()
# pay(wechat,100)
# pay(ali,200)
# pay(app,100)

#报错，告诉我们Applepay不规范，缺少pay
#TypeError: Can't instantiate abstract class Applepay with abstract methods pay