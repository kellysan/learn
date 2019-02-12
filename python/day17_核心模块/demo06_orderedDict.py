#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo06_orderedDict
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/2
#    Change Activity:  2019/2/2:

"""
orderedDict  有序字典，存储的顺序
"""

from collections import  OrderedDict
print(type(OrderedDict))
print(issubclass(OrderedDict,dict))

dict1 = OrderedDict()
print(dict1)

dict1["name"] = "王二狗"
dict1["age"] = 20
dict1["sex"] = "男性"
print(dict1)

#1 key value

keys = dict1.keys()
for keys in keys:
    print(keys,dict1.get(keys))

#2item
items = dict1.items()
for items in items:
    key,value = items
    print(key,value)


#item
for k,v in dict1.items():
    print(k,v)

print("-"*50)