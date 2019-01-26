#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo05_random
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/26
#    Change Activity:  2019/1/26:
"""
random 模块，随机
"""

import random

#1 获取随机小数  包含0 不包含1 [0,1)  0 <= x < 1
num1 = random.random()
print(num1)

#2 获取随机整数
num2 = random.randint(1,10)  # 1 <= x <= 10
print(num2)

#获取 n, n+1 之间的小数

num3 = random.uniform(1,10)
print(num3)

#4 在指定的范围去获取
num6 = random.randrange(1,10,2)
print(num6)

num7 = random.randrange(2,50,2)
print(num7)

#5 从指定的序列中获取 字符串，列表，元组
s1 = "王二狗喜欢李小花，他们都喜欢学习python"
list1 = ["李小花","王二狗","kiven","alex"]
print(random.choice(s1))
print(random.choice(list1))


#6 将一个列表随机打乱
#random.shuffle
random.shuffle(list1)
print(list1)

#7 取样，截取部分
list2 = [1,2,3,4,5,6,7,8,9,10]
test4 = random.sample(list2,4)
print(test4)