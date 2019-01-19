#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04_new方法
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/19
#    Change Activity:  2019/1/19:



"""
a1 = A()
    step1 开辟内存，创建对象
    step2 自动执行init方法

__new__()  #由object 类所提供的一个内置的静态方法，主要有两个作用
    1 在内存中为对象分配空间
    2 返回对象的引用
    3 将对象创建后的引用，复制给对象

python 的解释器获取到对象的引用，会调用init方法，把引用的作为self 的参数

重写new方法的代码比较固定
   1 调用object 的new方法，创建对象
   2 返回改对象，如果不反悔python的解释器读取不到该对象
"""
class A(object):

    def __new__(cls, *args, **kwargs):
        """
        new 专门用于开辟内存，创建对象，并返回对象
        :param args: 多值的元组参数
        :param kwargs: 多值的关键字参数
        :return:
        """
        print("new方法，创建对象，分配内存")
        # 2. 分配内存，返回对象的引用
        instance = object.__new__(cls)  #用于创建对讲，分配内存，得到的结果就是对象
        print("---->", instance)

        # 3 将instance 返回
        return  instance
    def __init__(self):
        print("init方法。。。。",self)


a1 = A()  #到底发生了什么
print(a1)