import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import pandas as pd


def scraping_function():
   #pages link 
   cities_urls = ['https://www.accuweather.com/en/ma/al-hoceima/246183/daily-weather-forecast/246183',
                  'https://www.accuweather.com/en/ma/tangier/6368/daily-weather-forecast/6368',
                  'https://www.accuweather.com/en/ma/tetouan/246100/daily-weather-forecast/246100']

   #define lists
   ht_list = []
   lt_list = []
   pr_list = []
   dt_list = []
   wc_list = []

   for url in cities_urls:
      page = requests.get(url,headers={'user-agent':'sss'}) #must add this attr
      sp = BeautifulSoup(page.content, 'lxml')

      ht = sp.find_all('span',{'class':'high'})
      lt = sp.find_all('span',{'class':'low'})
      pr = sp.find_all('div',{'class':'precip'})
      dt = sp.find_all('span',{'class':'module-header sub date'})
      wc = sp.find_all('div',{'class':'phrase'})

      for i in range(len(ht)): 
         ht_list.append(ht[i].text)
         lt_list.append(lt[i].text)
         pr_list.append(pr[i].text)
         dt_list.append(dt[i].text)
         wc_list.append(wc[i].text)
      print('switched')


   c1 = ['Al-hoceima' for i in range(len(ht))]
   c2 = ['Tanger' for i in range(len(ht))]
   c3 = ['Tetouan' for i in range(len(ht))]
   cities = c1+c2+c3

   header = ['Date','High temp','Low temp','Precip','Weather Condition','City']
   data = [dt_list,ht_list,lt_list,pr_list,wc_list,cities]
   records = zip_longest(*data)
   #save in csv file
   with open('weather_dataset.csv','w',newline='',encoding='UTF-8') as file:
      wr = csv.writer(file)
      wr.writerow(header)
      wr.writerows(records)
   return 'weather_dataset.csv'

