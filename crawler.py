#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

def main():
	#获取整个网页信息——非结构化数据
	res = requests.get('http://tianqi.eastday.com/hangzhou_history/58457_201706.html?btype=historyWeather&subtype=pre&idx=1')
	res.encoding = 'utf-8'
	#print res.text
	soup = BeautifulSoup(res.text,'html.parser')
	#print soup

	'''
	for weather in soup.select('tbody'):
	    for i in range(len(weather.select('tr'))):
	        #print weather.select('tr')[i].text
	        print weather.select('tr')[i].select('td')[0].text 
	        #print weather.select('tr')[i].select('td')[0].select('.week')[0].text 
	        print weather.select('tr')[i].select('td')[1].text
	        print weather.select('tr')[i].select('td')[2].text
	        print weather.select('tr')[i].select('td')[3].text
	        print weather.select('tr')[i].select('td')[4].text
	        print weather.select('tr')[i].select('td')[5].text
	        print weather.select('tr')[i].select('td')[6].text
	'''

	fout = open('E:/Web_crawler-for-Weather-master/weather.csv','wb')#用‘w’时csv出现空行，改用‘wb’            
	csv_writer = csv.writer(fout)
	CsvHead=['Date','High_temp','Low_temp','Weather','Wind','Number','Qai_lel']
	csv_writer.writerow(CsvHead)

	for weather in soup.select('tbody'):
	    for i in range(len(weather.select('tr'))):
	        Date = weather.select('tr')[i].select('td')[0].text 
	        High_temp = weather.select('tr')[i].select('td')[1].text
	        Low_temp = weather.select('tr')[i].select('td')[2].text
	        Weather = weather.select('tr')[i].select('td')[3].text
	        Wind = weather.select('tr')[i].select('td')[4].text
	        Number = weather.select('tr')[i].select('td')[5].text
	        Qai_lel = weather.select('tr')[i].select('td')[6].text
	        csv_writer.writerow([ x.encode('utf-8') for x in [Date,High_temp,Low_temp,Weather,Wind,Number,Qai_lel]])        
	fout.close()

if __name__ == '__main__':
	main()