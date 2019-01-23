#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_抛出异常
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/22
#    Change Activity:  2019/1/22:

"""
异常：
   程序执行过程中，不正常，python 解释器创建了这种类型异常的对象
       异常的对象


异常类型 class
Exception
ValueError



抛出异常： reise
    程序中主动抛出一个异常独享。
    需求，接收用户输入的密码 ，长度至少为8 否则抛出异常
1 接收用户输入
2 密码判断长度
3 少于8 抛出一个异常对象

语法
e1 = Exception("ddddd")
raise e1
"""
def input_password():
    pwd = input("请输入密码")

    if len(pwd) > 8:
        return pwd

    #产出异常对象抛出
    print("主动抛出异常")

    e1 = Exception("密码长度不够")

    # 抛出异常对象

    raise e1


res = input_password()
print("shu",res)
