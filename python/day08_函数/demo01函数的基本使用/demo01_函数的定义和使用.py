#! /usr/bin/env python
# @Author : sanyapeng
'''
方法，也叫函数
    1. 概念
        就是把具有独立功能的一段代码，封装起来，组成一个小的模块，在需要的时候进行调用
    2. 作用
        A 避免重复代码
        B 增强了程序的扩展性
    3. 使用
        step1 函数的定义
        step2 函数的调用
    4. 定义一个函数
        A,定义函数的语法
            使用关键字，
                def 函数名():
                    函数的代码，函数体，方法体
                说明：
                   a)def 关键字 define function 缩写
                   b)函数名，就是一个标识符，字母，数字，下划线组成，数字不能开头，多个单词拼接
                   c)() 是必须的，表示函数的标志，：必须的语法
                   d)函数里代码要注意和函数的声明，有锁紧
        B,调用
            函数名() 进行调用
        C,函数的参数
        D,函数的返回值
'''
print("求1-100的和")

i = 1
sum = 0
while i <=100:
    sum += i
    i += 1
print(sum)


def get_sum(k,v):
    sum = 0
    while k <= v:
        sum += k
        k += 1
    return sum

print("-"*50)
sum = get_sum(1,100)
print(sum)
print(get_sum(10,100))
print(get_sum(100,1000))

'''
# 练习1 定义个函数用于求5的阶乘
# 练习2 定义函数打印一个三角形
'''

def fac(x):
    product = 1
    while x >= 1:
        product *= x
        x -= 1
    print(product)

fac(10)

'''
    *        4    1    1
   ***       3    3    2
  *****      2    5    3
 *******     1    7    4
   
'''
# 打印指教三角形
def sjx(x):
    while x >=1:
        print('*'*x,end='\n')
        x -= 1


sjx(7)