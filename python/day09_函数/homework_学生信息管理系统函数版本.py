#! /usr/bin/env python
# @Author : sanyapeng


nodeInfo='''
   1 添加学生信息
   2 更新学生信息
   3 查找学生信息
   4 删除学生信息
'''


#stuList = []
stuList = [{"name":"伞亚朋","age":18,"sex":"男"}]

def stuAdd():
    '''
    用于添加学生信息

    :param name 学生姓名
    :param age 学生年龄，需要是数字
    :param sex 学生性别
    '''
    stuDict = {}
    name = input("请输入您要添加的学生姓名：")
    age = int(input("请输入您要添加学生的年龄："))
    sex = input("请输入您要添加学生的性别：")
    #将学生名称写入字典
    stuDict["name"] = name
    stuDict["age"] = age
    stuDict["sex"] = sex
    #将字典数据写入列表
    stuList.append(stuDict)
    print(stuDict)
    print(stuList)


def stuSelect():
    '''
        查找学生
    :param name:  学生姓名
    :return:
    '''
    name = input("请输入要查找的学生姓名")
    for dict in stuList:
        if dict["name"] == name:
            print("这是您要查找的学生信息")
            for k,v in dict.items():
                print("{}:{}".format(k,v))
        else:
            print("您要查找的学生不存在")


def stuDel():
    '''
    删除学生
    :param name: 学生姓名
    :return:
    '''
    name = input("请输入要删除的学生姓名")
    for dict in stuList:
        if dict["name"] == name:
            stuList.remove(dict)
            print("{} 学生信息已删除".format(name))
            print(stuList)
        else:
            print("您要删除的信息不存在")


def stuChage():
    '''
    修改学生信息
    :param name:
    :return:
    '''
    name = input("请输入您要修改学生信息名称：")
    for dict in stuList:
        if dict["name"] == name:
            print("这是您要修改学生的信息")
            for k,v in dict.items():
                print(k,v)
            stuChagekey = input("请您输入您要修改的选项：")
            stuChageValue = input("请您输入您要修改的内容：")
            dict[stuChagekey] = stuChageValue
            print("这个是修改后的信息")
            for k,v in dict.items():
                print(k,v)
        else:
            print("您输入的学生信息不存在")
        break

if __name__ == '__main__':
    while True:
        print(nodeInfo)
        choice = int(input("请输入您要的操作："))
        if choice == 1:
            stuAdd()
        elif choice == 2:
            stuChage()
        elif choice == 3:
            stuSelect()
        elif choice == 4:
            stuDel()
        else:
            print("您输入的信息有误，请重新输入")