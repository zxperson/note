官方文档：http://python.usyiyi.cn/translate/python_352/library/functions.html
1. abs(x)
    返回一个数的绝对值。参数可以是整数或者浮点数。

    In [6]: abs(-100)
    Out[6]: 100

2. all(iterable)
    如果iterable中所有的元素都为True，或iterable为空（empty），返回True。否则返回False

    In [7]: a = [1,2,3,4]

    In [8]: all(a)
    Out[8]: True


    In [9]: a = [1,2,3,False]

    In [10]: all(a)
    Out[10]: False

    补充下：False 和 True 是bool类 创建出来的对象。bool 这个类 只能创建 False 和 True 这两个对象。

3. any(iterable)
    如果iterable里任何一个元素为True，返回 True。如果iterable为空（empty）,返回 False. 

    n [14]: a = [0,-1,True]

    In [15]: any(a)
    Out[15]: True

4. bool([x])
    参考官方文档

5. id(object)
    在cpython里，返回对象在内存的地址

6. len(s)
    返回对象的长度(元素个数)

7. range
    参考课件

8. map
    代码：
        def t1(x,y):
            return x+y

        ret = map(t1,[1,2,3,4],[100,200,300,400])
        print(ret)   #结果是：[101, 202, 303, 404]


        def t2(x,y):
            return (x,y)
            
        ret2 = map(t2,[1,2,3,4],['a','b','c','d'])
        print(ret2)  #结果是：[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


        ret3 = map(lambda x: x*x,[1,2,3,4])
        print(ret3)  #结果是：[1, 4, 9, 16]

        #map函数可以合并两个列表，根据你自己定义的函数。
        #注意:在python3中，map函数返回的是map类的实例对象，所以需要用list函数转换成列表

9. filter
    过滤不满足条件的元素

    代码：
        ret = filter(lambda x:x%2,[1,2,3,4,5,6])
        print(ret)

        #python3中返回值是一个迭代器。

        #打印结果是[1,3,5]
        #1%2=1,True，把1添加到结果列表中
        #2%2=0,False,不添加。
        #以此类推。。。。。。。

        # 上面的代码 去掉列表中 能被2整除的数字，那么如果想去掉不能被2整除的数字呢？

10. reduce
    实现累积

    代码：
        ret = reduce(lambda x,y:x+y,[1,2,3,4,5])
        print(ret)

        ret1 = reduce(lambda x,y:x+y,[1,2,3,4,5],100)
        print(ret1)

        ret2 = reduce(lambda x,y:x+y,['a','b','c'])
        print(ret2)

        ret3 = reduce(lambda x,y:x+str(y),['a','b','c',100])
        print(ret3)

        #ret:首先把1给x，把2给y，相加
        #然后把3给y，把之前相加的结果给x，再一次相加，以此类推，实现累加。

        #ret2中x的起始值为100,所以y的第一个值是1，后面和ret一样。x默认是列表的第一个值

        #python3中需要导入functools模块才可以用reduces函数

11. sorted
    排序

    测试：
        In [1]: t_list = [{'name':'aa','age':18},{'name':'bb','age':15},{'name':'cc','age':20},{'name':'dd','age':16}]

        In [2]: sorted(t_list,key=lambda x:x['age'])   # sorted函数还有一个reverse参数，可以控制升序排序还是降序排序
        Out[2]: 
        [{'age': 15, 'name': 'bb'},
         {'age': 16, 'name': 'dd'},
         {'age': 18, 'name': 'aa'},
         {'age': 20, 'name': 'cc'}]

12. zip
    返回值是一个迭代器

    测试：
        In [1]: x = [1,2,3]
        In [2]: y = [4,5,6]

        In [11]: list(zip(x,y))
        Out[11]: [(1, 4), (2, 5), (3, 6)]

    测试2：
        In [3]: x2, y2 = zip(*zip(x,y))

        In [4]: x2
        Out[4]: (1, 2, 3)

        In [5]: y2
        Out[5]: (4, 5, 6)

    测试3:
        In [6]: x2, y2 = zip(*[(1, 4), (2, 5), (3, 6)])

        In [7]: x2
        Out[7]: (1, 2, 3)

        In [8]: x2, y2 = zip(*((1, 4), (2, 5), (3, 6)))

        In [9]: x2
        Out[9]: (1, 2, 3)
		
	测试4：
		In [5]: x2,y2 = zip((1,4),(2,5),(3,6))

		In [6]: x2
		Out[6]: (1, 2, 3)

		In [7]: y2
		Out[7]: (4, 5, 6)

13. enumerate
    
    代码：
        #同时遍历索引和值
        list1 = ["这", "是", "一个", "测试"]

        for index, item in enumerate(list1):
            print(index, item)


        #enumerate还可以接收第二个参数，用于指定索引起始值，如：
        #for index, item in enumerate(list1, 1):
        #    print index, item
        #>>>
        #1 这 
        #2 是
        #3 一个
        #4 测试


14. list

    把 对象 转换成 列表。参数可以是一个可迭代对象，也可以是一个迭代器。

    代码：
        class test(object):
            def __init__(self, b):
                self.a = 0
                self.b = b

            def __iter__(self):
                print('test--1')
                return self

            def __next__(self):
                print('--test--2')
                if self.a < self.b:
                    i = self.a
                    self.a += 1
                    return i
                else:
                    raise StopIteration()

        it = test(10)
        print(list(it))

        # list(it), 首先调用 it对象的 __iter__ 方法，获取一个迭代器，然后调用迭代器的 __next__方法，生成所有的值，保存到列表当中，返回。

15. isinstance(object, classinfo)

    判断  object 是否是 classinfo 的一个实例对象。
    classinfo 可以是 一个类，也可以是 一个元组，元组中是多个类。


16. hasattr(obj,name)

    判断 属性 是否存在 

    代码：
    class A(object):
    def __init__(self, age):
        self.age = age

    a = A(18)
    print(hasattr(a,"age"))  # 判断 "age" 是否是 a对象的一个属性

17. getattr(obj,name,[,default])
    
    获取属性的值    

    代码：
    class A(object):
        def __init__(self, age):
            self.age = age

    a = A(18)
    print(getattr(a,"age"))        # 打印 18
    print(getattr(a,"name","xx"))  # 打印 xx
    print(getattr(a,"name"))       # 抛出 AttributeError 异常

18. setattr(obj,name,value)

    设置对象属性的值

    setattr(x,"foobar",123) 相当于 x.foobar = 123

19. slice(start, stop, step)
    
    返回一个切片对象。

    代码：

    t = ["a","b","c","d"]
    s = slice(1,3)
    print(t[1:3])    #  输出 ["b","c"]
    print(t[s])      #  输出 ["b","c"]

20. ord(c)

    返回 字符 对应的 unicode编码(十进制)

    代码：
    In [2]: ord('a')
    Out[2]: 97

21. chr(i)

    返回 unicode编码(十进制) 对应的字符

    In [4]: chr(97)
    Out[4]: 'a'

    print(chr(0x1F602))   # 打印 emoji表情😂
                          # Emoji表情代码大全：http://www.luxuqing.com/emoji/index.html


22. int(x,base=10)

    base 参数代表进制。如果手动指定了这个参数，x必须是 str、bytes、bytearray 类型的数据。

    例子1：
    In [24]: a = int()

    In [25]: a
    Out[25]: 0

    例子2：
    In [23]: int("0x12", base=16)    # 把16进制的12 转换成十进制整数，然后返回。
    Out[23]: 18     


    In [28]: int("0b100", base=2)    # 把 二进制100 转换成十进制整数，然后返回。
    Out[28]: 4




