#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

# 定义常量， 默认都用大写字母表示
AUTHOR_NAME = "CDP"

age = 25

"""
# 判断一次，使用if判断
guess_num = int(input("input your age:"))

if guess_num == age:
    print("OK!!!")
elif guess_num > age:
    print("too big!!!")
else:
    print("too little!!")
"""


"""
# 循环判断10次

for i in range(10):
    guess_num = int(input("input your age:"))
    if guess_num == age:
        print("OK!!!")
        break  # 输入正确就终止，跳出

    elif guess_num > age:
        print("too big!!!")

    else:
        print("too little!!")
"""

# 判断循环到第三次后是不是继续
for i in range(10):
    guess_num = int(input("input your age:"))
    if guess_num == age:
        print("OK!!!")
        break  # 输入正确就终止，跳出

    elif guess_num > age:
        print("too big!!!")

    else:
        print("too little!!")

    if i == 2:
        msg = input("can you go again:")

        if msg == 'y':
            continue  # 跳出当次循环
        else:
            break