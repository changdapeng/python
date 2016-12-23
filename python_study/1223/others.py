#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
异常处理:

"""

# 自定义异常
# ---------
class MyException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message




# 断言，条件成立执行后面的，条件 不成立，不执行后面
# --------------------------------------------
num = input("num:")
assert 1 == int(num)



while True:
    num1 = input("num1:")
    num2 = input("num2:")

    # 这里面的代码正常执行，except中的代码不执行，
    # 如果出错（出错位置下面的代码不再执行），执行except中的代码
    # -----------------------------------------------------
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        print("result: ", result, "\n")

        # 主动触发异常
        # ----------
        # raise Exception("主动出错一下")  # Exception 位置可以指定抛出的异常类型
        raise MyException("我的异常")


    except MyException as e:
        print(e)

    # e 对象中封装了错误信息
    # --------------------
    except Exception as e:  # Exception 处可以指定只捕获某种错误，Exception 指代所有类型错误
        print("出现异常，信息如下:")
        print(e)


    # 如果try中没有出错，执行else中的代码
    # --------------------------------
    else:
        print("没有出错，else")


    # 无论出错还是没有出错，都执行finally中的代码
    # ---------------------------------------
    finally:
        print("无论出错还是没有出错，都执行这里")


