#! /usr/bin/env python
# Autor:


'''
python 内置高阶函数
A 列表.sort(key,reverse=True)
    第二个参数，key=函数名，用于表示排序规则，函数名不带括号
        def sort/_rule(x):
            :return len(x)
    第三个参数，reverse=False,True

    总结：
        默认情况下，排序，按照数值升序
                  降序  reverse=True

        自定义排序 自己定义函数规则
        list.sort(key=函数名)
        列表中的每一个原色，应用到key这个函数上，根据函数的返回值进行升序排列
        实际上返回的是，原始的数据排列

map
filter
reduce
'''


list1 = [1,3,2,4,6,5]
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#可以根据key自定义排序
list2 = [5,-8,13,-7,6,-4]

list2.sort()
print(list2)

list2.sort(key=abs)
print(list2)

#排列字符串
list3 = ["apple","oragne","abc","helloword","zz"]
list3.sort()  #默认排序
print(list3)

#按照字母长度排序

def sort_rule(str1):
    return len(str1)

list3.sort(key=sort_rule)
print(list3)

print('dddd',list3.sort(key=sort_rule,reverse=True))
print(list3)

'''
练习1 给定的字符串忽略大小写排序
练习2 给定一个字典，
'''
print("---"*10)
list4 = ["bob","rose","Tom","jerry","Jack"]
list4.sort()
print(list4)
def sort_rule1(str1):
    return str1.lower()

list4.sort(key=lambda str :  str.lower())
print(list4)

students= [
    {
        "name": "王二狗",
        "age": 18,
        "score": 88
    },
    {
        "name": "三胖",
        "age": 19,
        "score": 58
    },
    {
        "name": "李小花",
        "age": 25,
        "score": 98
    }
]

#按照年龄升序排列

students.sort(key = lambda x:x.get("age"))
#students.sort(key=lambda student:student.get("age"))
print(students)

#按照年龄降序排列
students.sort(key=lambda x:x.get("age"),reverse=True)
print(students)

#按照成绩升序排列

students.sort(key=lambda x:x.get("score"))
print(students)


#按照成绩降序排列
students.sort(key=lambda x:x.get("score"),reverse=True)
print(students)
