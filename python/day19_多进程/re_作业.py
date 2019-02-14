#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       re_作业
#    Description :
#    Author :          SanYapeng
#    date：            2019-02-13
#    Change Activity:  2019-02-13:

import re



s1 = """
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
"""

res1 = re.search(r"https://.+?\.jpg", s1)
print(res1.group())
s2 = """
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
def my_rep1(m1):
    return m1.group(1)

r2 = re.sub(r"(http://.+?/)(.*)",my_rep1,s2)
print(r2)

r3 = re.findall(r"(http://.+?/)",s2)
print(r3)


s4 = "hello world ha ha"
r5 = re.split(r" +",s4)
print(r5)

r6 = re.findall(r"\b[a-zA-Z]+\b",s4)
print(r6)