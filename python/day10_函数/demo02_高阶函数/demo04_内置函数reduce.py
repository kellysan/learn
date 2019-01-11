#! /usr/bin/env python
# @Author : sanyapeng

'''
reduce()规约
   1 python3 中reduce()不在是内置函数，移到 functiontools模块
   2 reduce()
       第一个参数 func
           def fun(x,y)
               return
       第二个参数 序列
          [元素1，元素2]
       第三个参数，初始值
'''

from functools import reduce

#累计求和
def get_sum(a,b):
    return a + b

list = [1,2,3,4]

res = reduce(get_sum,list,0)
print(res)

#改成lambda
res2 = reduce(lambda a,b:a+b,list,10)
print(res2)


#阶乘
'''
1 函数
2 序列
3 初始值
'''
res3 = reduce(lambda a,b:a * b,[1,2,3,4,5],1)
print(res3)

res4 = reduce(lambda a,b:str(a) + str(b),[1,3,5,7,9],"")
print(res4)