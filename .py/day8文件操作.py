#绝对路径下    由电脑自己创建文件编码方式为ansi    也可以用gbk gb2312打开
# f = open('E:\模特主妇护士老师.txt',mode='r',encoding='ansi')
# content = f.read()
# print(content)
# f.close()

#相对路径下    由pycharm中创建的文件编码方式为utf-8
# f = open('模特主妇护士老师.txt',mode='r',encoding='utf-8')   #open中有一步将read转化为str格式了
# content = f.read()
# print(content,type(content))
# print(f)
# f.close()

#图片等是用 rb 转换为bayes类型
# f = open('模特主妇护士老师.txt',mode='rb')
# content = f.read()
# print(content)
# f.close()

#对于写w:没有文件就会创建文件
#先将原文件的内容删除之后再写
# f = open('log',mode='w',encoding='utf-8')
# f.write('葫芦娃葫芦娃一根藤上七个娃')
# f.close()

#写入byes内容
# f = open('log',mode='wb')
# f.write('葫芦娃葫芦娃一根藤上七个娃'.encode('utf-8'))
# f.close()


#在r+模式下，读写是正常的，先用write再用read就会出现问题
# f = open('log',mode = 'r+b')
# print(f.read())
# f.write('打几把，小鸡鸡'.encode('utf-8'))
# print(f.read())
# f.close()


# f = open('log',mode = 'r+',encoding = 'utf-8' )
# print(f.read())
# f.close()


# f = open('log',mode='w+',encoding='utf-8')
# f.write('我了个大擦擦')
# f.seek(0)    #调光标至0位置
# print(f.read())
# f.close()

# f = open('log',mode = 'w+b')
# f.write('我爸是李刚'.encode('utf-8'))
# f.seek(0)
# print(f.read())
# f.close()

# a模式是追加模式  只能执行一个动作write
# f = open('log',mode = 'a',encoding='utf-8')
# f.write('我是大帅比')
# f.close()



#可以多执行一个动作
# f = open('log',mode='a+',encoding='utf-8')
# f.write('我爱猪猪猪猪')
# f.seek(0)
# print(f.read())
# f.close()

# #功能详解
# f = open('log',mode='r+',encoding='utf-8')
# f.seek(6)           #seek按照字节来找（3个字节一个中文字符  在utf-8中）
# s = f.read()
# # s = f.read(3)    #read读出来的都是字符(能看到的最小单位)
# print(s)
# #解决断点续传问题
# print(f.tell())  #告诉我光标的位置
# f.seek(f.tell())
# f.close()

#可以随意定位置，查看等
# f = open('log',mode='r+',encoding='utf-8')
# # f.write('曌宇')
# # count = f.tell()
# # f.seek(count-9)
# # print( f.read(2))
# # f.tell()
# # f.readable()   #可读的
# # line = f.readline()   #一行一行读
# # line1 = f.readlines()  #每一行当成列表中的一个元素
# # f.truncate(9)            #截取前9个字节
# # print(f.read())
# for line in f:
#     print(line)
# f.close()

#用with open不用关闭
# with open('log',mode='r+',encoding='utf-8') as f,\
#         open('log',mode='a+',encoding='utf-8')as f1:
#     f.write('我了个大叉叉')
#     print(f.read(),f1.read())

# #注册、登录
# username = input('请输入您要注册的用户名')
# password = input('请输入您的密码')
# with open('list_of_info',mode='w',encoding='utf-8')as f:
#     f.write('{}\n{}'.format(username,password))
# print('恭喜你注册成功')
# lis = []
# i = 0
# while i < 3:
#     uname = input("请输入您的用户名")
#     upassword = input('请输入您的密码')
#     with open('list_of_info', mode='r+', encoding='utf-8')as f1:
#         for line in f1:
#             lis.append(line)
#     if uname  == lis[0].strip() and upassword ==lis[1].strip():
#         print('登录成功')
#         break
#     else:print('账号或密码错误')
#     i+=1
