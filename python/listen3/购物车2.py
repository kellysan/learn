#! /usr/bin/env python
product_list = [
    ('IPhone',4800),
    ('Bike',800),
    ("Mac Pro",12000),
    ('coffice',20),
    ('book',100)
]
shopping_list = []

salary = input("请输入您的工资:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        use_input = input("请输入您要购买的商品：")
        if use_input.isdigit():
            use_input = int(use_input)
            if use_input < len(product_list) and use_input >= 0:
                buy_item = product_list[use_input]
                if buy_item[1] < salary:
                    shopping_list.append(buy_item)
                    salary -= buy_item[1]
                    print("您购买了[%s]已经方放入购物车，您还剩下\033[31;1m[%s]\033[0m。" %(buy_item,salary))
                else:
                    print("、033[41;0m您就剩下[%s]这么点钱了，还买什么买。\-33[0m")
        if use_input == 'q':
            print("-------- shopping list -------")
            for buy in shopping_list:
                print(buy)
            print("您还剩下",salary)
            exit()
        else:
            print("Invalid option")3