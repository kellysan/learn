#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo05_defaultdict
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/2
#    Change Activity:  2019/2/2:

"""
带默认值的字典，如果这个值不存在，获取key对相应的value值报错 K

defaultdict(函数)
    创建一个字典，如果可以不存在，获取默认
"""
from collections import  defaultdict

dict1 = {"name":"王二狗","age":30}


print(dict1["name"])
#print(dict1["ag"])  报错


def foo():
    return "无结果"

#dict2 = defaultdict(foo)
dict2 = defaultdict(lambda :"None")

print(dict2)
print(dict2["age"])
dict2["name"] = "sanyapeng"
print(dict2)
print("-"*50)

