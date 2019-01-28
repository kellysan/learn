#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo01_datatime
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/26
#    Change Activity:  2019/1/26:

"""
python 核心模块
1 日期 datatime
   模块名称，和其中的类名称一样 都叫datetime


   1年365天 year %y
   1天24小时 day %d
   1小时60分钟 hour %h
   1分钟60秒  minute %m
   1秒 1000毫秒      %s
   1毫秒 1000微秒
   1微秒 1000纳秒    ns

   类 datetime
       类属性 max min
       类方法 now()，today()

       实例属性：
           年，月，日，时，分，秒，微秒
           year month day hour minute second microsecond

           星期几
           isoweekday
   时间戳：计算机中表示时间，其实是使用一个数字来表示（long类型的整数）
       开始日期 1970年0点0分0点 基准值
       当前日期距离基准值的时间，python中的单位是秒，其他语言都是毫秒

   python格式化日期
   %y  两位的年
   %Y  四位数字表示年份

   %m  表示月份
   %D  表示日期

   %H  表示小时  24小时进制
   %M  表示分钟
   %S  表示秒

"""

from datetime import datetime

print(datetime)
print(type(datetime))


#功能
# 1. 获取当前时间
time1 = datetime.now()
print(time1)
# 结果为 2019-01-26 09:38:17.491226


#2 获取指定时间

#3 类属性
print(datetime.max)
print(datetime.min)

#4 实例属性，获取年月日时分秒
date_msg = "年：%s,月：%s,日：%s，时：%s，分：%s，秒：%s,微秒：%s" %(time1.year,time1.month,time1.day,time1.hour,time1.minute,time1.second,time1.microsecond)
print(date_msg)


"""
练习1 2017年11月27日
练习2 14：30：44秒
"""

#5 now() today() 时区上区别
time3 = datetime.today()
print(time3)


#6 获取星期几

print(time1.weekday())
print(time1.isoweekday())


#7 操作时间戳 timeseamp
#获取时间戳
print("-----------------------------------")
time6 = datetime.now()
print("time6",time6)
time_num = time6.timestamp()
print(time_num)

#将时间戳转换为时间对象
time7 = datetime.fromtimestamp(time_num)
print(time7)

#8 时间和字符串之间的转换
#字符串转换日期
str1 = "2017-10-10" #字符串
time5 = datetime.strptime(str1,"%Y-%m-%d")
print("----",time5)

now_time = datetime.now()


# 日期转字符串
str2 = now_time.strftime(r"%Y-%m-%d")
print("--->",str2)

#9 时间计算
