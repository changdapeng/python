#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com




def register(username, passwd):
    """
    用户用户注册
    :param username: 用户输入的用户名
    :param passwd:   用户输入的密码
    :return: True 表示注册成功  False表示注册失败
    """
    f = open("db", "a")
    temp = "\n" + username + "|" + passwd
    f.write(temp)
    f.close()
    return True



def login(username, passwd):
    """
    用于用户登录
    :param username: 用户输入的用户名
    :param passwd:  用户输入的密码

    :return:  True表示登录成功， False表示登录失败
    """
    f = open("db", "r")

    for line in f:
        line_list = line.strip("\n").split("|")
        if line_list[0] == username and line_list[1] == passwd:
            return True

    return False



def main():
    nu = int(input("输入 1：登录   2：注册"))
    if nu == 1:
        username = input("请输入用户名：")
        passwd = input("请输入密码：")

        ret = login(username, passwd)
        if ret is True:
            print("登录成功")
        else:
            print("登录失败")
    elif nu == 2:
        username = input("请输入用户名：")
        passwd = input("请输入密码：")

        ret = register(username, passwd)
        if ret is True:
            print("注册成功")
        else:
            print("注册失败")



main()