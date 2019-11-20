"""
对于不定长参数的函数的装饰器使用

"""


def set_func(func):

    # 接收不定长参数的时候，直接接收所有的参数即可，因为装饰器就是相当于直接调用内部函数
    def call_func(*args, **kwargs):
        print("---------1---")
        print("---------2---")
        # 拆包
        func(*args, **kwargs)
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("---------test1---- %d" % num)
    print("---------test1---- ", args)
    print("---------test1---- ", kwargs)


test1(100)
test1(100, 200, 300)
test1(100, 200, 300, mm="123")



