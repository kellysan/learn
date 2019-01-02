#! /usr/bin/env python
# @Author : sanyapeng
'''
字典 key：value 名值对，无序
    1 增加
        字典["newkey"] = "newvalue"
    2 删除
        pop["key"]
        del 字典["key"]
    3 修改 不存在就添加
        字典["key"] = "newvalue"
    4 获取,查找
        字典["key"]
        字典.get("key") 如果没有返回的是none

    补充：
        in not in
        字典.keys() 得到一个可迭代的key列表
        字典.value()
        字典.items() 获取键值对的组合
'''

persion1 = {
    "name":"王二狗",
    "age": 18,
    "sex": "男"
}

print(persion1["name"])
print(persion1["age"])
print(persion1["sex"])

print(persion1.get("name"))
print(persion1.get("dddd"))


#元素增加

persion1["address"] = "北京市"
print(persion1)

if "qq" in persion1:
    print(persion1["qq"])
else:
    print("没有发现QQ")
    persion1["QQ"] = 44444444
    print(persion1)

# 获取所有的key
for key in persion1.keys():
    print(key)


for value in persion1.values():
    print(value)


print("*"*100)
for k,v in persion1.items():
    print(k,v)


print("*"*100)
for k,v in enumerate(persion1.items()):
    print(k,v)
print("*"*100,end="\n")
print(persion1.items())