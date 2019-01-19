#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_多态性
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/18
#    Change Activity:  2019/1/18:


"""
多态性，多种形态
    以继承和重写为前提，创建的不同的对象，执行的方法也不同

    多态性 对于强数据类型的语言提现比较明显 java
    而，python 是弱类型语言，对于多态的提现并不明显，推崇的是鸭子类型

    鸭子类型：


父类 Person
子类 Student
"""
class Father:

    def say(self):
        print("爸爸说话了，回家吃饭了")

class Son(Father):


    #子类重写
    def say(self):
        print("子类重写父类的方法，儿子说，我不吃饭了")


def my_test(obj):
    if isinstance(obj,Son):
        obj.say()
    else:
        print("不是父子，别哔哔")


f1 = Father()

my_test(f1)

s1 = Son()

my_test(s1)