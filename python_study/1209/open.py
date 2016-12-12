#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



# 打开文件
# -------
# 用open()打开时，最好指定编码参数： encoding = "utf-8"
# f = open("db", "r", encoding="utf-8")  # r 只读
# f = open("db", "w")  # w 只写，如果存在就先清空源文件，不存在就创建写内容
# f = open("db", "x")  # x 文件存在报错，不存在就创建写内容
# f = open("db", "a")  # a 追加
# f = open("db", "rb")  # b 表明以二进制方式打开
# f = open("db", "r+")  # + 表明以读写方式打开，常用



# 操作文件
# -------
# f = open("db", "r")
# data = f.read()
# print(data, type(data))


# f = open("db", "rb")
# data = f.read()
# print(data, type(data))


# f = open("db", "ab+")
# f.write(bytes("\n" + "小王小力小宏通通都在一起！", encoding="utf-8"))
# f.close()
#
# f = open("db", "rb")
# bye = f.read()
# data = str(bye, encoding="utf-8")
# print(data, "\n")



# f = open("db", "r+", encoding="utf-8")
# data = f.read()  # read()无参，表示读取全部
# # f.read(1)  # 如果以字符方式打开，1代表读取一个字符，如果以二进制模式打开，1代表读取一个字节
# print(data, "\n")
#
# # f.seek(1)  # 移动文件中的指针位置，1代表一个字节
# f.write("\n" + "小王小力小宏通通都在一起！")  # python中会在文件指针所在位置的后面写，并且会覆盖后面的内容。
#
# f.seek(1)
# print(f.tell())  # 返回指针的位置
# data = f.read()
# print(data, "\n")



# 把内存中文件的内容刷入到硬盘中
# f = open("db", 'a+', encoding="utf-8")
# f.write("一个好人")
# f.flush()



# 判断是否可读
# f = open("db", "r+", encoding="utf-8")
# ret = f.readable()
# print(ret)



# 仅读取一行
# f = open("db", "r+", encoding="utf-8")
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)



# 把文件指针后面的内容截断
# f = open("db", "r+", encoding="utf-8")
# f.seek(20)
# f.truncate()
# f.seek(1)
# line = f.read()
# print(line, "\n")



# for循环文件对象
# f = open("db", "r+", encoding="utf-8")
# for line in f:
#     print(line)






# 关闭文件
# -------
# f.close()

# 使用with open 同时打开 多个文件,代码块执行完，文件都自动关闭
# -----------------------------
# with open("db", "r+", encoding="utf-8") as f1, open("db2", "a+", encoding="utf-8") as f2:
#
#     for line in f1:
#         print(line)
#
#     f2.write("\n" + "1111111小王小力小宏通通都在一起！")
#     f2.seek(1)
#     for line2 in f2:
#         print(line2)

with open("db", "r+", encoding="utf-8") as f1, open("db2", "a+", encoding="utf-8") as f2:
    for line in f1:
        newline = line.replace("小王", "小常")
        f2.write(newline)
        f2.seek(1)

    for line in f2:
        print(line)