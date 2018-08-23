# import time

# print(time.time())   #时间戳 *****
# time.sleep(3)
# print(time.clock())   #计算cpu执行时间
# print(time.gmtime())  #标准时间time.struct_time(tm_year=2018, tm_mon=7, tm_mday=10, tm_hour=6, tm_min=31, tm_sec=57, tm_wday=1, tm_yday=191, tm_isdst=0)
# print(time.localtime())  #time.struct_time(tm_year=2018, tm_mon=7, tm_mday=10, tm_hour=14, tm_min=34, tm_sec=44, tm_wday=1, tm_yday=191, tm_isdst=0)
# print(time.strftime('%Y--%m--%d',time.localtime()))
#转化结构化时间
# a = time.strptime('2018-7--18 20:10:59','%Y-%m--%d %H:%M:%S')
# print(a)
# print(a.tm_year)
# print(a.tm_mday)
# print(time.ctime())     #目前时间(固定格式)
# print(time.ctime(3600)) #1970年后的3600秒
# print(time.mktime(a))     #时间换算成时间戳

# import datetime
#
# print(datetime.datetime.now()   #比较友好的本地时间表达


### random 模块
import random
# print(random.random())
# print(random.randint(1,8))   #包括8
# print(random.choice('hello'))
# print(random.choice(['123',4,'owjf',00]))
# print(random.sample(['123',4,[1,2],2,'草拟吗'],2))   #随机取俩
# print(random.randrange(1,3))

#验证码函数:
def v_code():
    code = ''
    for i in range(5):
        add = random.choice([random.randint(0,9),chr(random.randrange(65,91))])
    # for i in range(5):
    #     if random.choice():
    #         add = random.randrange(10)
    #     else:
    #         add= chr(random.randrange(65,91))
        code += str(add)
    print(code)
v_code()

