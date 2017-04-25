#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

import getpass

user = "CDP"
passwd = "123456"

"""
# 提示用户名错误是不安全的。
username = input("username:")

if username == user:
    password = input("password:")

    if password == passwd:
        print("OK! you can pass!")

    else:
        print("you password is not right!!!")
        print("please input it again:")
        password = input("password:")

        if password == passwd:
            print("OK! you can pass!")

        else:
            print("you password is not right!!!")
            print("please input it again:")
            password = input("password:")

            if password == passwd:
                print("OK! you can pass!")

            else:
                print("you password is not right!!!")
else:
    print("your username is not right!")
"""

# 安全并且简单的处理方式

username = input("username:")
password = input("password:")

if username == user and password == passwd:
    print("you are righr, you can go in !!!")
else:
    print("your username or password is not right please input it again:")

    username = input("username:")
    password = input("password:")

    if username == user and password == passwd:
        print("you are right, you can go in !!!")
    else:
        print("your username or password is not right please input it again:")

        username = input("username:")
        password = input("password:")

        if username == user and password == passwd:
            print("you are righr, you can go in !!!")
        else:
            print("你可以滚了 !!!")
