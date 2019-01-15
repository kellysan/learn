#! /usr/bin/env python
# @Author : sanyapeng


'''
装饰器:如果一个函数的定义已经完成，需要在不修改改函数的情况下，进行功能扩容
    使用装饰器



函数式编程。函数功能强大，函数可以看成变量，做为参数，作为返回值，高阶函数，闭包

耦合性，藕断丝连
    低耦合，降低程序耦合性

程序设计，开放，封闭
   封闭 对于已经实现好了的功能进行封闭
   开放，对外扩展开放



思路步骤：
step1 定义一个原始函数
step2 定义一个装饰器函数，闭包应用
'''

#定义装饰器函数

def strong(fun):
    print("开始装饰")
    #定义一个内部函数，增强fun函数功能
    def new_hello():
        print("我是装饰器中的新增功能，before")
        fun()  #如果有，就行相当于在员工能上扩展，如果没有，将原功能重新实现
        print("我是装饰器中的新增功能，after")
    print("结束")
    return new_hello

#1 先定义一个函数
@strong
def hello():
    print("hello 王二狗，这个是hello函数中的代码")


hello()


@strong
def test():
    print("另一个函数")

test()