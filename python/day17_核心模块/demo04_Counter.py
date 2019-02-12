#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04_Counter
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/2
#    Change Activity:  2019/2/2:


from collections import  Counter


#5 most_coummon(n)
str1 = "12hdosonvajfodaogjoajfoafoaojgaoroajdfsdsdfoadhogqreasdvoangofadshfochdsovjaofaochdvsogfhaoserwajv"
c1 = Counter(str1)
print(c1)
for k,v in c1.items():
    print(k,v)
print(c1)
res = c1.elements()
newlist = sorted(res)
print(newlist)
new = c1.most_common(3)
print(new)


"""
练习1： 给定字符串统计每个字符出现的次数
练习2： 给定一个列表中人名出现的次数["jack","David","Tom",","David","Tom","Lucy","David","David"]

"""
name_list = ["jack","David","Tom","David","Tom","Lucy","David","David"]
c2 = Counter(name_list)
print(c2)
for k,v in c2.items():
    print(k,v)