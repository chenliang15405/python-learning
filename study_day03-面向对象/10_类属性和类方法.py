"""
类也是一个对象，不过类对象在内存中只有一份

    可以给类定义方法和属性，类属性、类方法（相当于静态方法，静态属性）

1、类属性：

class Name:
    # 定义类属性
    count = 0


访问类属性：
    类名.类属性

    也可以通过 对象名.类属性  不推荐，因为有可能在   对象.类属性=值 会给当前对象定义一个实例属性，虽然不会
    影响到类属性的值，但是会定义一个新的实例属性


2、类方法

 语法：
    @classmethod
    def 类方法名(cls):
        pass

 在类方法内部，可以直接访问类属性和调用其他的类方法

 类方法需要修饰器@classmethod 来标识，告诉解释器这是一个类方法

 注意:
    1.类方法的第一个参数应该是cls，cls是当前调用类方法的类的引用
    2.通过  类名.类方法名 调用类方法，调用方法时，不需要传递cls参数，
    3.可以通过cls. 访问类的属性，或者cls. 调用其他类方法



"""


class Tool(object):

    # 定义类属性
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):
        print("当前的count为： %d " % cls.count)

    # 初始化方法
    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("锤子")
tool1 = Tool("尼泊尔")
tool1 = Tool("ak47")

# 调用类方法
Tool.show_tool_count()

# 调用类属性
print(Tool.count)



