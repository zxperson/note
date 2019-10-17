1. 动态添加 实例属性和类属性
    obj.name = "xx"
    cls.color = "白色"

    直接添加就行了。。

2. 动态的添加一个 实例方法

代码：
import types

class Person(object):
    pass

def run(self):
    print("---run----")

Person.run = types.MethodType(run, Person)  # 给Person类动态的添加一个实例方法

a = Person()
a.run()

3. 动态的添加一个 类方法或者静态方法

代码：
import types

class Person(object):
    pass

@classmethod
def run(cls):
    print("---run----")

Person.run = run  # 给Person类动态的添加一个 类方法

a = Person()
a.run()


