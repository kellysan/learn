#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_读取文件的其他方法
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/22
#    Change Activity:  2019/1/22:

"""
read() --读取文件中所有的数据
read(n) num 表示要读取的数据量（字节）
"""

f = open(r"test1.txt")
content = f.read(20)
print(content)
print("-"*10)
content = f.read(10)
print(content)