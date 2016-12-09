#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

import copy



# 拷贝
# ----
name = ['hello', 'world', [1, 2, 3, 4, 5], 'xiaowang', 'xiaoli', 'xiaohong']
name2 = name.copy()  # 浅copy
name22 = name  # 直接赋值操作，会直接把列表对象的地址付给变量
name3 = copy.deepcopy(name)  # 深copy

# 列表中的列表在copy的时候只copy子列表的地址，即默认为浅copy
name[2][1] = 222222222
name2[2][3] = 444444444
name2[1] = 'boy'
name22[0] = 'good'

print(name)
print(name2)
print(name22)
print(name3)



# 将列表的首尾颠倒
# ---------------
print("---------------------")
name.reverse()
print(name)



# 排序
# ----
age = [23, 21, 45, 2, 23, 44, 55, 34]
age.sort()
print(age)



# 列表的元素个数
# ------------
print(age.__len__())



# 在列表的最后追加列表
# ------------------
age.extend([24, 25, 26])
print(age)



# 弹出最后一个元素
# --------------
age.pop()
print(age)



# 在列表的最后追加一个元素
# ---------------------
age.append(222222)
print(age)



# 判断列表中有没有指定元素
# ---------------------
print(23 in age)



# 返回列表中指定元素的序列下标
# -------------------------
age_index = age.index(23)
print(age_index)



# 返回列表中指定元素的个数
# ----------------------
age_count = age.count(23)
print(age_count)



# 删除列表中的指定元素
# ------------------
age.remove(23)
print(age)
age.remove(23)
print(age)



# 删除列表中的元素
# --------------
del age[3]
print(age)



# 在制定位置插入指定的元素
# ---------------------
age.insert(1, 11111111)
print(age)



# 清空列表
# -------
age.clear()
print(age)





