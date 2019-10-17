1. 创建 多线程 

from threading import Thread
import time

def Mythrend():
    for i in range(5):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    t = Thread(target=Mythrend)
    t.start()
    print('-----1-------')

默认，主线程 会 等待子线程结束后，再退出。

2. 重写 run 方法

代码：
    from threading import Thread
    import time

    class MyThread(Thread):

        def __init__(self, n):
            Thread.__init__(self)  #注意 调用父类的__init__方法。
            self.n = n

        def run(self):
            for i in range(self.n):
                print('---线程名字:%s-- %d ---'% (self.name, i))
                time.sleep(1)

    if __name__ == "__main__":
        t = MyThread(5)
        t.start() 

3. 控制线程的结束

代码：
    from threading import Thread
    import time

    class ControlThread(object):
        def __init__(self):
            self._running = True

        def end(self):
            self._running = False

        def test(self, n):
            while self._running and n>0:
                print('---test---',n)
                n -= 1
                time.sleep(5)

    if __name__ == "__main__":
        c = ControlThread()
        t = Thread(target=c.test,args=(10,))
        t.start()

        time.sleep(2)
        c.end()
        t.join()
        print('---子线程已经结束----')

4. 多个线程之间，共享全局变量

代码：
    from threading import Thread
    import time

    g_num = 0

    def test1():
        global g_num
        for i in range(1000000):
            g_num += 1

        print('---test1----g_num=%d'% g_num)

    def test2():
        global g_num
        for i in range(1000000):
            g_num += 1

        print('---test2----g_num=%d' % g_num)

    if __name__ == "__main__":
        p1 = Thread(target=test1)
        p1.start()

        p2 = Thread(target=test2)
        p2.start()

        time.sleep(1)
        print('----g_num=%d'%g_num)

    执行的结果和我们预期的并不一样，为什么会这样呢？画图。

5. 互斥锁
    多个线程 同时 修改一个 共享数据，需要进行 线程同步。
    代码：
        from threading import Thread,Lock
        import time

        g_num = 0

        def test1():
            global g_num
            for i in range(1000000):
                if mutex.acquire():   # 默认 没有获得锁 之前会无限阻塞。获的锁之后，返回True。
                                      # timeout参数可以指定 超时时间，超时时间过了就会解阻塞。默认是-1，无限阻塞，直到获取到锁。
                    g_num += 1        # blocking = False ，获得锁之前 不会阻塞，返回值False。获的锁之后 返回值是True。
                    mutex.release()   # 当blocking=False时，禁止设置超时时间。

            print('---test1----g_num=%d'% g_num)

        def test2():
            global g_num
            for i in range(1000000):
                if mutex.acquire():
                    g_num += 1
                    mutex.release()

            print('---test2----g_num=%d' % g_num)

        if __name__ == "__main__":
            mutex = Lock()
            p1 = Thread(target=test1)
            p1.start()

            p2 = Thread(target=test2)
            p2.start()

            time.sleep(5)
            print('----g_num=%d'%g_num)

6. 死锁

代码：
import threading
import time

num = 0
mutex = threading.Lock()

class MyThread(threading.Thread):

    def run(self):
        global num
        time.sleep(2)

        if mutex.acquire():
            num = num + 1
            print(self.name + " set num to " + str(num))

            if mutex.acquire():
                num = num + 1
                print(self.name + " set num to " + str(num))
                mutex.release()
            mutex.release()

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    test()

# 屏幕输入一行信息之后，会产生死锁。死锁的原因：同一个线程里 两次进行加锁操作。
# 如何解决呢？第一种。方法 在 第二次加锁的时候，设置超时时间。第二种方法，直接把互斥锁换成 可重入锁。

            
6. 可重入锁 RLock
 可重入锁是指同一个锁可以多次被同一线程加锁而不会死锁。 
 实现可重入锁的目的是防止递归函数内的加锁行为，或者某些场景内无法获取锁A是否已经被加锁，这时如果不使用可重入锁就会对同一锁多次重复加锁，导致立即死锁。

 RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次acquire。
 直到一个线程所有的acquire都被release，其他的线程才能获得资源。

 代码：
 import threading
import time

num = 0
mutex = threading.RLock()

