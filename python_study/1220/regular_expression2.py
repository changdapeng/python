#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
正则表达式2：基本函数
"""

import re


# math 匹配字符串起始位置
# ---------------------
ret1 = re.match("cdp", "cdp love Python")  # 匹配成功，返回math object结果
print("ret1: ", ret1, type(ret1))
ret1 = ret1.group()
print("ret1: ", ret1, "\n")



# search 匹配找到的第一个信息
# -------------------------
ret2 = re.search("love", "cdp love Python")  # 匹配成功，返回math object结果
print("ret1: ", ret2, type(ret2))
ret2 = ret2.group()
print("ret2: ", ret2, "\n")
