一、列表的常见操作
1. append
向列表的末尾添加元素，直接修改原列表。

In [1]: test_list = ['a','b','c']

In [2]: test_list.append('d')

In [3]: test_list
Out[3]: ['a', 'b', 'c', 'd']

2. extend
在列表末尾一次性追加另一个序列中的多个值，直接修改原列表。

In [1]: test_list = ['a','b','c']

In [2]: test_list.extend(('1','2'))

In [3]: test_list
Out[3]: ['a', 'b', 'c', '1', '2']

3. insert
用于把指定的元素插入到列表里指定的位置。

In [1]: test_list = ['a','b','c']

In [2]: test_list.insert(1,'1')

In [3]: test_list
Out[3]: ['a', '1', 'b', 'c']

4. 直接通过索引修改 列表元素
In [1]: test_list = ['a','b','c']

In [2]: test_list[0] = '1'

In [3]: test_list
Out[3]: ['1', 'b', 'c']

5. index

和字符串find一样，查看某个元素在列表里的索引，如果不存在返回一个ValueError异常
In [1]: test_list = ['a','b','c']

In [2]: test_list.index('a')
Out[2]: 0

同样也可以 添加 起始位置 和 结束位置，注意，左开右闭。

6. count
查找某个元素在列表中出现的次数。

In [1]: test_list = ['a','b','c','a']

In [2]: test_list.count('a')
Out[2]: 2

7. del
删除列表中的某个元素，通过索引删除。

In [1]: test_list = ['a','b','c','a']
In [2]: del test_list[0]
In [3]: test_list
Out[3]: ['b', 'c', 'a']

8. pop
用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

In [1]: test_list = ['a','b','c','a']

In [2]: test_list.pop(0)    参数为索引
Out[2]: 'a'

In [3]: test_list
Out[3]: ['b', 'c', 'a']

9. remove
移除列表中某个值的第一个匹配项。

In [1]: test_list = ['a','b','c','a']

In [2]: test_list.remove('a')

In [3]: test_list
Out[3]: ['b', 'c', 'a']

10. sort
排序。注意：原列表会被修改。

1): 默认，升序排序。
In [1]: test_list = [1,2,3,4,5]

In [2]: test_list.sort()

In [3]: test_list
Out[3]: [1, 2, 3, 4, 5]

2):reverse参数
In [1]: test_list = [1,2,3,4,5]
In [2]: test_list.sort(reverse=True)

In [3]: test_list
Out[3]: [5, 4, 3, 2, 1]


3): key 参数
这个参数用来指定一个函数，此函数会在每个元素比较之前调用.

    In [1]: test_list = ['Hello','world','PYthon','itcast']

In [2]: test_list.sort(key=str.lower)

In [3]: test_list
Out[3]: ['Hello', 'itcast', 'PYthon', 'world']

11. reverse
将列表逆置。

In [1]: test_list = [1,2,3,4,5,6]

In [2]: test_list.reverse()

In [3]: test_list
Out[3]: [6, 5, 4, 3, 2, 1]

注意：以上所有的对列表的修改操作，都是在原列表上直接修改，列表是 可变类型。

In [4]: a = test_list.reverse()

In [5]: a is None
Out[5]: True

二、字典的操作。
首先，注意：字典的键必须是不可变类型。

1) 修改
直接通过键进行修改

In [1]: test_dict = {'a':1,'b':2}
In [2]: test_dict['a'] = 100

In [3]: test_dict
Out[3]: {'b': 2, 'a': 100}

2) 添加
直接通过键进行添加

In [1]: test_dict = {'a':1,'b':2}
In [2]: test_dict['c'] = 3
In [3]: test_dict
Out[3]: {'c': 3, 'b': 2, 'a': 1}

3) 删除
del
1) 删除字典中的某个元素

In [1]: test_dict = {'a':1,'b':2}
In [2]: del test_dict['a']

In [3]: test_dict
Out[3]: {'b': 2}

2) 删除整个字典

del test_dict

4) 清空
clear

In [1]: test_dict = {'a':1,'b':2}

In [2]: test_dict.clear()

In [3]: test_dict
Out[3]: {}

5) 检测键值对的个数

In [1]: test_dict = {'a':1,'b':2,'c':3}

In [2]: len(test_dict)
Out[2]: 3

