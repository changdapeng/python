#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
正则表达1：基本语法
就其本质而言，正则表达式（RE）是一种小型的、高度专业化的编程语言，（在python中）它内嵌在Python中，
并通过re模块实现。正则表达式模式被编译成一系列的字节码，然后由C编写的匹配引擎执行。

字符匹配：
1. 普通字符：大多数字符和字母都会和自身匹配。
            >>> re.findall("cdp", "cdp love python")
            ['cdp']

2. 2元字符： .  ^  $  *  +  ?  { }  [ ]  |  ( )  \

"""


import re



# .  除换行符以外的任何一个字符
# --------------------------
ret1 = re.findall("cdp", "cdp love Python")  # 按照参数1指定的条件在参数2中进行匹配
ret2 = re.findall("crp", "cdp love Python")
ret3 = re.findall("c.p", "cdp love Python")
print("ret1: ", ret1)
print("ret2: ", ret2)
print("ret3: ", ret3, "\n")



# ^  以什么字符开始
# $  以什么字符结尾
# ----------------
ret4 = re.findall("^cdp", "cdp love Python")
ret5 = re.findall("^cdp", "hi cdp love Python")
ret6 = re.findall("cdp$", "hi cdp love Python")
ret7 = re.findall("python$", "hi cdp love Python")
print("ret4: ", ret4)
print("ret5: ", ret5)
print("ret6: ", ret6)
print("ret7: ", ret7, "\n")



# *  代表匹配前面的字符 0 到 n 次
# ?  代表匹配前面的字符 0 到 1 次
# +  代表匹配前面的字符 1 到 n 次
# {} 指定匹配的次数
# -----------------------------

ret8 = re.findall("cdp", "cddddp love Python")
ret9 = re.findall("cd*p", "cddddp love Python")
ret10 = re.findall("cd?p", "cddddp love Python")
ret11 = re.findall("cd+p", "cddddp love Python")
ret12 = re.findall("cd{4}p", "cddddp love Python")
ret13 = re.findall("cd{1,5}p", "cddddp love Python")

print("ret8: ", ret8)
print("ret9: ", ret9)
print("ret10: ", ret10)
print("ret11: ", ret11)
print("ret12: ", ret12)
print("ret13: ", ret13, "\n")



# []  匹配中括号中的一个字符，元字符在中括号中没有特殊意义，除了 -(范围)  ^(非)  \(字符类型)
# -----------------------------------------------------------------------------------
ret14 = re.findall("c[abc]p", "cdp love Python")
ret15 = re.findall("c[abcd]p", "cdp love Python")
ret16 = re.findall("c[a-z]p", "cdp love Python")
print("ret14: ", ret14)
print("ret15: ", ret15)
print("ret16: ", ret16, "\n")



# \  后面跟元字符表示去除特殊功能
#    后面跟普通字符实现特殊功能
#    /d  匹配任何 十进制数，相当于[0-9]
#    /D  匹配任何 非数字字符，相当于[^0-9]
#    /s  匹配任何 空白字符，相当于[\t\n\r\f\v]
#    /S  匹配任何 非空白字符，相当于[^ \t\n\r\f\v]
#    /w  匹配任何 字母数字字符，相当于[0-9a-zA-Z]
#    /W  匹配任何 非字母数字字符，相当于[^ 0-9a-zA-Z]
#    /b  匹配一个 单词边界，也就是单词和空格间的位置
ret17 = re.findall("p", "cdp love python")
ret18 = re.findall(r"p\b", "cdp love python")
print("ret17: ", ret17)
print("ret18: ", ret18, "\n")
