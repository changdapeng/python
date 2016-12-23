#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

from backend.commons import Foo


# 在不修改原类的情况下，在类中的方法前后执行我们指定的方法
# -----------------------------------------------------
class MyFoo(Foo):
    def f1(self):
        print("Foo.f1() 之前的操作")
        super(MyFoo, self).f1()
        print("Foo.f1() 之后的操作")



