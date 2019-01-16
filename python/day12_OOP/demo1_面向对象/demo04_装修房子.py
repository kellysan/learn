#! /usr/bin/env python
# @Author : sanyapeng


'''
练习3 拜访家具（装修房子娶媳妇）
    1 房子 House 户型 总面积 和占地面积
    2 家具 houseItem 有名字和占地面积
        其中 席梦思 bed 占地4平米
        衣柜chest 占地2平米
        餐桌table 占地3.5 平米

    3 将以上三个家具添加到房子中
    4 打印房子是，要求输出，户型，总面积，剩余面积，驾驭名称列表
'''

#定义一个家具的类

class Furniture:

    def __init__(self,name,area):
        self.name = name
        self.area = area


#定义一个房子类
class House:

    def __init__(self,type,free_area):
        self.type = type
        self.furniture_list = []
        self.free_area = free_area

    def add_furniture(self,furniture,):
        '''
        #1 判断要添加的家具的面积，是否超越了房子的剩余面积
        # 将家具堵想，添加到房子的家具列表中
        # 更新方法的剩余面积


        :param furniture:
        :return:
        '''

    def add_furniture(self,furniture):
        if self.free_area < furniture.area:
            print("{} 这个家具，占地面积太大，无法摆放".format(furniture.name))
            return
        self.furniture_list.append(furniture)
        self.free_area -= furniture.area


    def show_info(self):
        print("您的这个房子是 {},剩余面积是{}".format(self.type,self.free_area))
        print("\t家具列表。")
        if len(self.furniture_list) == 0:
            print("\t对不起，您的房子还没有放置任何家具")
        else:
            for furniture in self.furniture_list:
                print("\t\t家具名称：{},家具面积 {}".format(furniture.name,furniture.area))



zhuozi = Furniture("电脑桌",1.4)
yizi = Furniture("椅子",0.8)
bed = Furniture("席梦思",4)
yigui = Furniture("大衣柜",2)
cazhu = Furniture("餐桌",4)

h1 = House("三室一厅",5)
h1.show_info()
h1.add_furniture(zhuozi)
h1.show_info()
h1.add_furniture(bed)
h1.add_furniture(bed)
h1.show_info()