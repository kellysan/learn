#! /usr/bin/env python
# @Author : sanyapeng

'''
函数的参数：
    形式参数，形参
        声明函数的时候，()里面的参数，本质就是一个变量
        形参就是一个变量，变量的数值对于函数来讲并不确定，由调用处来确定。

    实际参数，实参
        函数调用的时候，传递给形参的具体参数，就叫做实参

函数的调用
    A: 函数名对应
    B: 实参匹配形参
       如果一个函数有参数，那么调用的时候要传入相应的数据
返回值：
    函数执行结束后，犯规给调用处的结果
    需要使用return关键字
        1 将结果返回给调用处
        2 结束了方法的执行


'''

# def jieCheng(n):
#     res = 1
#     while n > 0:
#         res *= n
#         n -= 1
#     print("结果是 {}".format(res))
#
# num = int(input("shuzi:"))
# jieCheng(num)

#求和 并将这个函数结果给这个调用处
def get_num(n):
    sum1 = 0
    i = 1
    while i <= n:
        sum1 += i
        i += 1
    return sum1

res1 = get_num(10)
print(res1)


print("-"*50)
'''
练习1 定义一个函数接收两个参数，这个函数用于比较两个数的大小，并将大的数返回
练习2 定义一个函数，用于接收两个参数，用于求和，并将结果返回
'''

def diffNum(num1,num2):
    maxNum = 0
    if num1 > num2:
        maxNum = num1
    else:
        maxNum = num2
    return  maxNum

print(diffNum(1,10))

print('-'*100)

def sumNum(num1,num2):
    return num1 + num2

print(sumNum(1,2))

print('_'*40)
'''
判断闰年 
'''


def isLeapYears(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def getLeapYears(list1):
    res = []
    for year in list1:
        if isLeapYears(year):
            res.append(year)
    return res

data = [2000,2001,2002,2003,2004,2005]
print(getLeapYears(data))



print("判断日期")
def getDay(year,month):
    day = 0
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = 31
    elif month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
        day = 30
    elif month == 2:
        if isLeapYears(year):
            day = 29
        else:
            day = 28
    return day

res3 = getDay(2008,7)
print(res3)