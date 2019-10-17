一。介绍
    
    subprocess 提供了一个api 可以创建子进程并与之通信。

二。基本使用

1. 不采用 os.system(),执行 shell命令。call()

    call()方法默认使用 /bin/sh 来执行shell命令

代码：
import subprocess

subprocess.call(["ls","-l"])  # 执行 ls -l 命令


#call()的返回值是 shell命令的 退出码。如果退出码是0，代表 shell命令正常执行。所以可以判断 call()的返回值来检测错误。

2. check_call()


check_call() 类似 call(), 只不过，如果 shell命令发生了错误，会产生一个 CalledProcessError 异常

代码：
import subprocess

try:
    ret = subprocess.check_call(["ls","-2"])

except subprocess.CalledProcessError as err:
    print("ERROR is : %s" % err)
    print("shell命令的退出码：%s" % err.returncode)

3. call() 和 check_call() 一个参数：shell=True
    
    默认 shell=False

代码：
import subprocess

try:
    ret = subprocess.check_call(["ls","-2"], shell=True)

except subprocess.CalledProcessError as err:
    print("ERROR is : %s" % err)
    print("shell命令的退出码：%s" % err.returncode)


# 执行代码 发现，异常消失了。程序正常执行了。
# 当 shell=True 之后， 参数列表中，只有第一个元素 会被当成 shell命令执行。

正确的代码：
import subprocess

try:
    ret = subprocess.check_call("ls -2", shell=True)

except subprocess.CalledProcessError as err:
    print("ERROR is : %s" % err)
    print("shell命令的退出码：%s" % err.returncode)


4. shell=True 会产生安全隐患

代码：
from subprocess import call

s = input("输入字符串:")

call(s,shell=True)

# 执行代码，然后输入 rm -rf 1.txt 这个字符串，发现当前目录下的 1.txt 被删除了。。相当于 shell注入攻击

5. check_output()

shell命令 执行完毕后 捕获 标准输出 作为返回值。如果 shell命令发生了错误，会产生一个 CalledProcessError 异常

代码1：
import subprocess

output = None

try:
    output = subprocess.check_output(
        "echo to stdout;echo to stderr 1>&2",
        shell= True,
    )

except subprocess.CalledProcessError as err:
    print("Error is",err)

finally:
    print("output is", output)

打印结果：
to stderr
output is b'to stdout\n'

# 执行了两个shell命令。
# "to stdout" 在标准输出中，所以会被捕获。
#  1>&2 的意思是 标准输出 合并到 标准错误。所以"to stderr" 在 标准错误中。不会被捕获

代码2：
import subprocess

output = None

try:
    output = subprocess.check_output(
        "echo to stderr 1>&2;echo to stdout",
        shell= True,
    )

except subprocess.CalledProcessError as err:
    print("Error is",err)

finally:
    print("output is", output)

打印结果：
to stderr
output is b'to stdout\n'

# 执行 第一条命令的时候， 标准输出 合并到 标准错误。
# 执行 第二条命令的时候，不会合并。。所有捕获到了"to stdout"


代码3：
import subprocess

output = None

try:
    output = subprocess.check_output(
        "echo to stderr 1>&2",
        shell= True,
    )

except subprocess.CalledProcessError as err:
    print("Error is",err)

finally:
    print("output is", output)

打印结果：
to stderr
output is b''

代码4：
# 如果想要一起 捕获标准输出和标准异常呢？

import subprocess

output = None

try:
    output = subprocess.check_output(
        "echo to stdout;echo to stderr 1>&2",
        shell= True,
        stderr=subprocess.STDOUT
    )

except subprocess.CalledProcessError as err:
    print("Error is",err)

finally:
    print("output is", output)

打印结果：

output is b'to stdout\nto stderr\n'


三。subprocess.Popen()

1. 运行一个shell命令，读取它的所有输出。

代码：
import subprocess

proc = subprocess.Popen(["echo","to stdout"],stdout=subprocess.PIPE)

stdout_value = proc.communicate()[0]  #或者这样写：stdout = proc.stdout.read()
print("output is %s" % stdout_value)

打印结果：
output is b'to stdout\n'

