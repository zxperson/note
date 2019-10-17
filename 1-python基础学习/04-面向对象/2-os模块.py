一、os模块常用的操作：

1. os.name
    查看当前使用的操作系统
        In [11]: os.name
        Out[11]: 'posix'

2.os.curdir
   代表当前目录
        In [16]: os.curdir
        Out[16]: '.'

3.os.pardir
    代表上一级目录
        In [17]: os.pardir
        Out[17]: '..'

4. os.sep
    操作系统的路径分隔符
        In [18]: os.sep
        Out[18]: '/'

5.os.linesep
    操作系统换行符
        In [19]: os.linesep
        Out[19]: '\n'

6.os.getcwd()
    返回当前的工作路径
        In [2]: os.getcwd()
        Out[2]: '/home/python/workspace'

7.os.chdir
    切换工作目录
        In [3]: os.chdir('..')    返回上一级目录

8.os.listdir
    查看指定路径下的 文件名以及文件夹名，返回值为一个列表
        In [2]: os.listdir('.')
        Out[2]: ['test.py']

9.os.mkdir
    创建目录(单层)
        In [3]: os.mkdir('./aabb')    在当前的目录下创建一个名叫aabb的目录

10.os.makedirs
    递归创建目录
        In [2]: os.makedirs('./aabb/ccdd')

11.os.remove
    删除文件
        In [2]: os.remove('test.py')

12. os.rmdir
    删除目录(单层)
        In [2]: os.rmdir('./aabb')

    删除非空的文件夹将会抛出异常

13. os.removedirs
    递归的删除文件夹，遇到空文件夹会抛出异常
        In [4]: os.removedirs('./workspace')                                                                      

14. os.rename
    给文件或文件夹改名
        In [2]: os.rename('./aabb','./bbcc')

15. os.system
    执行shell命令
        In [7]: os.system('ls')

16. os.path.abspath
    返回绝对路径
        In [8]: os.path.abspath('.')
        Out[8]: '/home/python'

17. os.path.basename
    返回路径中的文件名
        In [6]: os.path.basename('/home/python/workspace/test.txt')
        Out[6]: 'test.txt'    

18. os.path.commonprefix
    返回列表(多个路径)中，所有路径 共有的最长的路径。
        In [7]: test_list = ['/home/python/abc','/home/python/dfg','/home/hehe']
        In [8]: os.path.commonprefix(test_list)
        Out[8]: '/home/'

19. os.path.dirname
    返回文件的路径(不包含文件名)
        In [11]: os.path.dirname('/home/python/test.txt')
        Out[11]: '/home/python'

20. os.path.exists
    路径存在则返回True,路径损坏返回False
        In [12]: os.path.exists('.')
        Out[12]: True

21. os.path.expanduser
    把path中包含的"~"转换成用户目录    
        In [18]: os.path.expanduser('~')
        Out[18]: '/home/python'

22. os.path.isabs
    检测一个路径是否为绝对路径，如果是绝对路径返回True，如果不是绝对路径返回False
        In [2]: os.path.isabs('.')
        Out[2]: False

23. os.path.isfile
    检测一个文件是否存在，如果存在返回True，不存在返回False
        In [3]: os.path.isfile('./aa.txt')
        Out[3]: False

24. os.path.isdir
    检测一个目录是否存在，如果存在返回True，不存在返回False
        In [4]: os.path.isdir('./hrhr')
        Out[4]: False

25. os.path.join
    用于路径拼接，将多个路径拼接为一个路径
        In [8]: os.path.join('/home','python','123')
        Out[8]: '/home/python/123'

26. os.path.getatime
    获取该文件上次访问过的时间,返回值为unix时间戳
        In [2]: os.path.getatime('./test.txt')
        Out[2]: 1496455400.0310266

27. os.path.getctime
    获取该文件属性上次被修改过的时间,返回值为unix时间戳

28. os.path.getmtime
    获取该文件内容上次被修改过的时间,返回值为unix时间戳

29. os.path.getsize
    获取该文件的大小,返回值单位是字节
        In [3]: os.path.getsize('./test.txt')
        Out[3]: 25


unix时间戳：从格林威治时间1970年01月01日00时00分00秒起至现在的总秒数。
注意，单位是秒

        




  



 
  

    


    



    












        









