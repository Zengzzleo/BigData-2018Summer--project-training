# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:37:33 2018

@author: 10257
"""

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'

def getHTMLText(url):
    c=0
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
    
    f=open('all_school.txt','r',encoding='utf-8')
    Xlist = []
    for i in range(2300):
        a = f.readline().split("-")
        a = a[2]
        a= a.split(".")
        a =a[0]
        Xlist.append(a)
    f=open("高考派数据",'a',encoding='utf-8')
    for x in Xlist:
        for t in range(1,3):
            for l in range(62,66):
                urls =('id={}&type={}&city={}&state=1'.format(x,t,l))
                req=r.Request(url,data=urls.encode(),headers=headers)
                Page=r.urlopen(req).read().decode('utf-8','ignore')
                f.write(Page+"\n")
        if x:
            c += 1
            print(str(c)+"写入代号为"+x+"的学校信息")
            
    print("写入成功")
    f.close()
getHTMLText(url)

    
            

           
