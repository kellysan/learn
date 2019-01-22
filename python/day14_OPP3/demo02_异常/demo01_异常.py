#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo01_异常
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/21
#    Change Activity:  2019/1/21:

"""
异常，就是不正常
    程序执行额过程中，发生了不正常事件，导致程序无法正常的执行到结束
    不正常事件，python 的解释器遇到了一个错误，就会抛出一个异常帝乡，打断程序的执行
"""
"""
需求，接收用户的输入的整数 + 10 进行输出

"""


str1 = input("信息：")
sum = 10 + int(str1)
print("结果是，%d" % sum)
print("voer")