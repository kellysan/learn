#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04_转义字符
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/12
#    Change Activity:  2019/2/12:

import re
"""
正则的规则：
一.一般的符号
  1.字面量
  2..点代表1个任意字符，除\n外
  3.[],匹配[]中任意字符都可以
  4.[abc],匹配a或b或c。1位
  5.[a-z],匹配任意一位的小写字母
  6.[^abc],除abc外的任意一位字符

二、特殊的符号
    1.\d,代表0-9数字，同[0-9]
    2.\D,与\d相反，同[^0-9]
    3.\w,匹配一个单词字符：a-zA-Z0-9_
    4.\W,与\w相反，非[a-zA-Z0-9_]
    5.\s,匹配空白字符。即空格，tab键,\n,\r等
    6.\b,单词边界
"""
"""
三、数量词
    1.*，出现的次数是0次或多次
    2.+,出现的次数是1次或多次
    3.?,出现的次数是0次或1次
    4.{M}，出现的次数刚好是m次
    5.{M,},至少M次
    6.{M,N},至少m次，至多n次
"""

"""
四、转义：\
    1.普通的字符-->特殊含义的字符
        n,r,t,b--->\n,\r,\t,\b
    2.特殊含义的字符-->普通字符
        ",',\-->\",\'

    "\"abc"-->"abc
    "\\abc"

转义字符和原始字符串
r""


\"-->"
\\-->\
\.-->.


\w,\d,\s,\b....-->正则中规定的字符


五、边界问题：
1.^,表示匹配的起始位置
2.$,表示结束的位置
"""

print(re.match(r"\w+\b","hove r"))
print(re.match(r"\w+\bve\b","ho ve r"))   #\b 边界不能做空格使用

"""
六，分组
    1. |
    2.（）代表了分组 
"""
print("六")
#身份证
print(re.match(r"[1-9]\d{16}(\d|X)$","130283198910100439"))

print("邮箱")
s1 = "wangergou@163.com"
s2 = "sanpang@qq.com"
s3 = "lixiaohua@sina.com"
s4 = "linux110@163.com"

print(re.match(r"\w+@(163|qq)\.com",s1))
print(re.match(r"\w+@(163|qq)\.com",s2))
print(re.match(r"\w+@(163|qq)\.com",s3))
m14 = (re.match(r"\w+@(163|qq)\.com",s4))
print(m14.group(0))

print("--------------")
s5 = "<html><h1>helloworld</h1></html>"

m5 = re.match(r"<(.+)><(.+)>(.+)</\2></\1>",s5)
print(m5.groups())
print(m5.group(1))

"""
给分组起别名
"""

s6 = "<html><h1>helloworld</h1></html>"
m6 = re.match(r"<(?P<t1>.+)><(?P<t2>.+)>(.+)</(?P=t2)></(?P=t1)>",s6)
print(m6)
print(m6.groups())

print("-" * 50)
s8 = "<html><body><center><h1>" \
     "hello</h1></center></body></html>"
# 续行符
print(s8)
m8 = re.match(r"<(.+)><(.+)><(.+)><(.+)>"
              r"(.+)</\4></\3></\2></\1>", s8)
print(m8)
