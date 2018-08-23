import abc

class All_file(metaclass=abc.ABCMeta):
    all_type = 'file'
    @abc.abstractmethod  #定义抽象方法，无需实现功能
    def read(self):
        pass
    @abc.abstractmethod
    def write(self):
        pass


# 抽象类：规范
# 单继承  实现功能是一样的，所以在父类中可以有一些基础的功能
# 多继承的情况 由于功能比较复杂 所以不容易抽象出相同的功能的实现

# 抽象类还是接口类： 面向对象的开发规范



# java ：
    #java内所有继承方式都是单继承，所以抽象类完美的解决了单继承需求中的规范问题
    #但是对于多继承问题，由于java本身语法的不支持，所以创建了接口Interface这个概念来解决多继承的规范化问题
# python：
    # python中没有接口类：
        # python中自带多继承 所以我们直接用class来实现了接口类
    # python中支持抽象类：一般情况下 单继承     不能实例化
        # 且可以实现python代码