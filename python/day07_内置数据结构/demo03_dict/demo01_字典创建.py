#! /usr/bin/env python
# @Author : sanyapeng

'''
列表 存储一组数据 [10,20,30]
元组 存储一组数据（1，2，3）
字典 dict
    dictionary  字典，使用key-value 来进行存储数据
    可以理解为一组无序的键值对组合
    容日中，成对儿(key:value)的数据

    字典语法：{}
    字典注意事项：
        1. key 必须是唯一的
        2. key的数据类型，是不可变的类型，字符串，数值，元组，而列表不可以
        3. value 没有要求
'''
# 1 直接定义字典
tels = {
    "王二狗":"1111111111",
    "李小花":"2222222222",
    "base":"3333333333",
    "jack":"44444444444"
}

print(tels)
print(type(tels))

dict1 = {}

# 可以使用dict()函数来创建字典
'''
可以使用dict()函数来创建字典
需要参数，需要一个列表
dict([]) 需要列表中的数据转换成键值对
    列表中存储的是列表或者原色用于表示键值对
        [name,小小雪] -->两个元素，第一个元素会被认为key,第二个元素被认为是value
    [
    [元素1：元素2]，
    [元素1：元素2]
    ]
'''

dict2 = dict([["name","小小雪"],("age",18),["sex","女"]])
print(dict2)
#字典推导式
d = {x: x ** 3 for x in range(3,10)}
print(d)
#使用dict() 配合关键字参数
print("—"*50)
dict3 = dict(name="王二狗",age=30,city="北京")
print(dict3)



'''
字典中的key 必须是唯一的

'''

print("—"*50)
dict4 = {
    2:"我是一个数字2",
    2:"我也是一个数字2，啦啦啦啦",
    "abc":"我是一个字符串",
    (10,20):"我是一个元组",


}
print(dict4)


'''
练习1:创建2个字典
    存储两个宠物狗信息，狗名字，年龄，品种，颜色
    
练习2： 创建1个字典
    小小雪
        姓名，年龄，性别，婚否，朋友，妈妈（姓名，年龄），朋友们（王二狗，李小花，三胖，rose）
        
'''

dict1 = {
    "name":"粪球",
    "age": 2,
    "kind":"中华田园犬",
    "clolr":"绿色"
}

dict2 = {
    "name":"啸天",
    "age": 2,
    "kind":"昆明犬",
    "clolr":"黑色"
}

print(dict1)
print(dict2)

dict3 = {
    "name":"小小雪",
    "age":18,
    "is_marry": False,
    "mothor":{
        "name":"小雪妈妈",
        "age":40
    },
    "friend":["王二狗", "李小花","三胖"]
}
print(dict3)
