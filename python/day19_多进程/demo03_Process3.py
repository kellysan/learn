#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo03_Process3
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-14
#    Change Activity:  2019-02-14:


from multiprocessing import  Process
import time
import os


def worker_1(interval):
    print("worker_1，父进程 {}")