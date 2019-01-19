#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_slot
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/19
#    Change Activity:  2019/1/19:


"""
使用 __slots__() 定义一个元组，元组中出现的属性名，就是该类对象可以有的属性，否则不允许添加
"""

class Student:
    __slots__ = ("name","age")  #student 对象属性只有 name和age
