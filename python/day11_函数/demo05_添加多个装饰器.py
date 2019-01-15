#! /usr/bin/env python
# @Author : sanyapeng
'''
装饰器：
    定义一个装饰函数(原始函数)
        内层函数，增强原始函数功能，retrun内层函数
添加多个
'''


def strong1(fun):
    def new_hello():
        print("装饰器1，新增功能")
        fun()
    return  new_hello


def strong2(fun):
    def new_hello2():
        print("装饰器2，新增功能")
        fun()
    return new_hello2


@strong1
@strong2
def hello():
    print("原始函数")


hello()

