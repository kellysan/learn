#! /usr/bin/env python

'''
1、完成第一个项目先录入征兵表格
思路，使用二元列表，第一个列表中存储名字，第二个列表中存储性别，第三个数组存储年龄，第四个数组存储特长
'''
zb_index = 0
zb_list =[]
name_list = []
sex_list = []
age_list = []
special_list = []

while True:
    print('''
    1、输入信息
    2、查询信息
    3、更改姓名
    4、更改年龄
    ''')
    choice = int(input("请输入你的选择："))

    if choice == 1:
        name = input("请输入姓名：")
        sex = input("请输入性别：")
        age = int(input("请输入年龄："))
        special = input("请输入特长：")
        if not name and not sex and not age and not special:
            continue
        else:
            print('''
                您输入的信息为
            姓名：{name}
            性别：{sex}
            年龄：{age}
            特长：{special}
            '''.format(name = name ,sex = sex ,age = age ,special = special))
            name_list.append(name)
            sex_list.append(sex)
            age_list.append(age)
            special_list.append(special)
        print(name_list)
        print(sex_list)
        print(age_list)
        print(special_list)

    #根据姓名查询输入的信息
    if choice == 2:
        searchName = input("请输入您要查询的姓名:")
        nameIndex = name_list.index(searchName)
        sexIndex = ageIndex = specialIndex = nameIndex
        print('''
        您要查询的信息为：
        姓名：{searchName}
        性别：{searchSex}
        年龄：{searchAge}
        特长：{searchSpecial}
        '''.format(searchName = name_list[nameIndex],searchSex = sex_list[sexIndex],searchAge = age_list[ageIndex],searchSpecial = special_list[specialIndex]))
    if choice == 3:
        searchName = input("请输入要更改的姓名")
        sexIndex = ageIndex = specialIndex = nameIndex = name_list.index(searchName)
        print('''
        需要要修改信息：
        姓名：{searchName}
        性别：{searchSex}
        年龄：{searchAge}
        特长：{searchSpecial}
        '''.format(searchName=name_list[nameIndex], searchSex=sex_list[sexIndex], searchAge=age_list[ageIndex],searchSpecial=special_list[specialIndex]))
        modifyName = input("请输入要修改的名称：")
        name_list[nameIndex] = modifyName
        print('''
        调整后信息：
        姓名：{modfiyName}
        性别：{modfiySex}
        年龄：{modfiyAge}
        特长：{modfiySpecial}
        '''.format(modfiyName=name_list[nameIndex], modfiySex=sex_list[sexIndex],modfiyAge=age_list[ageIndex], modfiySpecial=special_list[specialIndex]))
