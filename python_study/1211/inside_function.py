#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


import random



# 检测传递的值是否可以被调用
# ------------------------
def f1():
    pass

f2 = 123

ret1 = callable(f1)
ret2 = callable(f2)

print("callable ret1: ", ret1)
print("callable ret2: ", ret2, "\n")



# ASC码与对应字符之间的转换
# -----------------------
r = chr(65)
print("chr r: ", r)

b = ord("z")
print("ord b: ", b, "\n")



# 生成随机验证码
# -------------
# import random  # 使用random功能需要导入的模块
li = []

for i in range(6):
    num2 = random.randrange(0, 10)

    if num2 % 2 == 1:
        num = random.randrange(65, 91)  # 即产生 A-Z a-z 对应的ASCII码范围
        c = chr(num)
        li.append(c)
    else:
        num = random.randrange(0, 10)
        c = str(num)
        li.append(c)

result = "".join(li)
print("result: ", result, "\n")



# 编译字符串为python可执行的代码，并执行
# -----------------------------------
s = "print('hello world!')"
# 编译模式：single, eval, exec
r = compile(s, "<string>", "exec")  # 把字符串s 编译成python exec 可执行的代码
print(r)
exec(r)  # 执行我们编译好的代码 r, 没有返回值
exec(s)  # 也可以直接接受字符串, 自动转换成python代码并执行，没有返回值
print()

s2 = "8*8"
ret = eval(s2)  # 执行字符串中的表达式，并将执行结果返回
print("eval ret: ", ret, "\n")



# 查看一个对象都提供了什么功能
# -------------------------
print(dir(dict))  # 获取字典都提供了什么功能
# help(dict)



# 分别求出两数相除的商和余数
# -----------------------
ret = divmod(97, 10)
print("divmod ret: ", ret, type(ret), "\n")



# 判断一个对象是不是一个类的实例
# ---------------------------
li = []
ret = isinstance(li, list)
print("isinstance ret: ", ret, "\n")



# 根据指定的条件，过滤可迭代对象
# ---------------------------
li = [11, 22, 33, 44, 55]

# 指定过滤的条件
def func(a):
    if a > 22:
        return True

ret = filter(func, li)  # 根据指定的条件，循环判断可迭代对象中的元素，返回符合条件的元素。
print(ret, type(ret))  # filter 过滤器返回的是filter类型，可以使用list() tuple()转换
ret = list(ret)
print("filter ret: ", ret, "\n")



# lambda 表达式
# ------------
f1 = lambda a: a > 40
ret = f1(90)
print("lambda ret:", ret, "\n")

# 使用lambda表达式的简单写法
ret = filter(lambda a: a > 22, li)
print(list(ret), "\n")



# 根据指定的条件，批量对可迭代对象的元素进行操作
# -----------------------------------------
li = [11, 22, 33, 44, 55]

# 指定操作的条件
def func(a):
    return a + 100

ret = map(func, li)  # 根据指定的条件，循环对序列中的元素进行操作，返回运算后的结果。
print(ret, type(ret))  # map()返回的是map类型，可以使用list() tuple()转换
ret = list(ret)
print("map ret: ", ret, "\n")

# 使用lambda表达式的简单写法
ret = map(lambda a: a + 100, li)
print(list(ret), "\n")

# filter 函数返回True，将元素添加到结果中
# map    将函数返回值添加到结果中
