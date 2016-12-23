#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
面向对象：成员
1、字段：
    a、静态字段：保存在类中，在类定义的时（即代码加载时），就在内存中分配空间。
    b、普通字段：保存在对象中，在对象被创建时，在内存中分配空间。

2、方法：
    所有的方法属于类
    a、普通方法：至少一个self参数，由对象执行
    b、静态方法：任意参数，        由类执行（可以由对象执行）
    c、类方法：  至少一个cls参数， 由类执行（可以由对象执行）


3、属性：
    使用方法的方式定义，使用字段的方式调用、使用
    使用不同的装饰器，只是使用不同的方法处理时，调用对应的函数。对应的功能需要自己在函数中实现




成员修饰符：


特殊成员：


其他知识：


"""


class Foo(object):

    # NAME 为 静态字段，保存在类里面
    # ----------------------------
    NAME = "CDP"


    def __init__(self):
        # name 为 普通字段, 保存在对象里面
        # ------------------------------
        self.name = "cdp"



    # 静态方法，属于类，由类调用执行。
    # ----------------------------
    @staticmethod
    def f1(name, age):
        print(name, age)
        print("我是静态方法!")



    # 普通方法，属于类，由对象调用
    # -------------------------
    def show(self):
        print("name: ", self.name, "\t", "NAME: ", self.NAME, "\n")



    # 类方法，至少有cls这一个参数(参数自动传值，为类名)，是静态方法的一种
    # 比静态方法多了自动传递类名参数的功能，可用于
    # -------------------------------------------------------------
    @classmethod
    def f2(cls):
        # cls为类名，cls()为创建对象，可以用单例模式
        print("我是类方法  cls: ", cls, type(cls))



    # 属性，对象调用时，不用加()
    # ------------------------
    @property
    def f3(self):
        return self.name[1]


    @f3.setter  # f3.setter 中的f3为我们属性中函数名,用于实现如同字段的赋值操作
    def f3(self, value):
        print(value)


    @f3.deleter  # 用于实现如同字段的删除操作
    def f3(self):
        print("f3.deleter")



    # 用于获取foo的值，返回值为定义的属性foo的值
    def ff1(self):
        print("ff1")
        return 123


    # 用于为foo赋值
    def ff2(self):
        print("ff2")


    # 用于删除foo
    def ff3(self):
        print("ff3")


    # 常用的 属性 定义方式
    # fget fset fdel 分别指定对应的操作
    foo = property(fget=ff1, fset=ff2, fdel=ff3)



obj1 = Foo()
obj2 = Foo()

# 一般情况下，自己访问自己的字段, 但是对象也可以访问类中的静态字段
# 对象中的普通字段，只能对象自己访问。
# 静态字段用类访问（万不得已的时候可以使用对象访问）
print("Foo.NAME: ", Foo.NAME, "\n")
print("obj1.name: ", obj1.name, "\t", "obj1.NAME: ", obj1.NAME)
print("obj2.name: ", obj2.name, "\t", "obj2.NAME: ", obj2.NAME, "\n")

obj1.name = "王力宏"
# 如果 对象改写了类中的静态字段，那么对象就会保存自己的字段，并不会改写类中的静态字段。
obj1.NAME = "WANGLIHONG"
print("obj1.name: ", obj1.name, "\t", "obj1.NAME: ", obj1.NAME)

obj2.name = "周杰伦"
obj2.NAME = "zhoujielun"
print("obj1.name: ", obj1.name, "\t", "obj1.NAME: ", obj1.NAME)
print("obj2.name: ", obj2.name, "\t", "obj2.NAME: ", obj2.NAME, "\n")

print("Foo.NAME: ", Foo.NAME, "\n")


Foo.f1(123, 234)
obj1.f1(123, 234)
Foo.f2()
obj1.f2()

ret = obj2.f3  # 调用 属性
print(ret)

obj2.f3 = '好'
print(obj2.f3)

del obj2.f3


ret = obj2.foo
print(ret)







