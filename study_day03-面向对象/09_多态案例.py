"""
多态:
    前提就是 需要继承和重写父类方法

重写父类中的方法，创建子类的对象去调用，不同的子类对象，调用相同的方法是不同的结果

"""

class Dog(object):
    # 初始化方法定义属性
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 在玩耍..." % self.name )


class XiaoTianDog(Dog):
    def game(self):
        print("%s 在天上玩耍..." % self.name )


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 在和 %s 玩耍..." % (self.name, dog.name))
        dog.game()


# 这样就是多态，重写父类中的方法，创建子类的对象去调用，不同的子类对象，调用相同的方法是不同的结果
#wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

xiaoming = Person("小明")

xiaoming.game_with_dog(wangcai)
