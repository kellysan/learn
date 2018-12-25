#! /usr/bin/env python
'''
游戏的初步需求
1、注册、登录、验证
2、给角色起名字，初始化英雄
3、游戏的前奏
4、满血出场
5、有地图
6、发生随机事件
'''

s1 = 'friednfriednfriednfriednfriednfriednfriednnfriednfriednfriednfrnfriednfriednfriednfrnfriednfriednfriednfrnfriednfriednfriednfr'
dic1 = []
index1 = []
count = []

if('f' in s1):
    f1 = s1.count('f')
    print(f1)
    dic1.append(f1)
    index1.append(s1.find('f'))
if('r' in s1):
    r1 = s1.count('r')
    print(r1)
    dic1.append(r1)
    index1.append(s1.find('r'))
if('i' in s1):
    i1 = s1.count('i')
    print(i1)
    dic1.append(i1)
    index1.append(s1.find('i'))
if('e' in s1):
    e1 = s1.count('e')
    print(e1)
    dic1.append(e1)
    index1.append(s1.find('e'))
if('n' in s1):
    n1 = s1.count('n')
    print(n1)
    dic1.append(n1)
    index1.append(s1.find('n'))
if('d' in s1):
    d1 = s1.count('d')
    print(d1)
    dic1.append(d1)
    index1.append(s1.find('d'))
print(dic1)
print(index1)
s2 = [s1[index1[0]],s1[index1[1]],s1[index1[2]],s1[index1[3]],s1[index1[4]],s1[index1[5]]]
print(s2)
dic1.sort()
print(dic1)
print(dic1[0])

add = ''
for j in s2:
    add+=add.join(j)

print("add",add)

for i in 'f r i e n d':
    list = count.append(index1.append(s1.find('r'))
