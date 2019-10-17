一。
 SIGINT信号：程序终止信号（interrupt）,在用户键入INTR字符(通常是Ctrl+C)时发出，用于通知前台进程终止。
 SIGPIPE信号：管道破裂。比如采用管道通信的两个进程，一个进程 读管道没打开或者意外终止，另一个进程往管道中写数据，那么写进程就会收到内核发送的SIGPIPE信号。
              相当于 水管的一端 堵死了，你还往水管中 倒水。。能倒进去吗。。
              这个信号的缺省动作是终止进程。

SIGUSR1信号：留给用户使用的信号。缺省动作是 终止进程。

二。模块的基本使用

1.接收信号

代码：
import signal
import os
import time


# 定义主进程接受到信号之后的处理函数
def receive_signal(signum, stack):
    print("Received:",signum)

#注册信号处理函数,主进程接收到 SIGUSR1或者SIGUSR2 信号后，执行处理函数
signal.signal(signal.SIGUSR1, receive_signal)  # signal.SIGUSR1 实际上是一个数字，其他的信号也是数字
signal.signal(signal.SIGUSR2, receive_signal)

print("My pid is:",os.getpid())

while True:
    print("Waiting....")
    time.sleep(3)

# 打开终端运行程序，打开另外一个终端执行：kill -USR1 主进程pid，发送信号给主进程。如果在主进程代码里发送信号可以使用os.kill()。

2. 获取注册的处理程序

代码：
import signal

def alarm_received(n, stack):
    return

signal.signal(signal.SIGALRM,alarm_received)

signal_to_names = dict(
    [(getattr(signal, n),n) for n in dir(signal) if n.startswith("SIG") and "_" not in n]   
)

#print(sorted(signal_to_names.items()))

for s, name in sorted(signal_to_names.items()):   # s是信号的数值，name是信号的名字。
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:     
        handler = "SIG_DFL"
    elif handler is signal.SIG_IGN:
        handler = "SIG_IGN"

    print("%-10s (%2d):" % (name, s), handler)

# signal.SIG_DFL 代表信号的默认的处理函数，实际上是 数字 0
# signal.SIG_IGN 代表忽略信号。实际上是 数字 1

3. 发送信号

在程序中 模拟用户按下 CTRL+C 

下面的代码仅仅适用于python3.6

代码：
import signal
import os

i = 0
while True:
    print("i is %d" % i)
    i += 1
    if i >100:
        os.kill(signal.CTRL_C_EVENT)
        time.sleep(1)

4.闹铃

闹铃(Alarm)是一种特殊的信号，程序要求操作系统在过去一段时间后再发出这个信号通知，这对于避免一个I/O操作或者其他系统调用无限阻塞很有用。
一个进程中 只能设置一个闹钟。

代码：
import signal
import time

def receive_alarm(signum,stack):
    print("Alarm:",time.ctime())

signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print("Before:",time.ctime())
time.sleep(4)
print("After:",time.ctime())

# 在这个例子中，sleep 会在 2秒之后被中断，执行完 信号处理函数之后，会继续延时2秒，然后主进程继续执行。

5.忽略信号

想要忽略一个信号，需要注册SIG_IGN 作用处理程序

代码：
import signal
import os
import time

def do_exit(sig,stack):
    raise SystemError("退出了程序")

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print("主进程pid：",os.getpid())

signal.pause()  # 进程 休眠，直到接收到信号（任意信号），windwos平台不支持。

# 执行程序，然后按下CTRL+C 发送SIG_INT信号，会发现什么反应也没有。。因为SIG_INT信号 已经被忽略了。
# 打开另外一个终端执行：kill -USR1 主进程pid ，会抛出异常退出程序。

6. 等待信号到来

signal.pause 、signal.sigwait 

代码1:
import signal
import os

def do_exit(sig,stack):
    print("--test--")
    raise SystemError("退出了程序")

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print("主进程pid：",os.getpid())

signum = signal.sigwait([signal.SIGUSR1,signal.SIGINT])  # 当前线程休眠，直到接收到某些信号（列表当中的信号）。
                                                         # 函数的返回值是 信号的编号。 
print("信号的编号：",signum)                             
                                                            

7. 信号和线程

代码：
import signal
import threading
import os
import time

def signal_handler(signum, stack):
    print("Received signal %d in %s"% (signum,threading.current_thread().name))

signal.signal(signal.SIGUSR1, signal_handler)

def wait_for_signal():
    print("Waiting for signal in", threading.current_thread().name)
    signal.pause()
    print("Done waiting")

receiver = threading.Thread(target=wait_for_signal, name="receiver")
receiver.start()
time.sleep(0.1)

def send_signal():
    print("Sending signal in", threading.current_thread().name)
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name="sender")
sender.start()
sender.join()

print("Wating for", receiver.name)
signal.alarm(2)    # 2秒之后发送 SIGALRM 信号，这个函数不会阻塞主进程。
receiver.join()

#  最后一行 打印出来的字符跟 系统有关系。
#  信号是由 主线程接收的，子线程或者子进程无法接收到信号。尽量不要在 多线程中使用信号。
#  python中，多个子线程 发同一个信号（不可靠信号），第一个信号如果没有处理完，第二个信号就会被丢弃
#  主线程接收到了 SIGALRM 信号后，会执行默认的处理动作，即终止 所有的 线程。