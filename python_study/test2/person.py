#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return "[Person: %s, %s]" % (self.name, self.pay)



class Manger(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent+bonus)

    def something_else(self):
        pass








if __name__ == "__main__":
    """
    person.py test code
    """
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

    print(bob.lastname(), sue.lastname())
    sue.give_raise(0.1)
    print(sue.pay)

    print(sue)

    tom = Manger("Tom Jones", 50000)
    tom.give_raise(0.1)
    print(tom.lastname())
    print(tom)

    print("--All There--")
    for obj in (bob, sue, tom):
        obj.give_raise(0.1)
        print(obj)








