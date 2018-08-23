#序列化模块
    #数据类型转化成字符串的过程就是序列化
    #为了方便存储和网络传输
    #jason
        #dumps
        #loads
        #dump  与文件有关
        #load  load不能load多次
# import json
# data = {'username':['梨花','二傻子'],'sex':'male','age':16}
# json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
# # sort_keys 是否根据key排序，indent 缩进空格数，separators 分隔符是谁
# print(json_dic2)
    #pickle
        #方法和json一样
        #dump和load时候 文件是rb或者wb打开
        #支持python所有的数据类型
        #序列化和反序列化需要相同的环境
    #shelve
        #open方法
        #open方法获取了一个文件句柄
        #操作和字典类似
#模块的导入
#import
#from import
#as 重命名
#都支持多名字导入
# sys.moudles 记录了所有被导入的模块
# sys.path  记录了导入模块时候记录的路径
