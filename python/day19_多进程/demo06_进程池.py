#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo06_进程池
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-14
#    Change Activity:  2019-02-14:


from multiprocessing import  Pool
import os

def foo(name):
    print("foo", name)
    return name


if __name__ == '__main__':
    #1 打印主进程的pid
    print("main--- %d " % os.getpid())

    #2 创建进程池，已经存在了进程对象

    '''
    pool 表示进程池，事先已经存在了一些进程对象，直接分配任务即可
    第一个参数，numprocess 进程池中子进程对象数量
    第二个参数，子进程要执行的任务
    '''
    pool1 = Pool(3, foo, ("王二狗",))  #创建进程池并且分配了任务，一旦分配了任务就会自动执行
    #step 创建进程池，step2 apply()分配任务