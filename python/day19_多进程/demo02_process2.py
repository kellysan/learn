#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_process2
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-14
#    Change Activity:  2019-02-14:


from multiprocessing import Process
import os
import time

def test(*num):

    print("\t我是子进程，我的pid是 %s " % os.getpid())
    print("\t子进程接收到的参数",num)
    time.sleep(5)




if __name__ == '__main__':
    print("main ... pid: %s" % os.getpid())
    #创建子进程


    '''
   第一个参数 target 它代表的子进程要执行的任务，一个可执行对象
   第二个参数 name  进程的名字，如果不指定的系统编号  Process-1
   第三个参数 args 一个元组， 表示要传递给target目标的参数
   第四个参数 kw 关键字参数，字典
   第五个参数 group 绝大多数用不到
    '''
    p1 = Process(target=test, name="子进程", args=(1000, "王二狗"))
    p1.start()

    #子进程的名字
    print("子进程的名字 %s" % p1.name)

    p1.join()  #合并 参加 等待子进程结束
    print("主进程执行")
    """
    主进程中启动了子进程，在自己成没结束之前，主进程不会结束的
    p.join() 子进程执行结束后，主进程才会继续执行
    p.join(timeout) 子进程结束了，那么解除阻塞，主进程继续执行，时间到了也会解除阻塞，主进程还是会继续执行
    
    """