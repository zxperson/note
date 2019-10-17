import cv2

#开启摄像头
capture = cv2.VideoCapture(0)

while True:
    #采集数据，ret表示是否成功，frame表示采集到的数据
    ret, frame = capture.read()
    #创建窗口，把采集到的数据显示出来
    cv2.imshow('test',frame)
    #不断刷新图像频率 1ms ，返回值为 当前按键值
    key = cv2.waitKey(1)
    if key == 27:
        #关闭窗口，停止采集数据
        cv2.destroyAllWindows()
        break