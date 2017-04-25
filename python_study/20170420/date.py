#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
# 列表的常用方法

name = ["小王", "小力", "小宏"]
print(name)

name.append("xiaozhou")
print(name)

name2 = ["xiaojie", "xiaolun"]
name.extend(name2)
print(name)


name.insert(3, "王力宏")
print(name)

name.remove("王力宏")
print(name)

name.pop()
print(name)

name.pop(3)
print(name)

num = name.count("小王")
print(num)

name.reverse()
print(name)

name2 = name.copy()
name2.reverse()
print(name2)

"""


"""
# 列表当做堆栈来使用

stack = [3, 4, 5]

stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)
"""


"""
# 列表当做队列使用
# 在列表的末尾添加和弹出元素都非常的快，但是列表的开头插入和弹出元素却很慢，
# 因为所有的元素都要像左移一位。
# 若要实现一个队列，collection.deque被设计用于快速的从两端操作。
from collections import deque

queue = deque(["小王", "小力", "小宏"])
queue.append("xiaozhou")
queue.append("xiaojie")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)
"""


"""
# 列表解析式
# 列表解析式提供一个生成列表的简介方法。

# 例如，假使我们要创建一个方形列表：
squares = []
for x in range(10):
    squares.append(x*x)

print(squares)


# 同样的，使用列表解析式
squares = [x**3 for x in range(10)]
print(squares)


# 列表解析式由一堆方括号组成，方括号包含一个表达式，其后跟随一个for子句，
# 然后是零个或者多个for或if子句。
squares2 = [(x, y) for x in [1, 2, 3] for y in ["xiaowang", "xiaoli", "xiaohong"]]
print(squares2)

squares3 = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]
print(squares3)
"""


"""
# del语句可以根据索引从列表中删除一个元素，或者整个列表
a = [1, 23, 45, 67, 89, 104, 149, 345, 567]
del a[0]
print(a)

del a[2:4]
print(a)

# 清楚整个列表
del a[:]
print(a)

# 删除a对象
del a
"""


"""
# 集合是没有重复元素的无序容器
# {} 和 set() 可以用来创建集合。你必须用set()创建空的集合，而不能用{}。

basket = {"apple", "orange", "apple", "pear", "banana"}
print(basket)

print("orange" in basket)
print("bear" in basket)

a = set("hello world")
b = set("hello")

print(a)
print(b)
print(a - b)
"""

"""
# 字典，可以看做是无序的 键:值对 集合，要求是键必须是键必须是唯一的。
# 一个空的{}创建一个空的字典

tel = {"jack":4098, "sape":4139}
tel["guido"] = 4123
print(tel)

print(tel["jack"])

del tel["sape"]
print(tel)

print(list(tel.keys()))
print("jack" in tel)
print("tom" in tel)
"""


# 当循环遍历字典时，键和对应的值可以使用item()方法同时提取出来。

tel = {"jack":4098, "sape":4139, "tom":1234}

for name, num in tel.items():
    print("keys: {0}, values: {1}".format(name, num))




















