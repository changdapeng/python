#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
双层装饰器：

"""


LOGIN_USER = {"is_login": False}



# 定义装饰器，用于检测用户是否登录
# -----------------------------
def check_login(func):
    def inner(*args, **kwargs):
        if LOGIN_USER.get("is_login", None):
            print("欢迎当前用户 --- %s --- !!!" % LOGIN_USER["current_user"], "\n")
            ret = func(*args, **kwargs)
            return ret

        else:
            print("请登录!!!")

    return inner



# # 定义装饰器，用于检车用户是否登录并且是admin用户
# # -------------------------------------------
# def check_admin(func):
#     def inner(*args, **kwargs):
#         if LOGIN_USER.get("is_login", None) and LOGIN_USER.get("is_admin", None):
#             print("欢迎超级用户 --- %s --- !!!" % LOGIN_USER["current_user"], "\n")
#             ret = func(*args, **kwargs)
#             return ret
#         else:
#             print("请登录超级用户！！！")
#
#     return inner



# 定义装饰器，用于检测是否为admin用户
# --------------------------------
def check_admin(func):
    def inner(*args, **kwargs):
        if LOGIN_USER.get("is_admin", None):
            print("欢迎超级用户 --- %s --- !!!" % LOGIN_USER["current_user"], "\n")
            ret = func(*args, **kwargs)
            return ret
        else:
            print("请登录超级用户！！！")

    return inner



# 用户登录
# -------
def login(username, passwd):
    if username == "admin" and passwd == "admin":
        LOGIN_USER["is_login"] = True
        LOGIN_USER["current_user"] = username
        LOGIN_USER["is_admin"] = True
        print("欢迎超级用户 --- %s --- 登录!!!" % LOGIN_USER["current_user"])

    elif username == "cdp" and passwd == "123":
        LOGIN_USER["is_login"] = True
        LOGIN_USER["current_user"] = username
        LOGIN_USER["is_admin"] = False
        print("欢迎当前用户 --- %s --- 登录!!!" % LOGIN_USER["current_user"])
    else:
        print("用户名或者密码输入错误！")



# 超级用户后台管理
# --------------
# 判断条件优先的装饰器，其内部添加的功能，位于嵌套装饰后的函数的最外层
# 装饰器中函数back_manage()执行前添加的功能最先执行，函数back_manage()执行后添加的功能最后执行
@check_login  # 2、再装饰被 @check_admin 装饰后的 back_manage() 函数。
# 判断条件最后的装饰器，其内部添加的功能，位于嵌套装饰后的函数的最里层
# 装饰器中函数back_manage()执行前添加的功能最后执行，函数back_manage()执行后添加的功能最先执行
@check_admin  # 1、先装饰back_manage()函数，并生成新的back_manage()函数
def back_manage():
    print("欢迎超级用户：%s 管理后台！！！" % LOGIN_USER["current_user"], "\n")



# 查看用户信息
# -----------
@check_login
def user_profile():
    print("欢迎当前用户 --- %s ---!!!" % LOGIN_USER["current_user"])



def main():
    while True:
        inp = input("1、登录  2、查看用户信息  3、超级用户管理后台")
        if inp == '1':
            username = input("请输入用户名：")
            passwd = input("请输入密码：")
            login(username, passwd)
        elif inp == '2':
            user_profile()
        elif inp == '3':
            back_manage()
        else:
            print("error!!!")


main()
