
1. 一个 小案例：重写类的特殊方法。
    下面的例子，重写了类A的 __getattribute__ 魔法方法。


#coding:utf-8

def log_getattribute(cls):

    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print("getting:", name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls

@log_getattribute   # A = log_getattribute(A)
class A(object):

    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

a = A(42)    # A 此时 还是指向了 A 引用没有发生改变。注意看 装饰器的返回值，没有返回 内层函数的地址,而是返回了类本身。
a.x
print(a.x)    #打印 42
a.spam()

