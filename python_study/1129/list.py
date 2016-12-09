#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

name = [1, 2, 334, 324, 22, 342, 'huiyu', 'chagn', 123, 34, 1, 2, 1]

print(name)

print(name[1])
print(name[0:5])
print(name[2:8:2])

ele_index = name.index(1)
ele_count = name.count(1)
name[ele_index] = 11111111

print(name)

name2 = ['huiyu', 'ok', 'anny', 'lnn']

name.extend(name2)
print(name)

name3 = [23, 2, 344, 43, 43, 44, 6, 2, 76, 4545, 3, 2]

name3.sort()
print(name3)




