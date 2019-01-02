#! /usr/bin/env python

s = 'life is short'
s1 = 'liFE is short'
#首字母大写
print(s.capitalize())

#字符串标题化,整个字符串每个单词首字母大写
print(s.title())

#字母全大写,字符全小写
print(s1.upper())
print(s1.lower())


#大写字母转小写，小写字符转大写
print(s1.swapcase())


#填充  将字符串居中
s2 = "hello"

'''默认使用空格填充，可以指定填充字符串'''
print(s2.center(10,"*"))

#查找 ，如果通过find找到这个字符就返回下标，如果不存在就返回 -1
s3 = "hello world"
print(s3.find("or"))

#根据范围查找 第一个5是开始，第二个len(s3)是结束范围
print(s3.find("l",5,len(s3)))

#查找子串如果存在就返回下标，没有就报错 和 in，not in 作用相同
print(s3.index('ll'))

s4 = "hello123"
#判断字符串是否都是字母或者数字
print(s4.isalnum())

#判断字符串是否都是字母
print(s4.isalpha())

#是否全是数字
s5 = "100"
print(s5.isdigit())


s6 = "   hello word   "
#去掉字符串两端的空格，字符串中间的不能去掉,加参数去掉指定的字符
print(s6.strip())

s7 = "***hello word****"
print(s7.strip('*'))
print(s7.lstrip('*'))
print(s7.rstrip('*'))


#切割 默认不加参数使用空格切割，如果加入第一个参数，按照指定字符切割，会把内容放入列表，如果加入第二个参数（范围）指定了最大的切割数量
s8 = "ab-ccc-d-h"
print(s8.split('-'))
print(s8.split('-',1))

# 获取sub在字符串中出现的次数，没有是0
s9 = "hello王二狗pythonaaaphdfdfadfafafafaddfafafa"
print(s9.count('a'))