#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo03_自定义异常
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/22
#    Change Activity:  2019/1/22:

"""
自己定义一次那个，自己定义一个类，继承 Exception或Error 具有了异常类功能
    异常类：产生的对象，异常对象，能够通过raise 关键字抛出，并且打断程序执行

    异常类  Exception

    普通类 Person

    自定义类

"""
"""
定义一个函数，接收用户密码，密码长度小于8 抛出异常，要求的长度，接收的数据长度
"""
#1 定义异常类
