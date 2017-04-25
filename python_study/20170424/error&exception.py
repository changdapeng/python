#! /usr/bin/env python
# Author: CDP
# email: dapeng_chang@163.com

"""
Python（至少）有两种错误很容易区分：语法错误 和异常。

语法错误（也称为解析错误）,解析器重复违规行并显示指向检测到错误的行中最早点的一个“箭头”。
错误是由箭头前面的标记引起的（至少检测到是这样的）

即使语句或表达式在语法上正确，当尝试执行语句或表达式时也可能导致错误。
执行期间检测到的错误称为异常，并不是无条件致命的.
"""

# print(10 * (1/0))

"""
# 编写处理所选异常的程序

while True:
    try:
        x = int(input("Please enter a number"))
        break
    except ValueError:
        print("Oop! That was no valid number. Try again...")


# try 语句可能有多个子句，以指定不同的异常处理程序。
# except子句可以将多个异常命名为括号元组
try:
    pass
except (RuntimeError, TypeError, NameError):
    pass

"""


"""
# try ...except 语句有一个可选的 else 子句 ，其出现时，必须放在所有 except 子句的后面。
# 如果try子句不引发异常，那么它对于必须执行的代码非常有用。
import sys
for arg in ("a.txt",):
    try:
        f = open(arg, "r")
        # f.write("asdfasdfasdf\ndsfasdfasdfasdf\nasdfasdfasdfa\nasdfasdfasdf\n")
    except IOError:
        print("cannot open", arg)
    else:
        print(arg, "has", len(f.readlines()), "lines")
        f.close()

# 使用 else 子句比把额外的代码放在 try 子句中要好，
# 因为它可以避免意外捕获不是由 try ... except 语句保护的代码所引发的异常。

"""

"""
# 当异常发生时，它可能有一个关联的值，也称为异常的参数。参数的存在和类型取决于异常类型。
# except子句可以在异常名称之后指定一个变量。
# 这个变量将绑定于一个异常实例，同时异常的参数将存放在 instance.args 中。
# 为方便起见，异常实例定义了 __str__() ，因此异常的参数可以直接打印而不必引用 .args。
try:
    raise Exception("spam", "eggs")
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print(type(x), type(y))
    print(x, y)



# 异常处理程序不仅能处理在try子句直接发生的异常，
# 也能处理try子句调用的函数中（即使是间接地）发生的异常。

def this_fails():
    x = 1/0

try:
    this_fails()

except ZeroDivisionError as err:
    print("Handing run-time error:", err)

"""


"""
# raise 语句允许程序员强行引发一个指定的异常。
#raise NameError("HiThere")

# raise 的唯一参数指示要引发的异常。它必须是一个异常实例或异常类（从 Exception 派生的类）。


try:
    raise NameError("HiThere is an error!")
except NameError:
    print("raise an name error")
    raise

# 如果你确定需要引发异常，但不打算处理它，一个简单形式的 raise 语句允许你重新引发异常
"""

"""
# 程序可以通过创建新的异常类来命名自己的异常
# 异常通常应该继承 Exception 类，直接继承或者间接继承都可以。

class My_Error(Exception):
    pass


class InputError(My_Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(My_Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
"""

"""
# 定义清理操作
# try 语句有另一个可选的子句，目的在于定义必须在所有情况下执行的清理操作。

try:
    raise KeyboardInterrupt
finally:
    print("goodbye!!!")
"""

"""
# 不管有没有发生异常，在离开 try 语句之前总是会执行 finally 子句。
# 当 try 子句中发生了一个异常，并且没有 except 字句处理（或者异常发生在 except 或 else 子句中），
# 在执行完 finally 子句后将重新引发这个异常。
# try 语句由于 break 、contine 或return 语句离开时，同样会执行finally 子句。

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is ", result)
    finally:
        print("executing finally clause")

divide(2, 1)

divide(2, 0)

divide("2", "1")
"""

















































