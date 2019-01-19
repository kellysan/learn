#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo03_单利设计模式
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/19
#    Change Activity:  2019/1/19:

"""
设计模式： Design pattern
    设计模式是前人工作的总结和提炼，通常，被人们广泛流传的设计模式是指很对某一特定的问题的成熟解决方案。
    使用实际模式是为了可重用代码，让代码更容易 被他人理解

单例模式：一个类执行能产生一个对象,内存中只有也一个地址

类名() --> 含义 创建对象
    step1 开辟内存，创建对象
    step2 执行 init()

应用：
   播放器
   回收站
   程序连接数据库
       连接-->单例

"""

class A:
    pass

a1 = A()
a2 = A()
a3 = A()


class Connection:
    pass

c1 = Connection()
