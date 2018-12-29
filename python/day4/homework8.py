#! /usr/bin/env python
# @Author : sanyapeng

i = 1
while i < 10:
    #每一行的内容，打印i * j
    j = 1
    while j <= i:
        print("{} * {} = {}".format(i,j,i * j),end="\t")
        j += 1
    #换行
    print()
    i += 1