#! /usr/bin/env python
'''
python中的函数可以嵌套声明
定义一个函数：
    还可以在定义一个内部的函数
'''

def outer1():
    print("我是一个函数")

    def inner1():
        print("我是函数里的函数。。 内部函数")

    inner1()
outer1()