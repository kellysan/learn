#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_process
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-14
#    Change Activity:  2019-02-14:

"""
多任务，也叫多进程 同时执行多个程序
启动某一个程序，自己创建主进程
    主进程中，可以自己创建子进程
    step1 导入模块
        from multiprocessing import Process
    step2 创建process 类的对象，代表紫禁城

    step3 启动紫禁城，表示可以让cpu调度执行
"""

from multiprocessing import Process
import time
import os

def test():
    for i in range(1,1000):
        print("我在子进程中执行了",i)
        print("\t\t\t子进程的父ID为 {}".format(os.getppid()))
        print("\t\t\t子进程的id为 {}".format(os.getpid()))
        time.sleep(1)


if __name__ == '__main__':

    p1 = Process(target=test)
    p1.start()

    while True:
        print("A 主进程的pid为{}".format(os.getpid()))

        time.sleep(2)



