#! /usr/bin/env python
# @Author : sanyapeng

'''
函数中，修改外层函数的变量
    通过nolocal 关键字来标记的变量，以为这操作是外层函数的变量
'''
#
# def outer1():
#     a = 10
#     print(a)
#
#     def inner1():
#         nonlocal a
#         a = 20
#         print(a)
#     inner1()
#     print("-->",a)
#
# outer1()
#

'''
总结，变量的作用域
    1 全局变量，在函数外部声明的变量。所有函数都可以使用
        编码习惯： 为了区分局部变量和全局变量
            g_num，gl_num ...
            
    2 局部变量：在函数内部声明的变量，只有该函数内部
         局部变量的生命周期，函数被调用的时候局部变量才会创建，函数结束后被系统回收销毁
         
    3 函数中对于全局变量默认是只读，意味着不允许修改。
        A 如果在函数中直接修改全局变量，其实不是修改，是重新创建同名的局变量
        B 通过使用global 关键字修饰，标记这个变量是全局的
        
    4 函数嵌套 里层函数对于外层函数的变量，也是只读，表示不允许修改
        A 如果在内存函数中直接修改外层函数变量，其实不是修改，是重新创建新的同名的
        B 通过使用nolocal关键字，标记该变量是外层函数的
'''

def outer2():
    a = 10

    def inter2():
        a = 20

        def inter_inter1():
            nonlocal a
            a = 30
        inter_inter1()
        print("inner2_--->", a)
    inter2()
    print("outer2_", a)

outer2()