#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



# 代表所有的全局变量和局部变量
# ----------------
NAME = "小宏"

def show():
    a = 123
    print("locals(): ", locals())  # 打印我们定义的局部变量
    print("globals(): ", globals(), "\n")  # 打印我们定义的全局变量，和系统定义的全局变量

show()



# 生成指定对象的hash值
# ------------------
s = "小王"
hs = hash(s)
print("hash hs: ", hs, "\n")



# 返回指定对象的长度
# ----------------
s = "小力"
l = len(s)  # 查看s的字符长度
print("len l: ", l)
sb = bytes(s, encoding="utf-8")
lb = len(sb)  # 查看s的字节长度
print("len lb: ", lb, "\n")



# 返回指定序列对象的最大值、最小值、和
# --------------------------------
n = [11, 22, 33, 44]
n_max = max(n)
n_min = min(n)
n_sum = sum(n)
print("max: ", n_max, "\t", "min: ", n_min, "\t", "sum: ", n_sum, "\n")



# 求一个数的次方
# -------------
r1 = 2**10
r2 = pow(2, 10)
print("r1: ", r1, "\t", "r2: ", r2, "\n")



# 反转
# ----
li = [1, 2, 3, 4, 5]
li_re = reversed(li)
li_re = list(li_re)
print("reversed li_re: ", li_re, "\n")



# 四舍五入?
# -------
r = round(7, 4)
print("round r: ", r, "\n")



# 排序
# ----
li = [33, 22, 66, 11, 44, 77]
print("li: ", li)
li_so = sorted(li)
print("li_so: ", li_so, "\n")



# 混合
# ----
# l1 = ["小王", 11, 22, 33]
# l2 = [11, "小力", 22, 33]
# l3 = [11, 22, "小宏"]
l1 = ["小王", 11, 22, 33]
l2 = ["小力", 11, 22, 33]
l3 = ["小宏", 11, 22, 33]
li = zip(l1, l2, l3)
li = list(li)
print("zip li: ", li, "\n")



