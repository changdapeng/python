#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



# lambda 表达式
# ------------
def f1(a1):
    return a1 + 10

ret = f1(20)
print(ret)



f2 = lambda a1: a1 + 10
ret = f2(9)
print(ret)