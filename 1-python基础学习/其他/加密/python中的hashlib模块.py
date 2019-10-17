一、介绍

hashlib 模块 提供了常见的消息摘要算法，例如：MD5，SHA等。

二、基本使用

代码：
import hashlib

test1_md5 = hashlib.sha256()  # 以sha256算法为例，其他算法是一样的。
test1_md5.update(b"hello,world")
print(test1_md5.hexdigest())

# 如果 数据比较大，可以分多次进行。结果是一样的。
test2_md5 = hashlib.sha256()
test2_md5.update(b"hello,")
test2_md5.update(b"world")
print(test2_md5.hexdigest())   # 返回的是 十六进制的 str类型字符串
print(test2_md5.digest())   # 返回的是 bytes 字符串


二、 hexdigest 和 digest 区别。

代码：
In [31]: test_sha256 = hashlib.sha256()

In [32]: test_sha256.update(b"hello,world")

In [33]: test_sha256.hexdigest()  # 返回的是 str类型数据
Out[33]: '77df263f49123356d28a4a8715d25bf5b980beeeb503cab46ea61ac9f3320eda'

In [34]: test_sha256.digest()    # 返回的是 bytes类型的数据
Out[34]: b'w\xdf&?I\x123V\xd2\x8aJ\x87\x15\xd2[\xf5\xb9\x80\xbe\xee\xb5\x03\xca\xb4n\xa6\x1a\xc9\xf32\x0e\xda'

1.# str类型的数据是如何生成的呢？
	1）在通过sha256算法完成哈希之后，生成一个256bit的二进制数。
    2）每4bit二进制数，转换成一个十六进制数。
    3）把十六进制数转换成str类型的字符串。

2.# bytes类型的数据是如何生成的呢？
	1）在通过sha256算法完成哈希之后，生成一个256bit的二进制数。
	2）每4bit二进制数，转换成一个十六进制数。
	3）每两个十六进制数前面加上一个"\x"字符


	In [35]: b"\x77"
	Out[35]: b'w'

	In [36]: b"\x77\xdf"
	Out[36]: b'w\xdf'

	In [37]: b"\x77\xdf\x26"
	Out[37]: b'w\xdf&'

	在运行界面输出bytes时候，它是采取这样的原则的：
	每读一个字节就和ascii码比对一下，如果符合ascii码的可显示字符（特殊字符，字母和数字，控制字符除外），那这个字节就按照ascii码来表示，否则就按十六进制\x某某来表示。