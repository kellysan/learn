#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       nametuple
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/2
#    Change Activity:  2019/2/2:


from collections import namedtuple

Point = namedtuple("Point",["x","y","z"])
print(Point)

man = Point("王二狗","30","100")
print(man)
