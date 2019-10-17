一、python中的 文本文件对象（文本流对象）： 

1. open函数返回值（以文本方式打开）
2. sys.stdout
3. sys.stdin
4. sys.stderr
5. io.StringIO 这个类的返回值。


二、python中的 二进制文件对象（二进制流对象）：

1. open函数返回值（以二进制方式打开）
2. io.BytesIO 这个类的返回值。


三、标准输入 标准输出 标准错误

1. sys.stdout --  标准输出

代码：
import sys

sys.stdout.write('hello' + '\n')
print('hello')

# 两行代码执行效果是相同的。
# print函数，实际调用的就是sys.stdout.write()

2. sys.stdin  --  标准输入

代码：
import sys

s = sys.stdin.readline()
print(len(s))

# sys.stdin.readline( )会将标准输入全部获取，包括末尾的'\n'，因此用len计算长度时是把换行符'\n'算进去了的。
# 但是input( )获取输入时返回的结果是 不包含 末尾的换行符'\n'的。
#因此如果在平时使用sys.stdin.readline( )获取输入的话，不要忘了去掉末尾的换行符。
#可以用strip( )函数（sys.stdin.readline( ).strip('\n')）或sys.stdin.readline( )[:-1]这两种方法去掉换行。


3. sys.stderr  -- 标准错误

代码：
import sys

sys.stderr.write("haha")


# 默认情况下，标准输出和标准错误，会输出到屏幕中显示。标准输入，会读取键盘的输入。

# 如果修改了 sys.stdout的 引用，让它指向一个打开的文本文件对象，那么再使用print函数的时候，就不会向屏幕中输出，而是写入了文件中。
#例如：
#代码：
import sys

f = open("test.txt","w")

sys.stdout = f

print("haha")