6) keys
返回一个包含字典所有键的列表.
    注意：在python3中，返回值为一个可迭代对象，可以用list，把它转换成一个列表。

In [1]: test_dict = {'a':1,'b':2,'c':3}
In [2]: k = test_dict.keys()

In [3]: k
Out[3]: dict_keys(['c', 'a', 'b'])

In [4]: list(k)
Out[4]: ['c', 'a', 'b']

7) values
返回一个包含字典所有value的列表。
注意：在python3中，返回值为一个可迭代对象，可以用list，把它转换成一个列表。

In [1]: test_dict = {'a':1,'b':2,'c':3}

In [2]: v = test_dict.values()

In [3]: v
Out[3]: dict_values([3, 1, 2])

In [4]: list(v)
Out[4]: [3, 1, 2]

8). items
返回一个包含所有键值对元祖的列表。
注意：在python3中，返回值为一个可迭代对象，可以用list，把它转换成一个列表。

In [1]: test_dict = {'a':1,'b':2,'c':3}

In [2]: it = test_dict.items()

In [3]: it
Out[3]: dict_items([('c', 3), ('a', 1), ('b', 2)])

In [4]: list(it)
Out[4]: [('c', 3), ('a', 1), ('b', 2)]

9). has_key

检测字典是否包含某个key，返回True或者False

In [1]: test_dict = {'a':1,'b':2,'c':3}

In [2]: test_dict.has_key('a')
Out[2]: True

has_key 在 Python3中已经被删除了。那么在python3中是如何检测的呢？

官方推荐我们用 in

In [1]: test_dict = {'a':1,'b':2,'c':3}

In [2]: 'a' in test_dict
Out[2]: True

10). 字典默认值----setdefault

第一个参数：查找的键
第二个参数：键不存在时，设置的默认键值。

如果键存在，则返回这个键的值。
如果键不存在，则返回这个键，设置的默认值。然后把键值对加入到原来的字典中。

键存在：
In [1]: test_dict = {'a':1,'b':2,'c':3}

In [2]: test_dict.setdefault('a','haha')
Out[2]: 1

键不存在：
In [1]: test_dict = {'a':1,'b':2,'c':3}

In [2]: test_dict.setdefault('d','haha')     注意：如果不设置默认值，默认值会被自动设置成None.
    Out[2]: 'haha'

In [3]: test_dict
Out[3]: {'c': 3, 'a': 1, 'b': 2, 'd': 'haha'}

11.) 字典的默认值-----defaultdict

首先，需要 ： from collections import defaultdict

In [11]: d = defaultdict(list)
In [12]: d
Out[12]: defaultdict(<class 'list'>, {})

注意：d 是一个 defaultdict对象，参数必须是 可调用的或者None。可以把 d 当成一个字典用。想查看字典的结构可以 dict(d)
d 这个字典对象 有一个默认值(键的默认值)，这个默认值是[]。list 是Python中的一个内置函数。list()返回值是一个空列表。
如果参数是None，那么这个字典对象就没有默认值了，那你还不如直接去用普通的字典。。。。

例1：
In [2]: d = defaultdict(list)

In [3]: d['a']     # 当我们去访问一个不存在的 键 的时候，会自动把这个 键 添加到字典里，然后设置一个默认值[]
Out[3]: []         #  注意：只有 通过 d['a'] 或者 d.__getitem__('a') 这两种方式 访问 键，才会设置默认值。其他情况下会抛KeyError异常。
In [4]: d['a'].append(1)

In [5]: d['a'].append(2)

In [6]: dict(d)
Out[6]: {'a': [1, 2]}

例2：
In [7]: def zero():
    ...:        return 0
...:

In [8]: d = defaultdict(zero)

In [9]: d['a']
Out[9]: 0

In [10]: d['b']
Out[10]: 0

In [11]: dict(d)
Out[11]: {'b': 0, 'a': 0}

12). pop
删除指定键所对应的值，返回这个值并从字典中把它移除.

    In [1]: test_dict.pop('d')
Out[1]: 'haha'

In [2]: test_dict
Out[2]: {'c': 3, 'a': 1, 'b': 2}

13). get
和setdefault用法一样，不同的是：
当键不存在时，返回这个键，设置的默认值，并不会 把键值对加入到原来的字典中。
















    


















            







        











		







		
















