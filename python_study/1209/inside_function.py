#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



# 取绝对值
# -------
ab = abs(-22)
print(ab, "\n")



# 查看布尔值
# ---------
bo = bool(0)
# bo = bool(())
# bo = bool([])
print(bo, "\n")



# all()中传入可迭代对象，当其中所有元素为True的时候，才为True
# -------------------------------------------------------
#　n = all((1, 2, 3, 4))
n = all([1, 2, 3, 0])
print(n, "\n")



# any()中传入可迭代对象，当其中有一个元素为True的时候，就为True
# --------------------------------------------------------
# n = any([1, 2, 0 ,()])
n = any((0, (), [], {}))
print(n, "\n")



# 自动执行指定对象的__repr__方法，(了解即可)
# ---------------------------------------
class Foo:
    def __repr__(self):
        return "1111"

n = ascii(Foo())
print(n, "\n")



# 进制转换
# -------
print("把十进制转换为二进制：", bin(15))
print("把十进制转换为八进制：", oct(15))
print("把十进制转换为十六进制：", hex(15), "\n")



# 将字符串转换成对应的字节类型
# -------------------------
# utf-8 汉字占3个字节， GBK 汉字占2个字节
s = "小明"
n = bytes(s, encoding="utf-8")
print(n, "\n")



# 将字节类型转换成字符串
# --------------------
s = str(n, encoding="utf-8")
print(s, "\n")



