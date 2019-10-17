一。 基本教程

logging模块用来记录程序运行期间发生的一些事情。例如，使用try语句捕获异常之后，需要提醒下开发人员，这里有个异常出现。再比如，网站服务器要记录用户的ip地址，访问时间，访问的网址等等信息。

1.日志级别：
根据日志的严重程度划分成5个日志级别（从上到下等级递增）：

DEBUG：    调试信息。开发的时候调试程序才会用到。
INFO：     确认程序按照我们预期的去执行。
WARNING：  这表明发生了一些意想不到的事情，或者预示着在不久的将来会出现一些问题（例如，磁盘空间很低）。该程序仍按预期运行。
ERROR：    由于一个更严重的问题，该程序无法执行某些功能。
CRITICAL： 一个严重的错误，表明程序本身可能无法继续运行。

默认的日志级别为：WARNING。这意味着只有WARNING以及其以上的级别日志信息才会被记录。默认日志信息是打印到终端里。我们可以进行相关的配置，把日志信息保存到文件中。

2.demo1--日志打印到终端

import logging

logging.warning("警告！！！")
logging.info("确认信息！！")

执行结果：
WARNING:root:警告！！！ 

# 过于日志的输出格式，我们可以进行灵活的自定义，稍后会详细说明。

3. demo2--日志保存到文件

import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('调试信息')
logging.info('确认信息')
logging.warning('警告信息')

# 默认，日志信息是 追加到文件当中，如果你不想追加文件，每次运行时候都要清空以前的日志信息，那么你可以设置filemode参数：
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

4. demo3--程序中包含多个模块

# myapp.py
import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()

# mylib.py
import logging

def do_something():
    logging.info('Doing something')

运行后，查看日志文件：
INFO:root:Started
INFO:root:Doing something
INFO:root:Finished

# 此时我们不能跟踪每条日志的来源。想完成这个功能，参考后面的高级用法。

5. demo4--格式化字符串

import logging
logging.warning('%s before you %s', 'Look', 'leap!')

执行结果：
WARNING:root:Look before you leap!

6. demo5--改变消息显示的格式