#! /usr/bin/env python
# @Author : sanyapeng

'''
默认值参数
    1 概念：定义一个函数的时候，直接给形参赋值，叫做默认值参数

    2 语法：
        def 函数名(a,b='xxx')
    3 
'''

def test1(a,b=10):
    print(a)
    print(b)
    print("over")

test1(100,1000)  #如果传入了实参，就不适用默认参数
test1(1,)  #如果没有传入参数，使用默认参数