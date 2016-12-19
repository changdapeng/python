#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



"""
pickle 为Python的序列化和反序列化模块，和json的区别为：只能Python使用，不能用户跨语言的通信。
JSON 只支持Python的基本数据类型。
JSON 更加适合跨语言，主要是对字符串和基本数据类型做操作
pickle 主要是对python的所有类型做操作
"""

import pickle
import json


li = [11, 22, 33, 44]
s = pickle.dumps(li)
print(s, type(s))

li = pickle.loads(s)
print(li, type(li))
print()


class Foo(object):
    def __index__(self):
        pass

f = Foo()
# json.dumps(f)  # json 无法处理类
fp = pickle.dumps(f)
print(fp, type(fp))