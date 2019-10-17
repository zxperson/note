    1.  sys.path 
        当使用 import xxx 导入模块的时候，系统会去哪里找你指定的模块呢？
        sys.path 是一个列表，当使用 import xxx 导入模块的时候，系统会按照 这个列表里的 路径 去导入。
        ['',
         '/usr/bin',
         '/usr/lib/python35.zip',
         '/usr/lib/python3.5',
         '/usr/lib/python3.5/plat-x86_64-linux-gnu',
         '/usr/lib/python3.5/lib-dynload',
         '/usr/local/lib/python3.5/dist-packages',
         '/usr/lib/python3/dist-packages',
         '/usr/lib/python3/dist-packages/IPython/extensions',
         '/home/python/.ipython']
         这个列表的第一个元素，代表 当前路径。所以 import 的时候， 会优先 在当前路径搜索模块。

         当你在/home下写了一个模块，但是在其他的路径里无法导入的时候，你可以修改sys.path这个列表。

    2. == 和 is
        In [1]: a = [1,2,3]

        In [2]: b = [1,2,3]

        In [3]: a == b
        Out[3]: True

        In [4]: a is b
        Out[4]: False

    ==是判断值是否相等，is是判断是否指向同一个对象。is相当于验证DNA

    3. python3里 copy.copy和copy.deepcopy     
        In [2]: a = [1,2,3,4]

        In [3]: b = copy.copy(a)

        In [4]: id(a)
        Out[4]: 140307059565064

        In [5]: id(b)
        Out[5]: 140307043952520

        同样是 a 这个 列表，如果使用copy.deepcopy,发现，结果是一样的。这样没办法比较深拷贝和浅拷贝的区别。
        那么，我们换一种方式：

        In [7]: a = {"name":"laowang"}

        In [8]: b = [1,2,3,a,4,5,6]

        In [9]: c = copy.copy(b)

        In [10]: id(b)
        Out[10]: 140307059565064

        In [11]: id(c)
        Out[11]: 140307043953160

        In [12]: a["age"] = 18     #关键来了

        In [13]: b
        Out[13]: [1, 2, 3, {'age': 18, 'name': 'laowang'}, 4, 5, 6]

        In [14]: c
        Out[14]: [1, 2, 3, {'age': 18, 'name': 'laowang'}, 4, 5, 6]

        可以看到，copy.copy()这个浅拷贝，没有拷贝列表里的字典。

        ok，下面我们来看看copy.deepcopy():

        In [2]: a = {"name":"laowang"}

        In [3]: b = [1,2,3,a,4,5,6]

        In [4]: c = copy.deepcopy(b)

        In [5]: id(b)
        Out[5]: 140686388583048

        In [6]: id(c)
        Out[6]: 140686373051144

        In [7]: a["age"] = 18         #关键来了

        In [8]: b
        Out[8]: [1, 2, 3, {'name': 'laowang', 'age': 18}, 4, 5, 6]

        In [9]: c
        Out[9]: [1, 2, 3, {'name': 'laowang'}, 4, 5, 6]

        ok，可以发现，深拷贝，列表里面的字典也会拷贝。

        总结：浅拷贝，类似敷衍拷贝，偷工减料式拷贝。深拷贝才会完整的拷贝。

        继续看：

        In [1]: import copy

        In [2]: a = {"name":"laowang"}

        In [3]: b = (1,2,3,a,4,5,6)

        In [4]: c = copy.copy(b)

        In [5]: id(b)
        Out[5]: 139907563109704

        In [6]: id(c)
        Out[6]: 139907563109704

        总结： 
              1.如果 被拷贝的数据里没有嵌套其他的对象  [1,2,3,4]
              浅拷贝：拷贝的是可变类型，那么重新拷贝一份。
              深拷贝：拷贝的是可变类型，那么重新拷贝一份。

              2.如果 被拷贝的数据，嵌套了其他的对象呢？   [1,2,3,a,4,5,6]
              浅拷贝：拷贝的是可变类型，那么，会重新拷贝一份，但是 数据里面的其他对象， 仅仅拷贝引用。
              深拷贝：拷贝的是可变类型，那么，会重新拷贝一份，但是 数据里面的其他对象， 也会重新拷贝一份。

              3.如果 被拷贝的数据是 不可变的类型。
				浅拷贝：直接拷贝 引用。
				深拷贝：重新拷贝一份，元祖里面的嵌套的元素，也会完全拷贝一份。