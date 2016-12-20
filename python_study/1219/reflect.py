#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
实例： 伪造web框架的路由系统

反射： 利用字符串的形式去对象（模块）中操作（寻找）成员

基本操作：（下面的操作都是在内存中的操作）
getattr()   在对象中 寻找 指定的成员，并返回成员对象
hasattr()   在对象中 检查 指定的成员是否存在，返回True or False
delattr()   在对象中 删除 指定的成员
setattr()   在对象中 设置 指定的成员

__import__()  通过字符串导入对应的模块，并返回模块对象

"""



def run():
    inp = input("请输入要访问的url：")
    # inp 字符串类型
    m, f = inp.split('/')
    obj = __import__(m)  # 通过字符串格式导入对应的模块，返回模块对象。
    # # 如果模块在lib文件夹下
    # obj = __import__("lib." + m, fromlist=True)  # 安装路径导入，没有fromlist参数，只导入lib。
    ret = hasattr(obj, f)  # 判断comments模块中是否含有inp对应的成员
    if ret is True:
        func = getattr(obj, f)  # 去comments模块中寻找inp对应的成员并返回
        func()  # 执行我们找到的成员
    else:
        print("404")

run()