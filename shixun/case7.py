# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:37:51 2018

@author: 10257
"""
import urllib.request as r
import json
url = []
for i in range(0,100):
    i+=44
    url.append("https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s="+str(i)+"&ajax=true")

def PaQu():
    f=open('淘宝数据.csv','w',encoding='gbk')
    for i in range(100):
        data = r.urlopen(url[i]).read().decode('utf-8','ignore')
        data = json.loads(data)
        for i in range(40):
            f.write(data["mods"]["itemlist"]["data"]["auctions"][i]["view_price"]
            ,data["mods"]["itemlist"]["data"]["auctions"][i]["view_sales"],
            data["mods"]["itemlist"]["data"]["auctions"][i]["raw_title"]+'\n')            
    f.close()
    print("爬取结束")
PaQu()

  