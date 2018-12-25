#! /usr/bin/env python

sum = 0
for i in range(1,101):
    sum += i
    if i == 100:
        print(sum)

sum1 = 0
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        #print(i)
        sum1 += i
    if i == 100:
        print(sum1)