# 如果想要获取 子进程执行完成后的 标准输出或者标准错误 必须把stdout或者stderr设置为subprocess.PIPE, 把标准输出或者标准错误 中的数据 存储到管道中。
# communicate() 方法 返回的是一个元组。格式：(stdout_data,stderr_data)
# 管道就是 父进程和子进程 通信使用的一个内存缓冲区
# communicate() 方法 会等待子进程执行完，才会有返回值。

2. 运行一个shell命令,shell命令的输入，通过主进程传递进去。

代码：
import subprocess

print("write:")
proc = subprocess.Popen(["cat","-"],stdin=subprocess.PIPE)

proc.communicate("我是cat命令的输入".encode("utf-8"))   # 向子进程中 传入数据

打印结果：
write:
我是cat命令的输入

# 命令行中 输入 cat - 终端会等待用户的输入。用户输入什么，屏幕中就会打印什么。

3. 父进程和子进程 进行双向通信

代码：
import subprocess

print("popen2:")
proc = subprocess.Popen(["cat","-"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)

msg = b"through stdin to stdout"
stdout_value = proc.communicate(msg)[0]

print("\tpass through:", repr(stdout_value))

4. 捕获子进程的 标准错误数据

代码：
import subprocess

print("popen3:")
proc = subprocess.Popen("cat -; echo to stderr 1>&2",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True)

msg = b"through stdin to stdout"
stdout_value, stderr_value = proc.communicate(msg)

print("\tpass through:", repr(stdout_value))
print("\tstderr      :",repr(stderr_value))

打印结果：
popen3:
    pass through: b'through stdin to stdout'
    stderr      : b'to stderr\n'

5. 把 标准错误 合并到 标准输出
代码：
import subprocess

print("popen4:")
proc = subprocess.Popen("cat -; ls -2",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True)

msg = b"through stdin to stdout"
stdout_value, stderr_value = proc.communicate(msg)

print("\tpass through:", repr(stdout_value))
print("\tstderr      :",repr(stderr_value))

打印结果：
popen4:
    pass through: b"through stdin to stdoutls\xef\xbc\x9a\xe6\x97\xa0\xe6\x95\x88\xe9\x80\x89\xe9\xa1\xb9 -- 2\nTry 'ls --help' for more information.\n"
    stderr      : None


除了更改 Popen类的参数之外，还可以 通过命令行 实现同样的效果。如下面的代码所示：
import subprocess

print("popen4:")
proc = subprocess.Popen("cat -; ls -2 2>&1",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,

                        shell=True)

msg = b"through stdin to stdout"
stdout_value, stderr_value = proc.communicate(msg)

print("\tpass through:", repr(stdout_value))
print("\tstderr      :",repr(stderr_value))


6. 连接管道

使用Popen 执行 shell命令：ifconfig | grep "广播" | cut -d : -f 2 | cut -d " " -f 1

代码：
import subprocess

ifconfig = subprocess.Popen("ifconfig",
                        stdout=subprocess.PIPE,
                        shell=True)

grep = subprocess.Popen("grep 广播",
                        stdin=ifconfig.stdout,
                        stdout=subprocess.PIPE,
                        shell=True
                        )

cut1 = subprocess.Popen("cut -d : -f 2",
                        stdin=grep.stdout,
                        stdout=subprocess.PIPE,
                        shell=True
                        )

cut2 = subprocess.Popen('cut -d " " -f 1',
                        stdin=cut1.stdout,
                        stdout=subprocess.PIPE,
                        shell=True
                        )

end_stdout = cut2.communicate()[0]
print(end_stdout)

7. 两个py文件 通过管道缓冲区 进行双向通信

chuanzhi.py

代码：
import sys

sys.stderr.write("chuanzhi.py:starting\n")
sys.stderr.flush()

while True:
    next_line = sys.stdin.readline()   #程序会在这里阻塞，等待输入
    if not next_line:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write("chuanzhi.py:ending\n")
sys.stderr.flush()


game.py

代码：
import subprocess

print("One line at a time:")
proc = subprocess.Popen("python3 chuanzhi.py",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        shell=True
                        )

for i in range(5):
    proc.stdin.write(b"%d\n"%i)
    proc.stdin.flush()      # 刷新标准输入。
    output = proc.stdout.readline()
    print(output.rstrip())

remainder = proc.communicate()[0]  # 这里获取到的是空值
print(remainder)

打印结果：
One line at a time:
chuanzhi.py:starting
b'0'
b'1'
b'2'
b'3'
b'4'
chuanzhi.py:ending
b''

把game.py修改为：
import subprocess

print("One line at a time:")
proc = subprocess.Popen("python3 chuanzhi.py",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        shell=True
                        )

for i in range(5):
    proc.stdin.write(b"%d\n"%i)

proc.stdin.flush()
output = proc.communicate()[0]
print(output)

打印结果：
One line at a time:
chuanzhi.py:starting
chuanzhi.py:ending
b'0\n1\n2\n3\n4\n'


四。subprocess.run()

python3.5 中 新添加了一个run方法。

1.基本使用

代码：
import subprocess

completed = subprocess.run(["ls","-l"])
print("retruncode is %d" % completed.returncode)  #获取 shell命令执行完之后的 退出状态码  

# run 方法中的 shell参数和 call、check_call、check_ouput、Popen方法的 是一样的。
# 使用 run方法的时候，如果没有设置 check=True ，等效于 call()方法。
# 使用 run方法的时候，如果设置 check=True, 等效于 check_call()方法。
# 使用 run方法的时候，如果设置 check=True, stdout=PIPE，等效于 check_output()方法。只不过，标准输出的内容，存放在 run方法返回值的 stdout属性中。

2.获取 标准输出和标准错误

代码：
import subprocess

try:
    completed = subprocess.run("echo to stdout; echo to stderr 1>&2; exit 1",
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )

except subprocess.CalledProcessError as err:
    print("error is: %s" %err)

else:
    print("returncode is:%s",completed.returncode)
    print("Have {} bytes in stdout:{!r}".format(len(completed.stdout),completed.stdout.decode("utf-8")))
    print("Have {} bytes in stderr:{!r}".format(len(completed.stderr), completed.stderr.decode("utf-8")))

打印结果：
returncode is:%s 1
Have 10 bytes in stdout:'to stdout\n'
Have 10 bytes in stderr:'to stderr\n' 

# format 中 !r 代表在格式化之前 值 先调用 reper()函数。!s 代表 值 先调用str()函数。 !a 代表 值 先调用 ascii()函数。    

3. subprocess.DEVBULL

下面的例子中，把标准输出和标准错误 重定向到了 /dev/null 这个特殊文件中。
/dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。
但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。
相当于屏蔽了标准输出和标准错误

代码：
import subprocess

try:
    completed = subprocess.run("echo to stdout; echo to stderr 1>&2; exit 1",
                               shell=True,
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL
                               )

except subprocess.CalledProcessError as err:
    print("error is: %s" %err)

else:
    print("returncode is:%s",completed.returncode)
    print("Have {} bytes in stdout:{!r}".format(len(completed.stdout) if completed.stdout else 0,
                                                completed.stdout.decode("utf-8") if completed.stdout else "None"))
    print("Have {} bytes in stderr:{!r}".format(len(completed.stderr) if completed.stderr else 0,
                                                completed.stderr.decode("utf-8") if completed.stderr else "None"))

打印结果：
returncode is:%s 1
Have 0 bytes in stdout:'None'
Have 0 bytes in stderr:'None'

五。进程间传递信号

1. 进程之间信号传递

hehe.py

import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(["python3","chuanzhi.py"])
print("PARENT       : Pausing before sending signal...")
sys.stdout.flush()
time.sleep(1)
print("PARENT       : Signaling child")
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)


