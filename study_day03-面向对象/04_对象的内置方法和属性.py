"""
内置方法和属性：

    __def__ ： 对象被从内存销毁之前，会被自动调用
    __str__ ： 返回对象的描述信息，print函数输出使用， 相当于java中的toString()方法，该方法必须返回一个字符串
                打印对象，就相当于调用该方法


"""

class Cat:
    def __init__(self, new_name):
        self.name = new_name

    def __del__(self):
        print("对象生命周期结束")

    def __str__(self):
        # 必须返回一个字符串
        return "这是描述信息:[%s]" % self.name


tom = Cat("tom")

print(tom)




