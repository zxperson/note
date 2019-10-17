
# itsdangerous 模块介绍
https://itsdangerous.palletsprojects.com/en/1.1.x/

1. Signer类
把给定的字符串进行签名，然后把两者 拼接到一起。连接符号可以自己指定。可以看看源代码。

基本使用例子：
from itsdangerous import Signer
s = Signer('secret-key')
ret = s.sign('my string')
print(ret)   # 输出 b'my string.wh6tMHxLgJqB6oY1uT73iMlyrOA'

raw_str = s.unsign(b'my string.wh6tMHxLgJqB6oY1uT73iMlyrOA')
print(raw_str)  #输出 b'my string'

详解：
1）Signer类必须接收一个参数，作为秘钥，进行相关的初始化，例如：初始化 派生秘钥，盐值，哈希算法，具体可以查看源代码。
2）签名的时候默认先把 字符串 进行 utf8编码，然后计算签名。所以如果是中文，这里要注意了。
3）unsign 方法用来 验证 签名字符串是否是 合法的。如果验证通过，返回字符串本身（bytes类型）。


2. Serializer 类
Signer类 只能签名字符串,为了可以签名其他类型数据，Serializer 类提供了两个方法dumps/loads，类似json模块。

基本使用例子:
from itsdangerous.serializer import Serializer

s = Serializer("secret-key")
ret = s.dumps([1, 2, 3, 4])
print(ret)   # str类型：[1, 2, 3, 4].r7R9RhGgDPvvWl3iNzLuIIfELmo

raw_list = s.loads('[1, 2, 3, 4].r7R9RhGgDPvvWl3iNzLuIIfELmo')
print(raw_list)  # list类型: [1, 2, 3, 4]

详解：
1） dumps 先把 列表 序列化成 字符串，然后进行签名。
2） loads 验证 签名，如果通过，返回 反序列数据。
3） 可以通过定义子类的方式，更改 序列化 使用的模块。(默认使用 json模块)


3. 如果想要你的签名 支持有效期，
请参考：https://itsdangerous.palletsprojects.com/en/1.1.x/timed/


4. URLSafeSerializer 类
如果能够向只有字符受限的环境中传递可信的字符串的话，将十分有用。因此，itsdangerous也提供了一个URL安全序列化工具：
生成的签名和 JWS类似，只是少了 头部而已。

基本使用例子：
from itsdangerous.url_safe import URLSafeSerializer

s = URLSafeSerializer("secret-key")
ret = s.dumps([1, 2, 3, 4])
print(ret)  # 输出：WzEsMiwzLDRd.wSPHqC0gR7VUqivlSukJ0IeTDgo

raw_list = s.loads("WzEsMiwzLDRd.wSPHqC0gR7VUqivlSukJ0IeTDgo")
print(raw_list)  # 输出：[1, 2, 3, 4]


5. JSON Web Signature (JWS)    JSONWebSignatureSerializer 类
 和 URLSafeSerializer 类似，但是 这个类 生成的 签名和 JWS 是一样的，包含了头部。

基本使用例子:
from itsdangerous import JSONWebSignatureSerializer
s = JSONWebSignatureSerializer("secret-key")

ret = s.dumps({"user_id":1}, header_fields={"v": 1})  
print(ret)  # b"eyJ2IjoxLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxfQ.1dOfAWWvjZJBxF96HlUMlPqc6tnoLPxWAq6k_MpfycTRiQZ1IDdK9XmBahhV5i4JsjnSTZW-sWfW4jsYpI-Rvw"

raw_data = s.loads(b"eyJ2IjoxLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxfQ.1dOfAWWvjZJBxF96HlUMlPqc6tnoLPxWAq6k_MpfycTRiQZ1IDdK9XmBahhV5i4JsjnSTZW-sWfW4jsYpI-Rvw",return_header=True)

print(raw_data)  #输出：({'user_id': 1}, {'v': 1, 'alg': 'HS512'})

详解：
1) dumps 方法中 header_fields参数用来指定 自定义 JWS头部
2）loads 方法中 return_header 参数 用来指定，返回的 反序列化数据 是否包含 JWS头部。
   如果包含，载荷 和头部 以元组 形式返回

3）TimedJSONWebSignatureSerializer 默认过期时间 1小时
    文档：https://itsdangerous.palletsprojects.com/en/1.1.x/jws/



