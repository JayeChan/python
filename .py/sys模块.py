import sys
#与python解释器进行交互
# print(sys.argv)      #让交互界面可以上传参数
#
# def post():
#     print("ok")
# def download():
#     pass
# if sys.argv[1] == 'post':
#     post()
# elif sys.argv[1] == 'download':
#     download()
#
# sys.exit()    #退出程序
# sys.version()

# import time
# print(sys.path)       #找到模块的路径
# print(sys.path.append('放路径进来'))
# print(sys.platform)
import os

if sys.platform == 'win32':  #跨平台判断
    os.system('dir')
else:
    os.system('ls')

