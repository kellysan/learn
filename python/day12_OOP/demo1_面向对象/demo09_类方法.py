#! /usr/bin/env python
# Autor: sanyapeng

'''
类
    变量（属性）
       类属性，也叫类变量，属于类，由类调用，仅一份
       实例属性 也叫实例变量，属于对象，有对象调用，每个对象一份数据，对象之间的属性值互不影响

    方法（行为功能，其实就是函数）
        实例方法 属于实例，由对象调用，第一个参数必须是对象，self
           实例方法中，可以操作实例属性,也可以访问类属性 类名.属性
        类方法 第一个参数cls 表示该类 @classmethod
            可以访问类方法
        静态方法  @staticmethod



类方法
    1 语法规则，在方法上添加内置的装饰器 @classmethod
         @classmethod
         def 类方法名(cls)
             可以访问类的属性，但是不能访问对象属性

         类.类方法（cls就是该类本身）

         类方法中，可以操作类属性
    2 用法
       类方法中第一个参数 cls 表示该类本身，可以访问类属性
       类方法中不能直接访问实例属性 没有self

       如果一个方法中涉及到了对象属性，那么定义为实例方法
       如果一个方法总没有涉及对象属性，那么定义为类方法

       对象也可以访问类方法，但是不推荐使用
'''

class Person:

    #1 类属性
    country = "中国"

    #2 实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #3 实例方法，第一个参数必须是对象自己，使用self 表示，可以访问对象属性

    def show_info(self):
        print("姓名：{}，年龄：{}".format(self.name,self.age))


    # 4 类方法 语法，添加一个python内置装饰器
    #属于类，类调用
    @classmethod
    def test(cls):
        print("国家：{}".format(cls.country))


    #5 特殊情况1，一个类中操作类属性，还操作实
    @classmethod
    def test2(cls,p):
        print("国家:{},姓名：{},年龄：{}".format(cls.country,p.name,p.age))

    # 6 特殊情况2 操作类属性，也操作实例属性
    def test3(self):
        print("国家：{},姓名：{},年龄：{}".format(Person.country,self.name,self.age))

    # 7 定义静态方法，既不操作类的属性，也不操作实例属性，没有self 也没有cls
    @staticmethod
    def choose():
        print("请输入您的选择：")
        print("1 创建对象")
        print("2 代表")

p1 = Person("王二狗",30)
p1.show_info()

p2 = Person("李小花",18)
p2.show_info()

Person.test()
Person.test2(p1)
p1.test3()


p1.choose()