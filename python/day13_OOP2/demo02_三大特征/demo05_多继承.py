#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo05_多继承
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/17
#    Change Activity:  2019/1/17:

"""
多继承
    子类可以同时拥有多个父类功能

    注意点 不要在两个父类中使用同名方法

"""
class A:

    def fun1(self):
        print("A")


    def test1(self):
        print("A 中test1")

class B:

    def test1(self):
        print("B 中test1")

class C(A,B):
    pass

b = B()
b.test1()
c = C()
c.test1()


