#修改sys.path，把homework路径写到sys.path列表中
#之后所有模块导入都是基于homework
from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))

from core import main
if __name__ == '__main__':
    main.main()

# start 怎么写
# 配置文件怎么用
# 登录成功之后使用反射来获取身份对应的类
# 经常会用到的功能的封装：Mypickle类