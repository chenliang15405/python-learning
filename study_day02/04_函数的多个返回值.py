"""
元组可以包含多个数据，因此可以使用元组让函数一次返回多个值
如果函数返回的类型是元组，小括号可以省略

"""


def measure():
    print("测量开始")
    temp = 39
    wetnesss = 50
    print("测量结束")

    # 如果返回一个元组，可以省略()
    return temp, wetnesss

# 接收的参数类型也是元组
result = measure()
print(f"函数返回的元组类型的参数，接收也是元组: {result}")

print("元组中的第一个数据: %d" % result[0])

#  如果使用元组接收，需要单独使用元组中的数据不方便，可以使用变量单独接收
# 如果需要单独处理元组中的元素，可以定义多个变量接收函数返回的元组类型， 接收的变量个数也需要和元组中个数相同
gl_temp, gl_wetness = measure()

print("单独接收的函数返回的元组： %d 和 %d" % (gl_temp, gl_wetness))


# 实现两个数的交换
a = 6
b = 100
# 解法1
a = a + b
b = a - b
a = a - b

# 解法2 python专有解法
a, b = (a, b)
# 这就是从元组中接收两个变量，第一个变量接收第一个值，所以就可以实现数据交换
# 并且返回值是元组的函数，可以省略小括号
a, b = b, a
