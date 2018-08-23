#代码错误
#错误分为两种 1 逻辑错误   2 语法错误

#程序一旦发生错误，立即停止执行
#异常处理：  调试代码时不要用
try:
    1/0
    [][2]
    ret = int(input('number:'))
    print(ret*"*")
except ValueError:
    print('您输入的内容有误，请输入一串数字')
except IndexError:
    print('超出代码最大长度')
#万能异常处理
except Exception as error:
    print('你错了，老铁',error)
else:
    print("没啥异常耶~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
finally:
    print('============我来收尾，别管我============')
#有了万能的处理机制仍然需要把能预测到的问题单独处理
#单独处理异常需要放在万能异常之前
#finally 不管有没有错误都执行

# def func():
#     try:
#         print('打开一个文件')
#         f = open('file','r')
#         for line in f:
#             print(int(line))
#         return True
#     except:
#         return False
#     finally:
#         print('执行了finally')
#         f.close()
# func()

#finally 与return相遇依然会执行
#finally一般在函数中进行异常处理的收尾工作

