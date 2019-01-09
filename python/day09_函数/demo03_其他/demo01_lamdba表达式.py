#! /usr/bin/env python
# Autor: sanyapeng


'''
lambda 表达式
    语法：
       lambda 形参列表 ： 表达式
'''

#定义一个普通函数

def test1(a, b):
    return a + b

print(test1(1,5))

#使用lambda 表达式

print(test1)
num = lambda a, b, c: a + b + c
print(num(1,2,3))

