#从模块开始
# re 模块
#正则表达式
#用re模块操作正则表达式

#正则表达式用来做字符串匹配的
#判断字符串合不合法（注册手机号合法不合法）
# import re
# phone_number = input()
# if re.match('^(13|14|15|18)[0-9]{9}$',phone_number):
#     print('合法')
# else:
#     print(
#         '不合法'
#     )

#绿茶 白茶 黄茶 青茶 红茶 黑茶  —>发酵程度
#发酵程度和制作工艺

import re
#一共三个必须会的方法：
#1、findall （所有的都返回）    2、search （从中间找也行）     3、match（必须从头找）
# ret = re.findall('a','eva egon')
# print(ret)
#findall 会匹配所有满足匹配的结果，返回列表中(找所有)

# ret = re.search('e','eva egon')
# print(ret)
# print(ret.group())
#从前往后找到一个就返回，返回变量需要调用group才能给回结果，否则报错
# if ret:
#     print(ret.group())

# ret = re.match('e','eva egon')
# if ret:
#     print(ret.group())
#match是从头开始匹配，如果正则规则从头开始可以匹配上，就返回一个变量，匹配的内容需要用group才能显示
