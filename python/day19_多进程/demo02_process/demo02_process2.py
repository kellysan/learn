#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_process2
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-14
#    Change Activity:  2019-02-14:

from multiprocessing import  Process
import os


if __name__ == '__main__':
    #1 打印主进程的id号
    print("main pid %d" % os.getpid())

    #2

    def my_sum(x,y):
        return x + y

    sum = lambda x,y: my_sum(x,y)
    print("--->", sum(10,20))



