知识点：

1. tcp（传输控制协议）
特点：有连接的、可靠的。数据包大小没限制

服务器两种典型架构：C/S 、B/S
服务器流程：1.创建套接字socket 2.绑定地址 3. listen，使套接字可以被链接 4.accept等待客户端的链接
            5.接收、发送数据  6. 关闭 提供服务的套接字
客户端流程：1.建立套接字socket 2.connect，建立连接（三次握手） 3. 发送，接收 数据 4. 关闭套接字

2.三次握手

  建立连接

3.四次挥手

  断开连接

4.tcp连接的十一种状态

  CLOSING：如果客户端和服务器同时发起了关闭请求，那么此时它们的TCP状态就都为FIN_WAIT_1，
           并发送FIN段给对方，对方收到FIN段后，又发送确认段ACK段给对方，此时彼此的TCP状态就为CLOSING。

5.  2MSL 

    两倍的MSL
    MSL：数据包在网络当中最大存活时间，有可能是 30s，1分钟，2分钟。

    存在的意义：最后一个ACK包，如果丢了，对方会重新发送FIN包。

6. 网络通信过程
   非常重要。访问百度的过程。

7. 并发服务器


8.

#coding:utf-8

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#服务器地址
addr = ('192.168.253.3',8989)

client_socket.connect(addr)

client_socket.send(b'哈哈')

client_socket.close()

