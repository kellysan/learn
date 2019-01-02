#! /usr/bin/env python


num1 = [1,2,3]

num2 = num1.copy()

num3 = num1[:]

num4  = num1

print(id(num1))
print(id(num2))
print(id(num3))
print(id(num4))



print("*"*50)
num5 = [1,6,3,9,4]
fruit = ["apple","banana","organe","apple","mango","pear"]
print(num5)
num5.sort()
print(num5)
num5.sort(reverse=True)
print(num5)
print(fruit)

fruit.reverse()
print(fruit)

index = fruit.index("banana")
print(index)

# in not in
print("banana" in fruit)
print("banana" not in fruit)

#统计次数
print(fruit.count("apple"))


#清除列表
fruit.clear()
print(fruit)