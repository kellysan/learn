#! /usr/bin/env python
# @Author : sanyapeng
'''
序列解包：
    可以一次性将序列找那个的元素赋值给多个变量
    要求，变量的数量和序列的长度对应
'''

s1, s2, s3, = "你好啊"
print(s1)
print(s2)
print(s3)
#print(s4)


list1 = [10, 20, 30]
l1, l2, l3 = list1
print(l1)
print(l2)
print(l3)


t1, t2, t3 = (40,50,60)
print(t1)
print(t2)
print(t3)
