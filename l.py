# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:59:19 2023

@author: USER
"""
print('________________1__________________')
x={'hello':21,"hi":'reply'}
for key,values in x.items(): 
  print(key,x.get(key))
print('________________2__________________')
var={"carrot":{'quant':5,'price':100},'avoccado':{'quant':10,'price':300},
       'mango':{'quant':6,'price':900},"blueband":{'quant':9,'price':400}}
v=sum(item['quant']*item['price'] for item in var.values())
print(v)