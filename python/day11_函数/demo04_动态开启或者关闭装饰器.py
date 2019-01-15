#! /usr/bin/env python
# @Author : sanyapeng

'''
定义一个bool 类型的变量，用于开启和关闭装饰器
    on：
        True 使用装饰器
        False 不适用装饰器

'''

on = False


def strong(fun):


    if on:  #on 表示开启装饰器，
        def new_hello():
            print("新增功能")
            fun()
            print("新增功能")
        return  new_hello
    else:
        return fun

def hello():
    print("我是hello，你是二狗么")



hello = strong(hello)
hello()