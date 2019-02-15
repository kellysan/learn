#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo06_正则表达式其他方法
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/13
#    Change Activity:  2019/2/13:


"""
1 math() 匹配 从开始位置开始匹配
    re.match(pattern,string,flags)
2 search() 搜索

"""
import re


s1 = "hellow<h1>memeda</h1>"

# 2 search

r1 = re.search(r"<h1>\w+</h1>",s1)
print(r1)

# 4 替换
s4 = "hello world hello python php python java python php"

s5 = s4.replace("php", "**")


"""
re
第一个参数是规则
第二个参数repl 是要替换的内容
第三个是字符串
"""
s6 = re.sub(r"php","python",s4)
print(s6)

s7 = "djalfjasf0940239f-dis0ub0shsjfdjsohisjtfodjsfgop3423424"
s8 = re.sub(r"\d+","***",s7)
print(s8)

#叠词
'''
(.)\1+
'''
s12 = "我我今天天天天天真真高高高高兴兴兴兴"

list2 = re.match(r"(,)\1+",s12)
print(list2)


#切割

s16 = "hello:php,python,hello:java,python-java"

s17 = re.split(":|-|,",s16)
s18 = re.split("[:,-]",s16)
print(s17)
print(s18)


#规则对象