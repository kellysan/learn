#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo06_copy模块
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/28
#    Change Activity:  2019/1/28:

"""
拷贝：
    浅拷贝，只是拷贝了地址，没有真正的拷贝数据
        相当于共享

    深拷贝，将变量的数据，全部拷贝
copy 模块

"""
import copy

#浅拷贝
a = [10,20,30]
b = a
print(b)



print(copy)
print(type(copy))

e = copy.deepcopy(a)
print(e)
a[0] = 1000
print(a)
print(e)