#! /usr/bin/env python
# @Author : sanyapeng



def test2():
    print("打印test2 ...")


a = test2
print(type(a))
a()


# 3 给函数重新赋值

def test3():
    print("打印test3")

test3()
b = test3
b()


'''
函数的本质
'''