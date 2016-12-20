#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
python 模块中的特殊变量
"""

import s2
from bin import admin
import time

import os  # 跟系统相关的函数
"""
os.path.abspath(path)   返回path复返花的绝对路径
os.path.dirname(path)   返回path的目录，其实就是os.path.split(path)的第一个元素
os.path.join(path1[, path2[, .....]])   将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

"""
import sys  # 跟python解释器相关的函数
"""
sys.argv        命令行参数list，第一个元素是程序本身路径
sys.exit(n)     退出程序，正常退出时exit(0)
sys.version     获取Python解释程序的版本信息
sys.path        返回模块的搜索路径，初始化时使用Python环境变量的值
sys.platform    返回操作系统平台名称
# sys.stdin       输入相关
# sys.stdout      输出相关
# sys.stderror    错误相关
"""


# 查看模块中有哪些变量
# ------------------
# print(vars(s2))



# 文件中的注释
# -----------
print(__doc__)



# 当前程序文件所在的路径（相对路径）（常用）
# --------------------
print(__file__)



# 获取某个文件的绝对路径（常用）
# --------------------
abpath = os.path.abspath(__file__)
print(abpath)



# 找到某个文件的上级目录,并将其添加到环境变量中
# -----------------------------------------
dirpath = os.path.dirname(__file__)
sys.path.append(dirpath)
print(sys.path)



# 查看指定模块所在的包
# ------------------
print(__package__)
print(admin.__package__)




# 文件的特殊变量__name__ (可用于判断此文件是被直接执行，还是被其他的文件导入)（常用）
# ---------------------
print(__name__)  # 执行当前文件，__name__ 为 __main__
# 如果当前文件被导入，__name__ 为 文件名s1



# 进度条功能
# ---------
def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    # r = "\r%d%%" % rate_num
    r = "\r%s>%d%%" %('=' * rate_num, rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == "__main__":
    for i in range(0, 101):
        time.sleep(0.2)
        view_bar(i, 100)



