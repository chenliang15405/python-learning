"""
类也是一个对象

元类创建类，类创建实例对象

元类就是 type
可以用type创建


"""

# 创建了一个类，第一个参数是类名称，第二个参数是类的父类，第三个参数是属性
Test1 = type("Test1", (), {"num": 100, "num2": 200})

help(Test1)


# 创建有父类的类
Test2 = type("Test2", (Test1,), {"num": 100, "num2": 200})
help(Test2)

# 创建有实例方法的类
def test_2(self):
    print("test2-------")


Test3 = type("Test3", (), {"test_2": test_2})
help(Test3)

t = Test3()
t.test_2()


