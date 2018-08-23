import sys
from conf.config import *
from core.Manager import Manager
def login():
    '''
    登录函数，先到conf.config文件中读取userinfo的文件路径
    读取userinfo文件中的信息，查验用户名和密码
    登陆成功之后，查看这个人的身份，确定进入那个属兔
    :return:
    '''
    usr = input('用户名：')
    pwd = input('密码：')
    with open(userinfo) as f :
        for line in f:
            username,passwd,role = line.strip().split('|')
            if username == usr and passwd == pwd:
                print('\033[1;32m登录成功！\033[0m')
                return {'username':usr,'role':role}
            else:
                print('\033[1;31m登录失败！\033[0m')
# from core import Manager
def main():
    '''
    打印欢迎信息
    login：   三次登录   得到返回值：用户的姓名和身份
    打印用户身份对应的功能菜单
    #若用户想要调用任何方法，应该通过角色对象进行调用
    :return:
    '''
    print('\033[1;42m欢迎您登录选课系统\033[0m')
    ret = login()
    if ret:
        role_class = getattr(sys.modules[__name__],ret['role'])  #反射本模块中的角色
        obj = role_class(ret['username'])
        for i,j in enumerate(role_class.menu,1):
            print(i,j[0])
        try:
            ret = int(input('请输入操作序号：'))
            getattr(obj,role_class.menu[ret-1][1])()  #getattr(Manage,操作)
        except:
            print('对不起，您输入的内容有误！')
