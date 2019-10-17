# coding:utf-8

import socket

from multiprocessing import Process

HTML_ROOT_DIR = ""


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    #print("request data:", request_data)

    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello itcast"
    response = response_start_line + response_headers + "\r\n" + response_body
    #print("response data:", response)

    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))  # response.encode('utf-8')

    # 关闭客户端连接
    client_socket.close()


if __name__ == "__main__":
    #创建tcp套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 实现 端口的复用
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定地址
    server_socket.bind(("", 8000))
    # 把套接字 由主动变成被动
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        # print("[%s, %s]用户连接上了" % (client_address[0],client_address[1]))
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
