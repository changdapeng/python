#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com




# 去掉字符串中的指定字符，默认为空格
# -------------------------------
username = input("please enter you name:")

if username.strip() == "cdp":
    print("welcome!")




# 按照指定的字符拆分字符串
# ----------------------
names = "xiaowang,xiaoli,xiaohong"

name2 = names.split(",")
print(name2)



# 按照指定的字符把列表元素拼接在一起
# -------------------------------

print('|'.join(name2))



# 判断字符串中是否包含某个字符
# -------------------------
name = "changdapeng"
print('a' in name)



# 把字符串的首字母大写
# ------------------
print(name.capitalize())

name = "chang da peng"
print(name)
print(name.capitalize())



# 给字符串中的{}内的变量赋值
# -----------------------
msg = "hello, {name}, it's been a long time since love you..."

msg2 = msg.format(name = "lee")
print(msg2)

msg3 = "hhhhhh{0}, jjjjjjjjjjj{1}"
print(msg3.format(11111, 22222))



# 把字符串放到指定大小的中间位置，并使用指定的符号填充其他位置
# ------------------------------------------------------
boy = "xiao ming"
print(boy.center(30, '-'))



# 查找字符串中的指定的字符的位置
# ---------------------------
print(boy.find('o'))



# 判断字符串是否为数字
# ------------------
age = input("enter your age")
if age.isdigit():
    age = int(age)
    print(type(age))
else:
    print("invalid data!")



# 判断字符串是否已指定的字符开头或者结尾
# ----------------------------------
print(name.startswith('c'))
print(name.endswith("p"))



# 把字符串转换为大写或者小写
# -----------------------
print(name.upper())
print(name.lower())















