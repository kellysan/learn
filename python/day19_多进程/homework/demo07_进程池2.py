#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo07_进程池2
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-21
#    Change Activity:  2019-02-21:

from multiprocessing import Pool
import os

def foo(x):
    for i in range(10):
        print("main--",x,os.getpid())

if __name__ == '__main__':

    #1 创建一个进程池
    pool1 = Pool(3)

    #2 给进程分配任务
    for x in range(5):
        pool1.apply_async(foo,(x,))

    pool1.close()
    pool1.join()