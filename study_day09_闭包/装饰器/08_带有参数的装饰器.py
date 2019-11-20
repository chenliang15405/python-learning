"""
装饰器带有参数，实现向装饰器中传递参数，

装饰器带有参数的实现过程：
    1. 先传递实参到装饰器中，并返回该装饰器对象
    2. 使用返回的装饰器对象来装饰该函数

"""


def set_params(level_num):
    def add_xx(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("----权限验证级别1----")
            elif level_num == 2:
                print("----权限验证级别2----")
            return func(*args, **kwargs)
        return call_func
    return add_xx


@set_params(1)
def test1():
    print("----test1----")
    return "ok"


@set_params(2)
def test2():
    print("----test1----")
    return "ok"


test1()

test2()





