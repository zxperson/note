一. functools.partial

原理：

def partial(func, *args, **kwargs):

    def new_func(*f_args, **f_kwargs):
        new_kwargs = kwargs.copy()
        new_kwargs.update(f_kwargs)
        return func(*(args + f_args), **new_kwargs)

    return new_func


def add(a,b):
    return a + b

p = partial(add,3)    

print(p(5))    # 输出 8
print(p(6))    # 输出 9


小例子：
from functools import partial

def add(a,b):
    return a + b

p = partial(add,3)     #  把 参数 a 的值 固定为3.  冻结a参数。

print(p(5))  #输出 8
print(p(6))  #输出 9



二.  functools.update_wrapper 和 functools.wraps

1. functools.update_wrapper

先看代码：

def outer(func):

    def inner(*args, **kwargs):
        """ inner 函数的文档"""

        print("-----inner------")
        return func(*args, **kwargs)

    return inner


@outer
def hello():
    """ hello 函数文档"""

    print("hello")


if __name__ == "__main__":
    hello()
    print("hello函数的名字：%s" % hello.__name__)
    print("hello函数的帮助文档:%s " % hello.__doc__)

    #  hello函数添加了一个装饰器之后，想要访问hello函数的一些魔法属性（__name__,__doc__等等），实际打印出来的却是inner函数的魔法属性。
    #  这是使用了 装饰器 之后的一些副作用。。
    #  如何消除这些副作用呢？


消除副作用：

from functools import update_wrapper

def outer(func):

    def inner(*args, **kwargs):
        """ inner 函数的文档"""

        print("-----inner------")
        return func(*args, **kwargs)

    return update_wrapper(inner,func)     # 注意 update_wrapper(inner, func) 的返回值为inner.  把 被装饰函数的 属性，赋给 装饰函数。
                                          # inner 是装饰函数(wrapper)，func是被装饰函数(wrappered)。

@outer    # hello = outer(hello)
def hello():
    """ hello 函数文档"""

    print("hello")


if __name__ == "__main__":
    hello()   #  hello 实际指向了 inner 函数
    print("hello函数的名字：%s" % hello.__name__)     # 这里 实际访问的是 inner 函数的 __name__ 和 __doc__ 属性。
    print("hello函数的帮助文档:%s " % hello.__doc__)


2. functools.wraps

# 和 functools.update_wrapper 功能是一样的。。只是书写方式不一样

from functools import wraps

def outer(fun):

    @wraps(fun)
    def inner(*args, **kwargs):
        """ inner 函数的文档"""

        print("-----inner------")
        return fun(*args, **kwargs)

    return inner 


@outer
def hello():
    """ hello 函数文档"""

    print("hello")


if __name__ == "__main__":
    hello()
    print("hello函数的名字：%s" % hello.__name__)
    print("hello函数的帮助文档:%s " % hello.__doc__)

