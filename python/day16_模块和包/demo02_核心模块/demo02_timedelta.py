#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_timedelta
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/26
#    Change Activity:  2019/1/26:

"""
datetime 模块
    类 datetime
       定义时间
    timedelta


时间大小比较
"""

from datetime import datetime,timedelta

# 3天之后的日期
#1 获取当前时间对象
now = datetime.now()

# 获取时间间隔对象 天
delta1 = timedelta(days=3)


# 获取时间间隔对象 小时
delta2 = timedelta(hours=3)

delta2 = timedelta()
#
### 运算
#三天前
time1 = now + delta1
print(time1)

#三天后
time2 = now - delta1
print(time2)

#三小时后

time3 = now + delta2
print(time3)


# 时间对象还可以比较大小

print(time1 < time2)