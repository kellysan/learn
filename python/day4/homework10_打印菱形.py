#! /usr/bin/env python
# @Author : sanyapeng


i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{} * {} = {}".format(j, i, i * j), end='\t')
        j += 1
    print()
    i += 1