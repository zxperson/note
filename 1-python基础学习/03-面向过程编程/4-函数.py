一、函数

1.匿名函数
    定义方式：lambda a,b:a+b
    调用方式：test = lambda a,b:a+b
              a = test(1,2)    注意要去接受返回值

    匿名函数当做实参：
        def test(a,b,func):
            re = func(a,b)
            return re

        num = test(1,2,lambda a,b:a+b)

    匿名函数应用：
        In [1]: t_list = [{'name':'aa','age':18},{'name':'bb','age':15},{'name':'cc','age':20},{'name':'dd','age':16}]

        In [2]: sorted(t_list,key=lambda x:x['age'])   # sorted函数还有一个reverse参数，可以控制升序排序还是降序排序
        Out[2]: 
        [{'age': 15, 'name': 'bb'},
         {'age': 16, 'name': 'dd'},
         {'age': 18, 'name': 'aa'},
         {'age': 20, 'name': 'cc'}]


2. 函数的定义
        def func(a,b,c=100,*args,**kwargs):
            print(a)
            print(b)
            print(c)
            print(args)
            print(kwargs)
   
        func(1,2,3,4,5,6,7,8,name='xiao',age=18)


3. 在函数调用的时候，关键字参数一定要在位置参数后面。
        def func(a,b):
            print(a)
            print(b)
   
        func(a=100,2)

        上面的代码会报错。

4.函数参数的默认值如果是一个可变类型，例如列表，那么会有什么影响呢？
    看代码：
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

    通过上面我们可以看到，输出的结果不同。python函数的参数的默认值，只在函数定义的时候做初始化一次。
    我们修改后的代码中，li并不是一个参数，只是函数里的一个变量，每次调用这个函数的时候，li=[]都会被执行。

    python函数 要前面定义，后面调用，程序是从上往下逐条执行的。

5. 全局变量和局部变量名字相同
    a = 100

    def test():
        a = 200
        print('a=%d'%a)

    def test2():
        print('a=%d'%a)


    test()
    test2()

    打印结果:
        a=200
        a=100

    函数里如果仅仅需要访问全局变量，那么是不需要加 global 的 建议全局变量和局部变量的名字不要相同

    全局变量是 列表 字典 的时候，在函数里可以直接使用，不需要加 global 但是,建议大家 要加上,如果你加上了,其他开发人员
    可以很直观看到你修改了 全局变量

6. *args和**kwargs

    1).  *args
        def sum(a,b,*args):
            print(a)
            print(b)
            print(args)
    
        sum(1,2,3,4,5)
        sum(1,2,3)
        sum(1,2)

        1传给a，2传给了b，剩下的 3,4,5 组成了一个 元祖 传给了args。s

    2). **kwargs

        def sum(a,b,*args,**kwargs):
            print(a)
            print(b)
            print(args)
            print(kwargs)
     
        sum(1,2,3,4,5,name='xiao',age=19)

    3). 反转
        
        def sum(a,b,c):
            print(a)
            print(b)
            print(c)
   
        test_su = (1,2,3)
   
        sum(*test_su)

        反转就是类似解包。

        def sum(a,b,c):
            print(a)
            print(b)
            print(c)
   
        test_su = {'a':1,'b':2,'c':3}
   
        sum(**test_su)

        注意：
            代码；
                def test1(*args,**kwargs):
                    print(args)
                    print(kwargs)

                test1(*(1,2,3),**{'m':1,'a':2})



# 汉诺塔思想笔记
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1


def move(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
    else:
        move(n - 1, a, c, b)  # 子目标1
        move(1, a, b, c)  # 子目标2
        move(n - 1, b, a, c)  # 子目标3


n = input("enter the number:")
move(int(n), "A", "B", "C")
