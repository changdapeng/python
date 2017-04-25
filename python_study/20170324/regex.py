#!/usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

import re


patt = "(\w\w\w)-(\d\d\d)"


m = re.match(patt, "abc-123")
if m is not None:
    print(m.group())
else:
    print("m is None")

print(m.groups())


print("---------------------------------------------")



attn = re.subn("X", "Mr. Smith", "attn: X\n\nDear X, \n")
print(attn[0])