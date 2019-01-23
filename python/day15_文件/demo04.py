#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/22
#    Change Activity:  2019/1/22:


"""
判断条件
    1 空为假
    2 0 为假

read() 读取文件所有数据
read(num) 读书数量
readline() 读取一行
readlines()读取每一行返回一个列表
"""

f = open("test.txt")

# while True:
#     #concent = f.read(10)
#    # concent = f.readlines()
#     concent = f.readline()
#     print(concent)
#
#     if not concent:
#         break

for line in f:
    print(line)
f.close()


