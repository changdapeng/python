#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



count = 0

while True:

    count += 1

    if count > 50 and count < 60:
        continue

    print("你是风儿，我是沙，缠缠绵绵到天涯。。。", count)

    if count == 100:
        print("滚.........")
        break
