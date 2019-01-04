#! /usr/bin/env python
# @Author : sanyapeng

'''
递归函数：
    函数调用自己

    注意：
        1. 递归要有出口
        2. 逐渐向出口靠近
        3.

例：求1-5的和
定义一个函数，用于求1-n的和 get_sun()
n = 5 get_sum(5) 求1-5的和
1-4的和 ，加5
n = 4 get_sum(4) 求1-4的和
    get_sum(5) = get_sum(4) + 5
n = 3 get_sum(3)
    get_sum(4) = get_sum(3) + 4
n = 2
    get_sum(3) = get_sum(2) + 3

n = 1
   get_sum2 = get_sum(1) + 2
'''

def getSum(n):
    print('****')
    if n == 1:
        return 1
    else:
        return getSum(n-1) + n

print(getSum(5))


def getJc(n):
    print('***')
    if n == 1:
        return 1
    else:
        return getJc(n-1) * n

print(getJc(5))