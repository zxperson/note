import struct
import pickle
import socket
import cv2

'''
采集数据，把每一帧数据发送给服务器显示
'''
#服务器地址
SERVER_ADDR = ('127.0.0.1',8888)
#定义每次发送的数据包的大小，单位字节
PACKET_DATA_SIZE = 4096 * 4
#创建udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#启动摄像头
camera = cv2.VideoCapture(0)
#采集图像数据，发送给服务器
while True:
    #采集每一帧的数据
    ret,frame = camera.read()
    #把frame这个对象 序列化成 字符串
    pickled_frame = pickle.dumps(frame)
    print(len(pickled_frame))  #每一帧的数据大于64kb
    #获取 每一帧 数据的大小
    pickled_frame_size = len(pickled_frame)
    #计算 每一帧 分成几部分发送
    frame_send_num = pickled_frame_size // PACKET_DATA_SIZE + 1
    #发送 每个数据包
    for i in range(frame_send_num):
        start_index = i * PACKET_DATA_SIZE
        end_index = (i+1) * PACKET_DATA_SIZE
        flag = 0
        if i == frame_send_num - 1:
            flag = 1
        send_data = pickled_frame[start_index:end_index]
        # 按照协议 格式化 字符串
        struct_send_data = struct.pack('!ib%ss'%len(send_data), i, flag, send_data)

        #把数据发送给服务器
        udp_socket.sendto(struct_send_data,SERVER_ADDR)

        #接收应答包
        ack,addr = udp_socket.recvfrom(1024)

        #解包
        ack_num = struct.unpack('!i',ack)
        if ack_num == str(i):
            continue







