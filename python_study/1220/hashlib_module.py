#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



"""
hashlib 模块
用于加密相关的操作，代替了MD5模块的sha模块，主要提供SHA1，SHA224，SHA256，SHA384，SHA512
"""


import hashlib



obj = hashlib.md5(bytes("cdp_md5", encoding="utf-8"))  # 使用我们自定义的key，返回MD5加密对象。
obj.update(bytes("123", encoding="utf-8"))  # 指定加密使用的字符串，和编码
result = obj.hexdigest()  # 进行加密，并返回MD5值
print("result: ", result)