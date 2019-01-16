#! /usr/bin/env python
# Autor: sanyapeng


'''
练习1 定义一个狗类
    吃饭，看家，摇尾巴
    名字，颜色

    创建2个对象
        旺财
        大黄
'''

class Dog:

    '''
    :param
    '''
    def eat(self,):
        print(" {} 狗在吃饭".format(self.name))


    def kanj(self,):
        print(" {} 正在看家".format(self.name))


    def ywb(self,):
        print(" {} 在摇尾巴".format(self.name))


wancai = Dog()
wancai.name = "旺财"
wancai.eat()
wancai.kanj()
wancai.ywb()

print(wancai.name)
print(id(wancai))
print(type(wancai))

dog2 = Dog()
dog2.name = "大黄"
dog2.eat()
print(dog2.name)