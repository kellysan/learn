#! /usr/bin/env python
# @Author : sanyapeng

s1 = 'hello'
for char in s1:
    print(char)
else:
    print('遍历完成')

print('-------------')
for char in s1:
    if char == "l":
        print(char)
        #break
else:
    print('over')


s4 = "0123456789"



#逆序反转
print(s4[-1::-1])
print(s4[::-1])

print(s4[2:6])
print(s4[2:])
print(s4[:5])
print(s4[:])
print(s4[::2])
print(s4[1::2])
print(s4[2:-1])
print(s4[-2:])