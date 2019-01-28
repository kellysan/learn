#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       homework
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/28
#    Change Activity:  2019/1/28:


"""
课堂作业
1 创建一个列表，长度为10，数据是1-100的随机数
2 创建一个列表，长度为10，数据是1-100的随机偶数

3 打印当前日期

4 打印当前日期，按照指定的格式：
    格式1 2017年11月27日
    格式2 2017-11-27
    格式3 2017-11-27 16：33：44
    格式4 16：33：44


5 让当前程序睡眠5秒钟，在运行后面代码

第三部分
拼接一个字符串，长度为4，其实就是一个随机生成的验证码
内容是26个 小写字母和26个大写字母，以及数字0-9
0-9 48-57
a-z 97 122
A-Z 65-90

创建一个列表，长度为10，数据是1-10的随机数，要求去重复
"""

import random

#1
list1 = []
while len(list1) < 10:
    num1 = random.randint(1,100)
    list1.append(num1)

print("练习1")
print(list1)
#2
list2 = []
while len(list2) < 10:
    num2 = random.randrange(2,100,2)
    list2.append(num2)


print("练习2")
print(list2)

#3

from datetime import  datetime

print("练习3")
time1 = datetime.now()
print(time1)


print("练习4")
time2 = datetime.now()
time_format1 = "{}年{}月{}日"
print(time_format1.format(time2.year,time2.month,time2.day))
#将日期转换为字符串 格式2
time_format2 = datetime.strftime(time2,"%Y-%m-%d")
print(time_format2)

#格式3
format3 = "%Y-%m-%d %H:%M:%S"
time_format3 = datetime.strftime(time2,format3)
print(time_format3)

#格式4
format4 = "%H:%M:%S"
time_format4 = datetime.strftime(time2,format4)
print(time_format4)

print("练习5")
import time
def test_sleep():
    print("开始打印，等待5秒")
    #time.sleep(5)
    print("5秒结束")

test_sleep()

print(ord("A"))
print(chr(100))


print("第三部分")

list3 = []
while len(list3) < 10:
    num1 = random.randint(1,10)
    if num1 in list3:
        continue
    else:
        list3.append(num1)

print(list3)