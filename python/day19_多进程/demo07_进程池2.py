#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo07_进程池2
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-21
#    Change Activity:  2019-02-21:



"""
进程池，的操作步骤
step1 创建进程池对象
     p1 = Pool(3)
step2 分配任务
    p1.apply_async(foo, (x,))
同步
轮训
异步
"""
from multiprocessing import Pool
import os
import time


def foo(num):
    for i in range(5):
        print("--pid:{},--num:{}, --i:{}".format(os.getpid(), num, i))
        time.sleep(2)
    return num ** 2

if __name__ == '__main__':

    # 1 创建一个进程池
    pool1 = Pool(8)

    # 2 给进程分配任务
    for x in range(5):
        pool1.apply_async(foo, (x,))  #给主进程使用apply_async()给进程


    pool1.close() #不给进程池再分配任务了，关闭进程池
    pool1.join()  # 如果没有join 主进程结束，子进程不能执行，可能任务还没及执行完毕
    print("子进程结束")
    print("主进程结束")
