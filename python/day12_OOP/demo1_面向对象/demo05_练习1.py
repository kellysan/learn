#! /usr/bin/env python
# @Author : sanyapeng

'''
两个类
    公路  Road
       属性 公路名称，公路长度
    车 Car
       属性 车名，时速

       方法，求车在路上所用时间
'''


class Road:

    '''

    '''
    def __init__(self,name,length):
        self.name = name
        self.length = length


class Car:

    '''

    '''
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def get_time(self,road):
        print("{} 跑在 {},车速 {},用时{}".format(self.name,road.name))



# r1 = Road("秋名山",1080)
# c1 = Car("AE86",20)
# c2 = Car("GTR",120)
# c1.get_time(r1)
# c2.get_time(r1)
#
# r2 = Road("京哈高速",3000)
# c1.get_time(r2)
# c2.get_time(r2)