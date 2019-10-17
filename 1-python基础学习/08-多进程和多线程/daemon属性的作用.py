
daemon属性的作用（默认是False）：
如果为 False：
主进程或者主线程 如果 意外挂掉或者终止，子进程或者子线程 不会 挂掉。
主进程或主线程 都会等待 子进程或者子线程执行结束（执行完最后一行代码），然后主进程和主线程才会终止。

如果为 True：
主进程或者主线程 如果 意外挂掉或者终止，子进程或者子线程 会 挂掉。
主进程或者主线程 执行结束后（执行完最后一行代码），不会等待子进程或者子线程，而是会 直接终止子进程或者子线程。
可以使用join方法，让主进程或者主线程等待。


进程池中，daemon 默认是 True


代码：
from threading import Thread
import time
import sys

def test():
    while True:
        print("---test--")
        time.sleep(1)

if __name__ == "__main__":
    p = Thread(target=test)
    #p.daemon = True    或者 p.setDaemon(True) # 默认是False
    p.start()
    while True:
        print("主线程")
        time.sleep(1)
        sys.exit()     # 这里 可以用 Ctrl+C 代替。

# 主线程 终止 之后，子线程会继续执行。


