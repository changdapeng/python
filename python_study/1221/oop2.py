#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



"""
继承: 支持多继承


"""


class F1(object):  # 父类、基类

    def __init__(self):
        self.name = "cdp的爹"


    def show(self):
        print("F1 的 show() 方法 \n")


    def show_name(self):
        print(self.name)



class F2(F1):  # 子类、派生类

    # def __init__(self):
    #     self.name = "cdp"



    def bar(self):
        print("F2 的 bar() 方法 \n")



    def show(self):  # 自己类中的方法优先级高于同名的父类中继承的类方法
        print("F2 的 show() 方法 \n")




obj = F2()
obj.show()
obj.bar()
print(obj.name)
obj.show_name()