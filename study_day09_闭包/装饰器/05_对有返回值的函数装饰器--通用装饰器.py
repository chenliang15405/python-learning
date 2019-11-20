""""
对有返回值得函数的装饰器，也是通用装饰器

"""


def set_func(func):

    # 接收不定长参数的时候，直接接收所有的参数即可，因为装饰器就是相当于直接调用内部函数
    def call_func(*args, **kwargs):
        print("---------1---")
        print("---------2---")
        # 返回该函数的返回值，就算该函数没有返回值也不报错
        return func(*args, **kwargs)
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("---------test1---- %d" % num)

    return "ok"


@set_func
def test2():
    pass


ret = test1(100)
print(ret)

ret = test2()
print(ret)

