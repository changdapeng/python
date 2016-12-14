#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
字符串格式化：
1、占位符： %s %d
           %[(name)][flags][width].[precision]typecode
           name: 可选，用于选择指定的key
           flags：可选，用于表示对其方式，通常和 width 一起使用，无居中功能
           （+：右对齐  -：左对齐  空格：右对齐 。。。）
           width：可选，指定占位宽度
           .precision: 有用，小数点后保留的位数
           typecode: 必选，
           %s: 字符串
           %c：字符
           %d：十进制
           %o：八进制
           %x： 十六进制
2、
"""


# 常用
s1 = "%s 和 %s 是一对好基友" % ("夏洛克", "华生")
print("s1: ", s1, "\n")


# 常用
s2 = "%(name1)s 和 %(name2)s 是一对好基友" % {"name1": "夏洛克", "name2": "华生"}
print("s2: ", s2, "\n")


s3 = "%(name1)+10s 年龄%(age)+10d和%(name2)+10s是一对好基友" % {"name1": "夏洛克", "name2": "华生", "age":33}
print("s3: ", s3, "\n")


s4 = "%(name1)-10s和%(name2)-10s是一对好基友" % {"name1": "夏洛克", "name2": "华生"}
print("s4: ", s4, "\n")


s5 = "%(name1) 10s和%(name2) 10s是一对好基友" % {"name1": "夏洛克", "name2": "华生"}
print("s5: ", s5, "\n")


# 常用
s6 = "%s 有 %.2f 块钱。" % ("夏洛克", 1123.2344)
print("s6: ", s6, "\n")


# 常用
s7 = "%s 最喜欢的是字母 %c 。" % ("夏洛克", 65)
print("s7: ", s7, "\n")


# 常用
# 当字符串中出现占位符时，要打印 %，需使用 %%
s8 = "%s 最喜欢的 十进制数字是： %d 八进制数字是： %o 十六进制是： %x  %%" % ("夏洛克", 65, 65, 65)
print("s8: ", s8, "\n")