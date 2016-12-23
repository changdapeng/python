#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
面向对象：成员修饰符
1、公有（字段和方法）：可以被继承，可在外部访问
2、私有（字段和方法）：不可被继承，只能在内部访问
"""


class Foo(object):

    # 定义公有静态字段，可在外部访问，可被继承
    # ------------------------------------
    HATE = "懒惰"

    # 定义私有静态字段，不可以在外部访问，不可被继承
    # ------------------------------------------
    __LOVE = "lnn"



    def __init__(self, name, age):

        # 正常定义的，为公有普通字段，可在外部访问，可被继承
        # ---------------------------------------------
        self.name = name

        # 在字段前加两个下划线，为私有普通字段，不可在外部访问，不可被继承
        # ---------------------------------------------------------
        self.__age = age



    def show(self):
        print("HATE: ", self.HATE)
        print("__LOVE: ", self.__LOVE, "\n")



class Bar(Foo):

    def f2(self):
        print(self.name, "\n")  # 公有普通字段，可被继承
        # print(self.__age)  # 私有普通字段，不可被继承，






obj = Foo("cdp", 25)

print(Foo.HATE, "\n")
# print(Foo.__LOVE)

obj.show()


print(obj.name)
# print(obj.__age)

# (不建议使用的,不到万不得已不使用的)可以在外部访问私有成员
print(obj._Foo__age)



obj2 = Bar("cdp", 25)
obj2.f2()

print(Bar.HATE)
# print(Bar.__LOVE)
