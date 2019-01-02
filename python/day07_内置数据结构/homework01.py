#! /usr/bin/env python
# @Author : sanyapeng

# str1 = "dahfaaofjadDADAFe9792334235REBATvcxzcxzxzcvAHBczvcvARTAGAH"
#
# #count1 = 0
# count2 = 0
# count3 = 0
#
# for char in str1:
#     if char.isupper():
#         count1 += 1
#     elif char.islower():
#         count2 += 1
#     else:
#         count3 += 1
#
# print("大写字符一共{}个，小写字符{}个，数字{}个".format(count1,count2,count3))


'''
可以通过find 对比去查找是存在
'''
#切割 取图片的名字
pathName="http://192.168.0.1:8080/Day33_Servlet/aa.jpeg"

print(pathName.rfind("/"))
print(pathName[pathName.rfind("/") + 1])
name = pathName[pathName.rfind("/")+1:]
print(name)

s1 = "python"
str2 = "djafhpythonnjaofijpythondpythonaoppythonjpythonfjfopjpythonpakfpythonpdafjpythonpahjsgjpuythonpython"
s2 = str2.replace("python","")
print(s2)

count1 = (len(s2) - len(str2)) // len(s1)
print(count1)