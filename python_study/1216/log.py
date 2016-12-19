#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
日志系统

"""


import logging

# logging.basicConfig(filename="example.log", level=logging.INFO,
#                     format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %I:%M:%S %p",
#                     )
#
#
# logging.warning("user: [CDP] atempted wrong password three times!")


# 全局的log句柄
logger = logging.getLogger("TEST-LOG")  # 获取logger对象
logger.setLevel(logging.DEBUG)  # 设置一个全局的日志级别（handler的级别比logger不能更低）


# 向屏幕输出的 handler
ch = logging.StreamHandler()  # 把日志打印到屏幕
ch.setLevel(logging.DEBUG)  # 定义日志级别


# 向文件输出的 handler
fh = logging.FileHandler("access.log")  # 将日志打印到指定的文件
fh.setLevel(logging.WARNING)  # 定义日志级别


# 定义日志输出的格式
formatter = logging.Formatter("%(asctime)s - %(name)s -%(process)d- %(filename)s - %(funcName)s-%(lineno)s- %(levelname)s - %(message)s")


# 为handler指定输出的格式
ch.setFormatter(formatter)
fh.setFormatter(formatter)



# 把我们定义的handler 注册到 我们定义的logger 句柄
logger.addHandler(ch)
logger.addHandler(fh)


# 打印日志
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")
