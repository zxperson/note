一、random模块

    1. random.random()
        生成一个 0-1 之间的 随机浮点数。
            In [24]: random.random()
            Out[24]: 0.9772431306673274

    2. random.uniform(a,b)
        返回a,b之间的随机浮点数，注意，a可以比b大。
            In [29]: random.uniform(133,22)
            Out[29]: 64.24902478193212

    3. random.randint(a,b)
        返回a,b之间的随机整数。参数必须是整数，a一定小于b
            In [32]: random.randint(1,333)
            Out[32]: 174

    4. random.choice()
        从序列中随机获取一个元素。
            In [38]: random.choice([1,2,3,4,5])
            Out[38]: 4
   
    5. random.sample()
        从指定的序列中随机获取n个元素，组成一个新的序列，不会修改原来的序列。
            In [34]: random.sample([1,2,3,4,5,6,7],2)
            Out[34]: [4, 2]

    6. random.shuffle()
        把列表中的元素，顺序打乱，会修改原来的列表
        In [44]: a = [1,2,3,4,5,6]

        In [45]: random.shuffle(a)

        In [46]: a
        Out[46]: [4, 2, 5, 1, 6, 3]

二、sys模块
    首先，os模块主要是负责程序和操作系统的交互，sys模块主要负责程序和python解释器的交互

    1.sys.argv
        代码：
            import os
            import sys
   
            print(sys.argv)
            os.system(sys.argv[1])

    2. sys.exit()
        官方的解释：https://docs.python.org/3.5/library/sys.html

        代码1：
            import sys
   
            test_list = [1,2,3,4,5,6,7,8,9]
            for temp in test_list:
                print(temp)
                if temp > 5:
                    sys.exit(0)
                    #sys.exit('你的值太大了')    #注意这里输出的是stderr里内容。

        如果不加退出码，默认是正常退出。

        代码2：
            import sys
   
            def exit_func(value):
                '''程序结束前的清理工作'''
                print(value)
                sys.exit()
  
            print("hello")
  
            try:
                sys.exit(1)
     
            except SystemExit as err:
                print(err)
                print('----产生异常------')
                exit_func(err)
      
      
            print("ok")

    3.sys.path
        返回模块的搜索路径
            In [2]: sys.path
            Out[2]: 
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

        sys.path.append(path)    #自己添加一个路径

    4.sys.platform 
        返回操作系统平台名称
            In [4]: sys.platform
            Out[4]: 'linux'

    5.sys.modules
        这是一个字典，该字典是python启动后就加载在内存中。每当程序员导入新的模块，
        sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，
        从而加快了程序运行的速度。

        sys.modules.keys() 返回了一个列表，可以查看python在启动的时候默认加载了哪些模块。

        问题来了：那既然，Python在启动的时候已经加载了os模块了(sys.modules 字典里已经包含了os)，那么为什么我们还是不能直接使用呢？需要 import os 导入才可以？
                一个模块 加载与否 和 可见与否 并不是同一个概念。python虽然在启动的时候加载了一些模块到内存里，但是并不是可见的，需要import 才能变成可见的。 




    
    










    
 
    


    
