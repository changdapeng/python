#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

# Python开发规范，每一行不得超过80个字符
# 这里可以写注释

"""
Python开发规范，每一行不得超过80个字符
Python开发规范，每一行不得超过80个字符
Python开发规范，每一行不得超过80个字符
这里可以写多行注释，或者注释多行代码。
"""
# input() 默认接收的为字符串格式
name = input("input your name:")

# 使用int() 转换为数字格式
age = int(input("input your age:"))

job = input("input your job:")

"""
print("-----------BEGIN-----------")

print("name:\t", name, "\n", "age:\t", age, "\n", "job:\t", job)

print("------------END------------")
"""

msg = """
--------BEGIN------------
name:   %s
age:    %d
job:    %s
--------END------------
""" %(name, age, job)

print(msg)

