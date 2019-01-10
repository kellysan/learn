#! /usr/bin/env python
# Autor: sanyapeng

'''
一、列表推导，用于快速产生一个列表（列表生成式）
   [表达式， for x in 范围]
   [表达式 for x in 范围 for y in 范围]

   满足该公式，所有范围的数 列表中
      内存中，列表推导范围大，一次性产生所有数据存入了列中

二、生成器（generator）
    生成器，在python中，一边循环，一边产生数据，就叫做生成器
        理解，按照某种规则，产生数据

    方法一，只要把列表推导的[] 改成()

'''

#列表推导'
# 1，产生1-10的列表
list1 = [x for x in range(1,11)]
print(list1)

#产生1-10 的平方
list2 = [x ** 2 for x in range(1,11)]
print(list2)

#产生0-20 偶数

list3 = [x for x in range(1,20) if x % 2 == 0]
print(list3)

#
list4 = [int(str(x)+str(y)) for x in range(1,10) for y in range(0,10)]
print(list4)

# 2.生成器 创建生成器 [] 改为 ()
print("-"*30)
gen1 = (x for x in range(1,5))
print(gen1)
print(type(gen1))


#根据生成器对象，获取数据
'''
生成器的使用
step1 创建生成器对象 公式 （x for i in 范围） generator

step2 获取生成器数据
    调用next(生成器对象)
'''
print(next(gen1))
print(next(gen1))
for x in gen1:
    print("--->", x)