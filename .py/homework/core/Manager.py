#管理员类
import json
from conf.config import *
from core.Teacher import Teacher
from core.my_pickle import MyPickle
class Manager:
    menu = \
        [('创建讲师账号','createTeacher'),('创建学生账号','createStudent'),
        ('创建班级','createClasses'),('创造课程','createCourse'),
        ('查看课程','showCourse'),('查看班级','showClasses'),
        ('绑定班级','boundClass'),('退出','')]
    def __init__(self,name):
        self.name = name
        self.teacher_picke_obj = MyPickle(teacher_obj)
    @staticmethod
    def userinfo_handle(content):   #帮助每次的输入值
        with open(userinfo,'a') as f:
            f.write('\n%s'%content)
    def createTeacher(self):
        '''
        输入讲师姓名
        输入显示密码
        将讲师的信息写入userinfo文件里
        输入：讲师所在的学校
        实例化一个讲师对象，存储在讲师对应的文件中
        :return:
        '''
        name = input('请输入讲师姓名：')
        passwd = input('请输入密码：')
        school = input('请输入讲师所在的学校：')
        with open('E:\\k\\python project\\.py\\homework\\db\\userinfo.txt','a+',encoding='utf-8') as f:
            f.write("%s,%s,讲师,%s\n"%(name,passwd,school))
        return Teacher(name,passwd,school)
            #加一个确认与否的选项（可以看到输入是否有误）
    @staticmethod
    def createCourse():
        '''
        输入学科名称
        价格
        学习周期
        创建一个课程对象，dump进course文件
        :return:
        '''
        name = input('请输入课程名称：')
        price = input('请输入课程价格：')
        period = input('请输入课程周期：')
        school = input('请输入课程开设的学校：')
        f = open('E:\\k\\python project\\.py\\homework\\db\\course', 'a+', encoding='utf-8')
        json.dump('%s,%s,%s,%s'%(name,price,period,school),f,ensure_ascii=False)
        f.close()
        return Course(name,price,period,school)
    def showCourse(self):
        '''
        打开文件
        将文件的学科对象读出来，展示
        :return:
        '''

        pass
    def createClasses(self):
        '''
        输入：
        班级名称、学校
        绑定一个学科对象，想要调用查看学科方法获取学科对象，用户选择学科，在将对象绑定到班级
        创建一个属于这个班级的文件用于存储学生信息，将文件的路径存储到班级对象中
        创建一个班级对象（名称 学校 学科对象 讲师列表 学生信息所在文件目录，dump进class中
        :return:
        '''
        pass
    def showClasses(self):
        '''
        打开文件
        将文件的班级对象读出来，展示
        :return:
        '''
        pass
    def createStudent(self):
        '''
        输入学生姓名
        输入学生密码
        将学生信息写入userinfo文件里
        :return:
        '''
        pass
    def boundClass(self):
        '''
        管理选择为老师还是学生指定班级
        若是为老师绑定班级：
            找到指定的老师和对应的班级（通过show方法查看后确定）
            给讲师对象的班级属性的列表中加入一个新项，值为班级对象
            给班级对象中的讲师属性列表加入一个新项，值为讲师的对象
        若是为学生绑定班级：
            找到指定的学生和对应的班级
            给学生创建新的班级属性，将属性的值设为班级对象
            将学生对象的信息 根据班级对象中存储的学生信息存储路径 dump进文件
        :return:
        '''
        pass

# a.createTeacher()

#讲师类


#课程类

#

#通过反射来实现管理员的输入执行：   反射反射反射
# for k in Manager.menu:
#     print(k)
# key = input('请输入您想执行的操作：')
# print(Manager.menu[key])
# if hasattr(a,Manager.menu[key]):
#     f = getattr(a,Manager.menu[key])
#     obj = f()                  #的确是所输入的对象

# print(obj.name)   #的确是一个对象

#首先管理员身份登录
#登录之后 应该实例化一个对应身份的对象
#管理员对象能够调用所有的方法