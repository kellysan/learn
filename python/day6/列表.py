#! /usr/bin/env python
# @Author : sanyapeng



'''
#常用操作
    #列表中的增删改查
    A 增加元素
      a.append()
    B. 删除
    pop() 默认删除最后一个
    pop(1) 删除下标是1
    remove('王二狗') 根据元素删
    del 扩展内容，后边加的是列表和index

    C.修改 列表名[index] = new
'''

# 定义列表
names1 = ["王二狗","李小华","三胖"]
names2 = ["rose","jack","tom","jerry"]


# #添加数据
# #增加元素，在末尾添加
# print(names1)
# names1.append("啸天")
# print(names1)
#
# #增加元素,在指定位置添加
#
# names1.insert(2,"隔壁老王")
# print(names1)
#
# #删除数据 默认删除最后一个 pop 获取栈顶元素 后进先出
# names1.pop()
# print(names1)
# #删除指定位置元素
# names1.pop(1)
# print(names1)
#
# #删除数据 remove 删除指定元素
# names1.remove("王二狗")
# print(names1)
# #根据列表取值删除
# del names1[1]
# print(names1)
#
# #修改元素
# print(names2)
# names2[1] = 'lucy'
# print(names2)

#列表的合并
# +
# print('-'*50)
# names3 = names2 + names1
# print(names3)
# print(names1)
# print(names2)
# # append
# # print('*'*100)
# # names1.append(names2)
# # print(names1[3][1])
#
# # extend
# names1.extend(names2)
# print(names1)
# print(len(names1))

