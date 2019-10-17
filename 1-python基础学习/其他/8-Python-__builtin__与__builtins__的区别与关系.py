1. 在Python中，有一个内建模块，该模块中有一些常用函数。而该模块在Python解释器启动后、且没有执行程序员所写的任何代码前，
    Python会首先加载 该内建模块到内存,然后把內建模块的命令空间导入到当前代码的global作用域中，然后我们才能直接使用內建函数。
    如果仅仅加载，那么我们在自己的代码中还是无法直接使用內建函数。加载不等于导入。

2. 在Python2.X版本中，内建模块被命名为__builtin__，而到了Python3.X版本中，却更名为builtins。

3. 如果想要向内建模块中添加一些功能，以便在任何模块中都能直接使用而不 用再进行import，这时，就要导入内建模块，在内建模块的命名空间(即__dict__字典属性)中添加该功能。
    代码：
        import __builtin__

        def test():
            print('--test--')

        __builtin__.__dict__['new_test'] = test

        test()
        new_test()

    # test 只能在该模块中使用，而new_test可以在本程序中的其它任何一个模块中使用(如果不导入)，因为hello已经放到内建模块中了。

4. __builtins__ 同时存在于python2和Python3,并且功能相同。它就是对内建模块一个引用。
    1）. 在主模块__main__中: __builtins__是对内建模块__builtin__本身的引用，即__builtins__完全等价于__builtin__，二者完全是一个东西，不分彼此.此时，__builtins__的类型是模块类型。
    2）. 在非__main__模块中：__builtins__仅是对__builtin__.__dict__的引用，而非__builtin__本身。它在任何地方都可见。此时__builtins__的类型是字典。

    例如：
    创建一个 itcast.py 文件。在文件中写入如下代码：
        #coding:utf-8
        import __builtin__
        import haha

        def test():
            print('--test--')

        __builtin__.__dict__['new_test'] = test

        test()
        new_test()
        print(type(__builtins__))

        print('---------------分割线---------------------')
        haha.func()

    然后，创建一个 haha.py 文件。在文件中写入如下代码：
        def func():
            new_test()
            print(type(__builtins__))

    执行 python itcast.py ,看打印结果。
