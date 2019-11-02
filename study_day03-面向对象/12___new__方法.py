"""
__new__ 方法
    使用类名()创建对象时，首先调用object基类提供的 __new__方法，该方法为对象分配内存空间，并返回对象的引用，
    然后将对象的引用作为第一个参数传递给 __init__ 方法

重写__new__ 方法一定要 return super(),__new__(cls) 否则不能返回对象的引用，则就不会调用对象的初始化方法


python中的单例模式：

利用类属性和__new__ 方法


"""


class Singleton(object):

    # 定义类属性保存对象实例
    instance = None

    # 让初始化方法只执行一次
    init_flag = False

    # 重写__new__方法，判断是否返回同一个内存地址的对象
    def __new__(cls, *args, **kwargs):

        # 判断是否已经有对象存在
        if cls.instance is not None:
            return cls.instance

        # 如果内存中没有对象，则创建对象
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if Singleton.init_flag:
            print("不执行初始化方法")
            return

        # 没有初始化过，则执行初始化
        print("执行初始化")

        Singleton.init_flag = True



single1 = Singleton()
print(single1)

single2 = Singleton()
print(single2)

single3 = Singleton()
print(single3)










