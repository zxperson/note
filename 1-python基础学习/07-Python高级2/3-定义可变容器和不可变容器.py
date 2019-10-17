1. 不可变容器（序列）：
    为了制作一个不可变容器，你只需要定义 __len__ 和 __getitem__。

2.  可变容器（序列）：
    为了制作一个可变容器，你需要定义 __len__ 、__getitem__ 、__setitem__ 、__delitem__。


例子：
    class TestList(object):

        def __init__(self, value=None):
            if value is None:
                self.value = []

            else:
                self.value = value

        def __len__(self):
            return len(self.value)

        def __getitem__(self, key):
            return self.value[key]

        def __setitem__(self, key, value):
            self.value[key] = value

        def __delitem__(self):
            del self.value[key]

        def __iter__(self):
            return iter(self.value)

        def __reversed__(self):
            return reversed(self.value)

        def append(self, value):
            # 添加一个元素(末尾添加)
            self.value.append(value)

        def head(self):
            # 获取 第一个元素
            return self.value[0]

        def tail(self):
            # 获取除第一个元素外的所有元素
            return self.value[1:]


    t = TestList([1,2,3,4])  # t是一个 可变容器
    t[0] = 100
    print(list(t))

