
1.网络调试助手发送upd数据，接收后打印到终端

代码：
    from socket import *

    udp_socket = socket(AF_INET,SOCK_DGRAM)

    bind_addr = ('',7788)
    udp_socket.bind(bind_addr)             #给 套接字 绑定地址。如果不绑定，系统随机分配

    recv_data = udp_socket.recvfrom(1024)  #1024表示 每次接收到的 最大字节数
    print(recv_data)                       

    udp_socket.close()

recv_date是一个元组。如下格式：(b'haha\r\n', ('192.168.253.3', 8080))

2.tcp服务器

代码：
    from socket import *

    tcp_ser_socket = socket(AF_INET, SOCK_STREAM)

    tcp_ser_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)   #重复使用绑定的端口

    address = ('',7788)
    tcp_ser_socket.bind(address)

    tcp_ser_socket.listen(5)

    new_socket, client_addr = tcp_ser_socket.accept()

    recv_data = new_socket.recv(1024)
    print(recv_data)
    new_socket.send(b'thanks!')

    new_socket.close()

    tcp_ser_socket.close()

3.tcp客户端

代码：
    from socket import *

    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    ser_addr = ('192.168.253.3',7788)
    tcp_client_socket.connect(ser_addr)

    send_data = input('请输入要发送的数据:')
    tcp_client_socket.send(send_data.encode('gb2312'))

    recv_data = tcp_client_socket.recv(1024)
    print(recv_data.decode('gb2312'))

    tcp_client_socket.close()

注意编码。

4.单进程 非阻塞 tcp服务器

代码：
    from socket import *

    ser_socket = socket(AF_INET,SOCK_STREAM)
    ser_socket.setblocking(False)    # 设置 套接字 为 非阻塞
    ser_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)    #重复使用端口

    ser_addr = ('',7788)
    ser_socket.bind(ser_addr)

    ser_socket.listen(5)

    client_addr_list = []  # 保存 已连接的 套接字和地址端口
    del_list = []          # 保存 需要删除的 套接字和地址端口

    while True:
        try:
            client_socket,client_addr = ser_socket.accept()
        except:
            pass
        else:
            print('一个新的客户端到来%s'%str(client_addr))
            client_socket.setblocking(False)
            client_addr_list.append((client_socket,client_addr))

        for clientSocket,clientAddr in client_addr_list:
            try:
                recvData = clientSocket.recv(1024)
            except:
                pass
            else:
                if len(recvData)>0:
                    print("%s:%s"%(str(clientAddr),recvData.decode("gb2312")))
                else:
                    clientSocket.close()
                    del_list.append((clientSocket,clientAddr))
                    print("%s 已经下线"%str(clientAddr))
        for temp in del_list:
            client_addr_list.remove(temp)

5.单进程-select 
代码：
    import select
    import socket
    import sys

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('', 7788))
    server.listen(5)

    inputs = [server, sys.stdin]

    running = True

    while True:
        # 调用 select 函数，阻塞等待
        readable, writeable, exceptional = select.select(inputs, [], [])
        # 数据抵达，循环
        for sock in readable:
            # 监听到有新的连接
            if sock == server:
                conn, addr = server.accept()
                # select 监听的socket
                inputs.append(conn)
            # 监听到键盘有输入
            elif sock == sys.stdin:
                cmd = sys.stdin.readline()
                running = False
                break
            # 有数据到达
            else:
                # 读取客户端连接发送的数据
                data = sock.recv(1024)
                if data:
                    sock.send(data)
                else:
                    # 移除select监听的socket
                    inputs.remove(sock)
                    sock.close()
        # 如果检测到用户输入敲击键盘，那么就退出
        if not running:
            break 
    server.close()

5. gevent

异步编程 twisted tornado  gevent tulip

