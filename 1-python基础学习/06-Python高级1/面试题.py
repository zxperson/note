1. 深拷贝和浅拷贝
    1）. 观察如下的代码，写出打印结果。
        import copy
        a = [1,2,3,4,['a','b']]
        b = a
        c = copy.copy(a)
        d = copy.deepcopy(a)

        a.append(5)
        a[4].append('c')

        print('a = {}'.format(a))
        print('b = {}'.format(b))
        print('c = {}'.format(c))
        print('d = {}'.format(d))

        答案：
            a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
            b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
            c = [1, 2, 3, 4, ['a', 'b', 'c']]
            d = [1, 2, 3, 4, ['a', 'b']]


2. 装饰器 *args **kwargs
    2）.  有一个 字典{'a':1,'b':2,'c':3},现在有一个这个需求：
        向字典中添加新的键值对，如果字典中的键，已经存在，则取消添加，打印提示：键已经存在。
        如果键不存在，则添加到字典中。（请使用装饰器来实现,顺便复习下*args和**kwargs的用法）.

        答案1：
            a = {'a':1,'b':2,'c':3}

            def select(func):
                def inner(data,key,value):
                    if key in data:
                        print('已经存在')
                    else:
                        func(data,key,value)
                    
                return inner

            @select   #append=select(append)
            def append(data,key,value):
                data[key]=value
                print(data)

            if __name__ == "__main__":
                append(a,'hehe',199)

        答案2：
            a = {'a':1,'b':2,'c':3}

            def select(func):
                def inner(*args,**kwargs):
                    if len(args) == 0:
                        if kwargs['key'] in kwargs['data']:
                            print('键存在了')
                        else:
                            func(**kwargs)
                    else:
                        if args[1] in args[0].keys():
                            print('键存在了')
                        else:
                            func(*args)
                return inner
              
            @select   #append=select(append)
            def append(data,key,value):
                data[key]=value
                print(data)
              
            if __name__ == "__main__":
                #append(a,'hehe',199)
                append(*(a,'hehe',199))

                append(data=a,key='a',value=100)
                #append(**{'data':a,'key':'a','value':100})

3. python2中 range 和 xrange 的区别

    range 直接返回 一个列表。
    xrange 直接返回一个 可迭代对象，可以通过list把这个可迭代对象转换成列表。

    在 python3 中 已经没有 xrange了, 只有 range。但是 python2和python3中的range不同。
    python3中的 range返回一个 可迭代对象，可以通过list把这个可迭代对象转换成列表。

4. 列表推导式和字典推导式
    1）.列表推导式
        b = [(i,j) for i in range(1,3) for j in range(4,6)]

        等效于:
        b = []

        for i in range(1,3):
            for j in range(4,6):
                b.append((i,j))

    2）.字典推导式
    test_dict = {"a":10,"b":11}
    ret = { k:v for k,v in test_dict.items() }
    print(ret)

5. 正确使用闭包，就要确保引用的局部变量在函数返回后不能变，改写以下程序，让它能正确返回
计算 1*1 2*2 3*3 的函数。
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i

        fs.append(f)

    return fs

f1, f2, f3 = count()
print(id(f1),id(f2),id(f3))
print(f1(),f2(),f3())

改写后1：
def count():

    for i in range(1,4):
        def f():
            return i*i

        yield f

for f in count():
    print(f())

改写后2：
def count():
    fs = []

    def inner():
        for i in range(1,4):
            def f(num=i):
                return num*num
            fs.append(f)
        return fs


    return inner

f1, f2, f3 = count()()
print(id(f1))
print(id(f2))

print(f1(),f2(),f3())


6. 列表的append方法

append 方法添加的 有时候是 对象的引用。

代码：

info = ["a","b","c"]
d = {}
print("d 的id是：%d" % id(d))

L = []
for i in range(3):
    d["name"] = info[i]
    L.append(d)

print("L 列表的值：", L)

print([id(item) for item in L])

# 执行结果：
# d 的id是：140018245522344
# L 列表的值： [{'name': 'c'}, {'name': 'c'}, {'name': 'c'}]
# [140018245522344, 140018245522344, 140018245522344]

# 如何 达到想要的效果呢？