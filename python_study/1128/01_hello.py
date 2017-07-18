#! /usr/bin/env python
# -*- coding: utf-8 -*-


name = "CDP"
age = 25
address = "BeiJing"

print(name, "\n", age, "\n", address)

year = 1992  # 一个物理行，也是一个逻辑行
month = 7  # 一个物理行， 也是一个逻辑行
day = 24
hour = 19
minute = 6
second = 18

if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # 这三行物理航看成一个逻辑行
        print("我于{0}年{1}月{2}日{3}时{4}分{5}秒，出生。".format(year, month,
                                                      day, hour, minute, second))
        # 上面的两行物理行为一个逻辑行。



