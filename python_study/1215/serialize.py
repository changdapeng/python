#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



"""
序列化：
把python的数据类型转换成字符串

反序列化：
将字符串转换成python的数据类型
"""

import json
import requests


dic = {"name": "wanglihong"}
print(dic, type(dic))

# 序列化
str_dic = json.dumps(dic)  # 将python的基本数据类型转换成字符串
print(str_dic, type(str_dic))

# 反序列化
dic2 = json.loads(str_dic)  # 将字符串格式转换成python的基本数据类型，为兼容其他语言，使用双引号
print(dic2, type(dic2))
print()



# 获取json数据并转换为python数据类型
# -------------------------------
response = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=北京")
response.encoding = "utf-8"
print(response.text, type(response.text))
dic = json.loads(response.text)
print(dic, type(dic))
print()


li = [11, 22, 33]
json.dump(li, open("db", "a+"))  # 比dumps()多执行一部操作，将序列化的字符串写入到另外一个文件中
li = json.load(open("db", "r"))  # 比load()多执行一部操作，将文件中的字符串读出，并反序列化
print(li, type(li))
