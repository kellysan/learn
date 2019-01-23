#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo01_异常的传递
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/22
#    Change Activity:  2019/1/22:



# 定义也一个函数

def get_host(key):
    if key =="1":
        rough = 3
    elif key == "2":
        rough = 4

    return  rough




res = get_host("1")
print(res)

res = get_host("2")
print(res)