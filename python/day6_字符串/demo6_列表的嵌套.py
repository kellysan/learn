#! /usr/bin/env python

'''
列表，存储多个元素
     整数，
'''

nums = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]


print(nums[2][1])

print("--"*50)
for i in nums:
    print(i)
    for j in i:
        print(j)
'''
列表推导
start 表示起始值，range(5) 表示 range(0,5) 如果初始值未定义，使用0
end 表示结束值，单不包括结束值
ste 步长，每次跳跃的间距
'''


for i in range(5):
    print(i)


for i  in range(10,100):
    print(i,end="\t")
print()

for i in  range(1,11,2):
    print(i,end="\t")
print()
for i in range(0,21,2):
    print(i,end="\t")
print()

for i in range(1,10):
    for j in range(1,i+1):
        print("{} * {} = {}".format(i,j,i * j),end="\t")
    print()


str1 = "sdradasf"

print(str1.capitalize())