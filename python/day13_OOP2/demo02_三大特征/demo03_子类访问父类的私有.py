#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo03_子类访问父类的私有
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/17
#    Change Activity:  2019/1/17:

"""
父类的私有属性
    私有的属性和方法不允许外部直接访问
        注意：通过类的公有方法可以访问私有方法

    子类继承了父类
        不允许直接访问父类的私有属性和方法
        只允许访问公有属性和方法

        注意：如果父类的公有方法中有私有属性和私有方法也可以实现
"""

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test1(self):
        print("父类中的私有方法,访问父类的私有属性 {}{}".format(self.num1, self.__num2))

    def test2(self):
        print("父类的公有方法")

    def test3(self):
        print("父类的私有属性 {}".format(self.__num2))



class B(A):

    def fun(self):
        # 尝试访问父类的私有属性
        #print("尝试访问父类的私有属性：{}".format(self.__num2))


        # 能否访问父类的共有属性

        #print("尝试访问父类的共有属性：{}".format(self.num1))
        # 能否访问父类的私有方法

        #self.__test1()
        # 能否访问父类的共有方法
        self.test3()


a1 = A()
print(a1.num1)
a1.test2()

b1 = B()
b1.fun()