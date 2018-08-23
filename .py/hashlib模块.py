import hashlib
#加密模块
# m = hashlib.md5()
# print(m)
#
# m.update('hello world'.encode('utf-8'))
# print(m.hexdigest())       #用md5加密明码
#
# m.update('alex'.encode('utf-8'))
# print(m.hexdigest())
#
# m2 = hashlib.md5()
# m2.update('hello worldalex'.encode('utf-8'))
# print(m2.hexdigest())

s = hashlib.sha256()
s.update('hello world'.encode('utf-8'))
print(s.hexdigest())