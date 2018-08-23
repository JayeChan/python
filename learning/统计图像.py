import matplotlib
import pandas
import numpy
from pandas import  read_csv
import matplotlib.pyplot as plt

#简单图像
data = read_csv("F:\\BaiduNetdiskDownload\\5.1data.csv")
# font = {'family','SimHei'}
# matplotlib.rc('font',**font)
data['购买日期'] = pandas.to_datetime(data['日期'])      #购买日期的转化
# plt.plot(data['广告费用'],data['购买用户数'],'o')
# plt.plot(data['广告费用'],data['购买用户数'],'o',color = 'yellow')
# plt.plot(data['广告费用'],data['购买用户数'],'o',color = (0,0,1))  #红绿蓝三原色
# plt.plot(data['广告费用'],data['购买用户数'],'*',color = '#FFFF00')  #十六进制颜色代码
# plt.xlabel('广告费用')
# plt.ylabel('购买用户数')
# plt.grid(True)              #添加网格
# plt.show()


#折线图  折折折折折折折折折
#plot(x,y,style,color,linewidth)
#title("标题")
#style：- 连续曲线 ， - -虚线 ，-.  连续的用带点的曲线，：由点连成的曲线 ，.散点图（小点），o散点图（大点），,像素点（更小的点），*五角星图
# plt.plot(data['购买日期'],data['购买用户数'],'-',color = 'r')
# plt.grid(True)              #添加网格
#
# plt.show()

#饼图 饼饼饼饼饼饼饼饼饼饼饼饼饼饼饼饼饼饼
#pie(x,labels,colors,explode突出的块状序列,autopct占比显示格式，%.2f保留两位小数)
# data = read_csv("F:\\BaiduNetdiskDownload\\5.3data.csv")
# gb = data.groupby(
#     by = ['通信品牌'],as_index=False
# )['号码'].agg({'用户数':numpy.size})
#
# # font = {'family':'SimHei'}
# # matplotlib.rc('font',**font)
# plt.pie(gb['用户数'],labels=gb['通信品牌'],autopct='%.2f%%')
# plt.show()

#柱形图  柱柱柱柱柱柱柱柱
#bar(left,height,width,color)
#barh(bottom,width,height,color)