class MyThread(threading.Thread):

    def run(self):
        global num
        time.sleep(2)

        if mutex.acquire():
            num = num + 1
            print(self.name + " set num to " + str(num))

            if mutex.acquire():
                num = num + 1
                print(self.name + " set num to " + str(num))
                mutex.release()
            mutex.release()

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    test()

# 换成 RLock 之后，死锁问题没有了。

7. 线程间通信---队列
    Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO(先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。
    这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用。可以使用队列来实现线程间的同步。


8. Event 对象（线程间传递信号,线程同步）

想一个问题：子线程 循环 打印 10,9，.......1 这10个数字，在子线程执行的时候，主线程阻塞。
            当 子线程打印完5这个数字之后，想让 主线程 继续执行。

            那么，此时 我们可以用 Event对象 来 实现。

    代码：
        from threading import Thread,Event
        import time

        def test(n,event):
            while n > 0:
                if n == 5:
                    event.set()
                print('-----test---',n)
                n -= 1
                time.sleep(5)

        if __name__ == "__main__":
            event = Event()
            print('----1----')
            t = Thread(target=test,args=(10,event))
            t.start()
            event.wait()   # 主线程 会在这里 阻塞，直到 子线程 执行了 event.set()
            print('----主线程---')

    代码：
        from threading import Thread,Event
        import time

        def test(n,event):
            while n > 0:
                if n == 5:
                    event.set()    
                print('-----test---',n)
                n -= 1
                time.sleep(5)

        def test2(n,event):
            event.wait()
            while n > 0:
                print('----test2---', n)
                n -= 1
                time.sleep(5)

        if __name__ == "__main__":
            event = Event()
            print('----1----')
            t = Thread(target=test,args=(10,event))
            t2 = Thread(target=test2,args=(10,event))
            t.start()
            t2.start()
            event.wait()
            print('----主线程---')

# Event对象 内部管理了一个 标志. 是线程间安全通信的一种简单方法。
# set() 方法 把这个 内部标志 设置为True。所有等待它变成True的线程 都会被唤醒，调用wait()方法的线程就会 解阻塞。
# clear() 方法 把这个 内部标志 重置为 False。调用wait()的线程将会阻塞。直到 内部标志设置成True。
# is_set() 方法 用来判断 内部标志 是否为 True。如果 内部标志是True，这个方法返回True。
# wait() 方法 如果不传参数，阻塞线程，直到 内部标志被设置True。参数 timeout 可以指定超时时间，是一个浮点数。

9. Condition

除了使用Event对象外，还可以通过使用一个Condition对象来完成线程同步。
条件变量对象允许一个或者多个线程等待，直到另外一个线程通知它们。

代码：
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format="(%(threadName)-10s) %(message)s")

def consumer(cond):
    logging.debug("starting consumer thread")
    with cond:    # 获取 Condition对象 中的 底层锁，执行完代码后 自动释放。
        logging.debug("--test--")
        cond.wait()  # 释放锁，然后线程挂起。如果调用线程在调用该方法时没有获得锁，抛出RuntimeError异常。
        logging.debug("resource is available to consumer")

def producer(cond):
    logging.debug("starting producer available")
    with cond:
        logging.debug("marking resource available")
        cond.notifyAll()   # 唤醒所有 调用wait方法阻塞的线程。被唤醒的线程会抢夺锁，拿到锁的先执行。

condition = threading.Condition()  # 默认 Condition对象中的 底层锁 是 RLock。如果可以通过 lock参数，设置为 互斥锁。如果设置了，这个参数必须是 Lock对象或者RLock对象。

c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
c2 = threading.Thread(name="c2", target=consumer, args=(condition,))
p = threading.Thread(name="p", target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

# 注意 虽然Condition变量中包含一个RLock，但是不要把两者混为一起。
# 一般是不需要自己指定 Condition中的 底层锁的。除非，需要在多个Condition对象中共享一个锁。

9. 创建 线程池
    
    代码：
        from concurrent.futures import ThreadPoolExecutor
        import time

        def test(n):
            print('----',n)
            time.sleep(1)

        if __name__ == "__main__":
            pool = ThreadPoolExecutor(2)
            for i in range(10):
                pool.submit(test,i)
            pool.shutdown()
            

    代码：
        from concurrent.futures import ThreadPoolExecutor
        import time

        def test(n):
            print('----',n)
            time.sleep(1)

        if __name__ == "__main__":
            pool = ThreadPoolExecutor(2)
            for i in range(10):
                pool.submit(test,i)
            pool.shutdown(wait=True)  #那么 如果参数为False呢？如果为 True，主线程 ，会在这里阻塞。
            print('--hehe--')

10. 列举所有的线程

代码：
import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,format="(%(threadName)-10s) %(message)s")

