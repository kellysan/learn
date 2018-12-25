#! /usr/bin/env python

product_list = [
    ('IPhone',4800),
    ('Bike',800),
    ("Mac Pro",12000),
    ('coffice',20),
    ('book',100)
]
shopping_list = []

salary = input('请输入您的工资：')
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("请您输入您要购买的物品>>>")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                buy_item = product_list[user_choice]
                if buy_item[1] < salary:
                    shopping_list.append(buy_item)
                    salary -= buy_item[1]
                    print("Added [%s] into shopping crat,your current balance is \033[31;1m%s\033[0m." %(buy_item[0],salary))
                else:
                    print("\033[41;1m您只剩下[%s]啦，不够了还买什么买\033[0m。" % salary)
        elif user_choice == 'q':
            print("--------shopping list--------")
            for buy in shopping_list:
                print(buy)
            print("您的余额为:",salary)
            exit()
        else:
            print("Invalid option")