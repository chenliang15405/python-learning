"""
函数传递参数，传递的是变量的引用，就是说传递的是变量的内存地址

函数返回值，返回的也是变量的地址，而不是数据本身

"""

def test(num):

    print("在函数内部%d对应的内存地址是： %d" % (num, id(num)))

    result = "hello"

    print("在函数内部%s对应的内存地址是： %d" % (result, id(result)))

    return result


a = 10

print("a 变量保存数据的内存地址是： %d" % id(a))

# 调用test函数，本质上传递的是实参保存数据的引用，而不是参数的数据
result = test(a)

print("函数返回值得内存地址是： %d" % id(result))

