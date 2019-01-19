#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo01_身份运算符
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/19
#    Change Activity:  2019/1/19:


"""
is  判断两个引用是不是同一个对象，相当于判断地址
is not 判断两个引用是不是同一个对象，相当于判断地址

== 关系运算符 ，判断数值是否相等

"""

a = [10,20,30,40]
b = [10,20,30,40]
c = b


print(a == b)
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(b is c)
print(a is not b)