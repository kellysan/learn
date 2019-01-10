#! /usr/bin/env python
# Autor: sanyapeng


'''
lambda 表达式
    语法：
       lambda 形参列表 ： 表达式
    函数的本质，函数名指向了函数对象，
        可以向普通的变量一个样，赋值给别人，也可以改变数值

        def test()
           pass

        a = test 相当于把a赋值成函数

'''

#定义一个普通函数

def test1(a, b):
    return a + b

print(test1(1,5))

#使用lambda 表达式

print(test1)
num = lambda a, b, c: a + b + c
print(num(1,2,3))

print("*"*100)

lam1 = lambda a,b : a + b
lam2 = lambda a,b : a - b

def test7(num1,num2,oper):
    return oper(num1,num2)

print(test7(10,20,lam1))
print(test7(100,8,lam2))

print(test7(100,30,lambda a,b : a + b))