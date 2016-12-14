#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



"""
format参数：
[[fill] align] [sign] [#] [0] [with] [,] [.precision] [type]

fill   【可选】 空白处填充的字符
align  【对齐方式】
        < 内容左对齐
        > 内容右对齐
        = 内容右对齐，将符号防止在填充自负的左边
        ^ 内容居中
sign   【可选】有无符号数字
#      【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
,      【可选】为数字添加分隔符
width  【可选】格式化位所占宽度
.precision 【可选】小数位保留精度
type   【可选】格式化类型

"""


s1 = "王力宏{0}周杰伦".format(" > ")
print("s1: ", s1, "\n")

s2 = "{name:s} -------- {age:d} -----".format(name="王力宏", age=39)
print("s2: ", s2, "\n")

s3 = "-----{name:o^20s}----{high:#d}---{age:#x}---".format(name="王力宏", high=185, age=39)
print("s3: ", s3, "\n")
