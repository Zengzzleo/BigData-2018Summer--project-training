# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:57:30 2018

@author: 10257
"""

import urllib.request as r
import json
def PaQu():
    url = list()
    f=open('淘宝数据_西藏.txt','w',encoding='utf-8')
    for i in range(8):
        Page=44*i
        url.append("https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&p4ppushleft=1%2C48&ntoffset=4&loc=%E8%A5%BF%E8%97%8F&s="+str(Page)+"&ajax=true")
    print(len(url))        
    for i in range(8):
        data = r.urlopen(url[i]).read().decode('utf-8','ignore')
        data = json.loads(data)
        f.write(str(data)+'\n')
        print("爬取成功第{}条URl信息\n".format(i+1))
    f.close()
    print('爬取成功')##爬虫
def Result():
    try:
        PaQu()
    except  IndexError as I:
        print(I)
    finally:
        print('爬取结束')
Result()