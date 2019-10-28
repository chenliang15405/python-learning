"""

私有属性： 不能直接在外部访问的属性
私有方法： 不能直接在外部访问的方法

定义：
    在定义属性或者方法时，在属性名或者方法名前加上 __ 定义的就是私有属性或方法


没有真正意义的私有
    python在处理的时候，给私有方法和属性前面加上了 _类名 =》 _类名__属性名
    所以外界无法直接访问到

    可以通过 对象._类名__私有属性或方法  访问到


"""


class Man:

    def __init__(self, name):
        self.name = name
        # 定义私有属性
        self.__age = 18

    # 定义私有方法
    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaoming = Man("小明")

# 可以通过这种方式访问私有属性或者方法
print(xiaoming._Man__age)

xiaoming._Man__secret()