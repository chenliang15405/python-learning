"""
orm映射的实现，通过元类创建一个父类，父类中包含基本的操作方法，并且将元类中创建类时获取的属性名称
和对应的值传递过来，就可以实现orm映射

"""
class ModelMetaClass(type):

    def __new__(cls, name, bases, attrs):
        # 这里的new是指在需要创建的类被创建的时候，会将类对象、名称、属性、方法等传递过来
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是指定的Stringfield 或者integerField对象
            if isinstance(v, tuple):
                print("FOUND MAPPING : %s ===> %s" % (k, v))
                mappings[k] = v

        # 删除已经在字典中的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将属性名和对应的字段名称保存
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(object, metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            # 需要使用这个方法，因为self.name = value,表示属性名称就是name
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        args_temp = list()
        for temp in args:
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)

        sql = 'insert into %s (%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL: %s' % sql)


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')


u = User(uid=123, name="MMM", email="test@test.com", password="my-pwd")
u.save()
















