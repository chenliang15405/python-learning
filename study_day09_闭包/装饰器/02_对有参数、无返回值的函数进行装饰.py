
def set_func(func):

    def call_func(num):
        print("----这是1----")
        print("----这是1----")
        func(num)
    return call_func


@set_func
def test1(num):
    print("-----test1-----%d" % num)


# 其实就是说 这里调用的test1() 相当于就是调用闭包中的内部函数
test1(100)

