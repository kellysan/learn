#! /usr/bin/env python
# @Author : sanyapeng

'''
map()映射 内置函数
   字典：{无序的键值对组合：key --> value}

   map(函数，Iterable)
       将可以迭代的对象中的每一个元素，都应用到函数上，返回一个新的可迭代的对象
       Iterable 可迭代对象
       Iterator 迭代器


'''

# 1提供一个函数, 这个操作列表推导式也能干

def foo(x):
    return x ** 2

list1 = [1,2,3,4,5]


'''
 1 -- 1
 2 -- 4
 3 -- 9
 4 -- 16
 5 -- 25
'''

res1 = map(foo,list1)
print(res1)
print(type(res1))

list2 = list(res1)
print(list2)

#使用列表推导式
list3 = [x ** 2 for x in range(1,6)]
print(list3)

#生成器

def foo1(n):
    i = 0
    while i <= n:
        yield i ** 2
        i += 1

for i in foo1(7):
    print(i)



# 给定也一个列表

list4 = ["ananda","LISA","Rose","jaCk","Jerry"]

def foo2(str1):
    return str1.capitalize()


res3 = map(foo2,list4)
list5 = list(res3)
print(list5)

res4 = map(lambda x:x.capitalize(),list4)
list6 = list(res4)
print(list6)


list7 = [10,20,30]
list8 = [1,2,3]

def foo3(x,y):
    return x + y

res6 = map(foo3,list7,list8)
list9 = list(res6)
print(list9)