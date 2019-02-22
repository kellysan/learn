#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo09_队列
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-22
#    Change Activity:  2019-02-22:

from multiprocessing import Queue



if __name__ == '__main__':

    q = Queue(3)
    print(q.empty())
    print(q.full())

    q.put("消息1")
    q.put("消息2")
    print(q.get())
    print(q.get())