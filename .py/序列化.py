#序列化——专项一个字符串数据类型
#序列 ——字符串

#写文件只能写入字符串
#网络传输时候把其他数据转化为字符串

#从数据类型到字符串的过程叫做序列化
#从字符串转化为数据类型叫 反序列化

#jason模块
#pickle模块
#shelve模块


#json
    #通用的序列化格式
    #只有很少的一部分数据类型能通过json转化为字符串
#pickle(only python)
    #所有的python中的数据类型都能转化为字符串
    #pickle序列化的内容只有python能理解
    #且部分反序列化依赖代码
    #游戏存储，恢复
#shelve
    #序列化句柄
    #使用句柄直接操作

import json   #数字 字符串 列表 字典 元组
#dumps(序列化方法)  loads(反序列化方法)
# dic = {'k1':'v1'}
# str_d = json.dumps(dic)
# print(type(str_d))
# print(str_d)
# dic_d = json.loads(str_d)
# print(dic_d)
# print(type(dic_d))

#dump 与 load  不加s直接操作文件
# dic = {1:'a',2:'b'}
# f = open('fff','w',encoding='utf-8')
# json.dump(dic,f)
# f.close()
####
# f = open('fff')
# res = json.load(f)
# f.close()
# print(type(res),res)

# dic = {1:'中国',2:'发过'}
# f = open('fff','w',encoding='utf-8')
# a = json.dump(dic,f,ensure_ascii=False)   #防止之后转化为ASCII码
# f.close()
# f = open('fff','r',encoding='utf-8')
# res1 = json.load(f)
# print(res1)
# f.close()

l = [{'k':111},{'k2':222},{'k3':333}]
f = open('file','w')
for dic in l:
    str_d = json.dumps(dic)
    f.write(str_d+'\n')
f.close()
f = open('file')
for line in f:
    dic = json.loads(line.strip())
    l.append(dic)
f.close()
print(l)