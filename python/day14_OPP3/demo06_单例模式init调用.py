#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo06_单例模式init调用
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/19
#    Change Activity:  2019/1/19:
"""
单例模式，让一个类在内存中只产生一个对象
    step1 开辟内存，创建对象 --new
    step2 自动执行init 方法，用于初始化实例变量

    单例的操作步骤
    step1 重写new方法
        A 在类中添加一个类属性，用于控制产生对象，判断是否有对象存在
            如果默认为none 就创建对象，调用基本类object 的new 方法
            类属性 = object.__new__(cls)
        B 在init 执行初始化变量的的时候只执行一次
            定义一个布尔类型标记  first_init = False
            如果 first_init 为False 证明没有初始化属性，那么就执行，修改为True
            如果 first_init 为True 直接return
"""
# class AiQiYi:
#     # 定义一个类属性，标记内存地址
#     __instance = None
#
#     # 定义一个类属性，用来标记init是否执行过 默认为False
#     __first_init = False
#
#
#     #重写new方法 __new__()方法主要是用来开辟内存创建对象，继承与object
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         # 如果上述条件不成立直接return
#         return cls.__instance
#
#     def __init__(self,name):
#         if AiQiYi.__first_init:
#             return
#         else:
#             self.name = name
#             AiQiYi.__first_init = True
#
# a1 = AiQiYi("bababa")
# a2 = AiQiYi("dddd")
#
# print(a1.name)
# print(a2.name)


# class MusicPlayer:
#
#     #定义一个类属性
#
#     __instance = None
#
#     #定义一个leishuxing.yongyu控制init是否初次执行
#
#     __first_init = False
#
#     #重写new方法
#
#     def __new__(cls, *args, **kwargs):
#
#         #1 判断雷属性是不是None 证明内存中没有创建过
#         if cls.__instance is None:
#             cls.__instance =  object.__new__(cls)
#
#         #2 返回
#         return cls.__instance
#
#     def __init__(self,name):
#         if MusicPlayer.__first_init:
#             return
#         else:
#             self.name = name
#             MusicPlayer.__first_init = True
#
#
#
# play1 = MusicPlayer("网易云")
# play2 = MusicPlayer("有到")
#
# print(id(play1))
# print(id(play2))
# print(play1 is play2)
#
# print(play1.name)

class QQ(object):
    #

    __instance = None


    #

    __first_init = False


    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


    def __init__(self,name):
        if QQ.__first_init:
            return
        else:
            self.name = name
            QQ.__first_init = True