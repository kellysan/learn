#! /usr/bin/env python
# @Author : sanyapeng

'''
元组： tuple与列表累死，都适用用于存储一组数据
    和列表区别：
    1 列表是允许修改，但是元组一旦创建，内容不能修改
    2 列表使用 [] 元组使用()
元组的使用：
    A 元组的创建
        () 直接创建
        type(序列)
    B 元组的操作
        索引 tuple[index]
        切片 tuple[start,end]
'''

t1 = ("王二狗",18,"男","北京市冒烟胡同xx路")
print(t1)
print(t1[0])

index = 0
while index < len(t1):
    print(t1[index])
    index += 1

print()

for i in t1:
    print(t1)