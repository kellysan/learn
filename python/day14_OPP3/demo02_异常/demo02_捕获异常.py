#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_捕获异常
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/21
#    Change Activity:  2019/1/21:

"""
捕获异常，异常的一种处理方式
语法
try：
    有可能产生错误的代码
except 异常类型
    pass

except 异常类型2
    pass

except (异常3，异常4)
    pass
"""

str1 = input("信息：")
try:
    sum = 10 + int(str1)
    print("结果是，%d" % sum)
except ValueError:    #问题类型比较重要

    #程序出现错误，会进行处理
    print("输入的字符有误无法计算")

print("voer")


"""
练习1 自己设计一段代码有可能出现异常
"""