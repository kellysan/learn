#! /usr/bin/env python
# @Author : sanyapeng
'''
闭包的应用
    1 惰性求职（lazy）延迟求职
        迭代器的底层原理就是惰性求职

    2 计时器 10，9，8，7...1

    3 装饰器
'''


#定义一个函数
def test1(msg):
    def say_msg():
        print("hello: {}".format(str(msg)))
    return  say_msg

say = test1("王二狗")
say()
say()
say()
say()



def count_down(num):

    def next():
        nonlocal  num
        temp = num
        num -= 1
        return temp
    return next


next = count_down(10)
print(next())
print(next())