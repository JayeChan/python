# 登录认证
# 加密   解密
# 摘要算法
# 两个字符串：
# import hashlib    #提供摘要算法的模块  摘要算法过程不可逆
# md5 = hashlib.md5()
# md5.update(b'alex3714')
# print(md5.hexdigest())

# 不管算法多不同，摘要的功能始终不变
# 对于相同的字符串进行摘要算法处理，得到的值不变
# 不管使用什么算法，hashlib的方式永远不变
# import hashlib
# sha = hashlib.sha256()
# sha.update(b'alex3714')
# print(sha.hexdigest())

# 摘要算法
# 密码的密文存储
# 文件的一致性验证（检查下载文件是否与其他机器上的文件一致）
#


#用户登录
# import hashlib
# usr = input('username:')
# pwd = input('password:')
# with open('userinfo') as f:
#     for line in f:
#         user,passwd,role = line.split("|")
#         md5 = hashlib.md5()
#         md5.update(bytes(pwd,encoding='utf-8'))
#         md5_pwd = md5.hexdigest()
#         if usr == user and md5_pwd == passwd:
#             print('登录成功')
import hashlib
md5 = hashlib.md5(bytes('加盐',encoding='utf-8')+b'111')
md5.update(b'123456')
print(md5.hexdigest())