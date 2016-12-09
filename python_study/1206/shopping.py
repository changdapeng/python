#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
购物车程序：
用户启动时先输入工资
用户启动程序后打印商品列表
允许用户选择购买商品
允许用户不断的购买各种商品
购买时检测余额是否足够，如果足够直接扣款，否则打印余额不足
允许用户主动退出程序，退出时打印已购列表
"""

# 产品列表
product_list = {"iphone":7600,
                "macpro":15600,
                "mi":3000,
                "tesla":820000,
                "bike":1000,
                "cloth":700
                }

shop_car = []

shop_cost = 0

salary = input("please input your salary:")

if salary.isdigit():
    salary = int(salary)
else:
    exit("invaild data type...")


welcome_msg = "Welcome to shopping".center(30, '-')


exit_flag = False

while not exit_flag:

    # 打印欢迎语句
    print()
    print(welcome_msg)


    # 打印产品列表
    for key in product_list:
        print(key, product_list[key])


    # 等待用户选购或退出
    user_choice = input("what du you want to buy or 'q' to exit:")


    # 统计用户已花费的钱
    if user_choice in product_list:
        shop_cost += product_list[user_choice]

        if shop_cost > salary:
            print("you can't choice again, because you salay is not enough!")
            exit_flag = True
        else:
            shop_car.append(user_choice)
            print("you can buy it , you have cost:\033[31;1m[%s]\033[0m" %shop_cost)


    elif user_choice == 'q':
        print("your shop_car: ")

        for value in shop_car:
            print(value)

        print("your choice is pruduct !!!")
        print("you have cost:　", shop_cost)
        exit_flag = True

    else:
        print("your choice is err!!! ")


