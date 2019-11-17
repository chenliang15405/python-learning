"""
私有属性的访问可以通过setter、getter方法进行访问

    python中建议使用property来作为私有属性访问的形式

    有两种方式可以完成 getter、setter属性的访问(类属性、装饰器)：
        1. 装饰器：
            @property
        2. 类属性:
            NAME = property(get, set)

"""


class Money(object):
    """装饰器升级getter、setter"""

    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


m = Money()
print(m.money)
m.money = 200
print(m.money)


class Money2(object):
    """类属性升级getter、setter"""

    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        self.__money = value

    money = property(getMoney, setMoney)


m2 = Money2()

print(m2.money)
m2.money = 200
print(m2.money)
