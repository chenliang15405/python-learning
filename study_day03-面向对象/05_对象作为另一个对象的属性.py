"""
一个对象的属性可以是另外一个类创建的对象

定义没有初始值的属性：
    1.在定义属性时，如果不指定具体的初始值，则可以设置为None

    None表示什么都没有，是一个空对象


"""


class Gun:

    def __init__(self, name):
        self.name = name

    def fire(self):
        print("%s 突突突" % self.name)


ak47 = Gun("ak47")


class Person:

    def __init__(self, name):
        self.name = name

        # 设置对象的初始值为None,需要的时候在外部再赋值，这里先初始化
        self.gun = None

    def __str__(self):
        return "%s 使用 %s" % (self.name, self.gun)

    def tututu(self):
        if self.gun is None:
            print("还没有枪")
            return

        print("开火...")

        # 调用其他对象的方法
        self.gun.fire()


person = Person("小明")

# 在使用的时候外部再进行赋值
person.gun = ak47

# 调用方法
person.tututu()
