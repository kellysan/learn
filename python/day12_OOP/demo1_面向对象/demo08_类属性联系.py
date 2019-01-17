#! /usr/bin/env python
# Autor: sanyapeng

'''
统计类产生的对象,不是方法
'''

class Person:

    count = 0 #定义一个类属性，近一份，用于计数器

    def __init__(self,name):
        self.name = name
        Person.count += 1

    def eat(self,food):
        print("{} 正在吃 {}".format(self.name,food))

p1 = Person("王二狗")
p2 = Person("王二111狗")
p3 = Person("王vvvv二狗")
print(Person.count)

p1.eat("汉堡包")
print(p1.count)

p4 = Person("王dddd二狗")
print(Person.count)