def worker():
    pause = random.randint(1,5)
    logging.debug("sleeping %s", pause)
    time.sleep(pause)
    logging.debug("ending")

for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.current_thread()

for t in threading.enumerate():  #列举出所有的活着的线程对象。
    if t is main_thread:
        continue
    logging.debug("joining %s",t.getName())
    t.join()

11. 定时器 线程

代码：
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format="(%(threadName)-10s) %(message)s")

def delayed():
    logging.debug("worker runing")

t1 = threading.Timer(5,delayed)  # 5秒之后 再去执行线程
t1.setName("t1")
t2 = threading.Timer(5,delayed)
t2.setName("t2")

logging.debug("starting timers")
t1.start()
t2.start()

logging.debug("waiting before canceling %s", t2.getName())
time.sleep(2)
logging.debug("canceling %s",t2.getName())
t2.cancel()   # 关闭定时器。
logging.debug("done")

# Timer类 继承于 Thread 类。
# 定时器 线程 在延时期间是可以被关闭的，只需要调用 cancel 方法。
# t2 这个定时器线程，永远不会执行。

11. 限制资源的并发访问--信号量

信号量(Semaphore)，有时被称为信号灯，是在多线程环境下使用的一种机制。
有时候可能需要允许多个线程同时访问一个资源，但是要限制总数。例如，连接池支持同时连接，但是数目是固定的，或者一个网络应用支持固定数目的并发下载。

一个信号量 管理了一个内部计数器（实际上是一个整数）。调用acquire()方法时 减1 。调用release()方法时，加1 。这个计数器永远不能小于0。
当线程里调用了acquire()发现，内部计数器已经是0了，这个线程会阻塞，直到内部计数大于0。
信号量支持 上下文管理器。

代码：
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format="(%(threadName)-10s) %(message)s")

class ActivePool(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug("Running append: %s", self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug("Running remove: %s", self.active)

def worker(s, pool):
    logging.debug("Waiting to join the pool")
    with s:
        name = threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(3)
        pool.makeInactive(name)

pool = ActivePool()
s = threading.Semaphore(2)   # 创建 信号量对象，参数是 内部计数器的初始值。默认值是 1. 这里，保证了 最多只有两个线程在执行 信号量包裹的代码。
for i in range(4):
    t = threading.Thread(target=worker, name=str(i), args=(s,pool))
    t.start()


12. 线程特定数据 threading.local

在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看到，不会影响其他线程。
全局变量的修改必须要加锁。

代码：
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG,format="(%(threadName)-10s) %(message)s")

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug("No value yet")
    else:
        logging.debug("value=%s", val)

def worker(data):
    show_value(data)
    data.value = random.randint(1,100)
    show_value(data)

local_data = threading.local()
show_value(local_data)
local_data.value = 1000   # 绑定一个value属性，这个属性只能在 当前线程访问。
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()

# threading.local 最常用的地方就是为每一个线程绑定一个数据库连接，http请求，用户身份信息等

13.GIL锁

为什么 多线程里面 会有 GIL锁？
GIL锁是Cpython里面的。cpython解释器对于操作系统来说，就是一段C语言写的程序。
那么，cpython解释器里面的代码也需要去处理多个线程修改共享数据的问题。一开始
的时候，也是用互斥锁来处理的。也就是我们现在说的GIL锁。当后来发现GIL锁严重影响
性能时，已经晚了。如果是单核cpu的话，GIL锁不会影响效率。

python的多线程 不适合 执行 cpu密集型任务，比较适合执行 I/O密集型任务。线程在遇到I/O 阻塞的时候会主动释放GIL锁，触发cpu的调度。

cpu密集型任务:  特点是要进行大量的计算，消耗CPU资源.任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低.

I/O密集型任务:  涉及到网络、磁盘I/O的任务都是I/O密集型任务.
                这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。
                对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。





