#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
isinstance: 查看对象是不是由某个类（如果是这个类的父类，也同样返回True）创建的,
issubclass: 查看类是不是某个类的子类

执行父类的方法:  super(子类， self).方法()
"""


class Foo():
    pass


class Bar(Foo):
    pass



class C1():
    def f1(self):
        print("C1.f1 \n")


class C2(C1):
    def f1(self):
        # 主动执行父类中的方法
        super(C2, self).f1()
        print("C2.f1 \n")



obj = Bar()

ret = isinstance(obj, Bar)
print(ret)

ret = issubclass(Bar, Foo)
print(ret)

ret = isinstance(obj, Foo)
print(ret)



obj2 = C2()
obj2.f1()




