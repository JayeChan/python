#非常重要
#通过反射 使得输入什么（字符串类型）就能调用什么方法/属性
class Teacher:
    dic = {'查看学生信息':'show_student','查看讲师信息':'show_teacher'}
    def show_student(self):
        print('show_student')
    def show_teacher(self):
        print('show_teacher')
    @classmethod
    def func(cls):
        print('hahaha')

# # hasattr getattr delattr
# if hasattr(Teacher,'dic'):
#     ret = getattr(Teacher,'dic')     #Teacher.dic  类也是对象
#     ret2 = getattr(Teacher,'func')   #类.方法
# print(ret)
# print(ret2)
# ret2()
alex = Teacher()
# func = getattr(alex,'show_student')
for k in Teacher.dic:
    print(k)
key = input("输入需求：")
if hasattr(alex,Teacher.dic[key]):
    f = getattr(alex,Teacher.dic[key])     #若key=学生，相当于是alex.show_student的地址给了f
    f()                                    #调用alex.show_student()


#网络编程中有非常重要的应用  必考


#通过反射
#对象名 获取对象属性和普通方法
#类名 获取静态属性 和类方法 和静态方法

#普通方法 self
#静态方法 @staticmethod
#类方法 @classmethod
#属性方法 @property


# 作业 学院管理系统：开发规范
# 整理面向对象的所有知识点
