#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo01_
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/17
#    Change Activity:  2019/1/17:

'''
面向对象：
    编程思想，核心，类- 对象

    三大特征，java python
        封装性：
            打包，包裹
            面向对象编程第一步，将就将方法（行为功能）和属性（变量）封装到一个抽象类中
               对象.属性
               对象.方法
            函数，方法
                将方法的细节，属性等，封装到了一个类的内部
        继承性：
            爸爸，儿子
            类（父） 类（子类）
                存在了继承关系，子类继承父类，那么子类就可以使用父类的内容（属性，方法）

            意义
               1. 提高代码的重用性，避免重复代码
               2. 扩展类的功能，从父类的角度

        多态性：

'''
'''
继承性
   一个子类继承一个父类
   A 子类对象可以访问父类的方法和属性 避免重复代码
   B 子类中可以新增自己的属性和方法 扩展子类功能
   C 子类还可以重写，父类的方法
'''
#1. 定义一个父类

class Person:



    # 吃
    def eat(self):
        print("吃窝窝头")

    def sleep(self):
        print("睡觉了")


#2 定义子类

class Student(Person):

    # 新增方法
    def study(self):
        print("学习啦，把你爸爸乐坏了。。")

    # 重写方法
    # 改功能父类中已经有了，但是无法满足需求，那么子类可以重写实现，就是重写，保证和父类中方法的声明一样
    def eat(self):
        print("重写父类的方法，吃炸鸡，喝啤酒")

    def sleep(self):
        print("学生，睡之前了做梦玩手机")


    # 在子类中表示父类 python2.x 父类名.父类的方法(self)
        Person.sleep(self)
        super().sleep()
        print("学生，睡着了做梦玩手机")


'''
练习
'''