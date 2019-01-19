#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo03_鸭子类型
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/18
#    Change Activity:  2019/1/18:


class A:

    def say(self):
        print("A 类型可以说话了")


class B:

    def say(self):
        print("B 类型可以说话了")


def test(obj):
    obj.say()


t1 = A()

t2 = B()

test(t1)
test(t2)