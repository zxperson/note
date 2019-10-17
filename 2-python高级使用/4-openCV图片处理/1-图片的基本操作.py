import cv2

# 读取 一张图片
# 第二个参数的作用：
# 　　cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。
# 　　cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
# 　　cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道
img = cv2.imread('demo.png',cv2.IMREAD_GRAYSCALE)

# 创建一个窗口 加载显示图像，第一个参数是 窗口名字。窗口不能 改大小
cv2.imshow("whit",img)
# 创建 可以自由更改大小的窗口：cv2.namedWindow('whit', cv2.WINDOW_NORMAL) , 创建完窗口 调用 imshow 显示图片即可。


# waitKey 是一个键盘绑定函数。
# 需要指出的是它的时间尺度是毫秒级。函数等待特定的几毫秒，看是否有键盘输入。
# 特定的几毫秒之内，如果按下任意键，这个函数会返回按键的 ASCII 码值，程序将会继续运行。
# 如果没有键盘输入，返回值为 -1，如果我们设置这个函数的参数为 0，那它将会无限期的等待键盘输入
cv2.waitKey(0)



# 保存图片, 图片的名字不能是中文
cv2.imwrite('heibai.png',img)

# 删除 所有 创建 出来的窗口
cv2.destroyAllWindows()
# 删除 某个 窗口：cv2.destroyWindow()，在括号内输入你想删除的窗口名。