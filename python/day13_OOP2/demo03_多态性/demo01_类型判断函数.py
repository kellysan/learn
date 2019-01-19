#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo01_类型判断函数
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/18
#    Change Activity:  2019/1/18:

"""
type 返回变量类型
instance(变量，类型) -- bool

"""


class A:
    pass

class B(A):
    pass

class C:
    pass

a = A()

print(type(a))


print(isinstance(a,A))
print(issubclass(C,A))
print(issubclass(B,A))