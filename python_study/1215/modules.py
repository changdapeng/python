#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
模块:(等同于其他语言的 类库)
1、内置模块
2、第三方模块  (需要安装)
安装方法：
pip3： 在命令行下使用pip3直接安装
源码安装： 先下载源码包，然后解压，在解压后的文件夹中执行 python3 setup.py install

3、自定义模块

先导入后使用

导入模块的方式：
import 模块名                使用的时候：模块名.函数名
from 模块名 import 函数名     使用的时候：直接使用函数名

导入模块并为函数定义别名:
from 模块名 import 函数名 as 自定义函数名

"""

import sys
import module1


print("sys.argv: ", sys.argv)

for path in sys.path:
    print("sys.path: ", path)

module1.print_name()
