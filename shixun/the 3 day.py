# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:46:45 2018

@author: 10257
"""

import urllib.request as r
url = "http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
data = r.urlopen(url).read().decode('utf-8','ignore')

import json
data = json.loads(data)

A = [2,10,18,24,32]
temlist = []

def train1(A):
    for X in A:
        print(str(data['list'][X]['main']["temp"]))
        print(str(data['list'][X]['main']["pressure"]))
        print(str(data['list'][X]['main']["temp_max"]))
        print(str(data['list'][X]['main']["temp_min"])) 
        print(str(data["list"][X]["weather"][0]["description"]))
train1(A)
def train2(Tn,Nm):
    
    for i in Nm:
        print((str(Tn*int(data['list'][i]['main']["temp"]))))
    return True
a = train2("*",A)
import matplotlib.pyplot as plt
squares = []
for i in A:
    squares.append(int(data['list'][i]['main']["temp"]))
input_number=range(1,6)
plt.plot(input_number,squares,linewidth=5)
plt.title("version",fontsize=14)
plt.xlabel("day",fontsize=14)
plt.ylabel("temp",fontsize=14)
plt.scatter(input_number,squares,s=100)
plt.show()
'''L练习6 
每一行现实四个商品然后打印分割 只要第一个36个商品信息
列出36个商品
获得排序
按照销量排序
商品过滤，只要15天退款
'''
import urllib.request as r
url1 = "https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8"
data1 = r.urlopen(url1).read().decode('utf-8','ignore')
data1 = json.loads(data1)
price = data1["mods"]["itemlist"]["data"]["auctions"][0]["view_price"]
print(price)


