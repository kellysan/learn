#! /usr/bin/env python
# Autor: sanyapeng


def fob(n):
    a = 1
    b = 0
    c = 0
    i = 1
    while i <= n:
        c = a + b
        yield c
        a = b
        b = c
        i += 1

print(fob(12))

for i in fob(12):
    print(i)