chuanzhi.py

import os
import signal
import time
import sys

pid = os.getpid()
received = False

def signal_usr1(signum, frame):
    global received
    received = True
    print("CHILD %6s: Received USR1" % pid)
    sys.stdout.flush()

print("CHILD %6s: Setting up signal handler" % pid)
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print("CHILD %6s: Pausing to wait for signal" % pid)
sys.stdout.flush()
time.sleep(3)

if not received:
    print("CHILD %6s: Never received signal" % pid)


# 在命令行中执行：python3 hehe.py

打印结果：
# PARENT       : Pausing before sending signal...
# CHILD  38075: Setting up signal handler
# CHILD  38075: Pausing to wait for signal
# PARENT       : Signaling child
# CHILD  38075: Received USR1


# 每个print后面都有个flush，作用是 让系统的缓存立刻生效。

2. 进程之间信号传递

如果 Popen创建的进程也创建了子进程，那么这些“孙子辈”的子进程，不会接收到发给“爸爸辈”的 信号。

意思就是：爷爷-爸爸-孙子。 爷爷发给爸爸的信号，孙子是 收不到的。

把 上一个例子中的 hehe.py 修改为如下（chuanzhi.py不要修改）：
import os
import signal
import subprocess
import tempfile
import time
import sys

script = """#!/bin/sh
echo Shell script in process $$
python3 chuanzhi.py
"""

