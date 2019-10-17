一、命名空间(namespace)

    1.  命名空间是名字和对象的映射.可以把一个namespace理解为一个字典.大部分namespace都是按Python中的字典来实现的.
        各个命名空间是独立的，没有任何关系的，所以同一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响.

        顺便提一句，我称Python 中任何一个“.”之后的命名为属性--例如，表达式z.real 中的real 是对象z 的一个属性.
        严格来讲，从模块中引用命名是引用属性：表达式modname.funcname 中， modname 是一个模块对象，funcname 是它的一个属性.
        在这种情况下，模块的属性和模块中定义的全局名称之间会有一个简单的映射:它们共享相同的名称空间.

    2. 那么哪些可以是一个namespace呢?
       Python的 built-in names（包括内置函数，内置常量，内置类型）;
       一个模块的global names（这个模块定义的函数，类，变量）;
       一个函数的所有local names ;
       从某种意义上说，对象的属性集也构成了一个名称空间;

    3. 命名空间都是有创建时间和生存期的.
        对于Python built-in names组成的命名空间，它在Python解释器启动的时候被创建，在解释器退出的时候才被删除;
        对于一个Python模块的global namespace，它在这个module被import的时候创建，在解释器退出的时候退出;
        对于一个函数的local namespace，它在函数每次被调用的时候创建，函数返回或者或引发未在函数中处理的异常的时候被删除;

    4. 查看命名空间：
        1.  查看全局命名空间： globals()
        2.  查看本地命名空间： locals()
        3.  查看內建的命名空间：以Python3为例：import builtins  builtins.__dict__


二、作用域(scope)
    1.  作用域是Python程序（文本）的某一段或某些段，在这些地方，某个命名空间中的名字可以被直接访问。这个作用域就是这个命名空间的作用域。

        直接访问：对一个变量名的引用会在所有namespace中查找该变量，而不是通过属性访问.
        属性访问：所有名字后加 . 的都认为是属性访问.

        如 module_name.func_name ，需要指定 func_name 的名空间，属于属性访问。
        而 abs(-1) ， abs 属于直接访问。

        作用域 尽管范围是静态确定的，但它们是动态使用的。在执行期间的任何时间，至少有三个嵌套的作用域，其命名空间可以直接访问。

    2. 四个作用域分别是：
        Local：包含局部变量。比如一个函数/方法内部。
        Enclosing：包含了非局部(non-local)也非全局(non-global)的变量.比如两个嵌套函数，内层函数可能搜索外层函数的namespace，但该namespace对内层函数而言既非局部也非全局。
        Global：当前脚本的最外层。比如当前模块的全局变量。
        Built-in：Python __builtin__ 模块(python3中改为builtins模块).包含了内建的变量/关键字/函数等.

    3. 著名的”LEGB-rule”，即scope的搜索顺序
        Local -> Enclosing -> Global -> Built-in

        当有一个变量在 local 域中找不到时，Python会找上一层的作用域，即 enclosing 域（该域不一定存在）。
        enclosing 域还找不到的时候，再往上一层，搜索模块内的 global 域
        最后，会在 built-in 域中搜索。对于最终没有搜索到时，Python会抛出一个 NameError 异常。

    4. global 和 nonlocal 的用法
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