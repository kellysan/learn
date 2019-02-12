#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo03_deque
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/31
#    Change Activity:  2019/1/31:
"""
deque 双端队列
"""
from collections import deque

deque1 = deque([10,20,30,40])
print(deque1)

deque2 = deque([10,20,30,40,50])
print(deque2)


# 操作队列
deque2.insert(4,60)
print(deque2)


deque2.pop()
print(deque2)