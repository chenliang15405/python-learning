"""
多继承: 子类可以继承多个父类，并拥有所有父类的属性和方法

    语法：
        class 子类名(父类名1,父类名2,...)
            pass


多继承出现的问题:
    如果多个父类中有相同的方法或者属性，那么应该避免使用多继承
    虽然不报错，但是会根据方法的调用顺序来调用一个父类中的方法和属性


Python中的mro ---- 方法搜索顺序
    __mro__ 可以查看方法的搜索顺序，在多继承时，可以查看，方法和属性的搜索顺序
    该方法是类的方法


新式类和旧式类：

    新式类： 创建的类以Object类为父类的类，dir()函数查看该类的对象，会提供一些内置的属性和方法
    旧式类： 没有以Object类为父类，没有内置的方法

    Python3中默认定义类时，以Object为父类，
    Python2中不会默认继承Object父类




"""

class A:

    def test(self):
        print("A test")

class B:

    def test(self):
        print("B test")

    def demo(self):
        print("demo")


class C(A, B):

    pass



c = C()

c.test()
c.demo()

# 查看c中方法和属性的搜索顺序
print(C.__mro__)