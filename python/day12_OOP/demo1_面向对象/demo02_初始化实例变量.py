#! /usr/bin/env python
# Autor: sanyapeng

'''
一、创建对象的过程
    c1 = cat()
    自动完成以下2件事
        A 为对象分配内存空间-创建对象，开辟内存
        B 自动执行 __init__()方法

二、init()方法
   在Python中的任何一个勒种，都有__init__(),只能有一个
   在创建对象的时候，会自动调用__init__()

   1. 默认的时候init什么都没干
   2. 使用__init__初始化实例变量

实例变量：就是属于对象的属性
    实例，就是对象，类中的一个对象，也叫类中的一个实例 instance
    实例变量，对象的变量--> 属性
'''

class Cat:
    '''

    '''


    def __init__(self,name,age):
        print("这是一个初始化方法")
        self.name = name
        self.age = age

c1 = Cat("Tom",11)
print(c1.name)
print(c1.age)

c2 = Cat("露娜",10)
print(c2.name)
print(c2.age)


'''
练习1 创建人类，name age height
    方法 eat() run() showinfo（）
'''

print("分割线"*10)

class Human:

    '''
    人类
    '''


    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height


    def eat(self):
        print("{} 正在吃饭。".format(self.name))


    def run(self):
        print("{} 正在跑步".format(self.name))

    def showInfo(self):
        print("我的名字是{},我的身高是{},我的年龄是{}".format(self.name,self.height,self.age))


h1 = Human("Tom",23,123)
h1.eat()
h1.run()
h1.showInfo()
