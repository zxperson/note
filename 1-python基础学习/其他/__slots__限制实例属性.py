
代码1:
class Person(object):
    __slots__ = ("name", "age")   # 如果定义了这个属性，那么Person类 创建的实例对象，只能添加name和age两个实例属性。我们的代码会报错。

    def __init__(self, addr):
        self.addr = addr

a = Person("中国")
print(a.addr)

代码2：
class Person(object):
    __slots__ = ("name", "age")

    def __init__(self, addr):
        self.addr = addr

class Hehe(Person):
    pass

t = Hehe("中国")
print(t.addr)    # 注意：子类 不受父类的 __slots__ 属性的影响。
