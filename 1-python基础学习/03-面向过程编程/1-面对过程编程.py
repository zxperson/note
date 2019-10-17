1.  字典
    字典的键必须是 不可变类型

2.  元组
    和列表类似。不同的是 元组是 不可变类型
    元组 里面 如果只有一个元素：(100,)

    想一个问题：有一个元组(4,5) 里面每一个元素，都要用一个单独的变量保存，如何做呢？
        In [6]: a,b = (4,5)

        In [7]: a
        Out[7]: 4

        In [8]: b
        Out[8]: 5

    任何序列或者可迭代对象都可以通过一个简单的赋值操作来分解为单独的变量。变量的个数要和序列的长度一致。
    这样的操作叫做 序列解包

    当我们做序列解包时，想扔掉某些值的时候，该怎么做呢？
        In [9]: a,b,_ = (4,5,6)

3.  不可变类型和可变类型

    可变类型：列表、字典
    不可变类型：字符串、元组、整型、浮点型                                                               



4.  引用
    a=100  变量a实际保存的是100的地址。
            删除变量 del a   实际上删除的是引用

    a+=100 和 a=a+100 什么情况下等效？当a为 不可变类型的时候。      可变类型：列表、字典、集合、可变字节序列
                                                                不可变类型：字符串、元组、整型、浮点型

    代码：

        def self_add(a):
            a = a+a

        test_list = [1,2]


        self_add(test_list)

        print(test_list)

        打印结果：
            [1,2]

        如果把a=a+a 换成a+=a ,结果就会变成[1,2,1,2].

        当 a 为 可变类型的 时候 += 相当于 '原地修改'


5.  global 和 nonlocal 的区别以及使用方式
    在Python2 里面 没有 nonlocal


    代码1：
        def outer():

            b = 1
         
            def inner():
                global b
                
                b += 1    # 在 inner 函数里面想要修改 outer函数 b变量的值。
                print('inner_b is %d' % b)
                
            inner()
            print('outer_b is %d' % b)
        outer()

        # 抛出 NameError: global name 'b' is not defined 

    代码2：
        def outer():

            b = 1
         
            def inner():
                
                b = b + 1    # 此时 b 变量所在的命名空间属于 local作用域
                print('inner_b is %d' % b)
                
            inner()
            print('outer_b is %d' % b)
        outer()

        # 抛出 UnboundLocalError: local variable 'b' referenced before assignment

    代码3：
        def outer():

            b = 1
         
            def inner():
                nonlocal b
                b = b + 1
                print('inner_b is %d' % b)
                
            inner()
            print('outer_b is %d' % b)
        outer()

6. 函数参数的默认值如果是一个可变类型，例如列表，那么会有什么影响呢？
    
代码：
def test(a,li=[]):
    #print id(li)
    for i in range(a):
        li.append(i)
    print li

f(2)
f(3)

打印结果：
        [0, 1]
        [0, 1, 0, 1, 2]

那么，我们把代码修改一下：
    def test(a):
        li = []
        for i in range(a):
            li.append(i):
        print li

    test(2)
    test(3)

打印结果：
        [0, 1]
        [0, 1, 2]
            

7. 常见面试题

    1).  字符串 'abcpsjdgopijgdsfjgdjfgodjrrghejoh' ，统计每一个字符出现的个数，去重，然后从小到大进行排序。
        
        代码：
            s = 'abcpsjdgopijgdsfjgdjfgodjrrghejoh'
            li = []
            for i in s:
                li.append((i,s.count(i)))

            set_str = set(li)
            print(set_str)

            print(sorted(set_str,key=lambda x:x[1]))

    2).  [{'name':'aa','age':18},{'name':'bb','age':15},{'name':'cc','age':20},{'name':'dd','age':16}],请按照 字典中的age键的值，从小到大给字典排序。

            In [1]: t_list = [{'name':'aa','age':18},{'name':'bb','age':15},{'name':'cc','age':20},{'name':'dd','age':16}]

            In [2]: sorted(t_list,key=lambda x:x['age'])   # sorted函数还有一个reverse参数，可以控制升序排序还是降序排序
            Out[2]: 
            [{'age': 15, 'name': 'bb'},
             {'age': 16, 'name': 'dd'},
             {'age': 18, 'name': 'aa'},
             {'age': 20, 'name': 'cc'}]


