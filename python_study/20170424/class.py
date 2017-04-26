#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
类

命名空间 是从名称到对象的映射。
关于命名空间需要知道的重要一点是不同命名空间的名称绝对没有任何关系；
包含内建名称的命名空间在Python解释器启动时创建，并且不会被删除。
模块的全局命名空间在读入模块定义时创建；通常情况下，模块命名空间也会一直保存到解释器退出
在解释器最外层调用执行的语句，不管是从脚本文件中读入还是来自交互式输入，
都被当作模块 __main__ 的一部分，所以它们有它们自己的全局命名空间。
函数的本地命名空间在调用函数时创建，并在函数返回或引发未在函数中处理的异常时删除。

作用域是Python程序的文本区域，其中可直接访问命名空间。
global 语句可以用来指明某个特定的变量位于全局作用域并且应该在那里重新绑定；
nonlocal 语句表示否定当前命名空间的作用域，寻找父函数的作用域并绑定对象。
"""
"""
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
"""


"""
类定义的最简单形式如下：

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

类的定义就像函数定义（ def 语句），要先执行才能生效。

类对象支持两种操作：属性引用和实例化。
__doc__ 也是一个有效的属性，返回类的文档字符串
类实例化使用函数符号。只是假装类对象是一个无参数函数，返回类的一个新的实例。
许多类喜欢创建具有针对特定初始状态定制的实例的对象。因此类可以定义一个名为 __init__() 的特殊方法，
当类定义了 __init__() 方法，类的实例化会为新创建的类实例自动调用 __init__() 。
__init__() 方法可以带有参数，类实例化操作的参数将传递给 __init__() 。

能被实例对象理解的唯一操作是属性引用。有两种有效的属性名称，数据属性和方法。

"""

class BookName():
    def __init__(self, *args):
        self.book = ["数学", "语文", "英语"]
        for name in args:
            self.book.append(name)
        print(self.book)


book1 = BookName()
book2 = BookName("物理", "化学", "生物")

