script_file = tempfile.NamedTemporaryFile("wt")  # 该函数 返回一个 类文件对象 用于临时存储数据（实际对应磁盘上的一个临时文件）
script_file.write(script)                        # 当文件对象被 close或者del的时候，默认 临时文件会被删除。可以通过delete参数来控制是否删除。
script_file.flush()

proc = subprocess.Popen(["sh",script_file.name], close_fds=True)
print("PARENT       : Pausing before signaling %s..." % proc.pid)
sys.stdout.flush()
time.sleep(1)
print("PARENT       : Signaling clild %s" % proc.pid)
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)

#执行：python3 hehe.py
打印结果：
# PARENT       : Pausing before signaling 38627...
# Shell script in process 38627
# CHILD  38628: Setting up signal handler
# CHILD  38628: Pausing to wait for signal
# PARENT       : Signaling clild 38627
# CHILD  38628: Never received signal


3. 如何让“孙子辈”进程也能接收到爷爷的信号呢？

此时就需要用到进程组了。
Linux 的进程组是一个进程的集合，任何进程用系统调用 setsid 可以创建一个新的进程组，并让自己成为首领进程。
首领进程的子子孙孙只要没有再调用 setsid 成立自己的独立进程组，那么它都将成为这个进程组的成员。 
之后进程组内只要还有一个存活的进程，那么这个进程组就还是存在的，即使首领进程已经死亡也不例外。 
而这个存在的意义在于，我们只要知道了首领进程的 pid (同时也是进程组的 pgid)， 那么可以给整个进程组发送 signal，组内的所有进程都会收到。

因此利用这个特性，就可以通过 preexec_fn 参数让 Popen 成立自己的进程组， 然后再向进程组发送 SIGTERM 或 SIGKILL，中止 subprocess.Popen 所启动进程的子子孙孙。
当然，前提是这些子子孙孙中没有进程再调用 setsid 分裂自立门户。


把 上一个例子中的 hehe.py 修改为如下（chuanzhi.py不要修改）：
import os
import signal
import subprocess
import tempfile
import time
import sys

script = """#!/bin/sh
echo Shell script in process $$
python3 chuanzhi.py
"""

script_file = tempfile.NamedTemporaryFile("wt")
script_file.write(script)
script_file.flush()

def show_setting_sid():
    print("Calling os.setsid() from %s" % os.getpid())
    sys.stdout.flush()
    os.setsid()

proc = subprocess.Popen(["sh",script_file.name], preexec_fn=show_setting_sid)

print("PARENT       : Pausing before signaling %s..." % proc.pid)
sys.stdout.flush()
time.sleep(1)
print("PARENT       : Signaling process group %s" % proc.pid)
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)

打印结果：
# Calling os.setsid() from 40199
# PARENT       : Pausing before signaling 40199...
# Shell script in process 40199
# CHILD  40200: Setting up signal handler
# CHILD  40200: Pausing to wait for signal
# PARENT       : Signaling process group 40199
# CHILD  40200: Received USR1

# preexec_fn 这个参数如果被设置成一个可以调用的对象（例如：函数）。
# 这个对象将会被调用，在Popen 进程 创建完成之后，执行之前。




