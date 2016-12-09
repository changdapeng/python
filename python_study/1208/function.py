#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com



# 函数中没有return，Python中会自动默认return None
# ---------------------------------------------
def f1():
    print("123", "\n")
#    return True

ret = f1()
print(ret, "\n")



# 静态参数类型：1.普通参数 2.默认参数（从参数列表的最右边开始放） 3.指定参数
# --------------------------------------------------------------------
def sendemail(address, content, tag='BLOG'):

    print("发送邮件成功！！！")
    print(address, content, tag)
    return True


address = 'xiaohong'
content = 'nihao!!!'
tag = 'title'

ret = sendemail(address, content, tag = 'haha')
print(ret, "\n")



# 动态参数类型：1.*args 把args当做元组，传入参数作为元祖元素
# ------------------------------------------------------
def f2(*args):
    print(args, type(args))
    return True

li = [11, 22, 33, "xiaohong"]

# 个人理解：*可以 大致 按照C语言中的 指针* 和 取内容 理解。
# *args表明args为一个元祖（元组名代表元祖的地址），*li可以理解为取li列表中的内容
ret = f2(11, 22, 33, "xiaohong")  # 以 * 方式传进的参数会作为 args 元组 的元素
ret = f2(li)  # 传入的参数是列表也要作为args元祖的元素
ret = f2(*li)  # 在传入的参数前加*，相当于传入列表的元素给args元祖。
print(ret, "\n")



# 动态参数类型：2.**kwargs 把kwargs当做字典，传入参数作为字典元素
# -----------------------------------------------------------
def f3(**kwargs):
    print(kwargs, type(kwargs))
    return True

dic = {'k1':11, 'k2':22}

ret = f3(n1="xiaohong", n2="xiaoming", n3=25)  # kwargs为字典，传入的参数要作为字典的元素
ret = f3(kk=dic)  # 传入一个字典，那么这个字典也要作为kwargs字典的元素
ret = f3(**dic)  # 使用 ** 把字典中的元素传给kwargs字典作为其元素
print(ret, "\n")



# 万能参数：*args **kwargs, **潜规则的使用方式**
# --------------------------------------------
def f4(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    return True

ret = f4(11, 22, 33, name='xiaoming', age = 25)
print(ret, "\n")



# Python中传参数的时候列表和字典传递的是引用?
# ---------------------------------------
name = "xiaowang"
age = 18
friends = ["xiaohong", "xiaoming"]
like = {"read": "book", "eat": "mantou"}

def change_people(name, age, friends, like):
    name = "xiaogou"
    print(name)
    age += 10
    print(age)
    friends.extend(["xiaomao", "xiaozhu"])
    print(friends)
    like.clear()
    print(like)
    return True

ret = change_people(name, age, friends, like)
print("the ret: ", ret)
print("the name: ", name)
print("the age: ", age)
print("the friends: ", friends)
print("the like: ", like)
print()



# 全局变量
# -------
name = "xiaowang"  # 全局变量没有使用大写，不规范。。。
NAME = "name"  # 规定，定义全局变量的使用，使用大写！！！
the_num = [1, 2, 3, 4, 5]
def f1():
    global name  # 表示，name是全局变量
    # 如果对在局部变量内对全局变量重新赋值，需要在在前面加global
    name = "hahaha"  # 局部变量作用于内优先级高于全局变量
    print("局部变量: ", name)

    the_num.append(11)  # 在局部作用域内可以修改全局变量的列表、字典，如需重新赋值则同样需要加 global
    # 加不加global的原因在于，系统对于 = 不能确定是给一个旧的变量重新赋值还是创建一个新的变量的时候，要在修改的变量名前加global。
    print(the_num)

f1()
print("全局变量：", name)



