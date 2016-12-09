#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



people = {"name": "cdp", "age": 25, "heigth": 174, "weight": 70}

print(people)
print(type(people))

id_db = {
    12345: {
        "name": "xiaowang",
        "age" : 25
    },
    23456: {
        "name": "xiaoli",
        "age": 25
    },
    34567: {
        "name": "xiaohong",
        "age": 25
    }

}

print(id_db)
print(id_db[12345])
print(id_db[23456]["name"])



# 浅复制
# -----
id_db2 = id_db.copy()
print(id_db2)



# 使用指定的字典更新字典
# -------------------
id_update = {
    12345: {
        "name": "wangfei",
    },
    23456: {
        "name": "xiaoli",
        "age": 25
    }

}

id_db.update(id_update)
print("---------------------")
print(id_db)



# 把字典转换成列表（不建议使用）
# --------------
print(id_db.items())



# 返回字典的键、值
# --------------
print(id_db.keys())
print(id_db.values())  # 不建议使用



# 循环一个字典
# -----------
for key in id_db:
    print(key, id_db[key])



# 找到指定的键的值
# --------------
print(id_db.get(12345))



# 判断字典中有没有指定的键
# ---------------------
print(12345 in id_db)



# 删除指定的键对应的元素
# -------------------
id_db.pop(23456)
print(id_db)
print(id_db2)



# 在字典中取指定键的值，如果不存在就按我们指定的键和默认的值插入到字典中
# ---------------------------------------------------------------
print(id_db.setdefault(12345))
print(id_db.setdefault(123456, "hahah"))
print(id_db)



# （坑。。。。。。。。。。。）
# ---------------------
print("=====================================")
print(id_db.fromkeys([1, 2, 3, 4], 'ddddddd'))  # 按照列表中值为键，后面的值为值，生成新的字典
print(id_db)  # 原来字典的值不变
print("=====================================")



# 随机删除一个元素（不建议使用）
# --------------
id_db.popitem()
print(id_db)



# 清空字典
# -------
id_db.clear()
print(id_db)

