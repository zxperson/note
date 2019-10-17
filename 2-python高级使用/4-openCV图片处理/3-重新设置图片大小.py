import cv2

img = cv2.imread('demo.png')

# 重新设置 图片大小为 100 * 100
img2 = cv2.resize(img,(100,100), interpolation=cv2.INTER_CUBIC)


cv2.imwrite("1.png", img2)
