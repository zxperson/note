一。介绍

抽象基类（abstract base class,ABC）：抽象基类就是类里定义了纯虚成员函数的类。纯虚函数只提供了接口，并没有具体实现。
抽象基类不能被实例化(不能创建对象)，通常是作为基类供子类继承，子类中重写虚函数，实现具体的接口。

二。实现方式

1. 使用 assert 语句

代码：
class BaseClass(object):
    def action(self):
        assert False, 'subclasses of BaseClass must provide an action() method'

2. 使用 NotImplementedError 异常

代码：
class BaseClass(object):
    def action(self):
        raise NotImplementedError('subclasses of BaseClass must provide an action() method')

3. 使用 abc 模块

代码：
from abc import ABCMeta, abstractmethod

class BaseClass(metaclass=ABCMeta):
    @abstractmethod
    def action(self):
        pass

# 三种 方式区别： 前两种 抽象基类 都可以被实例化。使用abc模块创建的抽象基类，不能被实例化。
# 通常 推荐使用 abc模块

三。 使用方式

1. 子类 直接继承于 抽象基类

代码：
from abc import ABCMeta, abstractmethod

class BaseClass(metaclass=ABCMeta):
    @abstractmethod
    def action(self):
        pass

class Test(BaseClass):
    def action(self):
        print('---test---')

if __name__ == "__main__":
    t = Test()
    t.action()


2. 虚拟子类

将 虚拟子类 注册到 抽象基类 中。

代码：
from abc import ABCMeta, abstractmethod

class BaseClass(metaclass=ABCMeta):
    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def action2(self):
        pass

class Test(object):
    def action(self):
        print('---test---')

BaseClass.register(Test)

if __name__ == "__main__":
    t = Test()
    t.action()
    print(isinstance(t, BaseClass))      # 返回True
    print(issubclass(Test, BaseClass))   # 返回True
    print(Test.mro())    # 虚拟子类，不会继承 抽象基类的任何属性和方法。

    # 经注册后的虚拟子类可以被issubclass和isinstance等函数识别。
    # 但是注册的虚拟子类不会从抽象基类中继承任何方法或属性。具体可通过类属性__mro__查看类的真实继承关系。