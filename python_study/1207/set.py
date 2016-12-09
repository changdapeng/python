#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
set是一个无序不重复的序列
"""



# 列表复习
li = [11, 222, 11, 222]
print(li)
print(type(li), "\n")

tu = ("hello", "world", "xiaohong")
lt = list(tu)  # 调用list类的 __init__ 方法,
# 其内部原理为先创建一个新的集合，然后一个for循环添加传入的元素。
print(type(lt))
print(lt, "\n")



# 创建集合的两种方式
# ----------------
se1 = {111, 222, 111, 222, 333, 444}
se2 = set([11, 222, 11, 333])

print("se1: ", se1)
print(type(se1), "\n")

print("se2:", se2)
print(type(se2), "\n")



# 浅复制 和 直接复制（两个变量指向同一个对象）
se3 = se1.copy()
# se3 = se1
print(se3)

se1.add(22)
print(se1)
print(se3, "\n")



# 使用可迭代对象更新集合
# --------------------
# se1.update({66, 77})
se1.update([66, 77])
print("update se1: ", se1, "\n")



# 返回与传入的集合不同元素形成的集合，se1中存在，se2中不存在。
# ------------------------------------------------------
print(se1)
print(se2)
# se3 = se1.difference(se2)

# 返回两个集合中都不存在的元素形成的集合，se1中不存在或se2中不存在的元素组成的集合
# -------------------------------------------------------------------------
se3 = se1.symmetric_difference(se2)
print(se1)
print(se2)
print("difference se3: ", se3, "\n")



# 用se1中存在，se2中不存在的元素来更新se1集合（覆盖）
# ----------------------------------------------
# se1.difference_update(se2)

# 用se1中不存在 或 se2中不同在的元素来更新se1集合（覆盖）
# --------------------------------------------------
# se1.symmetric_difference_update(se2)
print("difference_update se1:", se1, "\n")



# 取两个集合的交集
# --------------
se3 = se1.intersection(se2)
print(se1)
print(se2)
print("intersection se3: ", se3, "\n")

# 取两个集合的交集，并更新se1
# ------------------------
# se1.intersection_update(se2)
print("intersection se1: ", se1, "\n")



# 判断两个集合是否存在空的交集（判断两个集合是否没有相同的元素）
# ----------------------
bo = se1.isdisjoint(se2)
print(se1)
print(se2)
print("isdisjoint bo: ", bo, "\n")



# 判断一个集合是否包含指定的集合
# ---------------------------
bo = se1.issuperset(se3)
print(se1)
print(se3)
print("issuperset bo: ", bo, "\n")

# 判断一个集合是否被包含于另一个集合
# -------------------------------
bo = se1.issubset(se2)
print(se1)
print(se2)
print("issubset bo: ", bo, "\n")



# 返回一个集合和另一个集合的并集
# ---------------------------
se3 = se1.union(se2)
print(se1)
print(se2)
print("union se3: ", se3, "\n")



# 添加元素
# -------
se1.add(44)
se1.add(44)
se1.add(555)
print(se1, "\n")



# 移除指定元素,不存在不报错
# -----------------------
se1.discard(44)
print(se1, "\n")



# 移除指定元素，不存在报错
# ----------------------
se1.remove(555)
# se1.remove(44)
print(se1, "\n")



# 移除某个元素,并作为返回值返回
# -----------
ret = se1.pop()
print(ret, "\n")



# 清空集合
# --------
se1.clear()
print(se1)



