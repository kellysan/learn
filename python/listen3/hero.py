#! /usr/bin/env python
import  os
welcome = 'welcome to Heroes world!'

i = 0
while True:
    if os.path.isfile('lock.log'):
        print("lockd")
        break
    username = input('login:')
    password = input('password:')
    i += 1
    '''检查输入的密码是否在数据库中'''
    if username == 'milo' and password == '123':
        print(welcome)
    else:
        if i == 3:
            open('lock.log','w').write(username)
            print("lockd by %s" %username)
            continue
