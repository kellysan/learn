#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo07_json
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/2
#    Change Activity:  2019/2/2:

import  json
#1 创建数据对象
dict = {
    "name":"王二狗",
    "age":18,
    "friend":["马冬梅","刘振","韩梅梅"]
}


#2. 将json 数据存储到本地 序列化存储
"""
dump()代表将内容存储到指定文件中  -- 序列化
第一个参数  要存储的对象
第二个参数 文件对象
第三个参数 操作模式

ensure_ascii=False 原样输出
"""
#json.dump(dict,open("data1.json",mode="w",encoding="utf-8",),indent=4)

dict2 = {
    "name": "李小花",
    "age": 28,
    "friend": ["马冬梅", "刘振", "韩梅梅"],
    "height": float(160),
    #"a":lambda a:"我是一个函数返回值a"
}

# file = open("data2.json",mode="w",encoding="utf-8")
# json.dump(dict2,file,
#           ensure_ascii=False,#用于标记非ASCII 的字符是否需要转义
#           indent=2, #代表缩进量
#           default=lambda a:"替代的数据a",  #一个函数，用于value不能直接被保存的时候替代的数据
#           #sort_keys=True  #序列化保存的时候，是否要排序
#
#           )
#
# file.close()


#返序列化

# with open("data3.json",mode="r",encoding="utf-8") as file3:
#     dict3 = json.load(file3)
#     print(dict3["info"])
#     print(dict3["page"])
#     print(dict3.get("state"))
#     print(dict3)

