#! /usr/bin/env python

i = 1
count = 0
while i < 500:
    bai = i // 100
    shi = i // 10 % 10
    ge  = i % 10
    if bai != 4 and shi != 4 and ge != 4:
        count += 1
        print(i)

    i += 1
print('_______________')
print(count)