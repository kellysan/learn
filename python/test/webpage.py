#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       webpage
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/2
#    Change Activity:  2019/2/2:

import  urllib3

url = "http://www.baidu.com"
webpage = urllib3.get_host(url)
print(webpage)