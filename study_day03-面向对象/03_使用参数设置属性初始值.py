"""
创建对象的同时，设置对象的属性（相当于java中的构造方法）

    在 __init__ 方法中传递参数，并通过 self.属性名 = 形参
    创建对象时，通过 类名(属性1，属性2,...)调用


"""


class Cat:

    # 通过 init方法的参数设置属性初始值
    def __init__(self, name):
        self.name = name


tom = Cat("tom")
print(tom.name)

lazy_cat = Cat("小明")
print(lazy_cat.name)