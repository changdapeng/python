#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com


"""
python支持 函数式 + 面向对象 编程


面向对象： 类 、 对象
面向对象的三大特性：封装、继承、多态


调用方法：
1、创建对象，使用类名 + ()
obj = Foo()
2、通过对象去执行方法
obj.send_mail("cdp", "good man")


对象是由类创建的，对象执行方法的时候，通过内部的类对象指针，在类中找到对应的方法执行。


类方法中的self参数：
1、self是一个Python会自动传值的参数，
2、当对象调用类方法时，对象本身会被传给self参数。


构造方法：
__init__(self)
当使用类名 + ()时 即构造对象时，自动执行构造函数。


什么时候使用面向对象编程：
1、当某一些函数具有相同参数时，将参数值一次性的封装到对象中，以后去对象中取值即可。


方法没有返回值，默认None
"""


class ManageSql(object):
    """
    进行数据库的增删改查操作
    """

    # 构造方法
    # self 为默认必须填写的参数,调用的时候Python自动传值
    # 此处的参数可以通过构造对象时，在类的()中传入参数赋值
    def __init__(self, username="cdp", password="passwordcdp", host="192.168.58.116:3306"):
        self.msg = []
        self.username = username
        self.password = password
        self.host = host
        print("这里是MangeSql的构造函数！\n")



    # 增
    def create_sql(self, message):
        if self.password == "password" + self.username:
            self.msg.append(message)
            print(self.msg)
            print("主机：%s  用户：%s  增加数据： %s " % (self.host, self.username, message))
            print("数据增加成功！\n")
        else:
            print("用户名或者密码不正确！！！")


    # 删
    def del_sql(self, message):
        if self.password == "password" + self.username:
            self.msg.remove(message)
            print(self.msg)
            print("主机：%s  用户：%s  查找数据： %s " % (self.host, self.username, message))
            print("数据查找成功！\n")
        else:
            print("用户名或者密码不正确！！！")



    # 改
    def put_sql(self, message1, message2):
        if self.password == "password" + self.username:
            nu = self.msg.index(message1)
            self.msg[nu] = message2
            print(self.msg)
            print("主机：%s  用户：%s  修改数据： %s " % (self.host, self.username, message2))
            print("数据修改成功！\n")
        else:
            print("用户名或者密码不正确！！！")



    # 查
    def get_sql(self):
        if self.password == "password" + self.username:
            print(self.msg)
            print("主机：%s  用户：%s " % (self.host, self.username))
            print("数据查看成功！\n")
        else:
            print("用户名或者密码不正确！！！")





obj = ManageSql("cdp", "passwordcdp", "192.168.58.116:3306")

obj.create_sql("cdp")  # 类中的方法只能通过对象来调用
obj.create_sql("楠楠")
obj.create_sql("周杰伦")
obj.create_sql("王力宏")

obj.del_sql("周杰伦")

obj.put_sql("王力宏", "夏洛克")

obj.get_sql()

