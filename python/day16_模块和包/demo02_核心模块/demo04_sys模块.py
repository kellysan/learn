#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04_sys模块
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/26
#    Change Activity:  2019/1/26:

"""
sys system 的缩写
    sys 模块中，定义的是和系统一些相关的信息内容

当执行demo04.py 文件的时候，可以直接接传入一些参数，有sys.arav来接收，列表，第一个元素是文件名
"""

import  sys
#1 获取系统参数
list1 = sys.argv
print(list1)


#2 结束程序
print("程序执行过程中。。。。")
#sys.exit(0)
print("程序执行结束")


# 程序执行时使用的模块信息

for item in sys.modules:
    print(item)