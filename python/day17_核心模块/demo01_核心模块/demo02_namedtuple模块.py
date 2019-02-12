#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_namedtuple模块
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/30
#    Change Activity:  2019/1/30:


"""
namedtuple 模块
    是一个函数，创建一个自定义的tuple对象
       可以给tuple元素起名字，也可以定义元素的个数

"""
"""
类描述

type(变量) 获取该变量的类型
isinstance(变量，类型)  bool
issubclass 子类
"""
from collections import  namedtuple
print(namedtuple)
print(type(namedtuple))


#判断一个类是不是一个类的子类  issubclass(子类，父类)
#判断一个类型  isinstance("a",str)

Point = namedtuple("Point",["x","y"])

#1 创建元组存储数据

tuple1=(10,20)
p1 = Point(10,20)
print(tuple1)
print(p1)

# 2 获取数据
print(tuple1[0])
print(p1[0])
print(p1.x)   #通过属性名获得数据

# 3 关于数据的修改
# 元组类型不让改


#4 实例方法__replace()  修改某个属性值，但是返回一个新的对象

p2 = p1._replace(y="a")

print(p1)
print(p2)

#5 扩展 _make 也可以用于创建point对象，参数iterable
p3 = Point._make([100,200])
print(p3)


#6 asdict()

d3 = p3._asdict()
print(d3)

#7 属性
print(Point._fields)

# 解包
a,b = p1
print(a)
print(b)

#循环取
for i in p1:
    print(i)

