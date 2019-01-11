#! /usr/bin/env python
# Autor: sanyapeng

'''
高阶函数：
    函数名理解为变量，
    将一个函数作为返回值，是高阶函数的另一种形式
'''


def foo(x):
    return x ** 3

def test1(x,y,fun):
    return fun(x) + fun(y)

print(test1(2,3,foo))

print(test1(5,-8,abs))

