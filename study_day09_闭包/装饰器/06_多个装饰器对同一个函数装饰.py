"""
多个装饰器对同一个函数进行装饰

其实多个装饰器就可以看做是 多层的过滤器

"""


def add_qx(func):
    print("-----开始进行装饰权限1的功能-----")

    def call_func(*args, **kwargs):
        print("-------11111---")
        return func(*args, **kwargs)
    return call_func


def add_xx(func):
    print("-----开始进行装饰xxxxx的功能-----")

    def call_func(*args, **kwargs):
        print("-----xxxxxxxx----")
        return func(*args, **kwargs)
    return call_func

"""
装饰的时候，是先装饰下面的装饰器，执行装饰的时候是先执行上面的装饰器
上面的装饰器传入的函数是下面装饰器装饰之后的函数引用
所以上面的装饰器中传入的func是下面的装饰器中返回的call_func

"""
@add_qx
@add_xx
def test1():
    print("----test1----")


test1()