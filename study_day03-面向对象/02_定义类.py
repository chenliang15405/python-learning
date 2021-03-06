"""
定义类的语法：
    class 类名:
        def 方法1(self, 参数列表):
            pass

        def 方法2(self, 参数列表：
            pass

注意:
    1. 方法和函数定义基本一样，就是第一个参数必须是self， self表示：哪个对象调用的方法，self就是这个对象的引用
        在方法内部，可以通过self. 方法对象的属性 或者 调用对象其他的方法

    2. 类名的命名规则要符合大驼峰命名法


创建对象：
    语法：
        对象变量名 = 类名()



初始化方法：
    在使用 类名() 创建对象时，会自动执行以下操作：
        1. 为对象分配空间
        2. 为对象设置初始值，调用python的内置方法： __init__方法，专门用来定义一个类有哪些属性的方法


对象中定义属性：
    在内部定义属性（推荐）：
        在__init__方法中，通过 self.属性名 = 属性的初始值  来定义属性
        这样定义属性之后，再使用Cat类创建的对象，都会拥有该属性

    在外部定义属性（不推荐）
        在创建对象之后，通过 对象.属性名 = 属性的值 定义属性


"""


class Cat:
    """这是一个猫类"""

    def __init__(self):
        print("这是一个初始化方法，会在对象创建时自动调用 ")

        # 定义对象属性
        self.name = "tom"


    def eat(self):
        print("吃")

    def drink(self):
        print("喝水")

tom = Cat()

# 调用对象方法
tom.eat()
tom.drink()

# 调用对象属性
print(tom.name)


