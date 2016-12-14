#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



li = [11, 22, 33, 44, 55]
result = filter(lambda a: a > 22, li)
print(result, type(result))  # result 是具有生成指定结果的能力的对象，叫做生成器

# 生成器，使用函数创造的
def func():
    print("start111")
    yield 1  # 如果一个函数中出现了yield，那么就称这个函数为生成器
    print("star2222")
    yield 2
    print("star3333")
    yield 3
    print("end！！！")

func()
print("------------------")
ret = func()
print(ret)
# for i in ret:
#     print(i)


r1 = ret.__next__()  # 进入函数执行print("start111"),找到yield获取yield后面的数据，返回1
print(r1)
print(r1)

r2 = ret.__next__()  # 继续向下执行print("start222"),找到yield获取yield后面的数据，返回2
print(r2)
print(r2)

r3 = ret.__next__()  # 继续向下执行print("start333"),找到yield获取yield后面的数据，返回3
print(r3)
print(r3)

print("---------------------- \n")


# 基于生成器，实现range()
# ---------------------
def myrange(num):
    start = 0
    while True:
        if start >= num:
            break
        yield start
        start += 1


ret = myrange(10)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)