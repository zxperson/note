import cv2
import struct
import pickle
import socket

#创建套接字
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定地址
udp_server.bind(('127.0.0.1',8888))

frame_data = b''

#接收每个数据包，并且组成完整的数据帧，然后显示
while True:
    recv,addr = udp_server.recvfrom(4096 * 4 + 100)
    num,flag = struct.unpack('!ib',recv[:5])

    frame_data += recv[5:]

    if flag == 1:
        frame = pickle.loads(frame_data)
        cv2.imshow('xxx监控系统',frame)
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break
        frame_data = b''

    #格式化 应答包
    send_data = struct.pack('!i',num)

    #发送应答包
    udp_server.sendto(send_data,addr)

