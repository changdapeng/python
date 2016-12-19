#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


import time
import datetime


"""
time 模块功能：
"""
# 时间戳
# -----
time1 = time.time()
print("time1: ", time1, type(time1), "\n")  # 从1970年开始计时到现在的秒数



# 系统当前时间(字符串格式)
# ----------------------
time2 = time.ctime()
print("time2: ", time2, type(time2), "\n")  # 返回系统当前时间的字符串格式



# 本地时间(struct_time时间对象格式)
# -------
time3 = time.localtime()
print("time3: ", time3, type(time3), "\n")



# 将时间戳转换成struct_time格式
# ---------------------------
time4 = time.gmtime()  # 格林尼治时间
print("time4: ", time4, type(time4))
print("year: ", time4.tm_year, "month: ", time4.tm_mon, "\n")



# 将struct_time格式转换成时间戳
# ---------------------------
time5 = time.mktime(time.localtime())
print("time5: ", time5, type(time5), "\n")



# 延时
# ----
print("-------- begin --------")
time.sleep(1)
print("--------- end ----------")
print()


# 将struct_time格式转换成指定的字符串格式
# -------------------------------
time6 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("time6: ", time6, type(time6), "\n")



# 将字符串格式的时间转换成时间兑现struct_time格式
# -------------------------------------------
time7 = time.strptime("2016-05-06", "%Y-%m-%d")
print("time7: ", time7, "\n")



"""
datetime模块功能：
"""
# 输出当前日期（字符串格式）
# -----------------------
datetime1 = datetime.date.today()
print("datetime1: ", datetime1, type(datetime1), "\n")



# 将时间戳转换成日期格式（字符串格式）
# --------------------------------
datetime2 = datetime.date.fromtimestamp(time.time())
print("datetime2: ", datetime2, type(datetime2), "\n")



# 当前时间（字符串格式）（主要用）
# -------------------
datetime3 = datetime.datetime.now()
print("datetime3: ", datetime3, type(datetime3), "\n")






