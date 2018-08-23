#吧解决一类问题的模块放在同一个文件夹里 ——包
#只有包含__init__.py的才能称之为一个包
# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/__inis__.py','w'))
# l.append(open('glance/db/models.py','w'))
# map(lambda f:f.close(),l)

# import sys
# sys.path.insert(0,'E:\\k\\python project\\.py')
# from glance.api import policy
# policy.get()

# 可以直接导入方法
import glance
glance.api.policy.get()
glance.api.versions.create_resource('我要你为我梳妆')
glance.cmd.manage.main()
glance.db.models.register_models('a')
#改成“.”可以随意移动包，只要能够找到包的位置，但是无法在包内调用外部的方法
#相对路径"."只有在外部可以应用

