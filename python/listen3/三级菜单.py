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
    for i in info:
        print(i)
    choice = input("请选择1")
    while not exit_flag:
        if choice in info:
            for i2 in info[choice]:
                print('\t',i2)
            choice2 = input('请选择2')
            while not exit_flag:
                if choice2 in info[choice]:
                    for i3 in info[choice][choice2]:
                        print('\t\t',i3)
                    choice3 = input("请选择3")
                    if choice3 in info[choice][choice2]:
                        for i4 in info[choice][choice2][choice3]:
                            print('\t\t\t',i4)
                        choice4 = input("最后一层请输入b")
                        if choice4 == 'b':
                            pass
                        if choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q'
                exit_flag = True

