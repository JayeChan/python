# logging 模块非常非常重要 必要要学会写日志 必须要记录下工作日志
import logging
#排错的时候需要打印很多细节帮助排错
#严重的错误记录下来
#有一些用户行为必须记录下来
# logging.basicConfig(level=logging.DEBUG,###########这里可以改
#                     format = '%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s',  #格式化
#                     datefmt = '%a,%d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a'
#                     )
# try:
#     int(input('num>>'))
# except ValueError:
#     logging.error('That is not a number')

# logging.debug('debug message')    #低级别
# logging.info('info message')        #正常信息
# logging.warning('warning message')  #警告信息
# logging.error('error message')      #错误信息
# logging.critical('critical message')#高级别（严重错误信息）

# basicconfig 简单，但能做的事少
    # 中文乱码问题
    # 不能同时往文件和屏幕上输出
# 配置log对象 稍微有点复杂

logger = logging.getLogger()  #创建一个logger对象

fh = logging.FileHandler('test.log',encoding='utf_8') #创建一个handler ，用于写入日志文件


ch = logging.StreamHandler()    #在创建一个handler，用于输出到屏幕（控制台）
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
#上边创建了四个对象

fh.setLevel(logging.DEBUG) #要进行DEBUG
#接下来关联   文件操作符 和 格式相关联
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)  #logger 对象和文件操作符关联   可以添加多个fh和ch对象
logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('警告警告')     #可以写中文了
logger.error('logger error message')
logger.critical('logger critical message')

# 程序充分的解耦
# 让程序变得高可定制



# zabbix 监控系统（高可定制化）

# logging有5种级别的日志记录模式
# 两种配置方式：basicconfig 和log对象

# django框架时会讲更多
