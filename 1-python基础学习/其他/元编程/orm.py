class ModelMetaclass(type):
    def __new__(cls, name, parent, attrs):
        """
        name:  "User"
        parent: ()
        attrs: {"uid":(..),"name":(..),"password":(..)}

        """
        mappings = {}

        for key,value in attrs.items():
            if isinstance(value, tuple):
                mappings[key] = value

        for k in mappings.keys():
            attrs.pop(k)       #  把 attrs 列表中的 uid，name，password 三个键 删除

        attrs["__mappings__"] = mappings
        attrs["__table__"] = name

        return type.__new__(cls, name, parent, attrs)

class User(object,metaclass=ModelMetaclass):
    uid = ("uid", "int unsigned")
    name = ("username", "varchar(30)")
    password = ("password", "varchar(30)")

    # __mappings__ = {
    #     "uid":("uid", "int unsigned"),
    #     "name":("username", "varchar(30)"),
    #     "password":("password", "varchar(30)")
    # }
    #
    # __table__ = "User"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    def save(self):
        fields = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v[0])    # ["uid", "username","password"] 对应表的 字段名字
            args.append(getattr(self, k, None))  # [123,"test","123456"]  对应表的 字段的值

        sql = "insert into %s (%s) value (%s)" % (self.__table__, ",".join(fields), ",".join([repr(i) for i in args]))
        print(sql)

u = User(uid=123,name="test",password="123456")
u.save()


改进代码：
class ModelMetaclass(type):

    def __new__(cls, name, parent, attrs):
        mappings = {}

        for key,value in attrs.items():
            if isinstance(value, tuple):
                mappings[key] = value

        for k in mappings.keys():
            attrs.pop(k)

        attrs["__mappings__"] = mappings
        attrs["__table__"] = name

        return type.__new__(cls, name, parent, attrs)

class Model(object,metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v[0])    # ["uid", "username","password"] 对应表的 字段名字
            args.append(getattr(self, k, None))  # [123,"test","123456"]  对应表的 字段的值

        sql = "insert into %s (%s) value (%s)" % (self.__table__, ",".join(fields), ",".join([repr(i) for i in args]))
        print(sql)


class User(Model):
    uid = ("uid", "int unsigned")
    name = ("username", "varchar(30)")
    password = ("password", "varchar(30)")

    # __mappings__ = {
    #     "uid":("uid", "int unsigned"),
    #     "name":("username", "varchar(30)"),
    #     "password":("password", "varchar(30)")
    # }
    #
    # __table__ = "User"

u = User(uid=123,name="test",password="123456")
u.save()

print(type(User))    

# model类是 ModelMetaclass 这个元类创建出来的
# User 类继承于 Model类，所以 User类 也是ModelMetaclass 这个元类创建出来的。