#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
递归：

"""

def func(num):
    if num == 1:
        return 1
    return num * func(num - 1)

x = func(5)
print(x)
