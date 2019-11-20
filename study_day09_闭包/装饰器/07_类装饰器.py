"""
使用类作为装饰器

"""


class Test(object):

    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("装饰器的功能-----")
        return self.func()


@Test   # 相当于 test1 = Test(test1)
def test1():
    print("-------")


# 因为这个test1 已经指向了类的实例对象，所以对象() 表示调用类的 __call__ 方法
print(test1())

