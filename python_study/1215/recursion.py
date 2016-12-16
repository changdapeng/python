#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



"""
递归：
"""

def func(n):
    n += 1
    print(n)
    if n >= 10:
        return "end!!"
    return func(n)



func(0)