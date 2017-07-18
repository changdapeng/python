#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

import shelve

from test2.person import Person, Manger



bob = Person("Bob Smith")
sue = Person("Sue Jones", job="dev", pay=100000)
tom = Manger("Tom Jones", 50000)



db = shelve.open("persondb")
for obj in (bob, sue, tom):
    db[obj.name] = obj

db.close()



