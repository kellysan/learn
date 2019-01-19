#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo05_单例模式
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/19
#    Change Activity:  2019/1/19:



"""

"""

class MusicPlayer:

    #定义一个类属性

    __instance = None

    #重写new方法

    def __new__(cls, *args, **kwargs):

        #1 判断雷属性是不是None 证明内存中没有创建过
        if cls.__instance is None:
            cls.__instance =  object.__new__(cls)

        #2 返回
        return cls.__instance
        print(cls.__instance)


play1 = MusicPlayer()
play2 = MusicPlayer()

print(id(play1))
print(id(play2))
print(play1 is play2)