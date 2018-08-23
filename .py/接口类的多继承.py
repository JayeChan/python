
#tiger 走路 游泳
#swan 走路 游泳 飞
#ying 走路 飞
from abc import abstractmethod,ABCMeta

class Walk_Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass
class Fly_Animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass
class Swin_Animal(metaclass=ABCMeta):
    @abstractmethod
    def swin(self):
        pass
class Tiger(Walk_Animal,Swin_Animal):pass
class Ying(Walk_Animal,Fly_Animal):pass
class Swan(Swin_Animal,Walk_Animal,Fly_Animal):pass

#接口隔离原则： 使用多个专门的接口，而不适用单一的总接口。既客户端不应该依赖那些不需要的接口
