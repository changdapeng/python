#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


import shelve



db = shelve.open("persondb")

for key in db:
    print(db[key])

