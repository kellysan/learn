#! /usr/bin/env python
# @Author : sanyapeng

def getDayOfMonth(month):
    '''
    用于根据给定的月份获取天数
    :param month
    :return:  返回天数
    '''

    day = 0
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = 31
    elif month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
        day = 30
    elif month == 2:
        day = 28
    return day

def getDays(month):
    # 1-month 前一个月的总天数
    i = 1
    sum = 0
    while i < month:
        sum  += getDayOfMonth(i)
        i += 1

    return sum
print(getDays(5))