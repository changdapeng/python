#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


LOGIN_USER = {"is_login": False}


# 定义装饰器，用户检测用户是否登录
# -----------------------------
def manage_login(func):
    def inner(*args, **kwargs):
        if LOGIN_USER["is_login"]:
            print("欢迎当前用户 --- %s --- !!!" % LOGIN_USER["current_user"], "\n")
            ret = func(*args, **kwargs)
            return ret

        else:
            print("请登录!!!")

    return inner



# 用户后台管理
# -----------
@manage_login
def back_manage():
    print("欢迎：%s 用户管理后台！！！" % LOGIN_USER["current_user"], "\n")



# 用户登录
# -------
def login(username, passwd):
    if username == "cdp" and passwd == "123":
        LOGIN_USER["is_login"] = True
        LOGIN_USER["current_user"] = username
        print("欢迎当前用户 --- %s --- 登录!!!" % LOGIN_USER["current_user"])
    else:
        print("用户名或者密码输入错误！")



# 主函数
# -----
def main():
    while True:
        inp = input("1.后台管理  2.登录")
        if inp == '1':
            back_manage()
        elif inp == '2':
            username = input("请输入用户名：")
            passwd = input("请输入密码：")
            login(username, passwd)
        else:
            print("error!")

        print("-------------------- \n")



main()
