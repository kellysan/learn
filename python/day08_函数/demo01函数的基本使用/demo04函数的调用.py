#! /usr/bin/env python

def test1():
    print("我是函数test1")


def test2():
    print("我是函数test2")


def test3():
    print("我是函数test3")
    test2()
    print("over")


test3()
test2()

'''
定义一个函数用于打印一行线
定义一个函数用于打印三行线
'''

def print1():
    print('_'*50)

print1()

def print_more(n):
    i = 1
    while i < n:
        print1()
        i += 1

print_more(44)

'''
求三个数的和
'''

def getSum(a,b,c):
    return a + b + c

print(getSum(10,20,30))
def getAvg(a,b,c):
    avg = getSum(a,b,c) /3
    return avg

print(getAvg(10,20,30))