代码1：
    import gevent
    import tiem

    gevent.monkey.patch_all()

    def test1():
        print('---test1-----')
        time.sleep(1)
        print('----test1----continue---')

    def test2():
        print('------test2-----')
        time.sleep(1)
        print('------test2----continue---')

    #t1 = gevent.spawn(test1)
    #t2 = gevent.spawn(test2)
    #t1.join()
    #t2.join()

    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2),     
    ])

    为什么必须要调用join方法呢？主进程 结束之后，协程里面的代码也就直接 结束了。

代码2：
    import time
    import gevent
    from gevent import select

    start = time.time()
    tic = lambda: 'at %1.1f seconds' % (time.time()-start)

    def gr1():
        print('started polling: %s' % tic())
        a = select.select([],[],[],2)     # 阻塞，之后 切换上下文
        print(a)
        print('end pooling: %s' % tic())

    def gr2():
        print('start polling: %s' % tic())
        select.select([],[],[],2)
        print('end pooling: %s' % tic())

    def gr3():
        print('hey lets do some stuff while the greenlets poll, %s' % tic())
        gevent.sleep(1)

    gevent.joinall([
        gevent.spawn(gr1),
        gevent.spawn(gr2),
        gevent.spawn(gr3),

    ])

    遇到 阻塞 之后，会自动切换 协程

代码3：
    import random
    import gevent

    def task(pid):
        gevent.sleep(random.randint(0,2)*0.001)
        print('Task %s done'% pid)

    def synchronous():   # 同步
        for i in range(1,10):
            task(i)

    def asynchronous():   #异步
        threads = [gevent.spawn(task,i) for i in range(10)]
        gevent.joinall(threads)

    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    asynchronous()

    上面的代码，分别以 同步和异步的方式 执行 task函数10次。同步执行 大概要消耗 0.02秒，异步执行 大概要消耗 0.0002秒。异步执行是 协程是随机切换的。

代码4：
    import gevent.monkey
    import gevent
    from urllib.request import urlopen
    gevent.monkey.patch_socket()   # 这句代码的意思是，当任务 遇到 I/O操作时，切换。如果不加，遇到I/O操作时，gevent不会切换。

    def fetch(pid):
        response = urlopen('http://www.baidu.com')
        result = response.getcode()
        print(result)
        print('Process %s:%s'%(pid,result))
        return result

    def synchronous():
        for i in range(1,10):
            fetch(i)

    def asynchromous():
        threads = []
        for i in range(1,10):
            threads.append(gevent.spawn(fetch,i))
        gevent.joinall(threads)

    print('Synchronous:')
    synchronous()

    print('Asynchromous')
    asynchromous()

代码5：
    import gevent
    from gevent import Greenlet

    def foo(message,n):
        gevent.sleep(n)
        print(message)

    thread1 = Greenlet.spawn(foo,"hrllo",1)
    thread2 = gevent.spawn(foo,"I Live!",2)
    threads = [thread1,thread2]

    gevent.joinall(threads)

#本地I/O gevent不会自动切换




    1.1 、进程池和socket一起使用的时候，会产生意想不到的问题。。。
        代码1：
            #coding:utf-8
            from multiprocessing import Pool
            from socket import *

            def func(new_socket):
                print('--test--')
                try:
                    new_socket.send(bytes('hehe',"utf-8"))
                except Exception as err:
                    print(err)
                else:
                    print('发送成功')
                finally:
                    new_socket.close()

            def main():
                p = Pool(2)
                tcp_ser_socket = socket(AF_INET,SOCK_STREAM)
                tcp_ser_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
                tcp_ser_socket.bind(('',7788))
                tcp_ser_socket.listen(5)
                while True:
                    new_socket,client_addr = tcp_ser_socket.accept()
                    print(client_addr)       
                    p.apply_async(func,(new_socket,))
                    # new_socket.close()   # 如果使用 Process类创建子进程，不使用进程池，那么，需要在这里关闭套接字。但是如果使用进程池，这里一定不能关闭套接字，
                p.close()                  # 这里 关闭套接字会导致，进程池里的 子进程 启动失败。
                p.join()

            if __name__ == "__main__":
                main()

            # 使用 python2 ，子进程 不会启动。
            # 使用 python3，可以正常执行。
















