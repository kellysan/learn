#! /usr/bin/env python
# Autor: sanyapeng


'''
关键字参数，使用函数的时候实参赋值给形参，调用时候写清楚形参的名字
  如果传入的实际的关键字参数和形参列表对不上使用**kw（keyword），接收之后封装为字典
'''

def test1(a,*b,c):
    print("a", a)
    print("b", b)
    print("c", c)

test1(10,20,30,c=40)

def test3(name="王二狗",age=30,**kwargs):
    print("name", name)
    print("age", age)
    print("kw", kwargs)


test3("李小花",age=18,sex="女",country="中国")
