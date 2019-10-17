1 bytes

    字节组成的有序的不可变序列(区别:字符串是字符组成的序列,以一个字符为单位;字节序列是字节组成的序列,以字节为单位)

2 bytearray

    字节组成的有序的可变序列(数组)

3 字符串

    字符组成 的有序序列



使用语法：bytearray([source[, encoding[, errors]]])

参数说明：
    如果 source 为整数，则返回一个长度为 source 的初始化数组；
    如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
    如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
    如果 source 为与 buffer 接口一致的对象，那么将使用只读方式将字节读取到字节数组后返回
    如果没有输入任何参数，默认就是初始化数组为0个元素。


1) source --整数

代码：
b = bytearray(3)
print(b)

b.append(1)

print(b)

输出：
bytearray(b'\x00\x00\x00')
bytearray(b'\x00\x00\x00\x01')

2) source -- 字符串

代码：
b = bytearray("中国",'utf-8')
print(b)

输出：
bytearray(b'\xe4\xb8\xad\xe5\x9b\xbd')

# 如果使用 append方法 添加 元素的话 会报错

3) source -- 可迭代类型

代码:
b = bytearray([1,2,3])
print(b)

print('--test1---')

print("数组中第一个元素：{}".format(b[0]))

print('--test2---')

for i in b:
    print(i)

输出：
bytearray(b'\x01\x02\x03')
--test1---
数组中第一个元素：1
--test2---
1
2
3

4) source -- 与 buffer 接口一致的对象

pass


常用方法：参数必须是 bytes类型数据
1. count(sub[, start[, end]])
    统计 某些 字符 出现的次数

代码：
b = bytearray("hello, he, he ", "utf-8")

print(b.count(b"he"))

2. index(sub[, start[, end]])

    返回 某个 元素 第一次出现的索引

代码：
b = bytearray("python hello, he, he ", "utf-8")

print(b.index(b"he"))

3. append(item)
    在末尾添加元素，只能添加数字[0-255]

代码：
b = bytearray("python hello, he, he ", "utf-8")

b.append(1)
print(b)

