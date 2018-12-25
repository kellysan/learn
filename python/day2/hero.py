#! /usr/bin/env python
'''
Heroes bata-0.1
san
milo srt map if
2018-05-11 2018-05-22
'''

print("欢迎来到英雄无敌世界")
mapmsg = '#######'
mapins = "-*- the world liki this -*- \n %s \n the '*' is you " %(mapmsg,)
instrucation = '''
contrl you hero:
'a' for left,'d' for right |"'''


print('welcome')
print("the world is like this ####")
name = input("请输入玩家昵称:")
hp = 100;
if not name:
    name = 'player01'

usermsg = {'name':name,'hp':hp}

print("your hero's name is:",usermsg['name'],"hp is:",usermsg['hp'])
print(mapins,instrucation)

userinput = input("'a' for left,'d' for right:")
if userinput == 'a':
    print("you are here *###")
elif userinput == 'd':
    print("you are here #*###")
