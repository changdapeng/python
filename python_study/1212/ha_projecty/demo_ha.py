#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

import json


def fetch(backend):
    result = []
    with open("ha.conf", "r", encoding="utf-8") as f:
        flag = False
        for line in f:
            if line.strip().startswith("b") and line.strip().strip("\n") == "backend" + backend:
                flag = True
                continue


            if flag == True and line.strip().startswith("backend"):
                """

                """
                flag = False
                break

            if flag == True and line.strip() == True:
                result.append(line)

    return result



def add(backend, record):







r = input("请输入一个字典")
dic = json.loads(r)
print(dic, type(dic))
bk = dic["name"]
print("your name is %s" % bk)








