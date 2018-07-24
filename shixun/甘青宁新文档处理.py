# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:29:00 2018

@author: 10257
"""

f= open("甘青宁新.txt","r",encoding='gbk').readlines()
School =[]
Number =[]
for line in f:
    School.append(line.split("(")[1].split(",")[0])
    Number.append(int(line.split(",")[1].split(")")[0]))
print(School)
print(Number)