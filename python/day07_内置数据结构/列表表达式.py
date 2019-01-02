#! /usr/bin/env python
# @Author : sanyapeng

list2 = [x ** 3 for x in range(0,11)]
print(list2)

list7 = [x for x in range(1,10) if x %2 == 0 ]
print(list7)

list8 = [x * 2 for x in range(1,10) if x % 2 == 1]
print(list8)