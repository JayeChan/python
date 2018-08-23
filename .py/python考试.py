# 1
# li = [1,3,2,'a',4,'b',5,'c']
#
# l3 = li[0::2]
# print(l3)
#
# l4 = li[1:7:2]
# print(l4)
#
# l5 = list(li[7])
# print(l5)
#
# l6 = li[-3::-2]
# print(l6)

#2
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]

# lis[0][1][2]['k1'][0] = lis[0][1][2]['k1'][0].upper()
# lis[0][1][2]['k1'][0] = 'TT'
# print(lis)

# lis[0][1][2]['k1'][1] = '100'
# lis[0][1][2]['k1'][1] = str(lis[0][1][2]['k1'][1]+97)
# print(lis)

# lis[0][1][2]['k1'][2] = 101
# lis[0][1][2]['k1'][1] = int(lis[0][1][2]['k1'][1])+100
# print(lis)

dic = {'k1':'v1',"k2":['alex','sb'],(1,2,3,4,5):{'k3':['2',100,'wer']}}
# dic["k2"].append('23')
# print(dic)

# dic["k2"].insert(0,'a')
# print(dic)

# dic[(1,2,3,4,5)]['k4'] = 'v4'
# print(dic)

# dic[(1,2,3,4,5)][(1,2,3)] = 'ok'
# print(dic)

# dic[(1,2,3,4,5)]['k3'] = 'qq'
# print(dic)

# i = 0
# sum = 0
# while i<100:
#     i += 1
#     sum = sum + i*((-1)**(i+1))
# print(sum)


# sum = 0
# for i in range(1,100) :
#     sum = sum + i*((-1)**(i))
# print(sum)

# for i in range(100,-1,-1):
#     print(i)

#计算用户输入内容中索引为奇数并且对应元素为数字的个数
# a = input('请输入内容：')
# b = -1
# j = 0
# for i in a:
#     b += 1
#     if b & 2 !=0:
#         if i.isdigit():
#             j += 1
#         else:
#             pass
# print(j)

def extendlist(val,lis = []):
    lis.append(val)
    return lis
lis1 = extendlist(10)
lis2 = extendlist(123,[])
lis3 = extendlist('a')
print(lis1,lis2,lis3)