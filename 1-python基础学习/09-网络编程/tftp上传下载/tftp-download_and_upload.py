# -*- coding:utf-8 -*-

import struct
from socket import *
import os

def download(udpSocket):

	#0. 获取要下载的文件名字:
	downloadFileName = input("请输入要下载的文件名:")

	requestFileData = struct.pack("!H%dsb5sb"%len(downloadFileName), 1, downloadFileName.encode('utf-8'), 0, b"octet", 0)

	#2. 发送下载文件的请求
	udpSocket.sendto(requestFileData, ("192.168.248.1", 69))

	flag = True #表示能够下载数据，即不擅长，如果是false那么就删除
	num = 0
	f = open(downloadFileName, "wb")

	a = 1
	while a:
		#3. 接收服务发送回来的应答数据
		responseData = udpSocket.recvfrom(1024)

		# print(responseData)
		recvData, serverInfo = responseData

		opNum = struct.unpack("!H", recvData[:2])  # 提取操作码,返回值是一个元祖

		packetNum = struct.unpack("!H", recvData[2:4])  #提取 块编号（包编号）,返回值是一个元祖

		print(packetNum[0])

		# print("opNum=%d"%opNum)
		# print(opNum)

		# if 如果服务器发送过来的是文件的内容的话:
		if opNum[0] == 3: #因为opNum此时是一个元组(3,)，所以需要使用下标来提取某个数据
			

			#计算出这次应该接收到的文件的序号值，应该是上一次接收到的值的基础上+1
			num = num + 1

			# 如果一个下载的文件特别大，即接收到的数据包编号超过了2个字节的大小
			# 那么会从0继续开始，所以这里需要判断，如果超过了65535 那么就改为0
			if num==65536:
				num = 0

			# 判断这次接收到的数据的包编号是否是 上一次的包编号的下一个
			# 如果是才会写入到文件中，否则不能写入（因为会重复）
			if num == packetNum[0]:
				# 把收到的数据写入到文件中
				f.write(recvData[4:])
				num = packetNum[0]

			#整理ACK的数据包
			ackData = struct.pack("!HH", 4, packetNum[0])
			udpSocket.sendto(ackData, serverInfo)

		elif opNum[0] == 5:
			print("sorry，没有这个文件....")
			flag = False

		# time.sleep(0.1)

		if len(recvData)<516:
			break

	if flag == True:
		f.close()
	else:
		os.unlink(downloadFileName)#如果没有要下载的文件，那么就需要把刚刚创建的文件进行删除

def upload(udpSocket):

	upload_file_name = input("请输入要上传的文件名:")
	#构造请求数据
	request_data = struct.pack("!H%dsb5sb"%len(upload_file_name), 2, upload_file_name.encode('utf-8'), 0, b"octet", 0)
	# 发送 上传请求
	udpSocket.sendto(request_data, ("192.168.248.1", 69))

	#打开文件
	f = open(upload_file_name,'rb')
	flag = 0
	while True:
		recv_data,addr = udpSocket.recvfrom(1024)
		# 提取 操作码和包编号
		opcode,pack_num = struct.unpack('!HH',recv_data[:4])
		if opcode == 4:
			if pack_num == flag:  # 代表 服务器接收到了 数据包
				flag += 1
				file_data = f.read(512)

				if flag == 65535:
					flag = 0

				send_data = struct.pack('!HH%ds' % len(file_data), 3, flag, file_data)
				udpSocket.sendto(send_data, addr)

                if len(file_data) < 512:
                    break
		else:
			print('服务器错误')
			break

def main():

	command = input('请输入指令（1：下载,2:上传）：')
	# 1.创建socket
	udpSocket = socket(AF_INET, SOCK_DGRAM)

	if command == '1':
		download(udpSocket)
	elif command == '2':
		upload(udpSocket)
	else:
		print('未知的指令！')

if __name__ == '__main__':
	main()
