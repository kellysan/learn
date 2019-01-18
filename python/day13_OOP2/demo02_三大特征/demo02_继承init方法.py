#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo02_继承init方法
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/17
#    Change Activity:  2019/1/17:

"""
继承中init方法
   1 如果子类中没有手动调用init方法，那么会自动调用父类的init方法
   2 如果子类中自己手动调用init方法，那么不会自动调用父类，需要自己也手动调用

        如果子类中初始化init 需要把父类的init 引入
        super().__init__(name,age)
        #Person.__init__(name, age)
"""

class Person:

    def __init__(self, name, age):
        print("父类的init方法")
        self.name = name
        self.age = age




class Student(Person):


    def __init__(self, name, age, school):
        print("子类的init方法")
        super().__init__(name,age)
        #Person.__init__(name, age)
        self.school = school



s1 = Student("王二狗",18,'蓝翔绩效')