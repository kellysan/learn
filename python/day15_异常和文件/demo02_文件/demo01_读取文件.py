#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_文件
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/22
#    Change Activity:  2019/1/22:

"""
step1 打开文件

step2 读取数据，写出数据

step3 关闭连接
"""

#1 打开文件

file1 = open(r"test1.txt",encoding="utf-8")
#file1 = open(r"test1.txt")

concent = file1.read()

print(concent)

file1.close()