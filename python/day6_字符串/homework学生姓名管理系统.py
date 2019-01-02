#! /usr/bin/env python


input_info = '''
    ==1701班级学生姓名管理系统==
    1，代表增加学生姓名
    2，代表删除学生姓名
    3，代表修改学生姓名
    4，代表查询学生姓名
    5, 退出系统"

'''
#print(input_info)
name_list = []

while True:
    print(input_info)
    choose = int(input("请输入您的选择"))

    if choose == 1:
        add_name = input("输入姓名")
        name_list.append(add_name)
        print(name_list)
    elif choose == 2:
        del_name = input("请输入你要删除的学生姓名")
        if del_name in name_list:
            name_list.remove(del_name)
        else:
            print("您输入的姓名有误")
    elif choose == 3:
        alter_name = input("请输入修改人名称：")
        index = 0
        while index <= len(name_list) - 1:
            if name_list[index] == alter_name:
                new_name = input("请输入新的名称")
                name_list[index] = new_name
                break
            index += 1
        else:
            print("没有你要找的人")
    elif choose == 4:
        select_name = input("请您输入要查询的姓名：")
        if select_name in name_list:
            print("您查找的学生在管理系统中")
        else:
            print("您要查询的学生姓名不存在")
    elif choose == 5:
        print("即将退出系统")
        exit()
    else:
        print("输入有误，请重新输入")
    print(name_list)