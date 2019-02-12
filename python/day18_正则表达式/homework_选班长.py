#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       homework_选班长
#    Description :
#    Author :          SanYapeng
#    date：            2019/2/4
#    Change Activity:  2019/2/4:

"""
选班长
"""
from collections import Counter
#初始化班长人选
list1 = ["Rose","Jack","李小花","三胖","王二狗"]

def vote():
    print(list1)
    list2 = []
    while True:
        ballot = input("请输入候选人姓名,voer表示结束")
        if ballot in list1:
            list2.append(ballot)
        elif ballot == "over":
            print("投票结束")
            break
        else:
            print("您输入的用户不存在！")
    return list2

def get_result():
    while True:
        list2 = vote()
        if not list2:
            return
        # 统计票数，通过 Counter方法来统计列表中每个字符出现的次数
        c1 = Counter(list2)

        #取出最高票数
        most_ballot = c1.most_common(1)[0][1]

        #第一种情况，不加判断直接,不考虑出现同票数情况
        # name = c1.most_common(1)[0][0]
        # ballot = c1.most_common(1)[0][1]
        # print("{}最高票数{},恭喜他当选班长，鼓掌，散花。".format(name,ballot))

        #第二种情况出现相同的票数
        #统计最高相同票数个数
        ballot_sum = 0

        #循环取出每个候选人的票数
        for i in c1.values():

            #判断 判断每个人的票数是不是和最高的相等
            if i == most_ballot:

                #如果最高票数相等，把最高票数统计
                ballot_sum += 1

        # 判断最高票数计数，如果最高票数就是1个人，那么选举结束，选出班长
        if ballot_sum == 1:

            #取出名字，选出列表中票数最高的元祖的 c1.most_common(1) 0 是其中的一个元组，0 是元组中的第一个元素 [('三胖', 3)]
            name = c1.most_common(1)[0][0]
            print("{}最高票数{},恭喜他当选班长，鼓掌，散花。".format(name, most_ballot))
            break
        else:
            print("{}票出现{}次，无法选出班长，请重新选。".format(most_ballot,ballot_sum))

            # 清除列表中的元素
            list1.clear()

            #新的列表，根据最高票数，筛选出列表中票数最高的人
            list3 = c1.most_common(ballot_sum)
            for i in list3:

                #取出元组中姓名，重新加入列表
                list1.append(i[0])

get_result()