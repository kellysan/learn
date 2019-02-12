#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo95_counter
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/31
#    Change Activity:  2019/1/31:


"""
统计集合中元素出现的次数
counter 是dict 的一个子类 也包含key value
"""

from collections import Counter

#1 创建一个计数器

print(Counter)
print(type(Counter))

# 创建一个counter(string) 计数器对象，统计字符串中每个字符出现的次数
c1 = Counter("aaodjfoahfgoashfoajofhaofhoadshfoahfohasofg")
print(c1)

c2 = Counter([10,20,10,20,30,10,30,10])
print(c2)

#通过字典来创建
c3 = Counter({"a":3,"b":5,"c":6})
print(c3)


#通过关键数参数
c4 = Counter(a=3,b=5,c=6)
print(c4)

#elements iterable  将计数器对象转为可迭代对象
it1 = c1.elements()

for i in it1:
    print(i)