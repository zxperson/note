一：原理

import time
import traceback

def func(number):
    li = [1,2,4]
    if number < 4:
        return li[number-1]
    else:
        if number > 3:
            return func(number-1)+func(number-2)+func(number-3)

class MyTimer(object):
    
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
    
        print("异常类是:", exc_type)
        print("异常的值(描述信息)是：", exc_val)
        for stack in traceback.extract_tb(exc_tb):  # 打印异常的回溯。
            print(stack)

        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
    
        print("函数的执行时间: %s 毫秒" % self.msecs)

        return True

with MyTimer():
    print(func(15))
    raise ValueError("haha")
    

'''
上下文管理协议(Context Management Protocol)：包含方法 __enter__() 和 __exit__()，支持该协议的对象要实现这两个方法。
上下文管理器(Context Manager)：支持上下文管理协议的对象，这种对象实现了__enter__() 和 __exit__() 方法。
运行时上下文(runtime context):由上下文管理器创建，通过上下文管理器的 __enter__() 和__exit__() 方法实现。可以理解为这两个方法里面的代码。
上下文表达式(Context Expression):with 语句中跟在关键字 with 之后的表达式，该表达式要返回一个上下文管理器对象.
语句体(with-body):with 语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的 __enter__() 方法，执行完语句体之后会执行 __exit__() 方法。
'''

# with 语句 执行 过程：
#1.执行 context_expression，生成上下文管理器 context_manager
#2.调用上下文管理器的 __enter__() 方法；如果使用了 as 子句，则将 __enter__() 方法的返回值赋值给 as 子句中的 变量。
#3.执行语句体 with-body
#4.不管是否执行过程中是否发生了异常，执行上下文管理器的 __exit__() 方法，__exit__() 方法负责执行“清理”工作，如释放资源等。
#  如果执行过程中没有出现异常，或者语句体中执行了语句 break/continue/return，则以 None 作为参数调用 __exit__(None, None, None) 
#  如果执行过程中出现异常，则使用 sys.exc_info 得到的异常信息为参数调用 __exit__(exc_type, exc_value, exc_traceback)方法
#5.出现异常时，如果 __exit__(type, value, traceback) 返回 False，则会重新抛出异常，让with 之外的语句逻辑来处理异常，这也是通用做法；
#  如果返回 True，则忽略异常，不会重新抛出异常。


注意： 如何捕获异常的详细信息呢？

import sys
import traceback

def test():
    raise NameError("ahha")

try:
    test()
except Exception as err:
    ex_type, ex_val, ex_stack = sys.exc_info()
    print(ex_type)
    print(ex_val)
    for stack in traceback.extract_tb(ex_stack):
        print(stack)


# 捕获异常的类，异常的值，和回溯信息。

二、 

from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)  # __enter__() 方法执行的代码（yield前面的代码）
    yield f               # f 赋值给 as 后面的变量
    f.close()            # __exit__() 方法执行的代码（yield后面的代码）

with my_open("out.txt", "w") as f:
    f.write("hello!")