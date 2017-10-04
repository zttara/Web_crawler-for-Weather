#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
#import re
mpl.rcParams['font.sans-serif'] = ['SimHei']

#data = pd.read_csv('E:/Jupter/web_crawl/weather.csv',encoding="gb2312")
data = pd.read_csv('E:/Web_crawler-for-Weather-master/weather.csv')

data.Qai_lel.value_counts().plot(kind='bar',color = 'blue',alpha=0.6)
plt.title(u"空气质量天数统计")
plt.ylabel(u"天数")  
#plt.ylim(0,20)
plt.yticks(range(23),rotation = 30)
plt.xticks(rotation = 360)

plt.show()