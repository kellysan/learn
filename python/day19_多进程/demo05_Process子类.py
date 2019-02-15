#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo05_Process子类
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-14
#    Change Activity:  2019-02-14


"""
多进程 多任务
    创建进程的方式
    1 其他操作系统 linux  mac windows除外 os.fork() 不是跨平台
    2 使用multiprocessing 包下的 Process 类
        创建Process 类的对象，就是创建一个进程对象， start
        p1 = Process(target= "任务")
    3 我们创建一个子类，继承Process
         run()
"""

from multiprocessing import  Process
import os
import time

#1 定义子类，用于进程类

class MyProcess(Process):
    #重写run
    def run(self):
        for i in range(10):
            print("My_Process，pid: %d,i --> %s" % (os.getpid(),i))
            time.sleep(1)


if __name__ == '__main__':
    #1 创建一个子进程对象
    p1 = MyProcess()
    p1.start()
    p1.is_alive()
    p1.join()
    print("子进程结束，主进程也结束")