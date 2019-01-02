#! /usr/bin/env python
# @Author : sanyapeng

'''
练习1 创建空字典，添加2个键值对
练习2 修改某一个key的值
练习3 删除某两个key
'''
import  time

myDict = {
    "name":"伞亚朋",
    "age":26,
    "sex":"男"
}

print(myDict)
myDict["age"] = 28
print(myDict)
myDict.pop("age")
myDict.pop("sex")
print(myDict)


nodeInfo= '''
    0 增加学生信息
    1 删除学生信息
    2 修改学生信息
    4 查找学生信息
    5 退出系统

'''
stuList = [{'name': '三胖', 'age': 14, 'class': '7年级1班', 'sex': '男'}]

while True:
    print(nodeInfo)
    choiceNum = int(input("请输入您需要的操作"))
    if choiceNum == 0:
        stuDict = {}
        stuName = input("请输入学生姓名：")
        stuDict["name"] = stuName
        stuAge = int(input("请输入学生年龄："))
        stuDict["age"] = stuAge
        stuClass = input("请输入学生班级：")
        stuDict["class"] = stuClass
        stuSex = input("请输入学生性别：")
        stuDict["sex"] = stuSex
        print("您输入的学生信息为：{}".format(stuDict))
        time.sleep(3)
        #判断确认是否写入数据库
        flag = input("信息即将写入数据库：Y/N")
        if flag == "y" or flag == "Y":
            print("信息写入数据库")
            stuList.append(stuDict)
            print(stuList)
        elif flag == "n" or flag == "N":
            print("即将退出，放弃写入")
            continue
        else:
            print("输入有误请重新输入")

    elif choiceNum == 1:
        delStuName = input("请输入删除学生姓名：")
        for list in stuList:
            if list["name"] == delStuName:
                stuList.remove(list)
                print("{} 学生信息已经删除".format(delStuName))
        print(stuList)

    elif choiceNum == 2:
        alterStuName = input("请输入要修改信息的学生名称")
        alterStukey = input("请输入要修改学生的信息选项")
        alterStuvalue = input("请输入要修改学生信息选项内容")
        for list in stuList:

    elif choiceNum == 3:
        pass
    elif choiceNum == 4:
        searchStuName = input("请输入要查找学生的姓名：")
        for list in stuList:
            if list["name"] == searchStuName:
                stuIndex = stuList.index(list)
                print(stuIndex)
                for k,v in list.items():
                    print(k,v)

    elif choiceNum == 5:
        print("您即将退出系统")
        exit()
    else:
        print("您输入的号码有误，请重新输入")