# python 天生支持多态
# 文件的多种形态
class Alipay:
    def pay(self,money):
        print('aaa',money)
class Wechat:
    def pay(self,money):
        print('bbb',money)

def pay(pay_obj,money):
    pay_obj.pay(money)

pay()
# 均支持 pay的多种形态
# python 是一门动态强类型语言
# 鸭子类型 : 不崇尚根据继承得来的相似性，仅仅自我实现代码就行了，两个类相似并不产生父类子类关系，而是鸭子类型
# list 和tuple类型非常相似
# index tuple的相似，是自己写代码时候的约束的，而不是通过父类约束的
# 优点：松耦合  （删除某一类的代码不影响其他类）
# 缺点：太随意


#   接口类和抽象类 在python中的应用并不是非常必要
#   python中不崇尚继承的形式来规范代码
#   例如 list和tuple如此相似的数据类型确不是通过继承来实现相似功能的