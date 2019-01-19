#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04_多态的联系
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/18
#    Change Activity:  2019/1/18:

from fabric.connection import

"""
需求：
   如花和自己的宠物花花小猫玩
   如梦和自己的宠物啸天 狗狗玩
   如歌和自己的宠物，兔子玉兔玩
"""

class Girl:
    def __init__(self, name):
        self.name = name

    def play_with_pet(self,pet):
        print("{} 和自己的宠物 {}玩".format(self.name,pet.name))
        pet.eat()
        if isinstance(pet,Dog):   # 添加判断因为猫没有看没这个方法，所有判断，类是否是dog 如果是dof 才执行如果不是，则不执行
            pet.look_doot()


class Pet:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{}开始吃东西了".format(self.name))

    def sleep(self):
        print("{}睡着了,玩累了".format(self.name))


class Cat(Pet):

    def __init__(self, name,clour):
        super().__init__(name)
        self.clour = clour
    def eat(self):
        print("{} 小猫吃鱼".format(self.name))

class Dog(Pet):

    def look_doot(self):
        print("{}小狗看门".format(self.name))


g1 = Girl("如花")
c1 = Cat("花花","白色")
d1 = Dog("旺财")

print(type(c1))

print(g1.name)
print(c1.name)

g1.play_with_pet(c1)
g1.play_with_pet(d1)

