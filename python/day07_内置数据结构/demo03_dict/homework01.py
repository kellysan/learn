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
    3 查找学生信息
    4 退出系统

'''
#stuList = [{'name': '三胖', 'age': 14, 'class': '7年级1班', 'sex': '男'}]
stuList = []
inputInfo = '''
   0 添加资料信息
   1 退出添加
   要求：类只能使用英文，年龄请输入数字，内容请正确添加
'''
while True:
    print(nodeInfo)
    choiceNum1 = int(input("请输入您需要的操作"))
    if choiceNum1 == 0:
        stuDict = {}
        while True:
            print(inputInfo)
            choiceNum2 = int(input("请输入您要的操作"))
            if choiceNum2 == 0:
                addStuKey = input("请输入要添加的类")
                addStuValue = input("请输入您要添加类的内容")
                stuDict[addStuKey] = addStuValue
                print(stuDict)
            elif choiceNum2 == 1:
                break
            else:
                print("选择输入有误，请重新输入")
            print("您输入的学生信息为：{}".format(stuDict))
            time.sleep(1)
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

    elif choiceNum1 == 1:
        delStuName = input("请输入删除学生姓名：")
        for list in stuList:
            if list["name"] == delStuName:
                stuList.remove(list)
                print("{} 学生信息已经删除".format(delStuName))
        print(stuList)

    elif choiceNum1 == 2:
        alterStuOldKey = input("请输入要修改学生的信息选项")
        alterStuOldValue = input("请输入要修改学生的信息选项内容")
        for list in stuList:
            if list[alterStuOldKey] == alterStuOldValue:
                alterIndex = stuList.index(list)
                for k,v in list.items():
                    print("这个是您要修改的信息\n {} {}".format(k,v))

        alterStuNewKey = input("请输入要修改的选项")
        alterStuNewValue = input("请输入要修改学生新信息选项内容")
        for alterDict in stuList:
            if alterDict[alterStuOldKey] == alterStuOldValue:
                alterDict[alterStuNewKey] = alterStuNewValue
            for k1,v1 in alterDict.items():
                print("这个是修改后的信息 \n {} {}".format(k1,v1))

    elif choiceNum1 == 3:
        searchStuName = input("请输入要查找学生的姓名：")
        for list in stuList:
            if list["name"] == searchStuName:
                stuIndex = stuList.index(list)
                print(stuIndex)
                for k,v in list.items():
                    print(k,v)

    elif choiceNum1 == 4:
        print("您即将退出系统")
        exit()
    else:
        print("您输入的号码有误，请重新输入")