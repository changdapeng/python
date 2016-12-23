#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com
"""
实际生产的代码，
我们调用别人写好的库，由setting中的变量指定：backend.commons，
但是需要在调用的类的方法前后增加功能，所以在文件lib中新建了类继承别人库中的类，并改写了方法。
当我们使用新的类的方法时，改写setting中的变量即可。不需要改写我们自己写的代码。
"""

from setting import ClassName, Path


def execute():
    model = __import__(Path, fromlist=True)  # 根据setting中的变量导入模块
    cls = getattr(model, ClassName)  # 使用反射，得到我们调用的类
    obj = cls()  # 创建对象
    obj.f1()  # 执行方法







if __name__ == "__main__":
    execute()
