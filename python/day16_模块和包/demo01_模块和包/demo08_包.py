#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo08_包
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/25
#    Change Activity:  2019/1/25:


"""
包 package
    1 概念
        包就是包含多个模块的一个特殊目录
        目录下有__init__.py 的文件
        包名的命名方式，满足标识符命名规范，字母小写，下划线连接

    2 导入包
        A 导入包下某个模块
             import 包名.模块 as
        B 导入该包下所有文件
            from 包名 import *
            设置下包下__init__.py 导入包的初始化文件
"""
import test包.d

test1()