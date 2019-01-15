#! /usr/bin/env python
# @Author : sanyapeng


on_strong1 = True
on_strong2 = False


def strong1(fun):
    if on_strong1:
        def new_test1():
            print("strong1增强函数")
            fun()
        return new_test1
    else:
        return fun


def strong2(fun):
    if on_strong2:
        def new_test1():
            print("strong2增强函数")
            fun()
        return new_test1
    else:
        return fun

@strong1
@strong2
def test1():
    print("原始函数")


test1()