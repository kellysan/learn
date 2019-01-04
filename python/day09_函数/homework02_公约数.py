#! /usr/bin/env python
# @Author : sanyapeng

def getCommon(a,b):
    i = b
    if a < b:
        i = a
    while i > 0:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1
print(getCommon(24,32))


def getCommon2(a,b):
    return a * b // getCommon(a,b)

print(getCommon2(24,32))