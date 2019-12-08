"""
with的用法和原理


with是上下文管理器，通过类对象中的 __enter__ 和 __exit__来执行特定的功能

"""


class Foo(object):

    def  __enter__(self):
        """进入with语句的时候被with调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exit with")


# open() 对象就是这样处理流的开启和关闭
with Foo() as f:
    print("hello")
