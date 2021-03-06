#! /usr/bin/env python
'''
注释，解释说明函数
    文档注释
        函数内置的属性， __doc__,使用该属性获取某个函数的文档说明注释，如果么有文档注释就是none
    添加文档注释：
       1 使用 3 引号包裹起来的部分叫做文档注释
       2 文档注释的第一行，通常用于编写该函数的功能
       3 然后一个空行
       4 对函数进行详细的描述，参数，返回值
'''

def getSum(a,b):
    '''
    该函数用于两个数的求和
    :param a 累加的第一个参数
    :param b 累加的第二个参数
    :return: 求和的结果
    '''
    return  a + b

print(getSum(10,10))
print(getSum.__doc__)