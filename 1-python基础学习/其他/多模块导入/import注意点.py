from xx import ab    # 这种导入方式，不能修改源文件中(xx.py)ab的值。 ab相当于当前模块的一个全局变量。
import xx   # 这种导入方式，可以修改源文件中的ab的值。例如：在当前模块中执行：xx.ab = True, 那么源文件xx.py中的 ab变量的值 也会修改为True.

程序主模块中，必须使用 绝对导入，不能使用相对导入。