1. assert 语句

断言

基本格式：
assert 表达式 [, 参数]

表达式如果返回True,程序继续运行。
表达式如果返回False,抛出AssertionError异常。

demo：
    In [1]: a = 100

    In [2]: assert type(a)==int,'a必须是一个整数'

    In [3]: assert type(a)==str,'a必须是一个整数'
    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)
    <ipython-input-3-7e63df9a3dcd> in <module>()
    ----> 1 assert type(a)==str,'a必须是一个整数'

    AssertionError: a必须是一个整数


2. exec 语句

python3 中 exec 是一个函数。

2.1 exec函数和eval函数类似，也是执行动态语句，只不过eval函数只用于执行表达式求值，而exec函数主要用于执行语句块。

    In [2]: eval('a=1+2')
      File "<string>", line 1
        a=1+2
         ^
    SyntaxError: invalid syntax


    In [3]: exec('a=1+2')

    In [4]: a
    Out[4]: 3

2.2 第一个参数为语句字符串，globals参数和locals参数为可选参数，如果提供，globals参数必需是字典，locals参数为mapping对象。

2.3 globals参数用来指定代码执行时可以使用的全局变量以及收集代码执行后的全局变量
    
    In [6]: g = {'num':2}

    In [7]: exec('num2 = num + 2',g)  # 如果指定了 g 参数。那么语句在执行完成后,num2 这个变量会被保存到g这个字典中。
                                      # 直接在ipython中输入 num2 ，无法查看。        
    In [8]: g['num']
    Out[8]: 2

    In [9]: g['num2']
    Out[9]: 4

2.4  locals参数用来指定代码执行时可以使用的局部变量以及收集代码执行后的局部变量

    In [2]: g = {'num':2}

    In [3]: l = {'num2':3}

    In [4]: exec('''
       ...: num2 = 13
       ...: num3 = num + num2
       ...: ''',g,l)

    In [5]: l['num2']   #l中num2值已经改变
    Out[5]: 13

2.5 为了保证代码成功运行，globals参数字典不包含 __builtins__ 这个 key 时，Python会自动添加一个key为 __builtins__ ，value为builtins模块的引用。
    如果确实要限制代码不使用builtins模块，需要在global添加一个key为__builtins__，value为{}的项即可（很少有人这么干吧）

    In [1]: g = {}

    In [2]: exec('a = abs(-1)',g)

    In [3]: g['a']
    Out[3]: 1




    In [4]: g = {'__builtins__':{}}

    In [5]: exec('a = abs(-1)',g)
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-5-fc720abe5005> in <module>()
    ----> 1 exec('a = abs(-1)',g)

    <string> in <module>()

    NameError: name 'abs' is not defined

2.6 当globals参数不提供时，Python默认使用globals()函数返回的字典去调用。当locals参数不提供时，默认使用globals参数去调用
    In [2]: num = 1

    In [3]: exec('num2 = num + 1') 

    In [4]: globals()
    Out[4]: 
    {'_oh': {},
     'Out': {},
     '_iii': 'clear',
     '__': '',
     '__name__': '__main__',
     '_i2': 'num = 1',
     '_i4': 'globals()',
     '_': '',
     '_dh': ['/home/python/smb_share/flask_study/demo_login'],
     '_ih': ['',
      "get_ipython().magic('clear ')",
      'num = 1',
      "exec('num2 = num + 1')",
      'globals()'],
     '__builtins__': <module 'builtins' (built-in)>,
     'quit': <IPython.core.autocall.ExitAutocall at 0x7f80b93ed6a0>,
     'num2': 2,
     '_ii': 'num = 1',
     '_sh': <module 'IPython.core.shadowns' from '/usr/lib/python3/dist-packages/IPython/core/shadowns.py'>,
     '_i': "exec('num2 = num + 1')",
     '_exit_code': 0,
     '_i3': "exec('num2 = num + 1')",
     '__builtin__': <module 'builtins' (built-in)>,
     '_i1': 'clear',
     'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x7f80bbb50208>>,
     '___': '',
     'exit': <IPython.core.autocall.ExitAutocall at 0x7f80b93ed6a0>,
     'num': 1,
     '__spec__': None,
     'In': ['',
      "get_ipython().magic('clear ')",
      'num = 1',
      "exec('num2 = num + 1')",
      'globals()'],
     '__package__': None,
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__loader__': None}

     执行完之后， num2这个变量，被添加到了 全局的命令空间中。

    >>> l = locals()
    >>> l
    {'__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__name__': '__main__', '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__doc__': None, 'l': {...}, 'num2': 2, 'num': 1}
    >>> 
    >>> exec('num3 = num + 1',{},l)#指定了globals参数，globals中无num变量，指定了locals变量，locals变量含有num变量 执行成功
    >>> l
    {'__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__name__': '__main__', '__spec__': None, 'num3': 2, '__builtins__': <module 'builtins' (built-in)>, '__doc__': None, 'l': {...}, 'num2': 2, 'num': 1}
    >>> 





True if a==0 else False  , 如果 a==0 就返回 True, 否则返回 False 