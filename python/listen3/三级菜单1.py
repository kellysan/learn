#! /usr/bin/env python

info = {
    '北京':{
        '朝阳':{
            '国贸':['央视','建外soho'],
            '望京':['Alibaba','望京soho']
        },
        '昌平':{
            '沙河':['oldboy','test'],
            '天通苑':['我爱我家','链家']
        }
    },
    '上海':{}
}


exit_flag = False

while not exit_flag:
    for l1 in info:
        print(l1)
    choice1 = input("请输入l1")
    if choice1 in info:
        while not exit_flag:
            for l2 in  info[choice1]:
                print('\t',l2)
            choice2 = input("请输入l2")
            if choice2 in info[choice1]:
                while not exit_flag:
                    for l3 in info[choice1][choice2]:
                        print('\t\t',l3)
                    choice3 = input("请输入l3")
                    if choice3 in info[choice1][choice2]:
                        for l4 in info[choice1][choice2][choice3]:
                            print('\t\t\t',l4)
                        choice4 = input("最后一层，输入b返回")
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True