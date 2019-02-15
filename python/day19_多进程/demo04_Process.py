#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04_Process
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-14
#    Change Activity:  2019-02-14:


"""
join 堵塞主进程，等待子进程结束
terminate()  结束进程，不管子进程是否完成
"""
from multiprocessing import  Process
import  os
import  time



def test():
    print("\t子进程的pid %s" % os.getpid())
    for i in range(10):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    print("父进程的pid %s" % os.getpid())

    p1 = Process(target=test)
    p1.start()

    time.sleep(3)
    p1.terminate()
    print("父进程结束")