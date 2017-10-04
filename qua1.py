#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import re
mpl.rcParams['font.sans-serif'] = ['SimHei']

#data = pd.read_csv('E:/Jupter/web_crawl/weather.csv',encoding="gb2312")
data = pd.read_csv('E:/Web_crawler-for-Weather-master/weather.csv')
date = range(1,31)
qua = data['Number']
#print qua

cValue = []
for j in range(len(qua)):
    if qua[j]<=50:
        cValue.append('limegreen')
    elif qua[j]>100:
        cValue.append('orange')
    else:
        cValue.append('cornflowerblue')
plt.scatter(date,qua,color = cValue,marker = '*')

plt.title(u'杭州2017年6月空气质量指数')
#plt.legend(loc='best')
a = []
for x in range(1,31):
    a.append(x)
plt.xticks(a,rotation = -30)
plt.xlabel(u'日期')
plt.ylabel(u'空气质量指数')
#plt.hlines(0, 0, 0.5, colors = "c", linestyles = "dashed")
plt.axhline(100,label="1",color='gray',linewidth=1,linestyle="--",alpha = 0.2)
plt.axhline(50,label="1",color='gray',linewidth=1,linestyle="--",alpha = 0.2)
plt.text(32,102,u'轻度污染')
plt.text(32,70,u'良')
plt.text(32,32,u'优')
#plt.grid(x1)
plt.show()