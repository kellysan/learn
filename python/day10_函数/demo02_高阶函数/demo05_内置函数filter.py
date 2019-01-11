#! /usr/bin/env python
# @Author : sanyapeng

'''
filter()
    过滤器 理解为筛选
        按照某种规则进行过滤

    第一个参数，函数 返回布尔类型
        用于过滤
           bool类型
    第二个参数，可迭代对象

'''

list1 = [1,2,3,4,5,6,7,8]
def foo(x):
    if x % 2 != 0:
        return True
    else:
        return False

res1 = filter(foo,list1)
print(list(res1))
print(type(res1))



'''
总结：
一、python的
'''

t1 = (1,2,3,4)
print(type(t1))
if 1 in t1:
    print("yes")
print(t1.count(1))
print(len(t1))

'''
作业
掷骰子
写也一个函数，判断一个数是否是质数
写一个函数，计算输入任意两个数之间所有的质数的和
定义一个函数，输入一个日期，判断该日期是今年的第几天，例如输入 2016-01-01 打印第一天
定义函数 输入也一个日期，判断该日期是否合法
传入多个参数，以list返回
传入多个参数，如果是数字累加和，如果是字符串就拼接
'''
print("练习"*20)

def ispre(x):
    if x > 1:
        for i in range(2,x):
            if x % i == 0:
                print(x,"不是质数")
                print(i,"乘以",x//i,"是",x)
                break
            else:
                print(x,"是质数")
    else:
        print(x,"不是质数")


ispre(3)

num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")
