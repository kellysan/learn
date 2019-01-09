#! /usr/bin/env python
# @Author : sanyapeng

'''
默认值参数
    1 概念：定义一个函数的时候，直接给形参赋值，叫做默认值参数

    2 语法：
        def 函数名(a,b='xxx')
    3

    1 混合参数，
        位置参数：必须传入的实参
        默认参数 参数名=默认值
        可变参数 *args
            可变参数也只能有一个，
    2 如果参数用列表或者元祖传出，需要用*解包
'''

# def test1(a,b=10):
#     print(a)
#     print(b)
#     print("over")
#
# test1(100,1000)  #如果传入了实参，就不适用默认参数
# test1(1,)  #如果没有传入参数，使用默认参数



def test3(*n):
    sum = 0
    for i in n:
        sum += i
    return sum

res = test3(1,2,3,4,5)
print(res)

list1 = [1,2,3,4,5]
print(sum(list1))


def test4(*n):
    return sum(n)

print(test4(1,2,3))


def test5(*args):
    str1 = ""
    for s in args:
        str1 += s

    return str1

str2 = test5("aa","gg","dd")
print(str2)


#列表中，有位置参数，也有可变参数


#列表中，有位置参数，有默认参数，有可变长参数


def test7(x,y=10,*z):
    print("x", x)
    print("y", y)
    print("z", z)

test7(11)
test7(10,20)
test7(10,20,30,40)


def test9(x,*args1):
    print("x", x)
    print("args1", args1)


test9(10,*[1,2,3],*[4,5,6])